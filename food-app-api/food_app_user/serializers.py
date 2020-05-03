
from django.contrib.auth import get_user_model,authenticate
from rest_framework import serializers

class UserSerilaizer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['FirstName','LastName','Email','password']

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class AuthTokenSerializer(serializers.Serializer):
    Email = serializers.CharField()
    password = serializers.CharField(
        style = {'input_type':'password'},
        trim_whitespace = False
        )

    def validate(self, attrs):
        Email = attrs.get('Email')
        password = attrs.get('password')

        user = authenticate(self.context.get('request'),username=Email,password=password)
        if not user:
            msg = 'Invalid login credentials'
            raise serializers.ValidationError(msg, code='authentication')
        attrs['user'] = user
        return attrs





