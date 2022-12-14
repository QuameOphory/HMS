# Generated by Django 4.1 on 2022-09-02 23:12

import billing.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_alter_billgroupcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billgroup',
            name='BillGroupID',
            field=models.CharField(default=billing.models.generateBillGroupID, max_length=250, verbose_name='BillGroup ID'),
        ),
        migrations.AlterField(
            model_name='billgrouptype',
            name='BillGroupTypeID',
            field=models.CharField(default=billing.models.generateBillGroupTypeID, max_length=250, verbose_name='BillGroup Type'),
        ),
    ]
