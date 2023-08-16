# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Contact
from tweet_app.models import TweetModel
from tweet_app.serializers import TweetSerializer

class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    tweets = TweetSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'header', 'bio' ,'followers_count', 'following_count', 'tweets',]

    def get_followers_count(self, profile):
        # Calculate the count of followers for the profile
        return profile.user.followers.count()

    def get_following_count(self, profile):
        # Calculate the count of following users for the profile
        return profile.user.following.count()

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
