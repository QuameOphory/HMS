from django.db import models
from django.utils.translation import gettext_lazy as _
import helpers
import datetime
# Create your models here.

LENGTH = 9

def generatePatientID():
    '''
    This function generates an ID for a patient record
    '''
    qs = Patient.objects.all().order_by('-CreatedAt')
    if qs.count() == 0:
        patientID = 'P000000001'
    else:
        last_id = qs[0].id
        new_id = int(last_id) + 1
        patientID = 'P' + str(new_id).zfill(LENGTH)
    return patientID

def generateNextOfKinID():
    '''
    This function generates an ID for a patient record
    '''
    qs = NextOfKin.objects.all().order_by('-CreatedAt')
    if qs.count() == 0:
        patientID = 'K000000001'
    else:
        last_id = qs[0].id
        new_id = int(last_id) + 1
        patientID = 'K' + str(new_id).zfill(LENGTH)
    return patientID


class Title(models.Model):
    TitleName = models.CharField(_("Title Name"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Title"
        verbose_name_plural = "Titles"
    
    def __str__(self) -> str:
        return f'{self.TitleName}'

class RelationType(models.Model):
    RelationTypeName = models.CharField(_("Relation Type"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Relation Type"
        verbose_name_plural = "Relation Types"
    
    def __str__(self) -> str:
        return f'{self.RelationTypeName}'

class PatientType(models.Model):
    PatientTypeName = models.CharField(_("Patient Type Name"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Patient Type"
        verbose_name_plural = "Patient Types"
    
    def __str__(self) -> str:
        return f'{self.PatientTypeName}'

class Gender(models.Model):
    GenderName = models.CharField(_("Gender Name"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Gender"
        verbose_name_plural = "Genders"
    
    def __str__(self) -> str:
        return f'{self.GenderName}'

class MaritalStatus(models.Model):
    MaritalStatusName = models.CharField(_("Marital Status Name"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Marital Status"
        verbose_name_plural = "Marital Statuses"
    
    def __str__(self) -> str:
        return f'{self.MaritalStatusName}'

class PatientInsScheme(models.Model):
    PatientInsSchemeID = models.CharField(_("Insurance Scheme ID"), max_length=255)
    PatientInsSchemeName = models.CharField(_("Insurance Scheme Name"), max_length=255)
    Address = models.TextField(_("Address"), blank=True, null=True)
    City = models.CharField(_("City"), blank=True, null=True, max_length=255)
    Location = models.CharField(_("Location"), blank=True, null=True, max_length=255)
    OfficePhone = models.CharField(_("Office Phone"), blank=True, null=True, max_length=255)
    OfficeFax = models.CharField(_("Office Fax"), blank=True, null=True, max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True, editable=False)

    class Meta:
        verbose_name = "Insurance Scheme"
        verbose_name_plural = "Insurance Schemes"
    
    def __str__(self) -> str:
        return f'{self.PatientInsSchemeID}'

class Country(models.Model):
    CountryName = models.CharField(_("Country"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Country Status"), default=True, editable=False)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
    
    def __str__(self) -> str:
        return f'{self.CountryName}'

class Religion(models.Model):
    ReligionName = models.CharField(_("Name of Religion"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Religion Status"), default=True, editable=False)

    class Meta:
        verbose_name = "Religion"
        verbose_name_plural = "Religions"
    
    def __str__(self) -> str:
        return f'{self.ReligionName}'

class DependentType(models.Model):
    DependentName = models.CharField(_("Dependent Type"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Dependent Type Status"), default=True, editable=False)

    class Meta:
        verbose_name = "Dependent Type"
        verbose_name_plural = "Dependent Types"
    
    def __str__(self) -> str:
        return f'{self.DependentName}'


class Patient(models.Model):
    PatientID = models.CharField(_("PatientID"), max_length=255, default=generatePatientID, unique=True)
    EmailAddress = models.CharField(_("Email Address"), max_length=255)
    TitleID = models.ForeignKey(Title, verbose_name = _("Title"), on_delete=models.SET_DEFAULT, default='1')
    FirstName = models.CharField(_("First Name"), max_length=255)
    SurName = models.CharField(_("Surname"), max_length=255)
    OtherName = models.CharField(_("Other Name"), max_length=255, blank=True)
    BirthDate = models.DateField(_("Date of Birth"))
    PatientTypeID = models.ForeignKey(PatientType, verbose_name =  _("Patient Type"), on_delete=models.SET_DEFAULT, default='NONE')
    GenderID = models.ForeignKey(Gender,  verbose_name = _("Gender"), on_delete=models.SET_NULL, null=True)
    Occupation = models.CharField(_("Occupation"), max_length=255)
    BusinessPhone = models.CharField(_("Business Phone"), max_length=255)
    ResidencePhone = models.CharField(_("Business Phone"), max_length=255)
    ResidenceAddress = models.TextField(_("Residence Address"))
    BusinessAddress = models.TextField(_("Business Address"), blank=True, null=True)
    CountryID = models.ForeignKey(Country, verbose_name =  _("Country"), on_delete=models.SET_NULL, default='NONE', blank=True, null=True)
    ReligionID = models.ForeignKey(Religion, verbose_name =  _("Religion"), on_delete=models.SET_NULL, default='NONE', blank=True, null=True)
    MaritalStatusID = models.ForeignKey(MaritalStatus, verbose_name =  _("Marital Status"), on_delete=models.SET_NULL, default='NONE', blank=True, null=True) 
    CreatedAt = models.DateTimeField(auto_now_add=True)
    Status = models.BooleanField(_("Patient Status"), default=True, editable=False)
    PatientRankLevel = models.ForeignKey('PatientRankLevel', verbose_name=_("Patient Rank Level"), on_delete=models.SET_NULL, null=True, default=1, editable=False)
    PatientRank = models.ForeignKey('PatientRank', verbose_name=_("Patient Level"), on_delete=models.SET_NULL, null=True, default=1, editable=False)
    PatientCategory = models.ForeignKey('PatientCategory', verbose_name=_("Patient Category"), on_delete=models.SET_NULL, null=True, default=1, editable=False)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
    
    def __str__(self) -> str:
        return f'{self.FirstName}  {self.OtherName}  {self.SurName}'

    def save(self, *args, **kwargs):
        '''
        The save function has been overriden to set the patient type
        '''
        adult = PatientType.objects.get(id=3)
        child = PatientType.objects.get(id=2)
        today = datetime.date.today()
        
        age = int(str((today - self.BirthDate) // 360)[0:2])
        if age < 18:
            self.PatientTypeID = child
        else:
            self.PatientTypeID = adult
        return super(Patient, self).save(*args, **kwargs)

class PatientRank(models.Model):
    PatientRankName = models.CharField(_("Patient Rank Name"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Patient Rank Status"), default=True, editable=False)

    class Meta:
        verbose_name = "Patient Rank"
        verbose_name_plural = "Patient Ranks"
    
    def __str__(self) -> str:
        return f'{self.PatientRankName}'

class PatientCategory(models.Model):
    PatientCategoryName = models.CharField(_("Patient Category Name"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Patient Rank Status"), default=True, editable=False)

    class Meta:
        verbose_name = "Patient Category"
        verbose_name_plural = "Patient Categories"
    
    def __str__(self) -> str:
        return f'{self.PatientCategoryName}'

class PatientRankLevel(models.Model):
    PatientRankLevelName = models.CharField(_("Patient Rank Level Name"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Patient Rank Level Status"), default=True)

    class Meta:
        verbose_name = "Patient Rank Level"
        verbose_name_plural = "Patient Rank Levels"
    
    def __str__(self) -> str:
        return f'{self.PatientRankLevelName}'

class PatientUnit(models.Model):
    PatientUnitName = models.CharField(_("Patient Unit"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Patient Unit Status"), default=True)

    class Meta:
        verbose_name = "Patient Unit"
        verbose_name_plural = "Patient Units"
    
    def __str__(self) -> str:
        return f'{self.PatientUnitName}'

class IdentificationType(models.Model):
    IdentificationTypeName = models.CharField(_("Type of Identification"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Identification Type Status"), default=True)

    class Meta:
        verbose_name = "Identification Type"
        verbose_name_plural = "Identification Types"
    
    def __str__(self) -> str:
        return f'{self.IdentificationTypeName}'

class NextOfKin(models.Model):
    NextOfKinID = models.CharField(_("Next of Kin ID"), max_length=255, unique=True, default=generateNextOfKinID)
    PatientID = models.ForeignKey(Patient, verbose_name = _("Patient"),  on_delete=models.CASCADE, db_index=True)
    NextOfKinName = models.CharField(_("Name of Next of Kin"), max_length=255)
    RelationTypeID = models.ForeignKey(RelationType, verbose_name = _("Relation To Patient"), on_delete=models.SET_NULL, null=True)
    ContactAddress = models.TextField()
    DateOfBirth = models.DateField(_("Date of Birth"), blank=True, null=True)
    Email = models.CharField(_("Email Address"), max_length=255, blank=True, null=True)
    CreatedAt = models.DateTimeField(_("Date Created"), auto_now_add=True)    
    Status = models.BooleanField(_("Next of Kin Status"), default=True, editable=False)

    class Meta:
        verbose_name = "Next of Kin"
        verbose_name_plural = "Next of Kins"

    def __str__(self) -> str:
        return f'{self.PatientID} [{self.NextOfKinName}]'

class PatientIdentification(models.Model):
    PatientID = models.ForeignKey(Patient, verbose_name = _("Patient"), on_delete=models.CASCADE)
    IdentificationType = models.ForeignKey(IdentificationType, verbose_name = _("Type of Identification"), on_delete=models.SET_NULL, null=True, blank=True)
    IdentificationNumber = models.CharField(_("ID Number"), max_length=255)
    IdentificationExpiry = models.DateField(_("Date of Expiry"), blank=True, null=True)
    IdentificationPictureFront = models.ImageField(_("Front Picture of ID"), upload_to = '', blank=True, null=True)
    IdentificationPictureBack = models.ImageField(_("Back Picture of ID"), upload_to = '', blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(default=True, editable=False)

    class Meta:
        verbose_name = "Patient Identification"
        verbose_name_plural = "Patient Identifications"

    def __str__(self) -> str:
        return f'{self.PatientID} [{self.IdentificationNumber}]'
