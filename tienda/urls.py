from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("personas", views.persona_listar, name="persona_listar"),
    path("empleados", views.empleado_listar, name="empleado_listar"),
    path("nueva_persona", views.nueva_persona, name="nueva_persona"),
    path("modificar_persona/<int:pk>",
         views.modificar_persona, name="modificar_persona"),
    path("modificar_empleado/<int:pk>",
         views.modificar_empleado, name="modificar_empleado"),
    path("eliminar_persona/<int:pk>",
         views.eliminar_persona, name="eliminar_persona"),
#---------------------------Articulos
     path("articulos", views.articulos_listar, name="articulos_listar"),
     path("nuevo_articulo", views.nuevo_articulo, name="nuevo_articulo"),
     path("eliminar_articulo/<int:pk>",
         views.eliminar_articulo, name="eliminar_articulo"),
     path("modificar_articulo/<int:pk>",
         views.modificar_articulo, name="modificar_articulo"),
]
