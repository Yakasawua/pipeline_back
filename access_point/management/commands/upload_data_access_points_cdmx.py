import csv
from django.core.management import BaseCommand
from django.core.files.storage import default_storage
from access_point.models import AccessPointsWifiCdmx
from django.db import transaction
from unidecode import unidecode

@transaction.atomic
class Command(BaseCommand):
    help = "upload data from wifi access points in Mexico city"

    def handle(self, *args, **options):
        try:
            csv_file = default_storage.open('puntos_de_acceso_wifi_cdmx.csv', 'r')

            csv_data = csv.reader(csv_file)
            next(csv_data)
            count = 0

            for row in csv_data:
                count += 1
                accesspoint = AccessPointsWifiCdmx(
                    id_txt=unidecode(row[0]),
                    program=unidecode(row[1]),
                    install_date=row[2],
                    latitude=row[3],
                    longitude=row[4],
                    colony=unidecode(row[5]),
                    town_hall=unidecode(row[6])
                )
                accesspoint.save()
            csv_file.close()
            self.stdout.write(self.style.SUCCESS("{} Wi-Fi access points created.".format(count)))
        except Exception as e:
            self.stdout.write(self.style.ERROR("Error: {}".format(e)))