from django.contrib import admin
from friendship.models import Follow
from friendship.models import FollowRequest

admin.site.register(Follow)
admin.site.register(FollowRequest)
