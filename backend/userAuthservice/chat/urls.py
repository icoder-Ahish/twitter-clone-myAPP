from django.contrib import admin
from django.urls import path,include
from chat.views import MessageViewSet
from rest_framework import routers
# from . import views


router = routers.DefaultRouter()
router.register(r'chat', MessageViewSet, basename="chat")


urlpatterns = [
    
    path("", include(router.urls))
    
]