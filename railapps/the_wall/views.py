from . import forms
from . import models
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.urls import reverse, reverse_lazy
# Create your views here.



class OverView(TemplateView):
    template_name = 'wall_base.html'

class OccoCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.Occupation

class WorkCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.Work

class OccoUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.Occupation

class WorkDeleteView(DeleteView):
    model = models.Work
    success_url = reverse_lazy("basic_app:list")

class OccoDeleteView(DeleteView):
    model = models.Occupation
    success_url = reverse_lazy("basic_app:list")
