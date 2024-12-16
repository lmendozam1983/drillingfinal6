from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView): 
    login_url = 'vehiculo/login/'  
    template_name = "index.html"
    


