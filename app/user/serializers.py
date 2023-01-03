"""
Django에서 사용하는 파이썬 객체나 쿼리셋 같이 복잡한 객체들을
Rest API에서 사용할 간단한 JSON 형태로 변환해주는 어댑터
참고:


Serializers for the user API View.
"""

from django.contrib.auth import (
    get_user_model,
)

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
