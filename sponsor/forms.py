from attr import attrs
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

