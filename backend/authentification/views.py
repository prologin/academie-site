from django.contrib.auth import get_user_model

from authentification.serializers import TokenObtainPairSerializer, RegisterSerializer

from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets, mixins
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status


class ObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = RegisterSerializer

    def get(self, request):
        return Response(self.serializer_class(request.user).data, status=status.HTTP_200_OK)