from django.contrib import admin
from .models import Title, Gender, MaritalStatus, PatientType, Patient, Country
from datetime import timedelta, date
# Register your models here.

admin.site.register(Title)
admin.site.register(Gender)
admin.site.register(MaritalStatus)
admin.site.register(PatientType)


@admin.display(description='Age')
def calculate_age(obj):
    dob = obj.Birthdate
    today = date.today()
    return str(today - dob)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    date_hierarchy = 'CreatedAt'
    list_display = ('FirstName', 'calculate_age')

    @admin.display(description='Age')
    def calculate_age(self, obj):
        dob = obj.BirthDate
        today = date.today()
        return str((today - dob) // 360)[0:2]


