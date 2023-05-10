from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
class UserView(APIView):
    def get(self, request):
        return Response({'message': 'get 요청합니다!'})
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': '회원가입 성공'})
    def put(self, request):
        return Response({'message': 'put 요청입니다!'})
    def delete(self, request):
        return Response({'message': 'delete 요청입니다!'})
# Create your views here.

# class UserLogin(APIView):
#     serializer_class = CustomTokenObtainPairSerializer
#     def post(self, request):
        
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         if not user:
#             return Response({'message': 'login 실패'})
#         login(request, user)
#         return Response({'message': 'login 성공'})
# class UserLogout(APIView):
#     def post(self, request):
#         logout(request)
#         return Response({'message': 'logout'})

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# class UserLogin(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self, request):
#         print(request.user)
#         user = request.user
#         # user.is_admin = True
#         # user.save()
#         return Response("get")