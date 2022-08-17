from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Title(models.Model):
    TitleName = models.CharField(_("Title Name"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Title"
        verbose_name_plural = "Titles"
    
    def __str__(self) -> str:
        return f'{self.RelationTypeName}'

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
    City = models.CharField(_("City"), blank=True, null=True)
    Location = models.CharField(_("Location"), blank=True, null=True)
    OfficePhone = models.CharField(_("Office Phone"), blank=True, null=True)
    OfficeFax = models.CharField(_("Office Fax"), blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Insurance Scheme"
        verbose_name_plural = "Insurance Schemes"
    
    def __str__(self) -> str:
        return f'{self.PatientInsSchemeID}'

class Country(models.Model):
    CountryName = models.CharField(_("Country"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
    
    def __str__(self) -> str:
        return f'{self.CountryName}'

class Religion(models.Model):
    ReligionName = models.CharField(_("Name of Religion"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Religion"
        verbose_name_plural = "Religions"
    
    def __str__(self) -> str:
        return f'{self.ReligionName}'

class DependentType(models.Model):
    DependentName = models.CharField(_("Name of Religion"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Dependent Type"
        verbose_name_plural = "Dependent Types"
    
    def __str__(self) -> str:
        return f'{self.DependentName}'

class Patient(models.Model):
    EmailAddress = models.CharField(_("Email Address"), max_length=255)
    TitleID = models.ForeignKey(Title, _("Title"), on_delete=models.SET_DEFAULT, default='1')
    FirstName = models.CharField(_("First Name"), max_length=255)
    SurName = models.CharField(_("Surname"), max_length=255)
    OtherName = models.CharField(_("Other Name"), max_length=255)
    BirthDate = models.DateField(_("Date of Birth"))
    PatientTypeID = models.ForeignKey(PatientType, _("Patient Type"), on_delete=models.SET_DEFAULT, default='NONE')
    GenderID = models.ForeignKey(_("Gender"), on_delete=models.SET_NULL, null=True)
    Occupation = models.CharField(_("Occupation"), max_length=255)
    BusinessPhone = models.CharField(_("Business Phone"), max_length=255)
    ResidencePhone = models.CharField(_("Business Phone"), max_length=255)
    ResidenceAddress = models.TextField(_("Residence Address"))
    BusinessAddress = models.TextField(_("Business Address"), blank=True, null=True)
    CountryID = models.ForeignKey(Country, _("Country"), on_delete=models.SET_DEFAULT, default='NONE')
    ReligionID = models.ForeignKey(Religion, _("Religion"), on_delete=models.SET_DEFAULT, default='NONE')
    MaritalStatusID = models.ForeignKey(MaritalStatus, _("Marital Status"), on_delete=models.SET_DEFAULT, default='NONE')
    PatientInsSchemeID = models.ForeignKey(PatientInsScheme, _("Patient Insurance Scheme"), on_delete=models.SET_NULL, null=True)
    PatientInsNo = models.CharField(_("Patient Insurance Number"), max_length=255)
    PatientDependentTypeID = models.ForeignKey(DependentType, _("Dependent"), on_delete=models.SET_DEFAULT, default='SELF')
    CreatedAt = models.DateTimeField(auto_now_add=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
    
    def __str__(self) -> str:
        return

class PatientRank(models.Model):
    PatientRankName = models.CharField(_("Patient Rank Name"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Patient Rank"
        verbose_name_plural = "Patient Ranks"
    
    def __str__(self) -> str:
        return f'{self.PatientRankName}'

class PatientRankLevel(models.Model):
    PatientRankLevelName = models.CharField(_("Patient Rank Level Name"), max_length=255)
    Description = models.TextField(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Patient Rank Level"
        verbose_name_plural = "Patient Rank Levels"
    
    def __str__(self) -> str:
        return f'{self.PatientRankLevelName}'

class PatientUnit(models.Model):
    PatientUnitName = models.CharField(_("Patient Unit"), max_length=255)
    Description = models(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Patient Unit"
        verbose_name_plural = "Patient Units"
    
    def __str__(self) -> str:
        return f'{self.PatientUnitName}'

class IdentificationType(models.Model):
    IdentificationTypeName = models.CharField(_("Type of Identification"), max_length=255)
    Description = models(blank=True, null=True)
    Status = models.BooleanField(_("Relation Type Status"), default=True)

    class Meta:
        verbose_name = "Identification Type"
        verbose_name_plural = "Identification Types"
    
    def __str__(self) -> str:
        return f'{self.IdentificationTypeName}'

class NextOfKin(models.Model):
    NextOfKinID = models.CharField(_("Next of Kin ID"), max_length=255, unique=True)
    PatientID = models.ForeignKey(Patient, verbose_name = _("Patient"),  on_delete=models.CASCADE, db_index=True)
    NextOfKinName = models.CharField(_("Name of Next of Kin"), max_length=255)
    PatientTypeID = models.ForeignKey(PatientType, verbose_name = _("Patient Category"), on_delete=models.SET_DEFAULT, default=1)
    RelationTypeID = models.ForeignKey(RelationType, verbose_name = _("Relation with Patient"), on_delete=models.SET_NULL, null=True)
    ContactAddress = models.TextField()
    DateOfBirth = models.DateField(_("Date of Birth"))
    Email = models.CharField(_("Email Address"), max_length=255, blank=True, null=True)
    Profession = models.CharField(_("Profession"), max_length=255)
    CreatedAt = models.DateTimeField(_("Date Created"), auto_now_add=True)
    EntryDate = models.DateTimeField(_("Entry Date"), auto_now_add=True)
    KeyPrefix = models.CharField(_("Key Prefix"), blank=True, null=True, max_length=255)
    PatientRankID = models.ForeignKey(PatientRank, _("Patient Rank"), on_delete=models.SET_NULL, null=True)
    PatientRankLevelID = models.ForeignKey(PatientRankLevel, _("Patient Rank Level"), on_delete=models.SET_NULL, null=True)
    PatientUnitID = models.ForeignKey(PatientUnit, _("Patient Unit"), on_delete=models.SET_NULL)
    ServiceNo = models.CharField(_("Service No."), max_length=255)
    IdentificationTypeID = models.ForeignKey(IdentificationType, _("ID Type"), on_delete=models.SET_NULL, null=True)
    IdentificationNumber = models.CharField(_("ID Number"), max_length=255)    
    Status = models.BooleanField(_("Next of Kin Status"), default=True)

    class Meta:
        verbose_name = "Next of Kin"
        verbose_name_plural = "Next of Kins"

    def __str__(self) -> str:
        return f'{self.PatientID} [{self.NextOfKinName}]'
