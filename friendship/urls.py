





from django.urls import path
from. import views
urlpatterns = [
    
  path('send_friend_request/<int:friend_2_id>/', views.Send_friend_request.as_view(), name='Send_friend_request'),
  path('accept_friend_request/<int:friend_1_id>/', views.Accept_friend_request.as_view(), name='Accept_friend_request'),
  
]