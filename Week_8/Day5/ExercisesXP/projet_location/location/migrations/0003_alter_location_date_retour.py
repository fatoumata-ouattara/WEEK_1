# Generated by Django 4.1.3 on 2022-12-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_alter_location_date_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='date_retour',
            field=models.DateField(blank=True, default=True),
        ),
    ]
