from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
import helpers
# Create your models here.

def generateHospitalID():
    qs = Hospital.objects.all()
    return helpers.generateID('H', qs=qs, length=4)

def generateBranchID():
    qs = Branch.objects.all()
    return helpers.generateID('B', qs=qs, length=4)

def generateDepartmentID():
    qs = Department.objects.all()
    return helpers.generateID('D', qs=qs, length=4)

class Hospital(models.Model):

    HospitalID = models.CharField(_("Hospital ID"), max_length=250, default=generateHospitalID)
    HospitalName = models.CharField(_("Hospital Name"), max_length=250)
    Description = models.TextField(_("Description"), blank=True, null=True)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    Status = models.BooleanField(_("Status"), default=True, editable=False)

    class Meta:
        verbose_name = _("Hospital")
        verbose_name_plural = _("Hospitals")

    def __str__(self):
        return self.HospitalName

    def get_absolute_url(self):
        return reverse("hospital_detail", kwargs={"pk": self.HospitalID})


class Branch(models.Model):
    HospitalID = models.ForeignKey(Hospital, verbose_name=_("Hospital"), on_delete=models.SET_NULL, null=True, default='H001')
    BranchID = models.CharField(_("Branch ID"), max_length=250, default=generateBranchID)
    BranchName = models.CharField(_("Branch Name"), max_length=250)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    Status = models.BooleanField(_("Status"), default=True, editable=False)

    class Meta:
        verbose_name = _("Branch")
        verbose_name_plural = _("Branches")

    def __str__(self):
        return self.BranchName

    def get_absolute_url(self):
        return reverse("branch_detail", kwargs={"branch_id": self.BranchID})

class Department(models.Model):
    '''
    Model definition for hospital departments: Units in the hospital
    '''
    DepartmentID = models.CharField(_("Department ID"), max_length=250, default=generateDepartmentID)
    DepartmentName = models.CharField(_("Department Name"), max_length=250)
    BranchID = models.ManyToManyField(Branch, verbose_name=_("Branch"))
    Description = models.TextField(_("Desccription"), blank=True, null=True, editable=False)
    Status = models.BooleanField(_("Status of Visit Type"), default=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")

    def __str__(self):
        return self.DepartmentName

    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"department_id": self.DepartmentID})



