


from django.urls import path
from .views import ReactionCreateView

urlpatterns = [
 path('create_or_del/<str:content_type>/<str:object_id>/', ReactionCreateView.as_view(), name='reaction-create_or_del'),
]