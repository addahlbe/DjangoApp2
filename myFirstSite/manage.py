#!/usr/bin/env python
# manage.py: A command-line utility that lets you interact with this Django project
# in various ways. Type python manage.py help to get a feel for what it can do. You
# should never have to edit this file; it's created in this directory purely for
# convenienve.
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myFirstSite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
