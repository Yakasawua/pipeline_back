from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import AccessPointsWifiCdmx
from .serializers import AccessPointSerializer

# Create your views here.
class AccessPointPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class AccessPointViewSet(viewsets.ModelViewSet):
    serializer_class = AccessPointSerializer
    pagination_class = AccessPointPagination

    def get_queryset(self):
        return AccessPointsWifiCdmx.objects.all()