
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import UserProfile

User = get_user_model()

class UserListSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='profile.role', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'role']



class RegisterSerializer(serializers.ModelSerializer):
  first_name = serializers.CharField(required=True)
  last_name = serializers.CharField(required=True)
  email = serializers.EmailField(required=True)
  password = serializers.CharField(write_only=True)
  confirm_password = serializers.CharField(write_only=True, required=True)
  
  class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
        
        
 # field level validation : check unique email
  def validate_email(self, value):
    if User.objects.filter(email=value).exists():
      raise serializers.ValidationError("Email is already in use.")
    return value
  
  # object level validation : check password and confirm_password match
  def validate(self, data):
    if data['password'] != data['confirm_password']:
      raise serializers.ValidationError("Passwords did not match.")
    return data
  
  # create user and hash password
  def create(self, validated_data):
    validated_data.pop('confirm_password')
    
    user = User(
      first_name = validated_data['first_name'],
      last_name = validated_data['last_name'],
      username = validated_data['username'],
      email = validated_data['email']
    )
    
    user.set_password(validated_data['password'])
    user.save()
    return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Safely extract role
        try:
            profile = user.profile  # <- use related_name
            role = profile.role
        except:
            role = 'user'
        if user.is_superuser:
            role = 'admin'
        token['role'] = role
        return token
  