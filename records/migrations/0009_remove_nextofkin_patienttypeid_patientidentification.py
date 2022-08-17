# Generated by Django 4.1 on 2022-08-17 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_remove_nextofkin_entrydate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nextofkin',
            name='PatientTypeID',
        ),
        migrations.CreateModel(
            name='PatientIdentification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdentificationNumber', models.CharField(max_length=255, verbose_name='ID Number')),
                ('IdentificationExpiry', models.DateField(blank=True, null=True, verbose_name='Date of Expiry')),
                ('IdentificationPictureFront', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Front Picture of ID')),
                ('IdentificationPictureBack', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Back Picture of ID')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, editable=False)),
                ('IdentificationType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.identificationtype', verbose_name='Type of Identification')),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.patient', verbose_name='Patient')),
            ],
            options={
                'verbose_name': 'Patient Identification',
                'verbose_name_plural': 'Patient Identifications',
            },
        ),
    ]
