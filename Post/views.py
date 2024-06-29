from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .import serializers
from. import models
from django.contrib.auth import authenticate

import re
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model
User = get_user_model()
from . import models

class Post_view(APIView): # 1
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PostSerializer
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = request.user
            photo = serializer.validated_data['photo']
            text = serializer.validated_data['text']
            if text or photo:
                post = models.Post.objects.create(photo=photo,text=text,owner_profile=user.profile)
                if post: return Response({"message": "post creation completed", "status": 1}, status=status.HTTP_200_OK)
            return Response({'error': "unknown errors", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
            
            
            
            
            
