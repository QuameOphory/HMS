from django.contrib import admin
from .models import (
    Sponsor,
    MainAccountHolder,
    BillingAccount,
    Department,
    SponsorStatus,
    SponsorType,
)
# Register your models here. 

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