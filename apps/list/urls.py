from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import ListViewSet

router = DefaultRouter()
router.register(r'', ListViewSet)
urlpatterns = router.urls
