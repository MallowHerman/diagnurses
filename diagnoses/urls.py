from django.urls import path
from .  import views

urlpatterns = [
    path('', views.DiagnosesListView.as_view(), name='diagnoses-list'),
    path('diagnostico/<slug:slug>/', views.DiagnosesDetailView.as_view(), name='diagnosis-detail'),
    path('search/', views.searchDiagnoses, name="search-diagnoses"),
    path('category/domain/<slug:slug>', views.diagnosesDomainCategory, name="diagnoses-domain-category"),
    path('category/class/<slug:slug>', views.diagnosesClassCategory, name="diagnoses-class-category")
]