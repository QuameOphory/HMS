from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        exclude = ('CreatedAt', 'Status', 'PatientRankLevel', 'PatientRank', 'PatientCategory')
        widgets = {
            'FirstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'SurName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SurName'}),
            'OtherName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Other Name'}),
            'PatientID': forms.TextInput(attrs={'class': 'form-control w-25'}),
            'TitleID': forms.Select(attrs={'class': 'form-control'}),
            'GenderID': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Gender'}),
            'EmailAddress': forms.EmailInput(attrs={'class': 'form-control'}),
            'BirthDate': forms.DateInput(attrs={'class': 'form-control w-50', 'placeholder': 'yyyy-mm-dd'}),
            'MaritalStatusID': forms.Select(attrs={'class': 'form-control'}),
            'CountryID': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Country'}),
            'ReligionID': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Religion'}),
            'Occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'BusinessPhone': forms.TextInput(attrs={'class': 'form-control'}),
            'BusinessAddress': forms.TextInput(attrs={'class': 'form-control'}),
            'ResidencePhone': forms.TextInput(attrs={'class': 'form-control'}),
            'ResidenceAddress': forms.TextInput(attrs={'class': 'form-control'}),
        


        }