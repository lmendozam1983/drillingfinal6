from django.http import HttpResponseRedirect 
from django.shortcuts import render, redirect
from .forms import CarForm 
from .models import CarModel
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate 
from .forms import CarForm, RegistroUsuarioForm, VehiculoForm
from django.contrib import messages 
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm
from django.contrib.contenttypes.models import ContentType
from .models import CarModel
from django.views.generic import TemplateView
from django.contrib.auth.decorators import permission_required
from django.urls import reverse

def carform_view(request):
    context = {}
    form = CarForm(request.POST or None, request.FILES or None)

    form.fields['marca'].widget.attrs.update({'class': 'form-control custom-input'})
    form.fields['modelo'].widget.attrs.update({'class': 'form-control custom-input'})
    form.fields['serial_carroceria'].widget.attrs.update({'class': 'form-control custom-input'})
    form.fields['serial_motor'].widget.attrs.update({'class': 'form-control custom-input'})
    form.fields['categoria'].widget.attrs.update({'class': 'form-control custom-input'})
    form.fields['precio'].widget.attrs.update({'class': 'form-control custom-input'})

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        print(form.errors) 

    context['form'] = form
    return render(request, "add.html", context)

def registro_view(request): 
    if request.method == "POST": 
        form = RegistroUsuarioForm(request.POST) 
        if form.is_valid(): 
            # obtenemos el content type del modelo 
            content_type = ContentType.objects.get_for_model(CarModel) 
            # obtenemos el permiso a asignar 
            visualizar_catalogo = Permission.objects.get(
                codename='visualizar_catalogo', 
                content_type=content_type
            ) 
            user = form.save() 
            # Agregamos el permiso al usuario el momento de registrarse 
            user.user_permissions.add(visualizar_catalogo) 
            login(request, user) 
            messages.success(request, "Registrado satisfactoriamente.") 
            return HttpResponseRedirect('/') 
        else:
            messages.error(request, "Registro inválido. Algunos datos son incorrectos.") 
    else:
        form = RegistroUsuarioForm()  # Cargar el formulario vacío en caso de GET
    
    # Renderiza la plantilla en caso de GET o si el formulario no es válido
    return render(
        request=request,
        template_name="registro.html",
        context={"register_form": form}
    )

    
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"Invalido username o password.")
        else:
            messages.error(request,"Invalido username o password.")
    form = AuthenticationForm()
    return render(request, "login.html",{"login_form":form})

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/') 

from django.views.generic import ListView
from .models import CarModel

class ListadoView(ListView):
    model = CarModel  
    template_name = "listado.html"  
    context_object_name = 'vehiculos' 

@permission_required('vehiculo.visualizar_catalogo', login_url='/login/')
def listar_vehiculos(request):
    vehiculos = vehiculos.objects.all()
    return render(request, 'listado.html', {'vehiculos': vehiculos})

@permission_required('vehiculo.add', login_url='/login/')
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado') 
    else:
        form = CarForm()
    return render(request, 'add.html', {'form': form})

