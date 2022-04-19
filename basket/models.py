
from django.db import models
from jwt_auth.models import CustomUser
from products.models import Product

# Create your models here.
class Basket(models.Model):
  owner = models.ForeignKey(CustomUser, related_name="basket_items", on_delete=models.CASCADE)
  product = models.ForeignKey(Product, related_name="basket_items", on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField()

  def __str__(self):
      return f'{self.owner} has added {self.product} to the basket'