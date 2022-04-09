import sys

from django.core.management.base import BaseCommand
from django.utils import autoreload


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            autoreload.run_with_reloader(self._restart_celery)
        except KeyboardInterrupt:
            print("Killing process", flush=True)
            pass

    @classmethod
    def _restart_celery(cls):
        if sys.platform == "win32":
            cls.run("taskkill /f /t /im celery.exe")
            cls.run("celery -A src worker --loglevel=info --pool=solo")
        else:  # probably ok for linux2, cygwin and darwin. Not sure about os2, os2emx, riscos and atheos
            cls.run("pkill celery")
            cls.run("celery worker -l info -A src")

    @staticmethod
    def run(cmd):
        import shlex
        import subprocess

        subprocess.call(shlex.split(cmd))
