# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-17 20:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180217_1908'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewEvent',
            new_name='Event',
        ),
    ]