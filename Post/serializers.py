


# serializers.py
from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer): # 1
    class Meta:
        model = Post
        fields = ['text','photo']

    















# for data pass to the clint site


from rest_framework import serializers
from .models import Post

class PostSerializer_data_pass(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'