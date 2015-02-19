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
    $ pip install -r requirements.txt
    

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
    
    $ ./manage.py migrate

De realizarse cambios en algún modelo ejecutar:

    $ ./manage.py makemigrations website

Reemplazar *website* con la aplicación que necesitamos migrar

En este punto tenemos nuestra instancia lista para correr el servidor de 
desarrollo:

    $ ./manage.py runserver

# Assets státicos. (sólo desarrolladores.)

Ahora queda generar los recursos de estilos, imágenes, íconos y scripts.
Para esto integramos [grunt](http://gruntjs.com/) y [bower](http://bower.io/).

Descargar las herramientas necesarias:

    $ npm install  

> a la fecha, grunt no incluye la interfaz de linea de comandos por defecto y 
> necesita ser instalado separado.
> para esto invocar:
    $ npm install -g grunt-cli
> utilizar *sudo* en caso que sea necesario

Instalar las bibliotecas utilizadas

    $ bower install

Ejecutar las tareas de grunt:

    $ grunt

Por defecto grunt funciona en modo `watch`, esto es: queda observando los archivos importantes de manera de re-ejecutar las tareas pertinentes.

Si sólo necesitamos `compilar` los recursos estáticos, invocar:

    $ grunt build

Ésto genera una carpeta `static/` en la raiz del proyecto, que podemos desplegar en nuestro servidor.

> Nota: Este texto y la nota de licencia están incluidos en el molde y se 
> aplicarán a todos los proyectos que cree con este método.
> Recomendamos con énfasis modificar estos textos para adaptarlos a su entorno.


Noticia de licencia
---------------
© 2015 
flood es software libre de Matías Iturburu, Marcelo Yornet.
distribuido bajo la licencia BSD. Una copia 
de esta licencia se incluye en el archivo COPYING.
Instale las dependencias necesarias:
