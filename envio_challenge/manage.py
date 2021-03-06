#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# Build paths inside the project like this: BASE_DIR / 'subdir'.
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
env_name = os.getenv('ENVIO_SETTINGS_ENV', 'dev')
env = environ.Env()
env.read_env(BASE_DIR / f'env/.env.{env_name}')


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'envio_challenge.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
