from rest_framework import serializers
from .models import Message


from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# from userAuthservice_app.serializers import userAuthSerializers


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'content', 'image', 'timestamp')
