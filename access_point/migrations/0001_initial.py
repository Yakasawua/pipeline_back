# Generated by Django 4.0.4 on 2023-02-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPointsWifiCdmx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_txt', models.CharField(blank=True, max_length=150, null=True)),
                ('program', models.CharField(blank=True, max_length=150, null=True)),
                ('install_date', models.CharField(blank=True, max_length=150, null=True)),
                ('latitude', models.CharField(blank=True, max_length=150, null=True)),
                ('longitude', models.CharField(blank=True, max_length=150, null=True)),
                ('colony', models.CharField(blank=True, max_length=150, null=True)),
                ('town_hall', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
