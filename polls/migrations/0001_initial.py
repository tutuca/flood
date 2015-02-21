# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoVivienda',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('estado', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=255)),
                ('dni', models.IntegerField()),
                ('tiene_dni', models.BooleanField(default=False)),
                ('edad', models.IntegerField()),
                ('parentesco', models.CharField(max_length=255)),
                ('enfermedades', models.CharField(max_length=255)),
                ('situacion_laboral', models.CharField(max_length=255)),
                ('ocupacion', models.CharField(max_length=255)),
                ('herramientas', models.TextField(default='')),
                ('notas', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoMejora',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('mejora', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoVivienda',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('piso', models.CharField(max_length=255)),
                ('paredes', models.CharField(max_length=255)),
                ('techo', models.CharField(max_length=255)),
                ('instalaciones', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('familia', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('manzana', models.CharField(max_length=255)),
                ('parcela', models.CharField(max_length=255)),
                ('tipo_tenencia', models.CharField(max_length=255)),
                ('recurrencia_inundacion', models.CharField(max_length=255)),
                ('notas', models.TextField(default='')),
                ('alta', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
                ('estado_vivienda', models.ForeignKey(to='polls.EstadoVivienda')),
                ('mejora_necesaria', models.ManyToManyField(to='polls.TipoMejora')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tipovivienda',
            name='vivienda',
            field=models.ForeignKey(to='polls.Vivienda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='persona',
            name='vivienda',
            field=models.ForeignKey(to='polls.Vivienda'),
            preserve_default=True,
        ),
    ]
