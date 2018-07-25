from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ClientHome(TemplateView):
    template_name = 'campaigns/chome.html'
