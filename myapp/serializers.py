from rest_framework import serializers
#from django.contrib.auth.models import User
from myapp.models import User
import logging

class UserSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)
    password=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password1","password2","phone_number","password","profile_picture","role","address"]

    def create(self, validated_data):
        password1=validated_data.pop("password1")
        password2=validated_data.pop("password2")
        return User.objects.create_user(**validated_data,password=password1)
    
    def validate(self, data):
        if data["password1"]!=data["password2"]:
            raise serializers.ValidationError("password mismatch")
        
        return data
    

logger = logging.getLogger(__name__)

class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username)
            logger.debug(f"Found user by username: {user.username}")
        except User.DoesNotExist:
            raise serializers.ValidationError("No account found with this username.")

        # Check user role
        if not (user.role=="admin"):
            raise serializers.ValidationError('This is not a admin account.')

        # Verify password
        if not user.check_password(password):
            logger.debug(f"Password verification failed for user: {user.username}")
            raise serializers.ValidationError('Invalid password.')
        
        logger.debug("Authentication successful.")
        attrs['user'] = user
        return attrs
    
class StaffLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username)
            logger.debug(f"Found user by username: {user.username}")
        except User.DoesNotExist:
            raise serializers.ValidationError("No account found with this username.")

        # Check user role
        if not (user.role=="office_staff"):
            raise serializers.ValidationError('This is not a office stafff account.')

        # Verify password
        if not user.check_password(password):
            logger.debug(f"Password verification failed for user: {user.username}")
            raise serializers.ValidationError('Invalid password.')
        
        logger.debug("Authentication successful.")
        attrs['user'] = user
        return attrs
    

class LibrarianLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username)
            logger.debug(f"Found user by username: {user.username}")
        except User.DoesNotExist:
            raise serializers.ValidationError("No account found with this username.")

        # Check user role
        if not (user.role=="librarian"):
            raise serializers.ValidationError('This is not a librarian account.')

        # Verify password
        if not user.check_password(password):
            logger.debug(f"Password verification failed for user: {user.username}")
            raise serializers.ValidationError('Invalid password.')
        
        logger.debug("Authentication successful.")
        attrs['user'] = user
        return attrs