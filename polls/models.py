from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class EstadoVivienda(models.Model):
    estado = models.CharField(max_length=255)

    def __str__(self):
        return self.estado

@python_2_unicode_compatible
class TipoMejora(models.Model):
    mejora = models.CharField(max_length=255)

    def __str__(self):
        return self.mejora


@python_2_unicode_compatible
class Vivienda(models.Model):
    autor = models.ForeignKey('auth.User', editable=False)
    familia = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    manzana = models.CharField(max_length=255)
    parcela = models.CharField(max_length=255)
    tipo_tenencia = models.CharField(max_length=255)
    recurrencia_inundacion = models.CharField(max_length=255)
    notas = models.TextField(default='')
    estado_vivienda = models.ForeignKey(EstadoVivienda)
    mobiliario_afectado = models.BooleanField(default=False)
    mejora_necesaria = models.ManyToManyField(TipoMejora)
    alta = models.DateTimeField(auto_now_add=True, editable=False)

    @property
    def cantidad_personas(self):
        return self.persona_set.all().count()

    def __str__(self):
        return self.familia

@python_2_unicode_compatible
class Persona(models.Model):
    vivienda = models.ForeignKey(Vivienda)
    nombre = models.CharField(max_length=255)
    dni = models.IntegerField()
    tiene_dni = models.BooleanField(default=False)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length=255)
    enfermedades = models.CharField(max_length=255)
    situacion_laboral = models.CharField(max_length=255)
    ocupacion = models.CharField(max_length=255)
    herramientas = models.TextField(default='')
    notas = models.TextField(default='')

    def __str__(self):
        return self.nombre

@python_2_unicode_compatible
class TipoVivienda(models.Model):
    vivienda = models.ForeignKey(Vivienda)
    piso = models.CharField(max_length=255)
    paredes = models.CharField(max_length=255)
    techo = models.CharField(max_length=255)
    instalaciones = models.CharField(max_length=255)

    def __str__(self):
        return ''.join([self.piso, self.paredes, self.techo, self.instalaciones])
