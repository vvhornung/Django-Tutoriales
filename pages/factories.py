import factory
from faker import Faker
from .models import Product, Comment

fake = Faker()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    price = factory.LazyFunction(lambda: fake.random_int(min=100, max=10000))
    description = factory.Faker('sentence')

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    product = factory.Iterator(Product.objects.all())
    description = factory.Faker('paragraph')
