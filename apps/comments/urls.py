from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import CommentViewSet

router = DefaultRouter()
router.register(r'viewset', CommentViewSet)
urlpatterns = router.urls