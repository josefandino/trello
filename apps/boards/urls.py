from rest_framework.routers import DefaultRouter

from .views import BoardViewSet

router = DefaultRouter()
router.register (r'api/v1', BoardViewSet)
urlpatterns = router.urls

