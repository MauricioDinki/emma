# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-15 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suscriptions', '0008_auto_20160914_2306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name': 'Report', 'verbose_name_plural': 'Reports'},
        ),
        migrations.RemoveField(
            model_name='history',
            name='mood',
        ),
    ]