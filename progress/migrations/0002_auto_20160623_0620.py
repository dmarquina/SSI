# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='fecha'),
        ),
    ]
