from django.contrib.auth import get_user_model

from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from typing import Any, Dict


Users = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ('id', 'email', 'full_name', 'is_active', 'created_at', )


class SignUpSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=128, required=True)
    
    class Meta:
        model = Users
        fields = ('id', 'email', "password", "re_password", 'full_name', 'is_active', 'created_at', )
    
    def validate(self, attrs):
        password, re_password = attrs.get("password"), attrs.pop("re_password")
        if not (password and re_password):
            raise serializers.ValidationError({"Error": "you must support password and re_password fields"})
        
        if password != re_password:
            raise serializers.ValidationError({"Error": "password and re_password fields must be the same"})
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        instance = Users.objects.create_user(**validated_data)
        return instance
    
    def update(self, instance, validated_data):
        return serializers.ValidationError({"Error": "This method isn't availabel"})
    
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "email": instance.email,
            "full_name": instance.full_name,
            "is_active": instance.is_active,
            "created_at": instance.created_at
        }


class LogInSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        attrs = super().validate(attrs)
        attrs.update({"user_id": self.user.id, "email": self.user.email})
        
        return attrs


class NewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)
    re_password = serializers.CharField(max_length=128)
    
    def validate(self, attrs):
        res = super().validate(attrs)
        
        password, re_password = attrs.get("password"), attrs.get("re_password")
        
        if password != re_password:
            raise serializers.ValidationError({"Error": "Password and re_password fields must be the same"})
        
        return res
