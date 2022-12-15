from .models import Diagnoses

def nav_obj(request):
    return {'nav_obj': Diagnoses.objects.all()}