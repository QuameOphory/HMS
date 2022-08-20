from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
import helpers
from records.models import (
    Patient,
    RelationType
)

# Create your models here.

def sponsorStatusID():
    qs = SponsorStatus.objects.all()
    return helpers.generateID('SS', qs)
def sponsorTypeID():
    qs = SponsorType.objects.all()
    return helpers.generateID('ST', qs)
def sponsorID():
    qs = Sponsor.objects.all()
    return helpers.generateID('S', qs)
def mainAccountHolderID():
    qs = MainAccountHolder.objects.all()
    return helpers.generateID('MA', qs)
def billingAccountID():
    qs = BillingAccount.objects.all()
    return helpers.generateID('BA', qs)
def departmentID():
    qs = Department.objects.all()
    return helpers.generateID('D', qs)

class SponsorType(models.Model):
    """Model definition for SponsorType."""

    # TODO: Define fields here
    SponsorTypeID = models.CharField(_('Sponsor Type ID'), max_length=255, default=sponsorTypeID)
    SponsorTypeName = models.CharField(_('Sponsor Type Name'), max_length=255)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Sponsor Type Status"), default=True, editable=False)
    CreatedAt = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        """Meta definition for SponsorType."""

        verbose_name = 'Sponsor Type'
        verbose_name_plural = 'Sponsor Types'

    def __str__(self):
        """Unicode representation of SponsorType."""
        return self.SponsorTypeName

    def get_absolute_url(self):
        return reverse("sponsor_type_detail", kwargs={"sponsor_type_id": self.SponsorTypeID})

def sponsorStatusID():
    qs = SponsorStatus.objects.order_by('-CreatedAt')
    return helpers.generateID('SS', qs)        

class SponsorStatus(models.Model):

    SponsorStatusID = models.CharField(_("Sponsor Status ID"), max_length=250, default=sponsorStatusID)
    SponsorStatusName = models.CharField(_("Sponsor Status Name"), max_length=250)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Status"), default=True, editable=False)
    CreatedAt = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Sponsor Status")
        verbose_name_plural = _("Sponsor Statuses")

    def __str__(self):
        return self.SponsorStatusName

    def get_absolute_url(self):
        return reverse("sponsor_status_detail", kwargs={"sponsor_status_id": self.SponsorStatusID})

class Sponsor(models.Model):

    SponsorID = models.CharField(_("Sponsor ID"), max_length=250, default=sponsorID)
    SponsorName = models.CharField(_("Sponsor Name"), max_length=250)
    SponsorTypeID = models.CharField(_("Sponsor Type"), max_length=250)
    SponsorStatusID = models.CharField(_("Sponsor Status"), max_length=250)
    Address = models.TextField(_("Address"), blank=True, null=True)
    City = models.CharField(_("City"), max_length=250)
    Location = models.CharField(_("Location"), max_length=250, blank=True, null=True)
    OfficePhone = models.CharField(_("Office Phone"), max_length=250)
    OfficeFax = models.CharField(_("Office Fax"), max_length=250)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Sponsor Type Status"), default=True, editable=False)
    CreatedAt = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sponsor_detail", kwargs={"sponsor_id": self.SponsorID})

class MainAccountHolder(models.Model):

    MainAccountHolderID = models.CharField(_("Dependant ID"), max_length=250, default=mainAccountHolderID)
    MainAccountHolderName = models.CharField(_("Dependant Name"), max_length=50)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Sponsor Type Status"), default=True, editable=False)
    CreatedAt = models.DateTimeField(_("Created At"), auto_now_add=True)


    class Meta:
        verbose_name = _("Main Account Holder")
        verbose_name_plural = _("Main Account Holders")

    def __str__(self):
        return self.MainAccountHolderName

    def get_absolute_url(self):
        return reverse("main_account_holder_detail", kwargs={"main_account_holder_id": self.MainAccountHolderID})

class Department(models.Model):

    DepartmentID = models.CharField(_("Department ID"), max_length=250, default=departmentID)
    DepartmentName = models.CharField(_("Department Name"), max_length=250)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Sponsor Type Status"), default=True, editable=False)
    CreatedAt = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"department_id": self.DepartmentID})


class BillingAccount(models.Model):
    MainAccountHolderID = models.ForeignKey(MainAccountHolder, verbose_name=_("Main Bill Account"), on_delete=models.SET_NULL, null=True)
    #if the sponsor account of the patient is not cash and the patient is an adult, insert record into MainAccountHolder table
    BillingAccountID = models.CharField(_("Billing Account ID"), max_length=250, default=billingAccountID)
    BillingAccountName = models.CharField(_("Billing Account"), max_length=250, editable=False, blank=True)
    PatientID = models.ForeignKey(Patient, verbose_name=_("Patient"), on_delete=models.CASCADE)
    SponsorID = models.ForeignKey(Sponsor, verbose_name=_("Sponsor Account"), on_delete=models.CASCADE)
    RelationTypeID = models.ForeignKey(RelationType, verbose_name=_("Relation"), on_delete=models.SET_DEFAULT, default=3)
    InsuranceNumber = models.CharField(_("Insurance Number"), max_length=250)

    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Billing Account Status"), default=True, editable=False)
    CreatedAt = models.DateTimeField(_("Created At"), auto_now_add=True)


    class Meta:
        verbose_name = _("Billing Account")
        verbose_name_plural = _("Billing Accounts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("billing_account_detail", kwargs={"billing_account_id": self.BillingAccountID})

    

