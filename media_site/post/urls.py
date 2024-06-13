from django.urls import include
from django.urls import path
from post.views import CommentViewSet
from post.views import LikeViewSet
from post.views import PostViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

post_router = DefaultRouter()
post_router.register("post", PostViewSet, basename="post")

comment_router = DefaultRouter()
comment_router.register("comment", CommentViewSet, basename="comment")

like_router = DefaultRouter()
like_router.register("like", LikeViewSet, basename="like")

urlpatterns = [
    path("", include(post_router.urls)),
    path("", include(comment_router.urls)),
    path("", include(like_router.urls)),
]
