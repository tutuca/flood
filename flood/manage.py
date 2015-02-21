from __future__ import print_function
import os
import sys
import webbrowser
import django


def do_manage():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flood.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


def do_runserver():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flood.settings")
    from django.conf import settings
    from django.core.management import call_command

    django.setup()

    port = 8000
    db_file = os.path.join(settings.BASE_DIR, 'db.sqlite3')

    if not os.path.exists(db_file):
        call_command('migrate')

    webbrowser.open('http://localhost:%s' % port)
    call_command('runserver')


if __name__ == "__main__":
    do_runserver()
