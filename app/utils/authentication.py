from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken


class CustomJWTAuthentication(authentication.BaseAuthentication):
    """
    validate token
    """
    @staticmethod
    def setattr_anonymous(user):
        setattr(user, 'id', 0)
        return user

    def authenticate(self, request):
        try:
            # validation through business logic
        except TokenError as e: # 만료된 경우 TokenError 발생
            user = AnonymousUser()
            return self.setattr_anonymous(user), None


