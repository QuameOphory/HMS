from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from facility.models import Branch
from records.models import Patient
from sponsor.models import BillingAccount
import helpers

# Create your models here.

class VisitType(models.Model):
    '''
    Model definition for types of Visitations: First time, Subsequent, Review, Emergency
    '''
    VisitTypeID = models.CharField(_("Visit Type ID"), max_length=250)
    VisitTypeName = models.CharField(_("Visit Type"), max_length=50)
    VisitTypeCost = models.DecimalField(_("Visit Type Cost"), max_digits=5, decimal_places=2)
    Description = models.TextField(_("Desccription"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Status of Visit Type"), default=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Visit Type")
        verbose_name_plural = _("Visit Types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("visit_type_detail", kwargs={"visit_type_id": self.VisitTypeID})

class HospitalDepartment(models.Model):
    '''
    Model definition for hospital departments: Units in the hospital
    '''
    HospitalDepartmentID = models.CharField(_("Hospital Department ID"), max_length=250)
    HospitalDepartmentName = models.CharField(_("Department"), max_length=250)
    BranchID = models.ForeignKey(Branch, verbose_name=_("Branch"), on_delete=models.SET_NULL, null=True)
    Description = models.TextField(_("Desccription"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Status of Visit Type"), default=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    

    class Meta:
        verbose_name = _("Hospital Department")
        verbose_name_plural = _("Hospital Departments")

    def __str__(self):
        return self.HospitalDepartmentName

    def get_absolute_url(self):
        return reverse("hospital_department_detail", kwargs={"hospital_department_id": self.HospitalDepartmentID})


class ConsultationType(models.Model):
    '''Model definition for the types of consultations'''
    ConsultationTypeID = models.CharField(_("Consultation Type ID"), max_length=250)
    ConsultationTypeName = models.CharField(_("Consultation Type Name"), max_length=250)
    Department = models.ForeignKey(HospitalDepartment, verbose_name=_("Department"), on_delete=models.CASCADE)
    #BillGroupID = models.ForeignKey(BillGroup, verbose_name=_(""), on_delete=models.CASCADE)
    CashConsultationFee = models.DecimalField(_("Cash Cons. Fee"), max_digits=5, decimal_places=2)
    RegistrationFee = models.DecimalField(_("Registration Fee"), max_digits=5, decimal_places=2, blank=True, null=True)
    ReviewFee = models.DecimalField(_("Review Fee"), max_digits=5, decimal_places=2, default=0.00, blank=True)
    Description = models.TextField(_("Desccription"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Status of Visit Type"), default=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Consultation Type")
        verbose_name_plural = _("Consultation Types")

    def __str__(self):
        return self.ConsultationTypeName

    def get_absolute_url(self):
        return reverse("consultation_type_detail", kwargs={"consultation_type_id": self.ConsultationTypeID})


class VisitStatus(models.Model):
    '''Model definition for status of visitation: unattended, diagnosed, etc'''
    VisitStatusID = models.CharField(_("Visit Status ID"), max_length=250)
    VisitStatusName = models.CharField(_("Visit Status Name"), max_length=250, editable=False)
    ManualVisitNumber = models.CharField(_("Manual Visit Number"), max_length=250)
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



class Visitation(models.Model):
    '''Model definition for visitations / hospital attendance'''
    VisitationID = models.CharField(_("Visitation ID"), max_length=250)
    VisitationName = models.CharField(_("Visitation Name"), max_length=250)
    VisitStatusID = models.ForeignKey(VisitStatus, verbose_name=_("Status"), on_delete=models.CASCADE)
    PatientID = models.ForeignKey(Patient, verbose_name=_("Patient"), on_delete=models.CASCADE)
    VisitTypeID = models.ForeignKey(VisitType, verbose_name=_("Visit Type"), on_delete=models.SET_NULL, null=True)
    HospitalDepartmentID = models.ForeignKey(HospitalDepartment, verbose_name=_("Department"), on_delete=models.SET_NULL, null=True)
    ConsultationTypeID = models.ForeignKey(ConsultationType, verbose_name=_("Consultation Type"), on_delete=models.SET_NULL, null=True)
    BillingAccountID = models.ForeignKey(BillingAccount, verbose_name=_("Billing Account"), on_delete=models.CASCADE)
    VisitationFee = models.CharField(_("Consultation Fee"), max_length=250)
    ManualReceiptNumber = models.CharField(_("Manual Receipt Number"), max_length=250, blank=True, null=True)
    #ReceiptNumber = models.ForeignKey('Receipt', verbose_name=_("Receipt"), on_delete=models.CASCADE, blank=True, null=True)
    VisitDate = models.DateField(_("Visit Date"), auto_now_add=True)
    Description = models.TextField(_("Desccription"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Status of Visit Type"), default=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    

    class Meta:
        verbose_name = _("Visitation")
        verbose_name_plural = _("Visitations")

    def __str__(self):
        return self.VisitationName

    def get_absolute_url(self):
        return reverse("visitation_detail", kwargs={"visitation_id": self.VisitationID})

