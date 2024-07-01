

from django.utils import timezone
from . import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()



class Send_friend_request(APIView):  # this is to request someone to be freind
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request, friend_2_id,*args, **kwargs):
        try:
            if not User.objects.filter(id=friend_2_id).exists():return Response({'error':"unkown error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            user1 = request.user
            user2 = User.objects.get(id=friend_2_id)
            models.Friendship.objects.create(friend_one=user1.profile,friend_two=user2.profile)
            return Response({'message': 'successfully request sent'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Accept_friend_request(APIView):  # this is to accept friend request
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,friend_1_id,*args, **kwargs):
        try:
            if not User.objects.filter(id=friend_1_id).exists(): return Response({'error':"unkown error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            user2 = request.user
            user1 = User.objects.get(id=friend_1_id)
            frindship_obj = models.Friendship.objects.get(friend_one=user1.profile,friend_two=user2.profile,is_active=False)
            if not frindship_obj: return Response({'error':"unkown error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            frindship_obj.is_active=True
            now = timezone.now()
            frindship_obj.accepted_date=now
            frindship_obj.save()
            return Response({'message': 'successfully request accepted'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)