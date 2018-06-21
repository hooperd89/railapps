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
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.

# Summary/ Overview View

class IndexView(LoginRequiredMixin,PermissionRequiredMixin,TemplateView):
    permission_required = ('the_wall.view_work','the_wall.view_occo')
    login_url = '/accounts/login'
    redirect_field_name = ''
    template_name = 'wall_index.html'

# Work views

class WorkListView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required = ('the_wall.view_work','the_wall.view_occo')
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Work
    paginate_by = 50

class WorkDetailView(LoginRequiredMixin,PermissionRequiredMixin, DetailView):
    permission_required = ('the_wall.view_work','the_wall.view_occo')
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Work
    paginate_by = 50

class WorkCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required = ('the_wall.view_work','the_wall.view_occo')
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Work
    fields ='__all__'

class WorkUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = ('the_wall.view_work','the_wall.view_occo')
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Work
    fields ='__all__'

class WorkDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    permission_required = ('the_wall.view_work','the_wall.view_occo')
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Work
    success_url = reverse_lazy('the_wall:work_list')

# Occupation Views

class OccupationListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    permission_required = ('the_wall.view_work','the_wall.view_occo')
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Occupation
    paginate_by = 50

class OccupationDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ('the_wall.view_work','the_wall.view_occo')
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Occupation
    paginate_by = 50

class OccupationCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    permission_required = ('the_wall.view_work','the_wall.view_occo')
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Occupation
    fields ='__all__'

class OccupationUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = ('the_wall.view_work','the_wall.view_occo')
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Occupation
    fields ='__all__'

class OccupationDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    permission_required = ('the_wall.view_work','the_wall.view_occo')
    login_url = '/accounts/login'
    redirect_field_name = ''
    model = Occupation
    success_url = reverse_lazy('the_wall:work_list')
