from django.urls import path
from .views import index, room, rooms


urlpatterns = [
    path('', index, name='base-index'),
    path('room/<str:roomId>/', room, name='base.room'),
    path('room/', rooms, name='base.rooms'),
]
