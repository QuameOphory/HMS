from django.urls import path
from . import views

urlpatterns = [
    path('<patient_id>/add/', views.BillingAccountCreateView.as_view(), name='sponsor_create'),
]
