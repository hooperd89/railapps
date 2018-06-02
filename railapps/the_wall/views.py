from . import forms
from . import models
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from .models import Occupation, Work
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.



class IndexView(LoginRequiredMixin,TemplateView):
    login_url = '/accounts/login'
    redirect_field_name = ''
    template_name = 'wall_index.html'

class WorkListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Work
    paginate_by = 50

class WorkDetailView(LoginRequiredMixin,DetailView):
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Work
    paginate_by = 50

class OccoListView(ListView):
    model = Occupation

class OccoDetailView(DetailView):
    model = Occupation

class WorkCreateView(CreateView):
    model = Work
    fields ='__all__'

class WorkUpdateView(UpdateView):
    model = Work
    fields ='__all__'


class WorkDeleteView(DeleteView):
    model = Work
    success_url = reverse_lazy('the_wall:work_list')
