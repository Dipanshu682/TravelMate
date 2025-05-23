from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from .models import ChatRoom, Message
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@login_required
def send_invite(request, user_id):
    current_user = request.user
    other_user = get_object_or_404(User, pk=user_id)

    chat_room = ChatRoom.objects.filter(
        models.Q(user1=current_user, user2=other_user) |
        models.Q(user1=other_user, user2=current_user)
    ).first()

    if not chat_room:
        chat_room = ChatRoom.objects.create(user1=current_user, user2=other_user)

    return redirect('chat_room', room_id=chat_room.id)

@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    if request.user not in [room.user1, room.user2]:
        return redirect('home')

    return render(request, 'chat/room.html', {'room': room})

@login_required
def fetch_messages(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    return JsonResponse([
        {'user': msg.user.username, 'message': msg.content, 'timestamp': msg.timestamp.strftime('%H:%M')}
        for msg in messages
    ], safe=False)

@require_POST
@login_required
def send_message(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    content = request.POST.get('message')
    if content:
        Message.objects.create(room=room, user=request.user, content=content)
    return JsonResponse({'status': 'ok'})
