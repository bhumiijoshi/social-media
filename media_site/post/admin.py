from django.contrib import admin

from .models import Post,PostAttachment,Comment,Like

admin.site.register(Post)
admin.site.register(PostAttachment)
admin.site.register(Comment)
admin.site.register(Like)
