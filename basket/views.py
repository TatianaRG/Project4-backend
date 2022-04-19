
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied

from basket.models import Basket
from basket.serializers import BasketSerializer, PopulatedBasketSerializer

# Create your views here.
class BasketListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, _request):
      basket_items = Basket.objects.filter(owner = self.request.user)
      serialized_items = PopulatedBasketSerializer(basket_items, many=True)
      return Response(serialized_items.data, status = status.HTTP_200_OK)

    def post(self, request):
      request.data['owner'] = request.user.id
      basket = BasketSerializer(data=request.data)
      if basket.is_valid():
        basket.save()
        return Response(basket.data, status=status.HTTP_201_CREATED)
      return Response (basket.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class BasketDeleteProduct(APIView):
    permission_classes = (IsAuthenticated, )

    def delete(self, request, pk):
      try:
        item_to_delete = Basket.objects.get(pk=pk)
        if item_to_delete.owner.id != request.user.id:
          raise PermissionDenied()
        item_to_delete.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
      except Basket.DoesNotExist:
        raise NotFound()