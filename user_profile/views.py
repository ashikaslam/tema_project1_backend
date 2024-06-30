from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .import models

     

class Profile_data(APIView):
    def get(self, request, *args, **kwargs):
            posts = models.UserProfile.objects.all()[:50]
            serializer = serializers.UserProfileSerializer(posts, many=True)
            return Response({'all_posts': serializer.data})
        