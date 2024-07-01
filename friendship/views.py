

from django.utils import timezone
from . import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from extra_fruction import problem_solver
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
        
        
        
        

class get_frends_of_a_user(APIView):   # this is the viwe to see friend of a user
    # we will add  freatur to serarc frind by name from frrind list 
    def get(self,request, user_id,*args, **kwargs):
        try:
            if not User.objects.filter(id=user_id).exists():return Response({'error':"unkown error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            user=User.objects.get(id=user_id)
            profile =user.profile
            all_friendship_obj_arr_1 =   profile.friendships_initiated.filter(is_active=True)
            all_friendship_obj_arr_2 =   profile.friendships_received.filter(is_active=True)
            fnd_list = problem_solver.frind_list(all_friendship_obj_arr_1,all_friendship_obj_arr_2)
            print(fnd_list)
            return Response({"fnd_list": fnd_list, "status": 1}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)