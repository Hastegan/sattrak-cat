# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-28 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20161109_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='tle',
            name='date_added',
            field=models.DateTimeField(null=True),
        ),
    ]