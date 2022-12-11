from django.forms import ModelForm
from .models import Diagnoses

class DiagnosesForm(ModelForm):
    class Meta:
        model = Diagnoses
        fields = '__all__'
        exclude = ['slug']