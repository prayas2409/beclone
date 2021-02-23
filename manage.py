#!/usr/bin/env python
import os
import sys

import django


def run(event, context):
    """
    Lambda entry point
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_assessment.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv) #['manage.py', 'runserver'])


if __name__ == '__main__':
    """
    Local entry point
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_assessment.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
