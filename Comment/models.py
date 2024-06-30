from django.db import models
from user_profile.models import UserProfile
#from Post.models import Post
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    owner_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    parent_obj = GenericForeignKey('content_type','object_id')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # static_info
    total_reactions = models.PositiveIntegerField(default=0)
    total_comments = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return f'Comment by {self.owner_profile.user.username} on {self.created_at}'

    class Meta:
        ordering = ['-created_at']
