from django.db import models

# Create your models here.
class AccessPointsWifiCdmx(models.Model):
    id_txt = models.CharField(max_length=150, blank=True, null=True)
    program = models.CharField(max_length=150, blank=True, null=True)
    install_date = models.CharField(max_length=150, blank=True, null=True)
    latitude = models.CharField(max_length=150, blank=True, null=True)
    longitude = models.CharField(max_length=150, blank=True, null=True)
    colony = models.CharField(max_length=150, blank=True, null=True)
    town_hall = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.id_txt