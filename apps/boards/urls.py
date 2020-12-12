from rest_framework.routers import DefaultRouter

from .views import BoardViewSet

router = DefaultRouter()
router.register (r'', BoardViewSet)
urlpatterns = router.urls

