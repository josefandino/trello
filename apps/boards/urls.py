from rest_framework.routers import DefaultRouter

from .views import BoardViewSet,BoardListUser

router = DefaultRouter()
router.register(r'', BoardViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('myboards',BoardListUser.as_view(),name="expenses")
]