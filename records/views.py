from django.shortcuts import render
from .models import Patient, PatientType
from django.views.generic import CreateView
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

