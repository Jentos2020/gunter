from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'my_dog/index.html'

class BioPage(TemplateView):
    template_name = 'my_dog/bio.html'

class APIPage(TemplateView):
    template_name = 'my_dog/api.html'