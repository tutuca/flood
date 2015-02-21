# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_admin_user(apps, schema_editor):
    User = apps.get_registered_model('auth', 'User')
    admin = User(
        username='admin',
        email='admin@admin.com',
        password=make_password('cambiame'),
        is_superuser=True,
        is_staff=True
    )
    admin.save()


def create_default_data(apps, schema_editor):
    TipoMejora = apps.get_model('polls', 'TipoMejora')
    for m in (
            "Herramientas",
            "Limpieza Vivienda",
            "Pintura",
            "Revoques Parciales",
            "Muros o Paredes",
            "Cubierta de chapa",
            "Losa de viguetas",
            "Puertas",
            "Ventanas",
            "Pisos",
            "Instalación eléctrica",
            "Instalación gas"):
        mejora = TipoMejora.objects.create(mejora=m)
        mejora.save()


    EstadoVivienda = apps.get_model('polls', 'EstadoVivienda')
    for e in (
            "Destrucción Total",
            "Destrucción Parcial Grave",
            "Destrucción Parcial Leve"):
        estado = EstadoVivienda(estado=e)
        estado.save()


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_vivienda_mobiliario_afectado'),
        ('auth', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_admin_user),
        migrations.RunPython(create_default_data)
    ]

