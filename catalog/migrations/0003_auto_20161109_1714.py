# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20161104_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogentry',
            name='decay_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
