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
    """Model definition for Sponsor Type.
    eg. Self, Corporate, Private Insurance
    """

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
    '''
    Model definition for Sponsor Status: Valid/Suspended
    '''
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
    '''
    Model definition for sponsor
    '''
    SponsorID = models.CharField(_("Sponsor ID"), max_length=250, default=sponsorID)
    SponsorName = models.CharField(_("Sponsor Name"), max_length=250)
    SponsorTypeID = models.ForeignKey(SponsorType, verbose_name=_("Sponsor Type"), max_length=250, on_delete=models.SET_NULL, null=True)
    SponsorStatusID = models.ForeignKey(SponsorStatus, verbose_name=_("Sponsor Status"), max_length=250, on_delete=models.SET_NULL, null=True, default=1)
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
        return self.SponsorName

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
        return self.DepartmentName

    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"department_id": self.DepartmentID})


class InsuranceGroup(models.Model):
    '''
    this class shows the group of insurance: corporate, private insurance, health insurance, cash, etc
    '''
    InsuranceGroupID = models.CharField(_("Insurance Group ID"), max_length=250)
    InsuranceGroupName = models.CharField(_("Insurance Group Name"), max_length=520)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Billing Account Status"), default=True, editable=False)
    CreatedAt = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Insurance Group")
        verbose_name_plural = _("Insurance Groups")

    def __str__(self):
        return self.InsuranceGroupName

    def get_absolute_url(self):
        return reverse("InsuranceGroup_detail", kwargs={"issurance_group_id": self.InsuranceGroupID})

class ReceiptType(models.Model):
    '''
    this class sets the receipt type of an insurance scheme whether the scheme is billed in cash/credit
    '''
    ReceiptTypeID = models.CharField(_("ReceiptTypeID"), max_length=250)
    ReceiptTypeName = models.CharField(_("Receipt Type Name"), max_length=50)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Billing Account Status"), default=True, editable=False)
    CreatedAt = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Receipt Type")
        verbose_name_plural = _("Receipt Types")

    def __str__(self):
        return self.ReceiptTypeName

    def get_absolute_url(self):
        return reverse("receipt_type_detail", kwargs={"receipt_type_id": self.ReceiptTypeID})



class BillingCategory(models.Model):
    '''
    this class helps to set configuration on pricing for insurance categories
    '''
    BillingCategoryID = models.CharField(_("Insurance Type ID"), max_length=250)
    BillingCategoryName = models.CharField(_("Insurance Type Name"), max_length=250)
    ConsultationPercent = models.IntegerField(_("Consultation Percentage"), blank=True, null=True, default=100)
    DrugPercent = models.IntegerField(_("Drug Percentage"), blank=True, null=True, default=100)
    ServicePercent = models.IntegerField(_("Service Percentage"), blank=True, null=True, default=100)
    ItemPercent = models.IntegerField(_("Item Percentage"), blank=True, null=True, default=100)
    TreatmentPercent = models.IntegerField(_("Treatment Percentage"), blank=True, null=True, default=100)
    DiagnosisPercent = models.IntegerField(_("Diagnosis Percentage"), blank=True, null=True, default=100)
    LabTestercent = models.IntegerField(_("Lab Test Percentage"), blank=True, null=True, default=100)
    BedPercent = models.IntegerField(_("Bed Percentage"), blank=True, null=True, default=100)

    class Meta:
        verbose_name = _("Billing Category")
        verbose_name_plural = _("Billing Categories")

    def __str__(self):
        return self.BillingCategoryName

    def get_absolute_url(self):
        return reverse("insurance_type_detail", kwargs={"insurance_type_id": self.pk})


class InsuranceScheme(models.Model):
    '''
    this class is the different insurance schemes offered by sponsors
    '''
    InsuranceSchemeID = models.CharField(_("Insurance Scheme ID"), max_length=250)
    InsuranceSchemeName = models.CharField(_("Insurance Scheme Name"), max_length=250)
    BillingCategoryID = models.ForeignKey(BillingCategory, verbose_name=_("Billing Category"), on_delete=models.CASCADE)
    SponsorID = models.ForeignKey(Sponsor, verbose_name=_("Sponsor"), on_delete=models.CASCADE)
    ReceiptTypeID = models.ForeignKey(ReceiptType, verbose_name=_("Receipt Type"), on_delete=models.SET_NULL, null=True)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Billing Account Status"), default=True, editable=False)
    CreatedAt = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Insurance Scheme")
        verbose_name_plural = _("Insurance Schemes")

    def __str__(self):
        return self.InsuranceSchemeName

    def get_absolute_url(self):
        return reverse("insurance_scheme_detail", kwargs={"insurance_scheme_id": self.InsuranceSchemeID})




class BillingAccount(models.Model): #insuredpatient
    MainAccountHolderID = models.ForeignKey(MainAccountHolder, verbose_name=_("Main Bill Account"), on_delete=models.SET_NULL, null=True, default=2)
    #if the sponsor account of the patient is not cash and the patient is an adult, insert record into MainAccountHolder table
    BillingAccountID = models.CharField(_("Billing Account No."), max_length=250, default=billingAccountID)
    BillingAccountName = models.CharField(_("Billing Account"), max_length=250, editable=False, blank=True)
    PatientID = models.ForeignKey(Patient, verbose_name=_("Patient No."), on_delete=models.CASCADE)
    InsuranceSchemeID = models.ForeignKey(InsuranceScheme, verbose_name=_("Sponsor Account"), on_delete=models.CASCADE)
    RelationTypeID = models.ForeignKey(RelationType, verbose_name=_("Relation"), on_delete=models.SET_DEFAULT, default=1)
    InsuranceNumber = models.CharField(_("Insurance Number"), max_length=250)
    DepartmentID = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.SET_NULL, null=True)
    SponsorStatusID = models.ForeignKey(SponsorStatus, verbose_name=_("Status"), on_delete=models.SET_NULL, null=True, default=1)
    ExpiryDate = models.DateField(_("Expiry Date"), blank=True, null=True)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Billing Account Status"), default=True, editable=False)
    CreatedAt = models.DateTimeField(_("Created At"), auto_now_add=True)
    ReceiptType = models.ForeignKey(ReceiptType, verbose_name=_("Receipt Type"), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Billing Account")
        verbose_name_plural = _("Billing Accounts")

    def __str__(self):
        return f'{self.PatientID} - [{ self.InsuranceSchemeID }]'

    def get_absolute_url(self):
        return reverse("billing_account_detail", kwargs={"billing_account_id": self.BillingAccountID})

    

