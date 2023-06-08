from rest_framework import viewsets
from user.models import User
from user.serializers import UserSerializer
from django.contrib import auth
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from user import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_access_policy import AccessViewSetMixin
from user import policies


class UserViewSet(AccessViewSetMixin, viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    access_policy = policies.UserAccessPolicy

    def get_queryset(self):
        return self.access_policy.scope_queryset(self.request, self.queryset)

    @action(methods=['POST'], detail=False, authentication_classes=[])
    def login(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = auth.authenticate(username=email, password=password)
        try:
            Token.objects.get(user=user).delete()
        except Token.DoesNotExist:
            pass
        if user:
            token = Token.objects.create(user=user)
            auth.login(request, user)
            user_serializer = serializers.UserSerializer(user)
            return Response(
                {"token": token.key, "user": user_serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=['GET'], detail=False)
    def profile(self, request):
        if request.user.is_authenticated:
            serializer = self.serializer_class(request.user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=['POST'], detail=False)
    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)