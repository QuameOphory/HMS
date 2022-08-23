from django.contrib import admin
from .models import Receipt, Invoice, PaymentMode, PaymentType 
# Register your models here.

@admin.register(PaymentMode)
class PaymentModeAdmin(admin.ModelAdmin):
    '''Admin View for PaymentMode'''

    list_display = ('PaymentModeID', 'PaymentModeName')
    list_filter = ('PaymentModeName',)
    readonly_fields = ('PaymentModeID',)
    search_fields = ('PaymentModeName',)


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    '''Admin View for PaymentType'''

    list_display = ('PaymentTypeID', 'PaymentTypeName')
    list_filter = ('PaymentTypeName',)
    readonly_fields = ('PaymentTypeID',)
    search_fields = ('PaymentTypeName',)
    ordering = ('PaymentTypeName',)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    '''Admin View for Invoice'''

    list_display = ('InvoiceID', 'InvoiceAmount', 'InvoiceDate')
    list_filter = ('InvoiceID',)
    readonly_fields = ('InvoiceID',)
    search_fields = ('InvoiceID',)
    ordering = ('InvoiceDate',)


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    '''Admin View for Receipt'''

    list_display = ('ReceiptID', 'PatientID', 'PaymentTypeID', 'PaymentModeID', 'ReceiptAmount', 'ReceiptDate')
    list_filter = ('ReceiptID',)
    readonly_fields = ('ReceiptID',)
    search_fields = ('ReceiptID', 'PatientID',)