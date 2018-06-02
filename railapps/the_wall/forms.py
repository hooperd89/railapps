from django.forms import ModelForm
from .models import Occupation, Work

class CreateWorkForm(ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
