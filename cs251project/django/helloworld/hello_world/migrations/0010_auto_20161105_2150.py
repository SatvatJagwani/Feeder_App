# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 16:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0009_auto_20161105_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='endsem_exam_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='midsem_exam_date',
        ),
        migrations.AlterField(
            model_name='assignmentdeadline',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 5, 21, 50, 15, 631000)),
        ),
        migrations.AlterField(
            model_name='feedbackform',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 5, 21, 50, 15, 630000)),
        ),
    ]
