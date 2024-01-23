from django.shortcuts import render
from django.views.generic import ListView,TemplateView




class DashboardView(TemplateView):
    template_name = "dashboard/index.html"
    
