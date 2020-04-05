# Generated by Django 3.0.5 on 2020-04-05 07:08

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userdata_coords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='coords',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, null=True, srid=4326),
        ),
    ]