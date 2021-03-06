# Generated by Django 3.0.5 on 2020-04-04 08:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField(null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('description', models.TextField(null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
    ]
