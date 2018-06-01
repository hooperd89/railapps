from . import forms
from . import models
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from .models import Occupation, Work

# Create your views here.



class IndexView(TemplateView):
    template_name = 'wall_index.html'

class WorkListView(ListView):
    model = Work
    # context_object_name = 'work_list.html'
    # queryset = Work.objects.all()

class WorkDetailView(DetailView):
    model = Work
