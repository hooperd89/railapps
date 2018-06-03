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

# Summary/ Overveiew View

class IndexView(LoginRequiredMixin,TemplateView):
    login_url = '/accounts/login'
    redirect_field_name = ''
    template_name = 'wall_index.html'

# Work views

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

class WorkCreateView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Work
    fields ='__all__'

class WorkUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Work
    fields ='__all__'

class WorkDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Work
    success_url = reverse_lazy('the_wall:work_list')

# Occupation Views

class OccupationListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Occupation
    paginate_by = 50

class OccupationDetailView(LoginRequiredMixin,DetailView):
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Occupation
    paginate_by = 50

class OccupationCreateView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Occupation
    fields ='__all__'

class OccupationUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Occupation
    fields ='__all__'

class OccupationDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Occupation
    success_url = reverse_lazy('the_wall:work_list')
