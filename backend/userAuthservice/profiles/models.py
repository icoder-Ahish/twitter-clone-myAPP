from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='users/avatars/', default='avatar.png')
    header = models.ImageField(upload_to='users/headers/', default='header.jpg')
    bio = models.CharField(max_length=240, blank=True)
   
   
    def __str__(self):
        return f'Profile for user {self.user.username}'

    # Method to get the count of followers
    def get_followers_count(self):
        return self.user.followers.count()

    # Method to get the count of following users
    def get_following_count(self):
        return self.user.following.count()


class Contact(models.Model):
    user_from = models.ForeignKey(
        User,
        related_name='following',  # New related_name for following users
        on_delete=models.CASCADE
    )
    user_to = models.ForeignKey(
        User,
        related_name='followers',  # New related_name for followers
        on_delete=models.CASCADE
    )
    
    is_followers = models.BooleanField(default=False)
    
    class Meta:
        # Add a unique constraint to prevent duplicate follow relationships
        unique_together = ('user_from', 'user_to')

    # created = models.DateTimeField(auto_now_add=True, db_index=True)
    created = models.DateTimeField(null=True, blank=True, db_index=True)

   
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'