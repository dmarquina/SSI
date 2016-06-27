# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 04:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0003_remove_task_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('date', models.DateTimeField(null=True, verbose_name='fecha')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task', verbose_name='tarea')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]