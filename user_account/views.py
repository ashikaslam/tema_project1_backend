from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .import serializers
from . import models
from  . import Utility_function
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login,logout
User = get_user_model()

# this is step 1 to creat a account .
# here a user will pass his emil id and server will chek
# if the email is real eamil and is any id with  this email


class Varifi_email_before_registration(APIView):  # 1
    serializer_class = serializers.email_taker

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data['email']
            if User.objects.filter(email=email).exists():
                return Response({"error": "this eamil is already taken", "status": 0}, status=status.HTTP_400_BAD_REQUEST)

            else:

                otp = Utility_function.generate_otp()
                is_email_valid = Utility_function.send_otp_for_registration(
                    email, otp)
                if not is_email_valid:
                    return Response({"error": "could not sent eamil to your email id", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    Email_varification_obj = models.Email_varification(
                        email=email, otp=otp)
                    Email_varification_obj.save()
                    return Response({"message": "we sent an otp to your email", "status": 1}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# this is step 2 for creating id
# here we will chek if the valid or not
class Varifi_otp_before_registration(APIView):  # 2
    serializer_class = serializers.otp_taker

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            print(otp, email)
            Email_varification_obj = models.Email_varification.objects.filter(
                email=email, otp=otp).first()
            print(Email_varification_obj)
            if Email_varification_obj and Email_varification_obj.is_otp_valid:
                return Response({"error": "otp is valied", "status": 1}, status=status.HTTP_200_OK)

            else:
                return Response({"error": "otp is invalied", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# this is the final step of registration
class UserSignupView(APIView):  # 3
    serializer_class = serializers.UserSerializer
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data['email']
            Email_varification_obj = models.Email_varification.objects.filter(email=email).exists()
            if not Email_varification_obj:return Response({'error': "registration unsuccessful", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()  # This internally calls create() with validated data
            # jwt pass 
            Refresh = RefreshToken.for_user(user)
            login(request,user) # this line not for production just for testing
            return Response({'message': 'Login successful.', 'user_id': user.id, "access": str(Refresh.access_token), 'refresh': str(Refresh)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#  after a successfull regsitratoin the user will be asked to login

# this the viwe to login


class User_login(APIView):  # 4
    serializer_class = serializers.LoginSerializer

    def post(self, request):

        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            print(email, password)
            authenticated_user = authenticate(
                username=email, password=password)
            if authenticated_user:
                Refresh = RefreshToken.for_user(authenticated_user)
                login(request,authenticated_user) # this line not for production just for testing
                return Response({'message': 'Login successful.', 'user_id': authenticated_user.id, "access": str(Refresh.access_token), 'refresh': str(Refresh)}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "your email or passwrod is incorrect", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# account security................passowrd...................


# ................ change password


class PasswordChangeView(APIView):  # 5
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = serializers.PasswordChangeSerializer(
                data=request.data)
            serializer.is_valid(raise_exception=True)
            user = request.user
            current_password = serializer.validated_data['current_password']
            new_password1 = serializer.validated_data['new_password']
            if not user.check_password(current_password):
                return Response({'error': 'Current password is not correct'}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(new_password1)
            user.save()
            return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# now if someone forget his password then we will use this code of bellow>>>>>>

class RequestPasswordReset(APIView):  # 6
    permission_classes = [AllowAny]
    serializer_class = serializers.ResetPasswordRequestSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = request.data['email']
            user = User.objects.filter(email__iexact=email).first()
            if user:
                token_generator = PasswordResetTokenGenerator()
                token = token_generator.make_token(user)
                reset_obj = models.PasswordReset(email=email, token=token)
                reset_obj.save()
                reset_url = f"http://127.0.0.1:8000/auth/reset-password/{token}/"
                print(reset_url)
                link_send = Utility_function.send_link_for_pass_set(
                    email, reset_url)
                if not link_send:
                    return Response({"error": "we could not send link to your email", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
                return Response({"message": "we sent a link  your email", "status": 1}, status=status.HTTP_200_OK)
            return Response({"error": "User with this email not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# the link is sent successfully then will allwo user to chang with that link


class ResetPassword(APIView): # 7
    serializer_class = serializers.ResetPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, token):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            new_password = data['new_password']
            reset_obj = models.PasswordReset.objects.filter(
                token=token).first()
            if not reset_obj:
                return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.filter(email=reset_obj.email).first()
            if user:
                user.set_password(new_password)
                user.save()
                reset_obj.delete()
                return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No user found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class Logout(APIView): # 8
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.logoutSerializer
    def post(self, request):
        logout(request) # this line for testing not for production
        serializer  = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                refresh_token  = serializer.validated_data['refresh_token']
                RefreshToken(refresh_token).blacklist()
                return Response(status=status.HTTP_200_OK)
            except Exception as e:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)