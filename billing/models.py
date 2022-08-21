from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.

class BillGroupType(models.Model):
    '''
    Model definition for BillGroup types
    '''
    BillGroupTypeID = models.CharField(_("BillGroup Type"), max_length=250)
    BillGroupTypeName = models.CharField(_("BillGroup Type Name"), max_length=250)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    Status = models.BooleanField(_("Status"), default=True, editable=False)

    class Meta:
        verbose_name = _("BillGroupType")
        verbose_name_plural = _("BillGroupTypes")

    def __str__(self):
        return self.BillGroupTypeName

    def get_absolute_url(self):
        return reverse("billgroup_type_detail", kwargs={"billgroup_type_id": self.BillGroupTypeID})

class BillGroupCategory(models.Model):
    '''Model definition for billgroup category - superset of billgroup'''
    BillGroupCategoryID = models.CharField(_("BillGroup Cat. ID"), max_length=250)
    BillGroupCategoryName = models.CharField(_("BillGroup Cat. Name"), max_length=250)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    Status = models.BooleanField(_("Status"), default=True, editable=False)

    class Meta:
        verbose_name = _("BillGroupCategory")
        verbose_name_plural = _("BillGroupCategorys")

    def __str__(self):
        return self.BillGroupCategoryName

    def get_absolute_url(self):
        return reverse("billgroup_category_detail", kwargs={"billgroup_category_id": self.BillGroupCategoryID})


class BillGroup(models.Model):
    '''
    Model definition for billgroups
    '''
    BillGroupID = models.CharField(_("BillGroup ID"), max_length=250)
    BillGroupName = models.CharField(_("BillGroup Name"), max_length=250)
    BillGroupTypeID = models.ForeignKey(BillGroupType, verbose_name=_("BillGroup Type"), on_delete=models.SET_NULL, null=True)
    BillGroupCategoryID = models.ForeignKey(BillGroupCategory, verbose_name=_("BillGroup Cat."), on_delete=models.SET_NULL, null=True)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=True)
    Status = models.BooleanField(_("Status"), default=True, editable=False)

    class Meta:
        verbose_name = _("BillGroup")
        verbose_name_plural = _("BillGroups")

    def __str__(self):
        return self.BillGroupName

    def get_absolute_url(self):
        return reverse("billgroup_detail", kwargs={"billgroup_id": self.BillGroupID})

