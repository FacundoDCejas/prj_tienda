from django.contrib import admin
from .models import Autor, Libro

my_models = [Autor, Libro]

admin.site.register(my_models)
