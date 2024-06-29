



from django.urls import path
from. import views
urlpatterns = [
  path('varifi_email_before_registration/', views.Varifi_email_before_registration.as_view(), name='Varifi_email_for_registration'),
  path('otp_check_before_signup/', views.Varifi_otp_before_registration.as_view(), name='otp_check_before_signup'),
  path('signup/', views.UserSignupView.as_view(), name='user_signup'),
  path('login/', views.User_login.as_view(), name='login'),
  path('change-password/', views.PasswordChangeView.as_view(), name='change-password'),
  path('requestpasswordreset/', views.RequestPasswordReset.as_view(), name='RequestPasswordReset'),
  path('reset-password/<str:token>/', views.ResetPassword.as_view(), name='password-reset'),
  path('logout/',views.Logout.as_view(),name='logout'),
]