from django.db import models
from django.db.models import Q
from .models import User


class UserQuerySet(models.QuerySet):
    """
    
    """
    def exclude_admin_user(self):
        return User.objects.exclude(
            Q(is_staff=True) |
            Q(is_superuser=True)
        )


class ProfileQuerySet(models.QuerySet):
    """

    """