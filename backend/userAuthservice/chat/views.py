from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Message, Chat
from .serializers import MessageSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        receiver_id = self.request.query_params.get('receiver')
        sender_id = self.request.query_params.get('sender')

        receiver = get_object_or_404(User, id=receiver_id)
        sender = get_object_or_404(User, id=sender_id)

        chat = Chat.objects.filter(participants=sender).filter(participants=receiver).first()
        if not chat:
            return Message.objects.none()

        messages = chat.messages.order_by('timestamp')
        return messages

    def create(self, request, *args, **kwargs):
        receiver_id = request.data.get('receiver')
        sender_id = request.data.get('sender')

        receiver = get_object_or_404(User, id=receiver_id)
        sender = get_object_or_404(User, id=sender_id)

        chat = Chat.objects.filter(participants=sender).filter(participants=receiver).first()
        if not chat:
            chat = Chat.objects.create()
            chat.participants.add(sender, receiver)

        content = request.data.get('content')
        image = request.FILES.get('image')
        message = Message.objects.create(sender=sender, receiver=receiver, content=content, image=image)
        chat.messages.add(message)
        chat.save()

        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




