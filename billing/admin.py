from django.contrib import admin
from .models import BillGroup, BillGroupCategory, BillGroupType

# Register your models here.
@admin.register(BillGroup)
class BillGroupAdmin(admin.ModelAdmin):
    '''Admin View for BillGroup'''

    list_display = ('BillGroupID', 'BillGroupName', 'BillGroupTypeID', 'BillGroupCategoryID',)
    list_filter = ('BillGroupName',)
    readonly_fields = ('BillGroupID',)
    search_fields = ('BillGroupID', 'BillGroupName',)

@admin.register(BillGroupCategory)
class BillGroupCategoryAdmin(admin.ModelAdmin):
    '''Admin View for BillGroupCategory'''

    list_display = ('BillGroupCategoryID', 'BillGroupCategoryName',)
    list_filter = ('BillGroupCategoryName',)
    readonly_fields = ('BillGroupCategoryID',)
    search_fields = ('BillGroupCategoryName',)

@admin.register(BillGroupType)
class BillGroupTypeAdmin(admin.ModelAdmin):
    '''Admin View for BillGroupType'''

    list_display = ('BillGroupTypeID', 'BillGroupTypeName',)
    list_filter = ('BillGroupTypeName',)
    readonly_fields = ('BillGroupTypeID',)
    search_fields = ('BillGroupTypeName',)