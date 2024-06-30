







from django.urls import path
from. import views
urlpatterns = [
  path('', views.Profile_data.as_view(), name='user_profile'),
 
 
]