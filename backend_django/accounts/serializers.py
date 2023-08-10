from .models import COOPUser  # Ensure you're importing the correct model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = COOPUser
        fields = ['id', 'deposit_number', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = COOPUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
