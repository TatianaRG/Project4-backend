from products.views import ProductListView
from django.urls import path

from .views import *

urlpatterns= [
  path('products/', ProductListView.as_view()),
]