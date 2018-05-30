from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView,TemplateView
from the_wall.models import Occupation
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'the_wall/index.html'


class OccupationListView(ListView):
    model = Occupation

class NNEListView(ListView):
    model = Occupation
