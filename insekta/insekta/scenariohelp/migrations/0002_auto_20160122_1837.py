# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-22 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenariohelp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HelpedQuestion',
            new_name='SeenQuestion',
        ),
    ]
