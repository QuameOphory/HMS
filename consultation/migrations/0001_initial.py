# Generated by Django 4.1 on 2022-09-02 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facility', '0001_initial'),
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ConsultationTypeID', models.CharField(max_length=250, verbose_name='Consultation Type ID')),
                ('ConsultationTypeName', models.CharField(max_length=250, verbose_name='Consultation Type')),
                ('CashConsultationFee', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cash Cons. Fee')),
                ('RegistrationFee', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Registration Fee')),
                ('ReviewFee', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, verbose_name='Review Fee')),
                ('Description', models.TextField(blank=True, editable=False, null=True, verbose_name='Desccription')),
                ('Status', models.BooleanField(default=True, editable=False, verbose_name='Status of Visit Type')),
                ('CreatedAt', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('BillGroupID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.billgroup', verbose_name='')),
                ('DepartmentID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='facility.department', verbose_name='Department')),
            ],
            options={
                'verbose_name': 'Consultation Type',
                'verbose_name_plural': 'Consultation Types',
            },
        ),
    ]
