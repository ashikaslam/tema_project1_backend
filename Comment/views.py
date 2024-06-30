from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from Post .models import Post


from django.contrib.contenttypes.models import ContentType


class Make_comment(APIView):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CommentSerializer

    def post(self, request, content_type, object_id, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = request.user
            profile = user.profile
            if content_type == "post":  # if some one want to like of comment a post
                current_post = Post.objects.get(id=object_id)
                post_content_type = ContentType.objects.get(
                    app_label='Post', model='post')
                models.Comment.objects.create(owner_profile=profile, content_type=post_content_type,
                                              object_id=object_id, text=serializer.validated_data['text'])
                current_post.total_comments += 1
                current_post.save()
                return Response(status=status.HTTP_201_CREATED)

            else:
                pass  # if some one want to like of unlike a comment
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
