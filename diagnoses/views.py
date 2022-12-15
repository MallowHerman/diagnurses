from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import DiagnosesForm
from .models import Diagnoses
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class DiagnosesListView(ListView):
    model: Diagnoses
    queryset = Diagnoses.objects.filter(accepted=True)
    context_object_name: 'diagnoses_list'



def DiagnosesDetailView(request, slug):
    result = Diagnoses.objects.get(slug__icontains=slug)
    defining_characteristics = result.defining_characteristics.split('\n')
    related_factors = result.related_factors.split('\n')
    at_risk_population = result.at_risk_population.split('\n')
    associated_condition = result.associated_condition.split('\n')
    nic = result.nic.split('\n')
    noc = result.noc.split('\n')
    
    context = {
        'result': result,
        'defining_characteristics': defining_characteristics,
        'related_factors': related_factors,
        'at_risk_population': at_risk_population,
        'associated_condition': associated_condition,
        'nic': nic,
        'noc': noc

    }
    return render(request, 'diagnoses/diagnoses_detail.html', context)

def searchDiagnoses(request):
    if 'q' in request.GET:
        search_query = request.GET['q']
        result = Diagnoses.objects.filter(diagnosis__icontains=search_query)
        
        context = {
            'search_query': search_query,
            'result': result
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

def diagnosesPending(request):
    result = Diagnoses.objects.filter(accepted=False)

    if 'cancel' in request.POST:
        print('Cancel')

    context = {
        'result': result
    }
    return render(request, 'diagnoses/diagnoses_pending.html', context)