from rest_framework import serializers

from users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        # validated_data : {'email': 'example@ex.fr', 'password': 'example'}
        return User.objects.create_user(**validated_data)
