# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-11 03:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180211_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newevent',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile'),
        ),
    ]
