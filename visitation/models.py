from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from facility.models import Branch, Department
from records.models import Patient
from sponsor.models import BillingAccount
from consultation.models import ConsultationType
from cashier.models import Receipt
import helpers

# Create your models here.

def generateVisitTypeID():
    qs = VisitType.objects.all()
    return helpers.generateID('V', qs=qs, length=4)

def generateVisitStatusID():
    qs = VisitStatus.objects.all()
    return helpers.generateID('V', qs=qs, length=4)

class VisitType(models.Model):
    '''
    Model definition for types of Visitations: First time, Subsequent, Review, Emergency
    '''
    VisitTypeID = models.CharField(_("Visit Type ID"), max_length=250, default=generateVisitTypeID)
    VisitTypeName = models.CharField(_("Visit Type"), max_length=50)
    VisitTypeCost = models.DecimalField(_("Visit Type Cost"), max_digits=5, decimal_places=2, default=0.00)
    Description = models.TextField(_("Desccription"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Status of Visit Type"), default=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Visit Type")
        verbose_name_plural = _("Visit Types")

    def __str__(self):
        return self.VisitTypeName

    def get_absolute_url(self):
        return reverse("visit_type_detail", kwargs={"visit_type_id": self.VisitTypeID})

class VisitStatus(models.Model):
    '''Model definition for status of visitation: unattended, diagnosed, etc'''
    VisitStatusID = models.CharField(_("Visit Status ID"), max_length=250, default=generateVisitStatusID)
    VisitStatusName = models.CharField(_("Visit Status Name"), max_length=250)
    Description = models.TextField(_("Desccription"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Status of Visit Type"), default=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    

    class Meta:
        verbose_name = _("Visit Status")
        verbose_name_plural = _("Visit Statuses")

    def __str__(self):
        return self.VisitStatusName

    def get_absolute_url(self):
        return reverse("visit_status_detail", kwargs={"visit_status_id": self.VisitStatusID})


def generateVisitationID():
    qs = Visitation.objects.all()
    return helpers.generateVisitationID(qs=qs)

class Visitation(models.Model):
    '''Model definition for visitations / hospital attendance'''
    VisitationID = models.CharField(_("Visitation ID"), max_length=250, default=generateVisitationID, unique=True)
    VisitationName = models.CharField(_("Visitation Name"), max_length=250, blank=True, editable=False, null=True)
    VisitStatusID = models.ForeignKey(VisitStatus, verbose_name=_("Status"), on_delete=models.SET_NULL, null=True)
    PatientID = models.ForeignKey(Patient, verbose_name=_("Patient"), on_delete=models.CASCADE)
    VisitTypeID = models.ForeignKey(VisitType, verbose_name=_("Visit Type"), on_delete=models.SET_NULL, null=True)
    DepartmentID = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.SET_NULL, null=True)
    ConsultationTypeID = models.ForeignKey(ConsultationType, verbose_name=_("Consultation Type"), on_delete=models.SET_NULL, null=True)
    BillingAccountID = models.ForeignKey(BillingAccount, verbose_name=_("Billing Account"), on_delete=models.CASCADE)
    VisitationFee = models.CharField(_("Consultation Fee"), max_length=250)
    ManualReceiptNumber = models.CharField(_("Manual Receipt Number"), max_length=250, blank=True, null=True)
    ReceiptNumber = models.ForeignKey(Receipt, verbose_name=_("Receipt"), on_delete=models.CASCADE, blank=True, null=True)
    VisitDate = models.DateField(_("Visit Date"), auto_now_add=True)
    Description = models.TextField(_("Desccription"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Status of Visit Type"), default=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    

    class Meta:
        verbose_name = _("Visitation")
        verbose_name_plural = _("Visitations")

    def __str__(self):
        return f'{self.PatientID} -- [{self.VisitationID}]'

    def get_absolute_url(self):
        return reverse("visitation_detail", kwargs={"visitation_id": self.VisitationID})

