import imp
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class NationalityGroup(models.Model):
    '''
    Helps to group countries and apply common rules of logic to the group
    '''
    NationalityGroupID = models.CharField(_("Nationality Group ID"), max_length=250)
    NationalityGroupName = models.CharField(_("Nationality Group"), max_length=250)
    RegistrationPrice = models.DecimalField(_("Registration Price"), max_digits=5, decimal_places=2, default=0.00)
    ReviewPrice = models.DecimalField(_("Review Price"), max_digits=5, decimal_places=2, default=0.00)
    ConsultationPrice = models.DecimalField(_("Subsequent Visit Price"), max_digits=5, decimal_places=2, default=0.00)
    Description = models.TextField(_("Description"), blank=True, null=True)
    createdAt = models.DateField(_("Created At"), auto_now_add=True)
    Status = models.BooleanField(_("Status"), default=True, blank=True, null=True)

    class Meta:
        verbose_name = _("Nationality Group")
        verbose_name_plural = _("Nationality Groups")

    def __str__(self):
        return self.NationalityGroupName

    def get_absolute_url(self):
        return reverse("nationality_group_detail", kwargs={"nationality_group_id": self.NationalityGroupID})


# Create your models here.
class Nationality(models.Model):
    '''
    Model definition for nationality of patient
    --can set up price
    '''
    NationalityID = models.CharField(_("Nationality ID"), max_length=250)
    NationalityName = models.CharField(_("Nationality"), max_length=250)
    RegistrationPrice = models.DecimalField(_("Registration Price"), max_digits=5, decimal_places=2, default=0.00)
    ReviewPrice = models.DecimalField(_("Review Price"), max_digits=5, decimal_places=2, default=0.00)
    ConsultationPrice = models.DecimalField(_("Subsequent Visit Price"), max_digits=5, decimal_places=2, default=0.00)
    NationalityGroupID = models.ForeignKey(NationalityGroup, verbose_name=_("Nationality Group"), on_delete=models.SET_NULL, null=True, blank=True)
    Description = models.TextField(_("Description"), blank=True, null=True)
    createdAt = models.DateField(_("Created At"), auto_now_add=True)
    Status = models.BooleanField(_("Status"), default=True, blank=True, null=True)

    class Meta:
        verbose_name = _("Nationality")
        verbose_name_plural = _("Nationalities")

    def __str__(self):
        return self.NationalityName

    def get_absolute_url(self):
        return reverse("nationality_detail", kwargs={"nationality_id": self.NationalityID})
