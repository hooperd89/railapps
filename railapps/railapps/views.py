from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class AboutPage(TemplateView):
    template_name = 'about.html'

class HomePage(TemplateView):
    template_name = "index.html"
