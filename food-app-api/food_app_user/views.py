from rest_framework import generics
from food_app_user.serializers import UserSerilaizer

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerilaizer
