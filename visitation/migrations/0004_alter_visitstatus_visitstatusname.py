# Generated by Django 4.1 on 2022-09-03 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitation', '0003_remove_visitstatus_manualvisitnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitstatus',
            name='VisitStatusName',
            field=models.CharField(max_length=250, verbose_name='Visit Status Name'),
        ),
    ]