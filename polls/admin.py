from django.contrib import admin
from . import models


class PersonaAdmin(admin.ModelAdmin):
    list_filter = ('vivienda', 'vivienda__familia', 'vivienda__estado_vivienda',)
    list_display = ('nombre', 'vivienda', 'edad', 'dni', 'tiene_dni')

class PersonaInline(admin.StackedInline):
    model = models.Persona


class TipoViviendaInline(admin.TabularInline):
    model = models.TipoVivienda
    max_num = 1


class ViviendaAdmin(admin.ModelAdmin):
    inlines = [
        PersonaInline,
        TipoViviendaInline,
    ]
    list_display = ('familia', 'cantidad_personas', 'estado_vivienda', 'direccion',)
    list_filter = ('autor', 'alta', 'estado_vivienda', 'manzana', )

    def save_model(self, request, obj, *args):
        obj.autor = request.user
        obj.save()


admin.site.register(models.Vivienda, ViviendaAdmin,)
admin.site.register(models.TipoVivienda)
admin.site.register(models.TipoMejora)
admin.site.register(models.Persona, PersonaAdmin)
admin.site.register(models.EstadoVivienda)

