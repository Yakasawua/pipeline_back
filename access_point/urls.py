from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccessPointViewSet.as_view({ 'get': 'list' })),#list of all access points and also by colony
    path('<int:pk>/', views.AccessPointViewSet.as_view({ 'get': 'retrieve'})), #search by id
]