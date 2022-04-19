from django.urls import path
from .views import BasketDeleteProduct, BasketListView

urlpatterns= [
path('', BasketListView.as_view()),
path('<int:pk>/', BasketDeleteProduct.as_view())
]