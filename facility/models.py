from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Branch(models.Model):

    BranchID = models.CharField(_("Branch ID"), max_length=250)
    BranchName = models.CharField(_("Branch Name"), max_length=250)
    Description = models.TextField(_("Description"), blank=True, null=True, editable=False)
    CreatedAt = models.DateField(_("Created At"), auto_now_add=False)
    Status = models.BooleanField(_("Status"), default=True, editable=False)

    class Meta:
        verbose_name = _("Branch")
        verbose_name_plural = _("Branchs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Branch_detail", kwargs={"pk": self.pk})

