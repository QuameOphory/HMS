# Generated by Django 4.1 on 2022-08-17 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_alter_patient_patientdependenttypeid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='PatientDependentTypeID',
        ),
    ]