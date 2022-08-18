from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        exclude = ('CreatedAt', 'Status', 'PatientRankLevel', 'PatientRank', 'PatientCategory')