from django.urls import path
from .  import views

urlpatterns = [
    path('', views.DiagnosesListView.as_view(), name='diagnoses-list'),
    path('diagnostico/<slug:slug>/', views.DiagnosesDetailView, name='diagnosis-detail'),
    path('search/', views.searchDiagnoses, name="search-diagnoses"),
    path('category/domain/<slug:slug>', views.diagnosesDomainCategory, name="diagnoses-domain-category"),
    path('category/class/<slug:slug>', views.diagnosesClassCategory, name="diagnoses-class-category"),
    path('diagnoses/new', views.diagnosesCreate, name="diagnoses-create"),
    path('diagnoses/pending', views.diagnosesPending, name='diagnoses-pending'),
    path('diagnoses/delete/<int:id>', views.diagnosesDelete, name='diagnoses-delete'),
    path('diagnoses/approved/<int:id>', views.diagnosesApproved, name='diagnoses-approved'),
    path('diagnoses/edit/<int:id>', views.diagnosesEdit, name='diagnoses-edit'),
    
]