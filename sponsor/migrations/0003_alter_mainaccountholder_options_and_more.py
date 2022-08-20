# Generated by Django 4.1 on 2022-08-20 15:41

from django.db import migrations, models
import sponsor.models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0002_sponsortype_createdat_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainaccountholder',
            options={'verbose_name': 'Main Account Holder', 'verbose_name_plural': 'Main Account Holders'},
        ),
        migrations.AlterField(
            model_name='billingaccount',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='department',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='mainaccountholder',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='SponsorID',
            field=models.CharField(default=sponsor.models.sponsorID, max_length=250, verbose_name='Sponsor ID'),
        ),
        migrations.AlterField(
            model_name='sponsorstatus',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='sponsortype',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
    ]