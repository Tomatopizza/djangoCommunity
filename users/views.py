from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from rest_framework import status, permissions
from rest_framework.response import Response
from users.models import User
# Create your views here.

class FollowView(APIView):
    def post(self, request, user_id):
        follower_id = get_object_or_404(User, id=user_id)
        follow_id = request.user
        if follow_id in follower_id.followers.all():
            follower_id.followers.remove(follow_id)
            return Response("팔로우를 취소하였습니다.", status=status.HTTP_200_OK)
        else:
            follower_id.followers.add(follow_id)
            return Response("팔로우하였습니다.", status=status.HTTP_200_OK)