flood
===============

# Uso

Clone el paquete en algun lugar accesible:

    $ git clone git://github.com/Inventta/django-project-template.git

Cree y active un [entorno virtual](http://pypi.python.org/pypi/virtualenv) para el 
proyecto:

    $ cd ~/venvs/ # adapte este path a su preferencia
    $ virtualenv flood
    $ source flood/bin/activate

Instale las dependencias necesarias:

    $ cd ~/Proyectos/flood #el directorio donde hizo el clone 
    $ python setup.py develop
    

Modificar los parámetros de la base de datos

    #local_settings.py
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'flood',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
    }   

> En producción local_settings.py debería tener DEBUG=False
    
# Inicializar la base de datos.

Primero es necesario crear los esquemas y ejecutar las migraciones si hacen falta:
    
    $ manage migrate
    $ manage loaddata polls/fixtures/defaults.json

> De realizarse cambios en algún modelo ejecutar:
> 
>     $ manage makemigrations website

Reemplazar *website* con la aplicación que necesitamos migrar

En este punto tenemos nuestra instancia lista para correr el servidor de 
desarrollo:

    $ manage runserver
    
Ahora puede apuntar su navegador a http://localhost:8000 para acceder al sistema.


Noticia de licencia
---------------
© 2015 
flood es software libre de Matías Iturburu, Marcelo Yornet.
distribuido bajo la licencia BSD. Una copia 
de esta licencia se incluye en el archivo COPYING.
Instale las dependencias necesarias:
