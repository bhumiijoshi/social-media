from django.conf import settings
from django.db import models
from users.models import User

from media_site.models import BaseModel


class Follow(BaseModel):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )

    class Meta:
        unique_together = ("follower", "following")
        db_table = "follow"
        verbose_name = "Follow"

    def __str__(self):
        return f"{self.follower} is following {self.following}"


class FollowRequest(BaseModel):
    REQUEST_STATUS = (
        ("accepted", "Accepted"),
        ("not_accepted", "Not Accepted"),
        ("declined", "Declined"),
    )

    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_friend_requests"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_friend_requests"
    )
    status = models.CharField(
        max_length=20, choices=REQUEST_STATUS, default="not_accepted"
    )

    class Meta:
        unique_together = ("sender", "receiver")
        db_table = "follow_request"
        verbose_name = "Follow_Request"

    def __str__(self):
        return f"{self.sender} sended request to {self.receiver}"
