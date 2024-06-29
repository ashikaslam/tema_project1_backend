


# serializers.py
from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer): # 1
    class Meta:
        model = Post
        fields = ['text','photo']

    
