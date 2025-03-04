from concepts.models import Item
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        Item.objects.filter(source=Item.Source.WIKIDATA).delete()
        Item.objects.filter(source=Item.Source.NLAB).delete()
        Item.objects.filter(source=Item.Source.MATHWORLD).delete()
