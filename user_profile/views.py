from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status    


class Profile_data_1(APIView):  # small data
    def get(self, request, *args, **kwargs):
            posts = models.UserProfile.objects.all()[:50]
            serializer = serializers.UserProfileSerializer_1(posts, many=True)
            return Response({'all_posts': serializer.data})



class user_Profile_data(APIView):   # mid
    def get(self, request,id, *args, **kwargs):
          try:
            if models.UserProfile.objects.filter(id=id).exists():
               profile= models.UserProfile.objects.get(id=id)
               serializer = serializers.userProfileSerializer_2(profile, many=False)
               return Response({'profile': serializer.data})
            return Response({"error": "no data found for the given request", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
          except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class my_Profile_data(APIView):   # high
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            profile = request.user.profile
            serializer = serializers.myProfileSerializer(profile, many=False)
            return Response({'profile': serializer.data})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        








        
        
        
        
        
        
        
        
        
        
        

        