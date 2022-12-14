# Generated by Django 4.1 on 2022-09-02 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0002_alter_branch_branchid_alter_department_departmentid_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'Branch', 'verbose_name_plural': 'Branches'},
        ),
        migrations.AlterField(
            model_name='branch',
            name='HospitalID',
            field=models.ForeignKey(default='H001', null=True, on_delete=django.db.models.deletion.SET_NULL, to='facility.hospital', verbose_name='Hospital'),
        ),
    ]
