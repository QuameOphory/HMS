from django.contrib import admin
from .models import VisitType, VisitStatus, Visitation
# Register your models here.

@admin.register(VisitType)
class VisitTypeAdmin(admin.ModelAdmin):
    '''Admin View for VisitType'''

    list_display = ('VisitTypeID', 'VisitTypeName', 'VisitTypeCost')
    list_filter = ('VisitTypeName',)
    readonly_fields = ('VisitTypeID',)
    search_fields = ('VisitTypeName',)
    ordering = ('VisitTypeName',)

@admin.register(VisitStatus)
class VisitStatusAdmin(admin.ModelAdmin):
    '''Admin View for VisitStatus'''

    list_display = ('VisitStatusID', 'VisitStatusName',)
    list_filter = ('VisitStatusName',)
    readonly_fields = ('VisitStatusID',)
    search_fields = ('VisitStatusName',)
    ordering = ('VisitStatusName',)

@admin.register(Visitation)
class VisitationAdmin(admin.ModelAdmin):
    '''Admin View for Visitation'''

    list_display = ('VisitationID', 'VisitStatusID', 'VisitTypeID', 'DepartmentID', 'ConsultationTypeID', 'PatientID', 'BillingAccountID', 'VisitationFee',)
    list_filter = ('VisitationID', 'PatientID', 'VisitDate',)
    readonly_fields = ('VisitationID',)
    search_fields = ('VisitationID', 'PatientID', 'VisitDate',)
    ordering = ('VisitDate', 'PatientID',)