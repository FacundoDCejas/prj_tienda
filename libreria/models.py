from django.db import models


class Autor(models.Model):
    nombre = models.CharField("Nombre Autor", max_length=50)
    apellido = models.CharField("Apellido Autor", max_length=50)

    class Meta:
        ordering = ["apellido", "nombre"]
        verbose_name_plural = "Autores"

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)


class Libro(models.Model):
    titulo = models.CharField("Titulo del libro", max_length=50)
    editorial = models.CharField("Editorial del libro", max_length=50)
    autor = models.ForeignKey(Autor, null=True, blank=True,
                              on_delete=models.PROTECT, related_name="libro_autor")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return '%s (%s)' % (self.titulo, self.autor.apellido)
