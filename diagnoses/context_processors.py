from .models import Domains, Classes, Diagnoses

def nav_obj(request):
    return {
        'nav_obj_pending': Diagnoses.objects.filter(accepted='Pending'),
        'nav_domains': Domains.objects.all(),
        'nav_classes': Classes.objects.all()
        }