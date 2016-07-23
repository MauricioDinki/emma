# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-21 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20160717_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hiredservice',
            name='workshops',
        ),
        migrations.AddField(
            model_name='hiredservice',
            name='workshops',
            field=models.ManyToManyField(to='services.Workshop', verbose_name='Workshops'),
        ),
    ]