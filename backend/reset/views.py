import uuid

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from reset.serializers import ResetPasswordSerializer, ResetPasswordSerializerId

User = get_user_model()


class PasswordResetIdView(generics.CreateAPIView):

    serializer_class = ResetPasswordSerializerId
    permission_classes = [AllowAny]

    def post(self, request, id):
        serializer = self.get_serializer(data=request.data)
        user_id = cache.get(id)
        if user_id is None or not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(id=user_id)
        if user is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.set_password(request.data["password"])
        cache.delete(id)
        return Response(status=status.HTTP_200_OK)


class PasswordResetView(generics.CreateAPIView):

    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        val = serializer.is_valid()
        if not val:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        id = uuid.uuid4()
        user = User.objects.get(email=request.data["email"])
        cache.set(id, user.id, 60 * 15)

        email_plaintext_message = f"Wesh batard clique ici tkt: \nhttp://127.0.0.1:8080/reset/{id}/\n\nCordialement Mr Prologin"

        send_mail(
            f"Password Reset for {user.username}",
            email_plaintext_message,
            "noreply@prologin.org",
            [user.email],
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
