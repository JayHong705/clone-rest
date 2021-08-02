from rest_framework import viewsets, status

from app.api.account.serializers import ProfileSerializer
from app.rest_utils.mixins import CustomResponseMixin

from .models import Profile


class ProfileAPIViewSet(CustomResponseMixin, viewsets.GenericViewSet):
    """

    """
    queryset = Profile.objects.all()
    # authentication_classes =
    # permission_classes =
    serializer_class = ProfileSerializer

    def list(self, request):
        return self.response(
            status_code=status.HTTP_200_OK,
            data=self.get_serializer(self.queryset, many=True).data
        )