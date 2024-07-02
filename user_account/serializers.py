from user_profile.models import UserProfile
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError  # Correct import
from . import Utility_function
User = get_user_model()
GENDER = [
    ('male', 'male'),
    ('female', 'female'),

]

# register..................................


class email_taker(serializers.Serializer):  # 1
    email = serializers.EmailField()

class otp_taker(serializers.Serializer):  # 2
    email = serializers.EmailField()
    otp = serializers.IntegerField()
    token1 =serializers.CharField()
    token2 =serializers.CharField()


class UserSerializer(serializers.ModelSerializer):  # 3
    latitude = serializers.FloatField(required=False, allow_null=True)
    longitude = serializers.FloatField(required=False, allow_null=True)
    date_of_birth = serializers.DateField(required=True)
    profile_picture = serializers.URLField(required=False, allow_null=True)
    gender = serializers.ChoiceField(choices=GENDER)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password',
                  'date_of_birth', 'latitude', 'longitude', 'profile_picture', 'gender']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Extract the additional fields from validated_data
        latitude = validated_data.pop('latitude', None)
        longitude = validated_data.pop('longitude', None)
        date_of_birth = validated_data.pop('date_of_birth', None)
        profile_picture = validated_data.pop('profile_picture', None)
        gender = validated_data.pop('gender', None)
        # Create the user instance
        
        user = User.objects.create_user(**validated_data)
        current_profile = UserProfile.objects.create(
            user=user, date_of_birth=date_of_birth, gender=gender)
        if profile_picture:
            UserProfile.profile_picture = profile_picture
        if latitude and longitude:
            location_info = Utility_function.user_address_provider(
                latitude, longitude)
            print(location_info)
            try:
                current_profile.country = location_info['country']
                current_profile.state = location_info['state']
                current_profile.city = location_info['city']
                current_profile.latitude = location_info['latitude']
                current_profile.longitude = location_info['longitude']
            except Exception as e:
                pass
        current_profile.save()

        return user


# login............................
class LoginSerializer(serializers.Serializer):  # 4
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True, style={'input_type': 'password'})


# passwrod change with current password

class PasswordChangeSerializer(serializers.Serializer):  # 5
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


# now this the code if someone forget his/her passoword


class ResetPasswordRequestSerializer(serializers.Serializer):  # 6
    email = serializers.EmailField(required=True)


#
class ResetPasswordSerializer(serializers.Serializer):  # 7
    new_password = serializers.CharField(write_only=True, required=True)
    
    

class logoutSerializer(serializers.Serializer):  # 8
    refresh_token = serializers.CharField(write_only=True, required=True)
