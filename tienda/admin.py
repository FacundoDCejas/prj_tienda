from django.contrib import admin
from .models import Localidad, Persona

my_models = [Localidad, Persona]

admin.site.register(my_models)
