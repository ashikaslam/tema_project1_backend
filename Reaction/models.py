from django.db import models

# Create your models here.
from user_profile.models import  UserProfile
class Reaction(models.Model):
     owner_profile= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='rections')