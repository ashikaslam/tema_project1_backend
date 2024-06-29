
# ............................. email send code .................
# email send moudles
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework import status
import random,requests
from geopy.geocoders import Nominatim



def send_email(email,link):
    try:
        email_id = email
        email_subject = "sub!!!"
        email_body = render_to_string('active_email.html', {'link' : link})
        email = EmailMultiAlternatives(email_subject , '', to=[email_id])
        email.attach_alternative(email_body, "text/html")
        email.send()
        return Response({"message":"successsfully email sent","status":1},status=status.HTTP_200_OK)

    except Exception as  e:
               print('here')
               return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# bellow codes are useing.......................
def send_link_for_pass_set(email,link):
    try:
        email_id = email
        email_subject = "sub!!!"
        email_body = render_to_string('pass_set.html', {'link' : link})
        email = EmailMultiAlternatives(email_subject , '', to=[email_id])
        email.attach_alternative(email_body, "text/html")
        email.send()
        return True
    except Exception as  e:
        print(e)
        return False
           
        
     
     
def generate_otp():
        """Generate a random 4-digit OTP."""
        return random.randint(100000, 999999)   
   
def send_otp_for_registration(email,otp):
    try:
        email_id = email
        email_subject ="Create your Id on WeShare!"
        email_body = render_to_string('create_id.html', {'otp':otp})
        email = EmailMultiAlternatives(email_subject , '', to=[email_id])
        email.attach_alternative(email_body, "text/html")
        email.send()
        return True
    except Exception as  e:
        print(e)
        return False

def user_address_provider(Latitude , Longitude):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="MyApp")
    coordinates = f"{Latitude} , {Longitude}"
    # Get location in English
    location = geolocator.reverse(coordinates, language='en')

    address = location.raw['address']

    # Traverse the data
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    return {'city':city,'state':state,'country':country }


