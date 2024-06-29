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
    
    def __lt__(self,others): #  will sort by demand
        if self.created_at != others.created_at:return  self.created_at < others.created_at
        if self.total_reactions != others.total_reactions:return  self.total_reactions > others.total_reactions
        if self.total_comments != others.total_comments:return  self.total_comments > others.total_comments
        if self.total_share != others.total_share:return  self.total_share > others.total_share
        
        
    class Meta:
        ordering = ['total_reactions','total_comments','total_share','-created_at']
    
    
        

        
        
    
  
