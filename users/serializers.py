from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "full_name", "artistic_name"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data["password"]

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()

        return instance
