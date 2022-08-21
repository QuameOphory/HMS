# Generated by Django 4.1 on 2022-08-21 10:48

from django.db import migrations, models
import django.db.models.deletion
import sponsor.models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0018_alter_patient_patientrank_and_more'),
        ('sponsor', '0005_alter_billingaccount_sponsorstatusid'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaccount',
            name='ReceiptType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sponsor.receipttype', verbose_name='Receipt Type'),
        ),
        migrations.AlterField(
            model_name='billingaccount',
            name='BillingAccountID',
            field=models.CharField(default=sponsor.models.billingAccountID, max_length=250, verbose_name='Billing Account No.'),
        ),
        migrations.AlterField(
            model_name='billingaccount',
            name='PatientID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.patient', verbose_name='Patient No.'),
        ),
    ]
