from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reaction
from .serializers import ReactionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from Post .models import Post


from django.contrib.contenttypes.models import ContentType


class ReactionCreateView(APIView):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, content_type, object_id, *args, **kwargs):
        try:
            user = request.user
            profile = user.profile
            if content_type == "Post.post": # if some one want to like of unlike a post
                print(f"hello>> {user} {profile} {content_type} { object_id}")
                current_post = Post.objects.get(id=object_id)
                print(current_post, ">>")
                post_content_type = ContentType.objects.get(
                    app_label='Post', model='post')
                print(post_content_type)
                reactions = Reaction.objects.filter(
                    content_type=post_content_type, object_id=object_id, owner_profile=profile).exists()
                print(reactions)
                if reactions:
                    reactions = Reaction.objects.get(
                        content_type=post_content_type, object_id=object_id, owner_profile=profile)
                    reactions.delete()
                    current_post.total_reactions -= 1
                    current_post.save()
                    return Response(status=status.HTTP_202_ACCEPTED)
                else:
                    print("here>>")
                    reactions = Reaction.objects.create(
                        content_type=post_content_type, object_id=object_id, owner_profile=profile)
                    current_post.total_reactions += 1
                    current_post.save()
                    return Response(status=status.HTTP_201_CREATED)
            else:pass # if some one want to like of unlike a comment
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
