# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 04:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='observations',
            field=models.CharField(default=datetime.datetime(2016, 6, 21, 4, 33, 15, 461118, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='progress',
            field=models.IntegerField(default=0),
        ),
    ]
