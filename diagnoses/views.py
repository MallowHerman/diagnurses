from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import DiagnosesForm
from .models import Diagnoses
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required
def diagnosesCreate(request):
    if request.method == "POST":
        post = request.POST
        form = DiagnosesForm(post)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Novo diagnóstico adicionado com sucesso!")
                return redirect('diagnoses-list')
            except:
                pass
    else:
        form = DiagnosesForm()

    context = {
        'form': form
    }

    return render(request, 'diagnoses/diagnoses_create.html', context)