# Generated by Django 3.0.5 on 2020-04-05 06:38

from django.db import migrations
from django.contrib.postgres.operations import CreateExtension


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200405_1305'),
    ]

    operations = [
        CreateExtension('postgis'),
    ]
