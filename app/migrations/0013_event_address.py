# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-22 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180219_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default='301 W. Vermont Ave.', max_length=150),
            preserve_default=False,
        ),
    ]
