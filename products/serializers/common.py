
from unicodedata import category
from rest_framework import serializers
from ..models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
      model = Category
      fields = ('__all__')


class PopulatedCategorySerializer(CategorySerializer):
  products = ProductSerializer(many= True)

class PopulatedProductSerializer(ProductSerializer):
  category = CategorySerializer()
