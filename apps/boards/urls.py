from rest_framework.routers import DefaultRouter

from .views import BoardViewSet

router = DefaultRouter()
router.register (r'tablero', BoardViewSet)
urlpatterns = router.urls

