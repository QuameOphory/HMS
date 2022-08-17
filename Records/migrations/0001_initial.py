# Generated by Django 4.1 on 2022-08-17 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CountryName', models.CharField(max_length=255, verbose_name='Country')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='DependentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DependentName', models.CharField(max_length=255, verbose_name='Name of Religion')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Dependent Type',
                'verbose_name_plural': 'Dependent Types',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GenderName', models.CharField(max_length=255, verbose_name='Gender Name')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='IdentificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdentificationTypeName', models.CharField(max_length=255, verbose_name='Type of Identification')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Identification Type',
                'verbose_name_plural': 'Identification Types',
            },
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaritalStatusName', models.CharField(max_length=255, verbose_name='Marital Status Name')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Marital Status',
                'verbose_name_plural': 'Marital Statuses',
            },
        ),
        migrations.CreateModel(
            name='PatientInsScheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientInsSchemeID', models.CharField(max_length=255, verbose_name='Insurance Scheme ID')),
                ('PatientInsSchemeName', models.CharField(max_length=255, verbose_name='Insurance Scheme Name')),
                ('Address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('City', models.CharField(blank=True, max_length=255, null=True, verbose_name='City')),
                ('Location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
                ('OfficePhone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Office Phone')),
                ('OfficeFax', models.CharField(blank=True, max_length=255, null=True, verbose_name='Office Fax')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Insurance Scheme',
                'verbose_name_plural': 'Insurance Schemes',
            },
        ),
        migrations.CreateModel(
            name='PatientRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientRankName', models.CharField(max_length=255, verbose_name='Patient Rank Name')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Patient Rank',
                'verbose_name_plural': 'Patient Ranks',
            },
        ),
        migrations.CreateModel(
            name='PatientRankLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientRankLevelName', models.CharField(max_length=255, verbose_name='Patient Rank Level Name')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Patient Rank Level',
                'verbose_name_plural': 'Patient Rank Levels',
            },
        ),
        migrations.CreateModel(
            name='PatientType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientTypeName', models.CharField(max_length=255, verbose_name='Patient Type Name')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Patient Type',
                'verbose_name_plural': 'Patient Types',
            },
        ),
        migrations.CreateModel(
            name='PatientUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientUnitName', models.CharField(max_length=255, verbose_name='Patient Unit')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Patient Unit',
                'verbose_name_plural': 'Patient Units',
            },
        ),
        migrations.CreateModel(
            name='RelationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RelationTypeName', models.CharField(max_length=255, verbose_name='Relation Type')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Relation Type',
                'verbose_name_plural': 'Relation Types',
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReligionName', models.CharField(max_length=255, verbose_name='Name of Religion')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Religion',
                'verbose_name_plural': 'Religions',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TitleName', models.CharField(max_length=255, verbose_name='Title Name')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
            ],
            options={
                'verbose_name': 'Title',
                'verbose_name_plural': 'Titles',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmailAddress', models.CharField(max_length=255, verbose_name='Email Address')),
                ('FirstName', models.CharField(max_length=255, verbose_name='First Name')),
                ('SurName', models.CharField(max_length=255, verbose_name='Surname')),
                ('OtherName', models.CharField(max_length=255, verbose_name='Other Name')),
                ('BirthDate', models.DateField(verbose_name='Date of Birth')),
                ('Occupation', models.CharField(max_length=255, verbose_name='Occupation')),
                ('BusinessPhone', models.CharField(max_length=255, verbose_name='Business Phone')),
                ('ResidencePhone', models.CharField(max_length=255, verbose_name='Business Phone')),
                ('ResidenceAddress', models.TextField(verbose_name='Residence Address')),
                ('BusinessAddress', models.TextField(blank=True, null=True, verbose_name='Business Address')),
                ('PatientInsNo', models.CharField(max_length=255, verbose_name='Patient Insurance Number')),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('Status', models.BooleanField(default=True, verbose_name='Relation Type Status')),
                ('CountryID', models.ForeignKey(default='NONE', on_delete=django.db.models.deletion.SET_DEFAULT, to='records.country', verbose_name='Country')),
                ('GenderID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.gender', verbose_name='Gender')),
                ('MaritalStatusID', models.ForeignKey(default='NONE', on_delete=django.db.models.deletion.SET_DEFAULT, to='records.maritalstatus', verbose_name='Marital Status')),
                ('PatientDependentTypeID', models.ForeignKey(default='SELF', on_delete=django.db.models.deletion.SET_DEFAULT, to='records.dependenttype', verbose_name='Dependent')),
                ('PatientInsSchemeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.patientinsscheme', verbose_name='Patient Insurance Scheme')),
                ('PatientTypeID', models.ForeignKey(default='NONE', on_delete=django.db.models.deletion.SET_DEFAULT, to='records.patienttype', verbose_name='Patient Type')),
                ('ReligionID', models.ForeignKey(default='NONE', on_delete=django.db.models.deletion.SET_DEFAULT, to='records.religion', verbose_name='Religion')),
                ('TitleID', models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to='records.title', verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
        ),
        migrations.CreateModel(
            name='NextOfKin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NextOfKinID', models.CharField(max_length=255, unique=True, verbose_name='Next of Kin ID')),
                ('NextOfKinName', models.CharField(max_length=255, verbose_name='Name of Next of Kin')),
                ('ContactAddress', models.TextField()),
                ('DateOfBirth', models.DateField(verbose_name='Date of Birth')),
                ('Email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Email Address')),
                ('Profession', models.CharField(max_length=255, verbose_name='Profession')),
                ('CreatedAt', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('EntryDate', models.DateTimeField(auto_now_add=True, verbose_name='Entry Date')),
                ('KeyPrefix', models.CharField(blank=True, max_length=255, null=True, verbose_name='Key Prefix')),
                ('ServiceNo', models.CharField(max_length=255, verbose_name='Service No.')),
                ('IdentificationNumber', models.CharField(max_length=255, verbose_name='ID Number')),
                ('Status', models.BooleanField(default=True, verbose_name='Next of Kin Status')),
                ('IdentificationTypeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.identificationtype', verbose_name='ID Type')),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.patient', verbose_name='Patient')),
                ('PatientRankID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.patientrank', verbose_name='Patient Rank')),
                ('PatientRankLevelID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.patientranklevel', verbose_name='Patient Rank Level')),
                ('PatientTypeID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='records.patienttype', verbose_name='Patient Category')),
                ('PatientUnitID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.patientunit', verbose_name='Patient Unit')),
                ('RelationTypeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.relationtype', verbose_name='Relation with Patient')),
            ],
            options={
                'verbose_name': 'Next of Kin',
                'verbose_name_plural': 'Next of Kins',
            },
        ),
    ]
