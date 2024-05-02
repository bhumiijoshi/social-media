from django.conf import settings
from django.db import models
from media_site.models import BaseModel
from users.models import User


class Post(BaseModel):
    body = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
        db_table = "post"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        
    def __str__(self):
        return f"{self.created_by.username} - {self.body[:10]}"
    
class Like(BaseModel):
    post = models.ForeignKey(Post, related_name='post_likes',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
   

class Comment(BaseModel):
    body = models.TextField(blank=True, null=True)
    post = models.ForeignKey(Post, related_name='post_comments',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
                  

class PostAttachment(BaseModel):
    image = models.ImageField(upload_to='post_attachment')
    post = models.ForeignKey(Post, related_name='post_attachments',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='attachments', on_delete=models.CASCADE)



    