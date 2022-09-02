from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from facility.models import Department
from billing.models import BillGroup
import helpers

# Create your models here.

def generateConsultationTypeID():
    qs = ConsultationType.objects.all()
    return helpers.generateID('C', qs=qs, length=7)


class ConsultationType(models.Model):

    ConsultationTypeID = models.CharField(_("Consultation Type ID"), max_length=250, default=generateConsultationTypeID)
    ConsultationTypeName = models.CharField(_("Consultation Type"), max_length=250)
    DepartmentID = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.SET_NULL, null=True)
    BillGroupID = models.ForeignKey(BillGroup, verbose_name=_(""), on_delete=models.SET_NULL, null=True, editable=False)
    CashConsultationFee = models.DecimalField(_("Cash Cons. Fee"), max_digits=5, decimal_places=2, blank=True, null=True)
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
