from django.db import models

# Create your models here.
from user_profile.models import  UserProfile

from Reaction.models import Reaction
from Comment. models import Comment


class Post(models.Model):
    owner_profile= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField(null=True,blank=True)
    photo=models.URLField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # static_info
    total_reactions = models.PositiveIntegerField(default=0)
    total_comments = models.PositiveIntegerField(default=0)
    total_share = models.PositiveIntegerField(default=0)
    
    # dynamic_info
    def get_rectons(self):
        reaction_arr = self.rections
        count_of_reaction = reaction_arr.count()
        self.total_reaction = count_of_reaction
        self.save()
        
    def get_comments(self):
        comments_arr = self.comments
        count_of_comments = comments_arr.count()
        self.total_comments = count_of_comments
        self.save()
    
    class Meta:
        ordering = ['-created_at','total_reactions','total_comments','total_share']
        
        
    
  
