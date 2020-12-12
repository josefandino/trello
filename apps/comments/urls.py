from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import CommentViewSet

router = DefaultRouter()
router.register(r'api/v1', CommentViewSet)
urlpatterns = router.urls