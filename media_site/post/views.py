from django.shortcuts import render
from .models import User, Comment, Like, PostAttachment, Post
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework import viewsets
from media_site.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)