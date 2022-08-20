from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.PatientCreateView.as_view(), name='patient_add'),
    path('all/', views.PatientListView.as_view(), name='patient_list'),
    path('<patient_id>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('<patient_id>/edit', views.PatientUpdateView.as_view(), name='patient_edit'),
    
]
