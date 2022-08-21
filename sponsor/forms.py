from django import forms
from .models import BillingAccount
from records.models import Patient

class BillingAccountForm(forms.ModelForm):
    
    class Meta:
        model = BillingAccount
        fields = (
            "MainAccountHolderID",
            "BillingAccountID",
            "PatientID",
            "InsuranceSchemeID",
            "ReceiptType",
            "RelationTypeID",
            "InsuranceNumber",
            "DepartmentID",
            "SponsorStatusID",
            "ExpiryDate",
        )
        widgets = {
            "MainAccountHolderID": forms.Select(attrs={'classs': 'form-control'}),
            "BillingAccountID": forms.TextInput(attrs={'classs': 'form-control', 'readonly': True}),
            "PatientID": forms.Select(attrs={'classs': 'form-control'}),
            "InsuranceSchemeID": forms.Select(attrs={'classs': 'form-control'}),
            "ReceiptType": forms.Select(attrs={'classs': 'form-control', 'readonly': True}),
            "RelationTypeID": forms.Select(attrs={'classs': 'form-control'}),
            "InsuranceNumber": forms.TextInput(attrs={'classs': 'form-control'}),
            "DepartmentID": forms.Select(attrs={'classs': 'form-control'}),
            "SponsorStatusID": forms.Select(attrs={'classs': 'form-control'}),
            "ExpiryDate": forms.TextInput(attrs={'classs': 'form-control'}),
        }

