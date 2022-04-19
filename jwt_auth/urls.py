from django.urls import path
from .views import *

urlpatterns=[
  path('register/', RegisterView.as_view()),
  path('login/', LoginView.as_view()),
  path('profile/', ProfileView.as_view()),
  path('users/<int:pk>/', UserDetailView.as_view()),

]