from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccessPointViewSet.as_view({ 'get': 'list' })),#list of all access points and also by colony
    path('coordinates/', views.AccessPointByCoordinatesViewSet.as_view({ 'get': 'list' })),#paginated list of WiFi hotspots sorted by proximity to a given coordinate [lat, long]
    path('<int:pk>/', views.AccessPointViewSet.as_view({ 'get': 'retrieve'})), #search by id
]