# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-26 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_remove_servicecontractprocess_service_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicecontractprocess',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='servicecontractprocess',
            name='user',
        ),
        migrations.RemoveField(
            model_name='hiredservice',
            name='service_days',
        ),
        migrations.RemoveField(
            model_name='hiredservice',
            name='workshops',
        ),
        migrations.AddField(
            model_name='hiredservice',
            name='certifications',
            field=models.TextField(blank=True, null=True, verbose_name='Certifications'),
        ),
        migrations.AddField(
            model_name='hiredservice',
            name='emma_type',
            field=models.CharField(blank=True, choices=[(b'emma', b'Emma'), (b'frank', b'Frank')], max_length=30, null=True, verbose_name='Emma preference'),
        ),
        migrations.AddField(
            model_name='hiredservice',
            name='knowledges',
            field=models.TextField(blank=True, null=True, verbose_name='Knowledges'),
        ),
        migrations.AddField(
            model_name='hiredservice',
            name='languages',
            field=models.TextField(blank=True, null=True, verbose_name='Languages'),
        ),
        migrations.AddField(
            model_name='hiredservice',
            name='skills',
            field=models.TextField(blank=True, null=True, verbose_name='Skills'),
        ),
        migrations.DeleteModel(
            name='ServiceContractProcess',
        ),
    ]
