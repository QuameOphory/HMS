# Generated by Django 4.1 on 2022-09-02 22:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('records', '0018_alter_patient_patientrank_and_more'),
        ('facility', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentModeID', models.CharField(max_length=250, verbose_name='Payment Mode ID')),
                ('PaymentModeName', models.CharField(max_length=250, verbose_name='Payment Mode')),
                ('Description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('CreatedAt', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('Status', models.BooleanField(default=True, editable=False, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Payment Mode',
                'verbose_name_plural': 'Payment Modes',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentTypeID', models.CharField(max_length=250, verbose_name='Payment Type')),
                ('PaymentTypeName', models.CharField(max_length=250, verbose_name='Payment Type Name')),
                ('Description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('CreatedAt', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('Status', models.BooleanField(default=True, editable=False, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Payment Type',
                'verbose_name_plural': 'Payment Types',
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReceiptID', models.CharField(max_length=250, verbose_name='Receipt No.')),
                ('ManualReceiptID', models.CharField(blank=True, max_length=250, null=True, verbose_name='Manual Receipt No.')),
                ('ReceiptName', models.CharField(blank=True, editable=False, max_length=250, null=True, verbose_name='Receipt Name')),
                ('ReceiptAmount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Payment Amount')),
                ('ReceiptDate', models.DateField(default=django.utils.timezone.now, verbose_name='Receipt Date')),
                ('Description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('CreatedAt', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('Status', models.BooleanField(default=True, editable=False, verbose_name='Status')),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.patient', verbose_name='Patient')),
                ('PaymentModeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cashier.paymentmode', verbose_name='Payment Mode')),
                ('PaymentTypeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cashier.paymenttype', verbose_name='Payment Type')),
            ],
            options={
                'verbose_name': 'Receipt',
                'verbose_name_plural': 'Receipts',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InvoiceID', models.CharField(max_length=250, verbose_name='Invoice No.')),
                ('InvoiceName', models.CharField(blank=True, editable=False, max_length=250, null=True, verbose_name='Invoice Name')),
                ('InvoiceAmount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Payment Amount')),
                ('InvoiceDate', models.DateField(default=django.utils.timezone.now, verbose_name='Date of Invoice')),
                ('Description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('CreatedAt', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('Status', models.BooleanField(default=True, editable=False, verbose_name='Status')),
                ('DepartmentID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='facility.department', verbose_name='Issuing From')),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.patient', verbose_name='Invoice For')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
    ]
