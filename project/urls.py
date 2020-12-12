
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls') ),
    path('boards/', include('apps.boards.urls') ),
    path('cards/', include('apps.cards.urls') ),
    path('comments/', include('apps.comments.urls') ),
    path('list/', include('apps.list.urls') ),
]
