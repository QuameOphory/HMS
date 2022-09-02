from django.contrib import admin
from .models import ConsultationType
# Register your models here.

@admin.register(ConsultationType)
class ConsultationTypeAdmin(admin.ModelAdmin):
    '''Admin View for ConsultationType'''

    list_display = ('ConsultationTypeID', 'ConsultationTypeName', 'DepartmentID', 'CashConsultationFee', 'RegistrationFee', 'ReviewFee',)
    list_filter = ('ConsultationTypeName',)
    readonly_fields = ('ConsultationTypeID',)
    search_fields = ('ConsultationTypeName',)
