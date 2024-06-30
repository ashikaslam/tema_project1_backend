


from django.urls import path
from .views import ReactionCreateView

urlpatterns = [
    path('create/', ReactionCreateView.as_view(), name='reaction-create'),
]