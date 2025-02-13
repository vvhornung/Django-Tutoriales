from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product,related_name='coments', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'Comment on {self.product.name}'
