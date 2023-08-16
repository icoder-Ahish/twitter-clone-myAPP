from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Profile, Contact
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, ContactSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    # The function is use to get profile data by user id
    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')  # Retrieve the user_id from the URL
        user = get_object_or_404(User, id=user_id)  # Get the User object by user_id
        profile = get_object_or_404(Profile, user=user)  # Get the Profile object by the User object
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    # Getting all followers and following users
    @action(detail=True, methods=['get'])
    def followers_following(self, request, pk=None):
        user = self.get_object()  # Get the user based on the provided ID
        
        followers = user.followers.all()
        following = user.following.all()

        followers_list = [{"id": follower.id, "username": follower.username} for follower in followers]
        following_list = [{"id": following_user.id, "username": following_user.username} for following_user in following]
        
        return Response({
            "followers": followers_list,
            "following": following_list
        })
        
    @action(detail=False, methods=['post'])
    # Custom action to follow a user
    def follow(self, request):
        user_from_id = request.data.get('user_from')
        user_to_id = request.data.get('user_to')
        
        
        print(f'getting user_from and user_to ids {user_from_id } and {user_to_id}')

        user_from = get_object_or_404(Profile, user__id=user_from_id)
        user_to = get_object_or_404(Profile, user__id=user_to_id)

        # Check if the user is not following the target user already
        if not user_from.user.following.filter(id=user_to.user.id).exists():
            # Create a new Contact instance to represent the follow relationship
            Contact.objects.create(user_from=user_from.user, user_to=user_to.user,is_followers=True)
            
            return Response({'message': 'User followed successfully.'})

        return Response({'message': 'User is already followed.'})

    @action(detail=False, methods=['post'])
    def unfollow(self, request):
        user_from_id = request.data.get('user_from')
        user_to_id = request.data.get('user_to')

        user_from = get_object_or_404(User, id=user_from_id)
        user_to = get_object_or_404(User, id=user_to_id)

        try:
            contact = Contact.objects.get(user_from=user_from, user_to=user_to)
            contact.delete()
            return Response({'message': 'User unfollowed successfully.'})
        except Contact.DoesNotExist:
            return Response({'message': 'User is not followed yet.'})
