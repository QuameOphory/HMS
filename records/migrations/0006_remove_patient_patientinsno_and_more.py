# Generated by Django 4.1 on 2022-08-17 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_remove_patient_patientdependenttypeid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='PatientInsNo',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='PatientInsSchemeID',
        ),
        migrations.AlterField(
            model_name='patient',
            name='Status',
            field=models.BooleanField(default=True, editable=False, verbose_name='Patient Status'),
        ),
    ]
