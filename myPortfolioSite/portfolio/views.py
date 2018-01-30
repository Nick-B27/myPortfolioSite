from django.shortcuts import render
from django.views.generic import View, TemplateView

class IndexView(TemplateView):
    template_name = 'portfolio/index.html'

class ProjectView(TemplateView):
    template_name = 'portfolio/projects.html'
