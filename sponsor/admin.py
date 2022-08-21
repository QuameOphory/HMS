from django.contrib import admin
from .models import (
    Sponsor,
    MainAccountHolder,
    BillingAccount,
    Department,
    SponsorStatus,
    SponsorType,
    InsuranceScheme,
    InsuranceGroup, 
    BillingCategory,
    ReceiptType
)
# Register your models here. 

@admin.register(InsuranceScheme)
class InsuranceSchemeAdmin(admin.ModelAdmin):
    '''Admin View for InsuranceScheme'''

    list_display = ('InsuranceSchemeID', 'InsuranceSchemeName', 'BillingCategoryID', 'SponsorID', 'ReceiptTypeID',)
    list_filter = ('InsuranceSchemeName',)
    #readonly_fields = ('InsuranceSchemeID',)
    search_fields = ('InsuranceSchemeName',)

@admin.register(InsuranceGroup)
class InsuranceGroupAdmin(admin.ModelAdmin):
    '''Admin View for InsuranceGroup'''

    list_display = ('InsuranceGroupID', 'InsuranceGroupName',)
    list_filter = ('InsuranceGroupName',)
    readonly_fields = ('InsuranceGroupID',)
    search_fields = ('InsuranceGroupName',)

@admin.register(ReceiptType)
class ReceiptTypeAdmin(admin.ModelAdmin):
    '''Admin View for ReceiptType'''

    list_display = ('ReceiptTypeID', 'ReceiptTypeName',)
    list_filter = ('ReceiptTypeName',)
    readonly_fields = ('ReceiptTypeID',)
    search_fields = ('ReceiptTypeName',)

@admin.register(BillingCategory)
class BillingCategoryAdmin(admin.ModelAdmin):
    '''Admin View for BillingCategory'''

    list_display = ('BillingCategoryID', 'BillingCategoryName',)
    list_filter = ('BillingCategoryName',)
    readonly_fields = ('BillingCategoryID',)

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    '''Admin View for Sponsor'''

    list_display = ('SponsorID', 'SponsorName', 'SponsorTypeID', 'SponsorStatusID', 'Address', 'Location', 'OfficePhone')
    list_filter = ('SponsorName',)
    readonly_fields = ('SponsorID',)
    search_fields = ('SponsorName', 'SponsorID',)
    ordering = ('SponsorName',)


@admin.register(SponsorType)
class SponsorTypeAdmin(admin.ModelAdmin):
    '''Admin View for SponsorType'''

    list_display = ('SponsorTypeID', 'SponsorTypeName', 'Description', 'Status',)
    list_filter = ('SponsorTypeName', 'Status')
    readonly_fields = ('SponsorTypeID',)
    search_fields = ('SponsorTypeName',)
    ordering = ('SponsorTypeName',)

@admin.register(MainAccountHolder)
class MainAccountHolderAdmin(admin.ModelAdmin):
    '''Admin View for MainAccountHolder'''

    list_display = ('MainAccountHolderID', 'MainAccountHolderName', )
    readonly_fields = ('MainAccountHolderID',)

@admin.register(SponsorStatus)
class SponsorStatusAdmin(admin.ModelAdmin):
    '''Admin View for SponsorStatus'''

    list_display = ('SponsorStatusID', 'SponsorStatusName',)
    list_filter = ('SponsorStatusName',)
    readonly_fields = ('SponsorStatusID',)

@admin.register(BillingAccount)
class BillingAccountAdmin(admin.ModelAdmin):
    '''Admin View for BillingAccount'''

    list_display = ('MainAccountHolderID', 'BillingAccountID', 'BillingAccountName', 'PatientID', 'InsuranceSchemeID', 'RelationTypeID', 'InsuranceNumber',)
    list_filter = ('PatientID', 'InsuranceSchemeID')
    readonly_fields = ('BillingAccountID',)
    search_fields = ('PatientID',)
    ordering = ('PatientID',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    '''Admin View for Department'''

    list_display = ('DepartmentID', 'DepartmentName',)
    list_filter = ('DepartmentName',)
    readonly_fields = ('DepartmentID',)
    search_fields = ('DepartmentName',)