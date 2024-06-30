from django.db import models
from user_profile.models import UserProfile
from django.contrib.contenttypes.models import ContentType
from Reaction.models import Reaction
from django.contrib.contenttypes.models import ContentType

class Post(models.Model):
    owner_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField(null=True, blank=True)
    photo = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # static_info
    total_reactions = models.PositiveIntegerField(default=0)
    total_comments = models.PositiveIntegerField(default=0)
    total_share = models.PositiveIntegerField(default=0)
    
    # dynamic_info
    def get_reactions(self):
        post_content_type = ContentType.objects.get(app_label='Post', model='post')
        reactions = Reaction.objects.filter(content_type=post_content_type,object_id=self.id) 
        count_of_reactions = reactions.count()
        self.total_reactions = count_of_reactions
        self.save()
        return reactions
        
    # def get_comments(self):
    #     comments = Comment.objects.filter(post=self)
    #     count_of_comments = comments.count()
    #     self.total_comments = count_of_comments
    #     self.save()
    
    # def __lt__(self, others):
    #     if self.created_at != others.created_at: return self.created_at < others.created_at
    #     if self.total_reactions != others.total_reactions: return self.total_reactions > others.total_reactions
    #     if self.total_comments != others.total_comments: return self.total_comments > others.total_comments
    #     if self.total_share != others.total_share: return self.total_share > others.total_share
        
    # class Meta:
    #     ordering = ['total_reactions', 'total_comments', 'total_share', '-created_at']
    
    # def __str__(self) -> str:
    #     return f"{self.id} {self.text}"
