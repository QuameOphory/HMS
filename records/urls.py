from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.PatientCreateView.as_view(), name='patient_add'),
    path('all/', views.PatientListView.as_view(), name='patient_list'),
    path('<patient_id>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('<patient_id>/edit', views.PatientUpdateView.as_view(), name='patient_edit'),
    path('<patient_id>/next_of_kin/edit', views.PatientNextOfKinEditView.as_view(), name='patient_nextofkin_edit'),
    
]
