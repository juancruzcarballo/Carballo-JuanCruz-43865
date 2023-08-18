from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="inicio"),

    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="app/logout.html"), name="logout"),
    path('register/', register, name="register"),

        
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

    path('clientes/', ClienteList.as_view(), name="clientes"),
    path('create_cliente/', ClienteCreate.as_view(), name="create_cliente"),
    path('detail_cliente/<int:pk>/', ClienteDetail.as_view(), name="detail_cliente"),
    path('update_cliente/<int:pk>/', ClienteUpdate.as_view(), name="update_cliente"),
    path('delete_cliente/<int:pk>/', ClienteDelete.as_view(), name="delete_cliente"),

    path('empleados/', EmpleadoList.as_view(), name="empleados"),
    path('create_empleado/', EmpleadoCreate.as_view(), name="create_empleado"),
    path('detail_empleado/<int:pk>/', EmpleadoDetail.as_view(), name="detail_empleado"),
    path('update_empleado/<int:pk>/', EmpleadoUpdate.as_view(), name="update_empleado"),
    path('delete_empleado/<int:pk>/', EmpleadoDelete.as_view(), name="delete_empleado"),

    path('marcas/', MarcaList.as_view(), name="marcas"),
    path('create_marca/', MarcaCreate.as_view(), name="create_marca"),
    path('detail_marca/<int:pk>/', MarcaDetail.as_view(), name="detail_marca"),
    path('update_marca/<int:pk>/', MarcaUpdate.as_view(), name="update_marca"),
    path('delete_marca/<int:pk>/', MarcaDelete.as_view(), name="delete_marca"),


    path('vinos/', VinoList.as_view(), name="vinos"),
    path('create_vino/', VinoCreate.as_view(), name="create_vino"),
    path('detail_vino/<int:pk>/', VinoDetail.as_view(), name="detail_vino"),
    path('update_vino/<int:pk>/', VinoUpdate.as_view(), name="update_vino"),
    path('delete_vino/<int:pk>/', VinoDelete.as_view(), name="delete_vino"),

    path('buscar_vino/', buscarVino,  name="buscar_vino"),
    path('buscar3/', buscar3, name="buscar3"),

    path('about/', about, name="about"),

   ]