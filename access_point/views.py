from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

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