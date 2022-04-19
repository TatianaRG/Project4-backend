
from rest_framework.serializers import ModelSerializer

from products.serializers.common import PopulatedProductSerializer
from .models import Basket
from jwt_auth.serializers import UserSerializer

class BasketSerializer(ModelSerializer):
  class Meta: 
    model = Basket
    fields = ('__all__')

class PopulatedBasketSerializer(BasketSerializer):
  owner = UserSerializer()
  product = PopulatedProductSerializer()