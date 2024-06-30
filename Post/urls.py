



from django.urls import path
from. import views
urlpatterns = [
  path('create/', views.Post_view.as_view(), name='create'),
  path('home_page/', views.HomePage.as_view(), name='home_page'),
 
]