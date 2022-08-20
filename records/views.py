from django.urls import reverse
from django.shortcuts import render
from .models import NextOfKin, Patient, PatientType
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    FormView,
)
from django.views.generic.detail import SingleObjectMixin
from .forms import PatientForm
from django.contrib import messages
import helpers
from .forms import PatientNextOfKinFormSet
from django.http import HttpResponseRedirect
# Create your views here.

class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = "records/patient_add.html"

    def form_valid(self, form):

        self.object = form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Patient Created Successfully'
        )
        return super().form_valid(form)

class PatientListView(ListView):
    queryset = Patient.objects.filter(Status=True).order_by('FirstName')
    template_name = 'records/patient_list.html'
    context_object_name = 'patients'

class PatientDetailView(DetailView):
    template_name = 'records/patient_detail.html'

    def get_object(self):
        patient_id = self.kwargs['patient_id']
        self.object = Patient.objects.get(PatientID=patient_id)
        return self.object

class PatientUpdateView(UpdateView):
    form_class = PatientForm
    template_name = 'records/patient_add.html'

    def get_object(self):
        self.object = Patient.objects.get(PatientID = self.kwargs['patient_id'])
        return self.object


class PatientNextOfKinEditView(SingleObjectMixin, FormView):
    template_name = 'records/patient_nextofkin_edit.html'

    def get_object(self):
        patient = Patient.objects.get(PatientID = self.kwargs['patient_id'])
        return patient

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class = None):
        return PatientNextOfKinFormSet(**self.get_form_kwargs(), instance = self.object, queryset=NextOfKin.objects.none())

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Author Editted Successfully'
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self) -> str:
        return reverse('patient_detail', kwargs = {'patient_id': self.object.PatientID})


class NextOfKinUpdateView(UpdateView):
    template_name = 'records/patient_nextofkin_edit.html'

    def get_object(self):
        patient_id = self.kwargs['patient_id']
        next_of_kin_id = self.kwargs['next_of_kin_id']
        patient = Patient.objects.get(PatientID=patient_id)
        self.object = patient.nextofkin_set.all().filter(NextOfKinID=next_of_kin_id)
        return self.object