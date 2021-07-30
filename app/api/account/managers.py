from django.contrib.auth.models import BaseUserManager
from django.utils.crypto import get_random_string

from querysets import UserQuerySet, ProfileQuerySet


class UserDefaultManager(BaseUserManager.from_queryset(UserQuerySet)):
    """
    user를 생성하는 함수들을 포함한 manager
    """
    def create_user(self, identifier, password=None):
        user = self.model(identifier=identifier)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def _create_superuser(self, identifier, password=None):
        user = self.create_user(
            identifier=identifier,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

    def _create_socialuser(self, identifier):
        user = self.model(identifier=identifier)
        unique_password = get_random_string(length=32)
        user.set_password(unique_password)
        user.save(using=self._db)
        return user


class ProfileDefaultManager(BaseUserManager.from_queryset(ProfileQuerySet)):
    pass
