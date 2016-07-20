# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-16 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adults', '0017_auto_20160713_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalinfo',
            name='adult_name',
            field=models.CharField(default='mauricio mejia', max_length=50, verbose_name='Adult Full Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medicalinfo',
            name='current_medications',
            field=models.TextField(verbose_name='Current Medications'),
        ),
        migrations.AlterField(
            model_name='medicalinfo',
            name='diseases',
            field=models.TextField(verbose_name='Diseases'),
        ),
        migrations.AlterField(
            model_name='medicalinfo',
            name='drug_allergy',
            field=models.TextField(verbose_name='Drug Allergy'),
        ),
        migrations.AlterField(
            model_name='medicalinfo',
            name='food_allergy',
            field=models.TextField(verbose_name='Food Allergy'),
        ),
    ]