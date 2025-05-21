from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    user1 = models.ForeignKey(User, related_name='user1_rooms', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user2_rooms', on_delete=models.CASCADE)

    def __str__(self):
        return f"ChatRoom between {self.user1.username} and {self.user2.username}"

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] {self.user.username}: {self.content[:30]}..."
