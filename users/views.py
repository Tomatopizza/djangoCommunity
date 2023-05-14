
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from users.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework import permissions

from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny




from rest_framework.response import Response
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from users.models import Users

from users.serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


class UserView(APIView):
    def get(self, request):
        return Response({"message": "get 요청합니다!"})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "회원가입 성공"})

    def put(self, request):
        return Response({"message": "put 요청입니다!"})

    def delete(self, request):
        return Response({"message": "delete 요청입니다!"})





class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer




class ConfirmEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)

        return HttpResponseRedirect("/")  

    def get_object(self, queryset=None):
        key = self.kwargs["key"]
        email_confirmation = EmailConfirmationHMAC.from_key(key)
        if not email_confirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                email_confirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:

                return HttpResponseRedirect("/")  
        return email_confirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs

class FollowView(APIView):
    def post(self, request, user_id):
        follower_id = get_object_or_404(Users, id=user_id)
        follow_id = request.user
        if follow_id in follower_id.followers.all():
            follower_id.followers.remove(follow_id)
            return Response("팔로우를 취소하였습니다.", status=status.HTTP_200_OK)
        else:
            follower_id.followers.add(follow_id)
            return Response("팔로우하였습니다.", status=status.HTTP_200_OK)


