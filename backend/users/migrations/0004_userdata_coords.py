# Generated by Django 3.0.5 on 2020-04-05 06:40

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_create_extensions'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='coords',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
