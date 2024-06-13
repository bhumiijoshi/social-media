from django.urls import include
from django.urls import path
from friendship.views import FollowListView
from friendship.views import FollowRequestViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

router = DefaultRouter()
router.register("follow_request", FollowRequestViewSet, basename="follow_request")


urlpatterns = [
    path("", include(router.urls)),
    path("followers/", FollowListView.as_view(), name="follower-list"),
]
