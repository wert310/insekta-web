# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-21 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios', '0025_auto_20190616_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]