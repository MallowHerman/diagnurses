from .models import Diagnoses

def nav_obj(request):
    return {
        'nav_obj': Diagnoses.objects.all().filter(accepted="Approved"),
        'nav_obj_pending': Diagnoses.objects.all().filter(accepted="Pending")
        }