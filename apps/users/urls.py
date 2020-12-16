from rest_framework.routers import DefaultRouter
from django.urls import path

# from .views import UserViewSet, RegisterView, LoginAPIView
from apps.users.views import UserViewSet

router = DefaultRouter()

router.register(r'', UserViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('register/',RegisterView.as_view(),name= "register"),
#     path('login/', LoginAPIView.as_view(), name="login"),
# ]

# urlpatterns += router.urls


