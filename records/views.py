from django.shortcuts import render
from .models import Patient, PatientType
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
)
from .forms import PatientForm
from django.contrib import messages
import helpers
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