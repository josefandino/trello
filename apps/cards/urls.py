from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import CardViewSet

router = DefaultRouter()
router.register(r'', CardViewSet)
urlpatterns = router.urls