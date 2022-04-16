
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers.common import ProductSerializer

# Create your views here.


class ProductListView(APIView):

    def get(self, _request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        add_product = ProductSerializer(data=request.data)
        if add_product.is_valid():
            add_product.save()
            return Response(add_product.data, status=status.HTTP_201_CREATED)
        return Response(add_product.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
