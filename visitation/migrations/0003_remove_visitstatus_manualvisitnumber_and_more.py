# Generated by Django 4.1 on 2022-09-03 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitation', '0002_alter_visitstatus_visitstatusid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitstatus',
            name='ManualVisitNumber',
        ),
        migrations.AlterField(
            model_name='visitation',
            name='VisitationName',
            field=models.CharField(blank=True, editable=False, max_length=250, null=True, verbose_name='Visitation Name'),
        ),
    ]
