
from rest_framework import serializers

from .models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileSerializer_1(serializers.ModelSerializer): # level 1 small data
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ['id','first_name', 'last_name', 'profile_picture']
    def get_first_name(self, obj):
        return obj.user.first_name
    def get_last_name(self, obj):
        return obj.user.last_name

class userProfileSerializer_2(serializers.ModelSerializer): # this is not for profile owner some we will show less data
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        exclude = ['gender', 'latitude','longitude','is_profile_locked','date_of_birth']
    def get_first_name(self, obj):
        return obj.user.first_name
    def get_last_name(self, obj):
        return obj.user.last_name
    

class myProfileSerializer(serializers.ModelSerializer): # this is for the profile owner 
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        exclude = ['gender', 'latitude','longitude','is_profile_locked']
    def get_first_name(self, obj):
        return obj.user.first_name
    def get_last_name(self, obj):
        return obj.user.last_name
    def get_email(self, obj):
        return obj.user.email
    
    
class addProfilePicSerializer_during_register(serializers.Serializer): 
    profile_pic = serializers.URLField(required=True)
    
    
    
