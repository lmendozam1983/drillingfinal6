from django.urls import path
from .views import carform_view, registro_view, login_view, logout_view, ListadoView

app_name = 'vehiculo'  

urlpatterns = [
    path('add/', carform_view, name='add'),
    path('registro/', registro_view, name="registro"),
    path('login/', login_view, name="login"),
    path('logout',logout_view,name='logout'),
    path('listado/', ListadoView.as_view(), name="listado"),
]


