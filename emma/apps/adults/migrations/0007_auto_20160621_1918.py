# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-22 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
        ('adults', '0006_auto_20160529_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='First name')),
                ('last_name', models.CharField(max_length=25, verbose_name='Last name')),
                ('relation', models.CharField(max_length=25, verbose_name='Relation')),
                ('cell_phone', models.CharField(max_length=25, verbose_name='Cell Phone')),
                ('home_phone', models.CharField(max_length=25, verbose_name='Home Phone')),
            ],
            options={
                'verbose_name': 'Emergency Contact',
                'verbose_name_plural': 'Emergency Contacts',
            },
        ),
        migrations.CreateModel(
            name='MedicalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(max_length=25, verbose_name='Blood Type')),
                ('hospital_preferably', models.CharField(max_length=25, verbose_name='Hospital Preferably')),
                ('knows_pda', models.CharField(max_length=25, verbose_name='Knows PDA')),
                ('exercise_pda', models.CharField(max_length=25, verbose_name='Exercise PDA')),
                ('has_medical_insurance', models.BooleanField(default=False, verbose_name='Has Medical Insurance')),
                ('insurance_company', models.CharField(max_length=25, verbose_name='Insurance Company')),
                ('policy_number', models.CharField(max_length=25, verbose_name='Insurance Company')),
                ('policy_expiration_date', models.DateField(verbose_name='Policy Experation Date')),
                ('has_social_security', models.BooleanField(verbose_name='Has Social Security')),
                ('social_security_number', models.CharField(max_length=25, verbose_name='Social Security Number')),
                ('diseases', models.CharField(max_length=25, verbose_name='Diseases')),
                ('current_medications', models.CharField(max_length=25, verbose_name='Current Medications')),
                ('drug_allergy', models.CharField(max_length=25, verbose_name='Drug Allergy')),
                ('food_allergy', models.CharField(max_length=25, verbose_name='Food Allergy')),
            ],
            options={
                'verbose_name': 'Medical Information',
                'verbose_name_plural': 'Medical Information',
            },
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='adult',
        ),
        migrations.RemoveField(
            model_name='adult',
            name='emergency_phone',
        ),
        migrations.RemoveField(
            model_name='adult',
            name='marital_status',
        ),
        migrations.RemoveField(
            model_name='adult',
            name='phone',
        ),
        migrations.AddField(
            model_name='adult',
            name='familiar_structure',
            field=models.CharField(default=1, max_length=30, verbose_name='Familiar Structure'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adult',
            name='personality',
            field=models.CharField(default=1, max_length=30, verbose_name='Personality'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.AddField(
            model_name='medicalinfo',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.Doctor', verbose_name='Doctor'),
        ),
        migrations.AddField(
            model_name='medicalinfo',
            name='emergency_contact_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_contact_1', to='adults.EmergencyContact', verbose_name=b'Emergency Contact #1'),
        ),
        migrations.AddField(
            model_name='medicalinfo',
            name='emergency_contact_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_contact_2', to='adults.EmergencyContact', verbose_name=b'Emergency Contact #2'),
        ),
        migrations.AddField(
            model_name='adult',
            name='medical_information',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='adults.MedicalInfo', verbose_name='Medical Information'),
            preserve_default=False,
        ),
    ]
