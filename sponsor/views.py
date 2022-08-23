from django.shortcuts import render
from records.models import Patient
from .models import BillingAccount
from .forms import BillingAccountForm
from django.views.generic import (
    CreateView
)

# Create your views here.


class BillingAccountCreateView(CreateView):
    model = BillingAccount
    form_class = BillingAccountForm
    template_name = 'sponsor/sponsor_add.html'

    def get(self, request, *args, **kwargs):
        self.patient_id = self.kwargs['patient_id']
        self.patient = Patient.objects.get(PatientID=self.patient_id)
        self.patient_billing_accounts = self.patient.billingaccount_set.all()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.patient_id = self.kwargs['patient_id']
        self.patient = Patient.objects.get(PatientID=self.patient_id)
        self.patient_billing_accounts = self.patient.billingaccount_set.all()
        return super().post(request, *args, **kwargs)

    def get_initial(self):
        initial = {}
        initial['PatientID'] = self.patient
        initial['BillingAccountID'] = self.patient_id +  '-' + str(len(self.patient_billing_accounts)+1)
        return initial

    def form_valid(self, form):
        billing_account = form.save(commit=False)
        billing_account.BillingAccountName = str(self.patient) + f'[{str(billing_account.InsuranceSchemeID)}]'
        return super().form_valid(form)