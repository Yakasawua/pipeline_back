from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccessPointViewSet.as_view({ 'get': 'list' })),
]