from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.my_Profile_data.as_view(), name='my_profile'),
    path('user_profile_data/<int:id>/', views.user_Profile_data.as_view(), name='user_profile_data'),
]
