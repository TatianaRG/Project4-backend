from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    price = models.PositiveSmallIntegerField()
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.brand} from {self.category} category'
