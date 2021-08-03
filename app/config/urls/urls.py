from django.contrib import admin
from django.urls import (
    path,
    include
)
from api.urls import router_v1

urlpatterns = [
    path('api/', include('api.urls')),
    path('api/v1/', include((router_v1.urls, 'api-v1'))),
    path('tothemoon/', admin.site.urls)
]