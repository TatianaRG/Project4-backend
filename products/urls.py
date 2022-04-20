from products.views import ProductListView, CategoryListView
from django.urls import path

from .views import *

urlpatterns= [
  path('products/', ProductListView.as_view()),
  path('categories/', CategoryListView.as_view()),
  path('products/<int:pk>/', ProductDetailView.as_view()),
  path('products/new_in/', RecentListView.as_view()),
]