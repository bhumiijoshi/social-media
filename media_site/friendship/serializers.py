from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Follow
from .models import FollowRequest

User = get_user_model()


class FollowRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowRequest
        fields = ["id", "sender", "receiver", "created_at", "status"]

    def validate_receiver(self, value):
        if value == self.context["request"].user:
            raise serializers.ValidationError("You cannot follow yourself.")
        return value


class FollowUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class FollowSerializer(serializers.ModelSerializer):
    follower = FollowUsernameSerializer(read_only=True)
    following = FollowUsernameSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ["id", "follower", "following"]
