# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 11:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0005_auto_20170713_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='dataelement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='label.DataElement'),
        ),
    ]
