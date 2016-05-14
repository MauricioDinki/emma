# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 03:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emmas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HiredService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_per_week', models.PositiveSmallIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reference', models.CharField(max_length=25)),
                ('frequency', models.CharField(max_length=25)),
                ('coordinator', models.CharField(max_length=25)),
                ('emma_alternate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emma_alternate', to='emmas.Emma')),
                ('emma_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emma_assigned', to='emmas.Emma')),
            ],
            options={
                'verbose_name': 'Hired service',
                'verbose_name_plural': 'Hired services',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
            options={
                'verbose_name': 'Workshop',
                'verbose_name_plural': 'Workshops',
            },
        ),
        migrations.AddField(
            model_name='hiredservice',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service'),
        ),
    ]
