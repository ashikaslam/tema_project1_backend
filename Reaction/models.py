from django.db import models
from user_profile.models import UserProfile
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Reaction(models.Model):
    owner_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_reactions')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    parent_obj = GenericForeignKey('content_type', 'object_id')
    
    def __str__(self) -> str:
        return f"{self.content_type}"
