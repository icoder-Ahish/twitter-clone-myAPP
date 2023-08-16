# from rest_framework import serializers
# from userAuthservice_app.models import userAuthModal


# # Create serilizers for UserAuth

# class userAuthSerializers(serializers.HyperlinkedModelSerializer):
#     user_id = serializers.ReadOnlyField()
#     class Meta:
#         model = userAuthModal
#         fields = "__all__"
from django.contrib.auth.models import User
from rest_framework import serializers

class userAuthSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
