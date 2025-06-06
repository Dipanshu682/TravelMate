from django.urls import path
from . import views

urlpatterns = [
    path('send-invite/<int:user_id>/', views.send_invite, name='send_invite'),
    path('room/<int:room_id>/', views.chat_room, name='chat_room'),
    path('room/<int:room_id>/messages/', views.fetch_messages, name='fetch_messages'),
    path('room/<int:room_id>/send/', views.send_message, name='send_message'),
]
