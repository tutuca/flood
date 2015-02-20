from django.contrib import admin
from . import models


class PersonaInline(admin.TabularInline):
    model = models.Persona


class TipoViviendaInline(admin.TabularInline):
    model = models.TipoVivienda
    max_num = 1

class ViviendaAdmin(admin.ModelAdmin):
    inlines = [
        PersonaInline,
        TipoViviendaInline,
    ]


admin.site.register(models.Vivienda, ViviendaAdmin,)
admin.site.register(models.TipoVivienda)
admin.site.register(models.TipoMejora)
admin.site.register(models.Persona)
admin.site.register(models.EstadoVivienda)

