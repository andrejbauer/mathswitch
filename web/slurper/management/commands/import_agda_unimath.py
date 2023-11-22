from django.core.management.base import BaseCommand
from slurper import source_agda_unimath


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("importing agda-unimath data")
        source_agda_unimath.AU_SLURPER.save_items()
