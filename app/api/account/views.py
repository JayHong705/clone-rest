from rest_framework import viewsets, status
from api.account.serializers import ProfileSerializer
from utils.mixins import CustomResponseMixin

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

    def retrieve(self, request, pk):
        profile = Profile.objects.get(id=pk)

        return self.response(
            status_code=status.HTTP_200_OK,
            data=self.get_serializer(profile).data
        )
