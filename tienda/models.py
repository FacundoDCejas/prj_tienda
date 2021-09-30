from django.db import models
from datetime import datetime

# Clases para Personas ---------------------------------------------------


class Localidad(models.Model):
    nombre = models.CharField("Nombre Localidad", max_length=50)
    cp = models.CharField("Codigo Postal", max_length=10)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Localidades"

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    num_doc = models.CharField("Documento", max_length=10, primary_key=True)
    nombre = models.CharField("Nombre Persona/s", max_length=50)
    apellido = models.CharField("Apellido Persona/s", max_length=50)
    fecha_nac = models.DateField("Fecha de Nacimiento", default=datetime.now)
    localidad = models.ForeignKey(Localidad, null=True, blank=True,
                                  on_delete=models.PROTECT, related_name="persona_localidad")

    class Meta:
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return '%s - %s, %s' % (self.num_doc, self.apellido, self.nombre)


class Cliente(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True,
                                on_delete=models.PROTECT, related_name="cliente_persona")
    categoria = models.IntegerField("Categoria de Cliente")
    fecha_alta = models.DateField("Fecha de Alta", default=datetime.now)


class Cargo(models.Model):
    nombre = models.CharField("Nombre de Cargo", max_length=50)
    nivel = models.CharField("Nivel de Cargo", max_length=10)
    descripcion = models.CharField("Descripcion de Cargo", max_length=100)


class Empleado(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True,
                                on_delete=models.PROTECT, related_name="empleado_persona")
    legajo = models.IntegerField("Legajo de Empleado")
    cargo = models.ForeignKey(Cargo, null=True, blank=True,
                              on_delete=models.PROTECT, related_name="empleado_cargo")


# Clases para Articulos ---------------------------------------------------

class Articulo(models.Model):
    nombre = models.CharField("Nombre de articulo", max_length=50, null=True)
    marca = models.CharField("Marca de Articulo", max_length=50)
    descripcion = models.CharField("Descripcion de Articulo", max_length=100)
    categoria = models.CharField("Categoria de Articulo", max_length=100)
    stock = models.IntegerField("Stock de Articulo")
    precio = models.FloatField("Precio de Articulo")
    disponible = models.BooleanField(
        "Disponibilidad de Articulo", default=False)
    imagen = models.CharField("Imagen de Articulo", max_length=100)

    class Meta:
        ordering = ["marca", "nombre"]


class Movimiento(models.Model):
    tipo = models.CharField("Tipo de movimiento", max_length=50)
    cliente = models.ForeignKey(Cliente, null=True, blank=True,
                                on_delete=models.PROTECT, related_name="movimiento_cliente")
    numero = models.CharField("Numero de movimento", max_length=50)
    fecha = models.DateField("Fecha de Movimiento", default=datetime.now)

    class Meta:
        ordering = ["numero", "fecha"]


class Item(models.Model):
    articulo = models.ForeignKey(Articulo, null=True, blank=True,
                                 on_delete=models.PROTECT, related_name="item_articulo")
    movimiento = models.ForeignKey(Movimiento, null=True, blank=True,
                                   on_delete=models.PROTECT, related_name="item_movimiento")
