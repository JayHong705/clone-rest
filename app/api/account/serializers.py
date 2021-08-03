from rest_framework import serializers
from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = User
        fields = [
            'id',
            'identifier'
        ]

        read_only_fields = fields


class ProfileSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Profile
        fields = [
            'name',
            'device_token'
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    """
    유저와 프로필을 같이 가져오는 serializer
    """
    profile = ProfileSerializer()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + [
            'profile',
        ]