from django.contrib import admin
from .models import Branch, Department, Hospital
# Register your models here.

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    '''Admin View for Hospital'''

    list_display = ('HospitalID', 'HospitalName',)
    list_filter = ('HospitalName',)
    readonly_fields = ('HospitalID',)
    search_fields = ('HospitalName',)

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    '''Admin View for Branch'''

    list_display = ('BranchID', 'BranchName', 'HospitalID',)
    list_filter = ('BranchName',)
    readonly_fields = ('BranchID',)
    search_fields = ('BranchName',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    '''Admin View for Department'''

    list_display = ('DepartmentID', 'DepartmentName',)
    list_filter = ('DepartmentName',)
    readonly_fields = ('DepartmentID',)
    search_fields = ('DepartmentName',)
