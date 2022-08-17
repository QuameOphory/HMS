from django.contrib import admin
from .models import Title, Gender, MaritalStatus, PatientType
# Register your models here.

admin.site.register(Title)
admin.site.register(Gender)
admin.site.register(MaritalStatus)
admin.site.register(PatientType)

