from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer
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

class UserLogin(APIView):
    def post(self, request):
        user = authenticate(**request.data)

        if not user:
            return Response({'message': 'login 실패'})
        login(request, user)
        return Response({'message': 'login 성공'})
class UserLogout(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'logout'})
