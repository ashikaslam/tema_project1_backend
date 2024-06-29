




from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
import json
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User


GENDER = [
        ('male', 'male'),
        ('female', 'female'),
        
    ]
class UserProfile(models.Model):
    # inital _mustl_need
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    date_of_birth = models.DateField()
    profile_picture =models.CharField(max_length=255,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSooCX-nPSHN0kCVdUnm-eptCPvUF04YaxeHQ&s")
    gender = models.CharField(max_length=6, choices=GENDER,default='male')
    
    # presonal 
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    #  user locaton  or address
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True,default="not set")
    state = models.CharField(max_length=50, blank=True, null=True,default="not set")
    city = models.CharField(max_length=50, blank=True, null=True,default="not set")
    
    #privacy and security
    is_profile_locked=models.BooleanField(default=False)
    
    # platfomr_activity
    
    # other relations
    
    def get_friends(request):
        user = request.user
        initiated = user.friendships_initiated.filter(is_active=True).values_list('friend_two', flat=True)
        received = user.friendships_received.filter(is_active=True).values_list('friend_one', flat=True)
        friends_qs = User.objects.filter(id__in=list(initiated) + list(received))
    
        # friends_json = serializers.serialize('json', friends_qs, fields=('id')) # Add fields as needed
        
        # # Deserialize the JSON to ensure it's in the correct format
        # friends_data = json.loads(friends_json)
        
        # # Extract the actual list of friends data
        # friends_list = [friend['fields'] for friend in friends_data]
        # return JsonResponse(friends_list, safe=False)
    
    





   
    
    def __str__(self):
        return self.user.username

