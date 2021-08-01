from rest_framework.routers import SimpleRouter
from app.api.account.views import ProfileAPIViewSet

# router.register(<prefix>, <viewset>, basename=<prefix>)
router_v1 = SimpleRouter(trailing_slash=False)
router_v1.register('profile', ProfileAPIViewSet, basename='profile')

urlpatterns = []


