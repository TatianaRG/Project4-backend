from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
  email = models.CharField(max_length=50, unique=True)
  first_name = models.CharField(max_length=50, blank=True)
  last_name= models.CharField(max_length=50, blank=True)
  address = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=50, blank=True)
  profile_image= models.CharField(max_length=500, blank=True)
  favourites = models.ManyToManyField('products.Product', related_name='users', blank=True)

def __str__(self):
        return f'{self.email} {self.first_name} {self.last_name}'