# Generated by Django 4.1 on 2022-08-20 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0017_alter_patient_patientcategory'),
        ('sponsor', '0002_alter_billingaccount_mainaccountholderid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaccount',
            name='RelationTypeID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='records.relationtype', verbose_name='Relation'),
        ),
    ]
