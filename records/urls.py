from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.PatientCreateView.as_view(), name='patient_add'),
]
