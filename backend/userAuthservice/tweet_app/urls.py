from django.contrib import admin
from django.urls import path,include
from tweet_app.views import TweetViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'tweet', TweetViewSet, basename="tweet")

urlpatterns = [ 
    path("", include(router.urls))
    
]