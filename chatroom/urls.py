from django.urls import path
from .views import *

# app_name = 'chat'

urlpatterns = [
    path('', index, name='chat_index'),
    path('history/<str:room_id>/', history, name='history'),
    path('<str:group_id>/', room, name='room'),  
]
