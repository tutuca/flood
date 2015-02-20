from django.db import models


class EstadoVivienda(models.Model):
    estado = models.CharField(max_length=255)

    def __unicode__(self):
        return self.estado


class TipoMejora(models.Model):
    mejora = models.CharField(max_length=255)

    def __unicode__(self):
        return self.mejora


# Create your models here.
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
    mejora_necesaria = models.ManyToManyField(TipoMejora)
    alta = models.DateTimeField(auto_now_add=True, editable=False)

    @property
    def cantidad_personas(self):
        return self.persona_set.all().count()

    def __unicode__(self):
        return self.familia


class Persona(models.Model):
    vivienda = models.ForeignKey(Vivienda)
    nombre = models.CharField(max_length=255)
    dni = models.IntegerField()
    tiene_dni = models.BooleanField(default=False)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length=255)
    situacion_laboral = models.CharField(max_length=255)
    ocupacion = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre


class TipoVivienda(models.Model):
    vivienda = models.ForeignKey(Vivienda)
    piso = models.CharField(max_length=255)
    paredes = models.CharField(max_length=255)
    techo = models.CharField(max_length=255)
    instalaciones = models.CharField(max_length=255)

    def __unicode__(self):
        return ''.join([self.piso, self.paredes, self.techo, self.instalaciones])
