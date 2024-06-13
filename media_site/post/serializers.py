from rest_framework import serializers

from .models import Comment
from .models import Like
from .models import Post
from .models import PostAttachment
from .models import User


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="created_by.username")
    post_comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    post_likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    post_attachments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    body = serializers.CharField(required=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "body",
            "owner",
            "post_comments",
            "post_likes",
            "post_attachments",
        ]


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Comment
        fields = ["id", "body", "owner", "post"]


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Like
        fields = ["id", "owner", "post"]


class PostAttachmentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = PostAttachment
        fields = ["id", "owner", "post", "image"]
