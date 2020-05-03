from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from food_app_user.serializers import UserSerilaizer,AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerilaizer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    