#!/usr/bin/env python
import os
import sys
import signal


def sighandler(signum, frame):
    """
    Speed up exit under Docker.
    http://blog.lotech.org/fix-djangos-runserver-when-run-under-docker-or-pycharm.html
    """
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sighandler)
    signal.signal(signal.SIGINT, sighandler)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manager_site.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
