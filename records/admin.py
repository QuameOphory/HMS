from django.contrib import admin
from .models import (
    Title, Gender, MaritalStatus, 
    PatientType, Patient, Country, 
    Religion, NextOfKin, IdentificationType,
    PatientIdentification, RelationType, PatientRank,
    PatientRankLevel, PatientCategory
)
from datetime import timedelta, date
# Register your models here.

admin.site.register(Title)
admin.site.register(Gender)
admin.site.register(MaritalStatus)
admin.site.register(PatientType)
admin.site.register(Country)
admin.site.register(Religion)
admin.site.register(NextOfKin)
admin.site.register(IdentificationType)
admin.site.register(PatientIdentification)
admin.site.register(RelationType)
admin.site.register(PatientRankLevel)
admin.site.register(PatientRank)
admin.site.register(PatientCategory)

@admin.display(description='Age')
def calculate_age(obj):
    dob = obj.Birthdate
    today = date.today()
    return str(today - dob)

class NextOfKinInLine(admin.StackedInline):
    model = NextOfKin
    fields = ('NextOfKinID', 'NextOfKinName', 'ContactAddress', 'RelationTypeID')
    extra = 1

class PatientIdentificationInLine(admin.StackedInline):
    model = PatientIdentification
    extra: int = 1

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    date_hierarchy = 'CreatedAt'
    list_display = ('PatientID', 'FirstName', 'SurName', 'OtherName', 'calculate_age')
    empty_value_display = ''
    inlines = [
        NextOfKinInLine,
        PatientIdentificationInLine,
    ]

    @admin.display(description='Age')
    def calculate_age(self, obj):
        dob = obj.BirthDate
        today = date.today()
        return str((today - dob) // 360)[0:2]


