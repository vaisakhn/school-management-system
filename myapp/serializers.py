from rest_framework import serializers
#from django.contrib.auth.models import User
from myapp.models import User

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