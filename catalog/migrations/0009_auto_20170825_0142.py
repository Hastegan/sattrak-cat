# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-25 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20170822_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogentry',
            name='added',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='catalogentry',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
        migrations.RenameField(
            model_name='tle',
            old_name='date_added',
            new_name='added',
        ),
    ]