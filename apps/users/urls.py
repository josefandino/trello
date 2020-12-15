from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import UserViewSet, RegisterView, LoginAPIView

router = DefaultRouter()

router.register(r'', UserViewSet)



urlpatterns = [
    path('register/',RegisterView.as_view(),name= "register"),
    path('login/', LoginAPIView.as_view(), name="login"),
]

urlpatterns += router.urls