from django.db import models

# Create your models here.

from user_profile.models import UserProfile


class Friendship(models.Model):
    friend_one = models.ForeignKey(UserProfile, related_name='friendships_initiated', on_delete=models.CASCADE)
    friend_two = models.ForeignKey(UserProfile, related_name='friendships_received', on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    accepted_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.friend_one} -> {self.friend_two}"

