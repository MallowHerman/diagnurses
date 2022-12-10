from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Diagnoses

class DiagnosesListView(ListView):
    model: Diagnoses
    queryset = Diagnoses.objects.all()
    context_object_name: 'diagnoses_list'



class DiagnosesDetailView(DetailView):
    model = Diagnoses
    context_object_name: 'diagnosis_details'

def searchDiagnoses(request):
    if request.method == 'POST':
        search = request.POST['search-diagnoses']
        diagnoses_searched = Diagnoses.objects.filter(title__icontains=search)

        context = {
            'search': search,
            'diagnoses': diagnoses_searched
        }
        return render(request, 'diagnoses/diagnoses_search.html', context)

def diagnosesDomainCategory(request, slug):
    if request.method == 'GET':
        diagnoses_list = Diagnoses.objects.all().filter(domain__slug__icontains=slug)
        diagnosis_first_one = diagnoses_list[0]

        context = {
            'result': diagnosis_first_one,
            'diagnoses_list': diagnoses_list
        }
        return render(request, 'diagnoses/diagnoses_domain_category.html', context)

def diagnosesClassCategory(request, slug):
    if request.method == 'GET':
        diagnoses_list = Diagnoses.objects.all().filter(classe__slug__icontains=slug)
        diagnosis_first_one = diagnoses_list[0]

        context = {
            'result': diagnosis_first_one,
            'diagnoses_list': diagnoses_list
        }
        return render(request, 'diagnoses/diagnoses_class_category.html', context)