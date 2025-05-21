from django import template
from chat.models import ChatRoom

register = template.Library()

@register.filter
def chat_room_with(other_user, current_user):
    return ChatRoom.objects.filter(
        user1=current_user, user2=other_user
    ).first() or ChatRoom.objects.filter(
        user1=other_user, user2=current_user
    ).first()
