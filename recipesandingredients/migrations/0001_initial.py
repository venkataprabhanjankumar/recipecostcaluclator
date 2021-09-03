# Generated by Django 3.2.6 on 2021-09-01 11:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=225)),
                ('name', models.CharField(max_length=225)),
                ('price', models.IntegerField()),
                ('caseQuantity', models.IntegerField(blank=True, null=True)),
                ('packSize', models.IntegerField(blank=True, null=True)),
                ('qtyUnits', models.CharField(blank=True, max_length=225, null=True)),
                ('category', models.CharField(blank=True, max_length=225, null=True)),
                ('suppliers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=225), blank=True, null=True, size=None)),
                ('orderCode', models.CharField(blank=True, max_length=225, null=True)),
                ('brand', models.CharField(blank=True, max_length=225, null=True)),
                ('countryOfOrigin', models.CharField(blank=True, max_length=225, null=True)),
                ('storageAreas', models.CharField(blank=True, max_length=225, null=True)),
                ('parUnits', models.CharField(blank=True, max_length=225, null=True)),
                ('nutriationData', models.CharField(blank=True, max_length=225, null=True)),
                ('fromMeasurement', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=225), size=None), blank=True, null=True, size=None)),
                ('toMeasurement', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=225), size=None), blank=True, null=True, size=None)),
                ('majorAllergens', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=225), blank=True, null=True, size=None)),
                ('sugarAdded', models.BooleanField(blank=True, null=True)),
                ('usablePercentage', models.IntegerField(blank=True, null=True)),
                ('displayUnits', models.CharField(blank=True, max_length=225, null=True)),
                ('displayName', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
