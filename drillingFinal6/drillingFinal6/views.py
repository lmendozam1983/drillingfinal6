from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"  # Template que se muestra después de login
    login_url = '/login/'  # Redirige a login si el usuario no está autenticado
    redirect_field_name = 'next'  # Permite redirigir a la URL deseada después de login (si aplica)




