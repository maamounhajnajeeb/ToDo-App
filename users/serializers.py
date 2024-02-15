from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'is_active', 'created_at', )


class SignUpSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=128, required=True)
    
    class Meta:
        model = User
        fields = ('id', 'email', "password", "re_password", 'full_name', 'is_active', 'created_at', )
    
    def validate(self, attrs):
        password, re_password = attrs.get("password"), attrs.get("re_password")
        if not (password and re_password):
            raise serializers.ValidationError({"Error": "you must support password and re_password fields"})
        
        if password != re_password:
            raise serializers.ValidationError({"Error": "password and re_password fields must be the same"})
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        instance = User.objects.create_user(**validated_data)
        return instance
    
    def update(self, instance, validated_data):
        return serializers.ValidationError({"Error": "This method isn't availabel"})
