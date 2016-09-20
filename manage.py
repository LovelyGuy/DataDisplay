#!/usr/bin/env python
import os
import socket
import sys

if __name__ == "__main__":
    hostname = socket.gethostname()
    if hostname == 'hp-master':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DataDisplay.settings.dev")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DataDisplay.settings.default")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
