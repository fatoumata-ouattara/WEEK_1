# Generated by Django 4.1.4 on 2022-12-18 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_remove_avis_hotel_alter_reservation_date_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avis',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 18, 11, 38, 59, 158098)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_reservation',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 18, 11, 38, 59, 159062)),
        ),
    ]
