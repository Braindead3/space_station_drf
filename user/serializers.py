from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs) -> User:
        """
        Save user to db and validate password
        :return: New created User
        """
        if self.is_valid():
            user = User(
                username=self.validated_data['username']
            )
            password1 = self.validated_data['password']
            password2 = self.validated_data['password2']

            if password1 != password2:
                raise serializers.ValidationError({'password': 'Passwords must match.'})

            user.set_password(password1)
            user.save()

            return user
        else:
            return self.errors
