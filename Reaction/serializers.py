from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import Reaction

class ReactionSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField()
    class Meta:
        model = Reaction
        fields = ['content_type','object_id']

    # def create(self, validated_data):
    #     content_type_value = validated_data.pop('content_type')
    #     app_label, model_name = content_type_value.split('.')
    #     content_type = ContentType.objects.get(app_label=app_label, model=model_name)
    #     reaction = Reaction.objects.create(content_type=content_type, **validated_data)
    #     return reaction
    
# input json   
{
 
    "content_type": "Post.post",
    "object_id": 2
}