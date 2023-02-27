from rest_framework import serializers
from .models import AccessPointsWifiCdmx

class AccessPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessPointsWifiCdmx
        fields = '__all__'