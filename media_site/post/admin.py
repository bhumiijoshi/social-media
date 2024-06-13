from django.contrib import admin

from .models import Comment
from .models import Like
from .models import Post
from .models import PostAttachment

admin.site.register(Post)
admin.site.register(PostAttachment)
admin.site.register(Comment)
admin.site.register(Like)
