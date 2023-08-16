from django.contrib import admin
from tweet_app.models import TweetModel
from tweet_app.models import Retweet
from tweet_app.models import Mention
# Register your models here.


# Register your models here.

admin.site.register(TweetModel)
admin.site.register(Retweet)
admin.site.register(Mention)
