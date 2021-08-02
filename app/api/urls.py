from rest_framework.routers import SimpleRouter
from app.api.account import views as profile_view

# router.register(<prefix>, <viewset>, basename=<prefix>)
router_v1 = SimpleRouter(trailing_slash=False)
router_v1.register('profile', profile_view.ProfileAPIViewSet, basename='profile')

urlpatterns = []


