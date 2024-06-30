






from django.urls import path
from .import views 

urlpatterns = [
 path('make/<str:content_type>/<str:object_id>/', views.Make_comment.as_view(), name='Make_comment'),
]