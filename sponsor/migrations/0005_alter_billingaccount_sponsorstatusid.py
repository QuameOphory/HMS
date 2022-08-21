# Generated by Django 4.1 on 2022-08-20 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0004_billingaccount_expirydate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaccount',
            name='SponsorStatusID',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sponsor.sponsorstatus', verbose_name='Status'),
        ),
    ]
