from django.shortcuts import render
from datetime import datetime, timedelta
from time import strftime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

from jwt_auth.models import CustomUser
from products.serializers.common import PopulatedProductSerializer


from .serializers import PopulatedUserSerializer, UserSerializer
User= get_user_model()

# Create your views here.

class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'})

        return Response(serializer.errors, status=422)

class LoginView(APIView):

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials'})

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = self.get_user(email)
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid credentials'})


        dt = datetime.now() + timedelta(days=7)

        token = jwt.encode(
          {
            'sub': user.id,
            'exp': int(dt.strftime('%s'))
          },
          settings.SECRET_KEY, algorithm='HS256')

        return Response({'token': token, 'message': f'Welcome back {user.username}!'})


class ProfileView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
      user = CustomUser.objects.get(pk=request.user.id)
      serialized_user = PopulatedUserSerializer(user)
      return Response(serialized_user.data, status=status.HTTP_200_OK)

class UserDetailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
      user = CustomUser.objects.get(pk=pk)
      serialized_user = UserSerializer(user)
      return Response(serialized_user.data, status = status.HTTP_200_OK)

    def put(self, request, pk):
      user = CustomUser.objects.get(pk=pk)
      updated_user = UserSerializer(user, data=request.data)
      if updated_user.is_valid():
          updated_user.save()
          return Response(updated_user.data, status = status.HTTP_202_ACCEPTED)
      return Response(updated_user.data, status = status.HTTP_422_UNPROCESSABLE_ENTITY)