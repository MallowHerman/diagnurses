from django.contrib import admin
from .models import Diagnoses, Classes, Domains

admin.site.register(Diagnoses)
admin.site.register(Domains)
admin.site.register(Classes)
