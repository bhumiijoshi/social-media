from rest_framework.routers import DefaultRouter,SimpleRouter
from post.views import PostViewSet, CommentViewSet, LikeViewSet
from django.urls import path, include

post_router = DefaultRouter()
post_router.register("post", PostViewSet, basename="post")

comment_router = DefaultRouter()
comment_router.register("comment", CommentViewSet, basename="comment")

like_router = DefaultRouter()
like_router.register("like",LikeViewSet, basename="like" )

urlpatterns = [
    path('', include(post_router.urls)),
    path('', include(comment_router.urls)),
    path('', include(like_router.urls)),

]