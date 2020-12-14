from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import UserViewSet

router = DefaultRouter()

router.register(r'', UserViewSet)

urlpatterns = router.urls
