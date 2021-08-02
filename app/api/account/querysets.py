from django.db import models
from django.db.models import Q


class UserQuerySet(models.QuerySet):
    """
    
    """
    @staticmethod
    def exclude_admin_user(self):
        return self.objects.exclude(
            Q(is_staff=True) |
            Q(is_superuser=True)
        )


class ProfileQuerySet(models.QuerySet):
    """

    """