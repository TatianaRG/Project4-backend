
from email.policy import HTTP
from xml.dom import NotFoundErr
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Category, Product
from .serializers.common import PopulatedCategorySerializer, PopulatedProductSerializer, ProductSerializer, CategorySerializer

# Create your views here.

#PRODUCT
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

class ProductDetailView(APIView):
  def get_product(self, pk):
    try:
      return Product.objects.get(pk=pk)
    except Product.DoesNotExist:
      raise NotFound(detail= "There's no product with this PK")

  def get (self, _request, pk):
    product = self.get_product(pk=pk)
    serialized_product = PopulatedProductSerializer(product)
    return Response(serialized_product.data, status= status.HTTP_200_OK)

class RecentListView(APIView):
    def get(self, _request):
      recently_added = Product.objects.all().order_by('-pub_date')[:3]
      serializer = ProductSerializer(recently_added, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)



#CATEGORY
class CategoryListView(APIView):
    def get(self, _request):
      categories = Category.objects.all()
      serialized_categories = PopulatedCategorySerializer(categories, many=True)
      return Response(serialized_categories.data, status=status.HTTP_200_OK)

