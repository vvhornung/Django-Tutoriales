from django.core.management.base import BaseCommand
from pages.factories import CommentFactory
from pages.models import Product

class Command(BaseCommand):
    help = 'Seed the database with comments'

    def handle(self, *args, **kwargs):
        # Create 3 comments for each product
        for product in Product.objects.all():
            for _ in range(3):
                CommentFactory.create(product=product)
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded comments'))