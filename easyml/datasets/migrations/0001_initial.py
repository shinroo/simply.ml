# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.TechnicalUser')),
            ],
        ),
        migrations.CreateModel(
            name='LabelChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('parentset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Dataset')),
            ],
        ),
        migrations.AddField(
            model_name='dataelement',
            name='parentset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Dataset'),
        ),
    ]
