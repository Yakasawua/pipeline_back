from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.db.models import FloatField, F
from django.db.models.functions import Cast, Radians, Sin, Cos, ACos

from .models import AccessPointsWifiCdmx
from .serializers import AccessPointSerializer

# Pagination configuration
class AccessPointPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

#Get paginated list of access points
#If the colony parameter comes, it is filtered by the colony
#Otherwise all access points are returned
class AccessPointViewSet(viewsets.ModelViewSet):
    serializer_class = AccessPointSerializer
    pagination_class = AccessPointPagination

    def get_queryset(self):
        access_points = AccessPointsWifiCdmx.objects.all()
        colony = self.request.query_params.get('colony', None)
        if colony is not None:
            access_points = access_points.filter(colony=colony)
        return access_points

##paginated list of WiFi hotspots sorted by proximity to a given coordinate [lat, long]
class AccessPointByCoordinatesViewSet(viewsets.ModelViewSet):
    serializer_class = AccessPointSerializer
    pagination_class = AccessPointPagination

    def get_queryset(self):
        access_points = AccessPointsWifiCdmx.objects.all()
        try:
            # Get the latitude and longitude parameters from the GET request
            lat = self.request.query_params.get('lat', None)
            lon = self.request.query_params.get('lon', None)
            if (lat is not None) and (lon is not None):
                
                #transform latitude and longitude to float and radians
                radlat = Radians(float(lat))
                radlong = Radians(float(lon))
                #F('latitude') and F('longitude') are the model fields that are also transformed to float and radians
                radflat = Radians(Cast( F('latitude'), FloatField()))
                radflong = Radians(Cast( F('longitude'), FloatField()))
                
                #use 3959.0 for miles and 6371 for kilometers
                #haversine formula
                Expression = 6371 * ACos(
                    Cos(radlat) * Cos(radflat) *
                    Cos(radflong - radlong) +
                    Sin(radlat) * Sin(radflat)
                    )
                
                #ordering
                access_points = access_points.annotate(distance=Expression).order_by('distance')

        except Exception as e:
            print("Error", e)
        return access_points