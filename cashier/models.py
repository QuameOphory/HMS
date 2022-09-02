from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from records.models import Patient
from django.utils import timezone
from facility.models import Department
# Create your models here.

class PaymentType(models.Model):
    '''
    Model definition for Payment Types: eg: deposit, OPD, Lab, etc
    '''
    PaymentTypeID = models.CharField(_("Payment Type"), max_length=250)
    PaymentTypeName = models.CharField(_("Payment Type Name"), max_length=250)
    Description = models.TextField(_("Description"), blank=True, null=True)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    Status = models.BooleanField(_("Status"), default=True, editable=False)

    class Meta:
        verbose_name = _("Payment Type")
        verbose_name_plural = _("Payment Types")

    def __str__(self):
        return self.PaymentTypeName

    def get_absolute_url(self):
        return reverse("payment_type_detail", kwargs={"payment_type_detail": self.PaymentTypeID})

class PaymentMode(models.Model):

    PaymentModeID = models.CharField(_("Payment Mode ID"), max_length=250)
    PaymentModeName = models.CharField(_("Payment Mode"), max_length=250)
    Description = models.TextField(_("Description"), blank=True, null=True)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    Status = models.BooleanField(_("Status"), default=True, editable=False)
    

    class Meta:
        verbose_name = _("Payment Mode")
        verbose_name_plural = _("Payment Modes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("payment_mode_detail", kwargs={"payment_mode_id": self.PaymentModeID})


class Receipt(models.Model):
    '''
    Model definition for Receipts
    '''
    ReceiptID = models.CharField(_("Receipt No."), max_length=250)
    ManualReceiptID = models.CharField(_("Manual Receipt No."), max_length=250, blank=True, null=True)
    ReceiptName = models.CharField(_("Receipt Name"), max_length=250, blank=True, null=True, editable=False)
    PatientID = models.ForeignKey(Patient, verbose_name=_("Patient"), on_delete=models.CASCADE)
    PaymentTypeID = models.ForeignKey(PaymentType, verbose_name=_("Payment Type"), on_delete=models.SET_NULL, null=True)
    PaymentModeID = models.ForeignKey(PaymentMode, verbose_name=_("Payment Mode"), on_delete=models.SET_NULL, null=True)
    ReceiptAmount = models.DecimalField(_("Payment Amount"), max_digits=5, decimal_places=2)
    ReceiptDate = models.DateField(_("Receipt Date"), default=timezone.now)
    Description = models.TextField(_("Description"), blank=True, null=True)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    Status = models.BooleanField(_("Status"), default=True, editable=False)


    class Meta:
        verbose_name = _("Receipt")
        verbose_name_plural = _("Receipts")

    def __str__(self):
        return self.ReceiptID

    def get_absolute_url(self):
        return reverse("receipt_detail", kwargs={"receipt_id": self.ReceiptID})

class Invoice(models.Model):
    '''
    Model definition for invoices
    '''
    InvoiceID = models.CharField(_("Invoice No."), max_length=250)
    InvoiceName = models.CharField(_("Invoice Name"), max_length=250, blank=True, null=True, editable=False)
    InvoiceAmount = models.DecimalField(_("Payment Amount"), max_digits=5, decimal_places=2)
    DepartmentID = models.ForeignKey(Department, verbose_name=_("Issuing From"), on_delete=models.SET_NULL, null=True)
    PatientID = models.ForeignKey(Patient, verbose_name=_("Invoice For"), on_delete=models.CASCADE)
    InvoiceDate = models.DateField(_("Date of Invoice"), default=timezone.now)
    Description = models.TextField(_("Description"), blank=True, null=True)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    Status = models.BooleanField(_("Status"), default=True, editable=False)

    class Meta:
        verbose_name = _("Invoice")
        verbose_name_plural = _("Invoices")

    def __str__(self):
        return self.InvoiceID

    def get_absolute_url(self):
        return reverse("invoice_detail", kwargs={"invoice_id": self.InvoiceID})

