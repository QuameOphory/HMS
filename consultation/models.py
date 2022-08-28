from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from facility.models import Department


# Create your models here.


class ConsultationType(models.Model):

    ConsultationTypeID = models.CharField(_("Consultation Type ID"), max_length=250)
    ConsultationTypeName = models.CharField(_("Consultation Type"), max_length=250)
    DepartmentID = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.SET_NULL)
        


    class Meta:
        verbose_name = _("ConsultationType")
        verbose_name_plural = _("ConsultationTypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ConsultationType_detail", kwargs={"pk": self.pk})
