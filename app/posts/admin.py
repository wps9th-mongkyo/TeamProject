from django.contrib import admin

# Register your models here.
from .models import Post, PostImage


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'restaurant', 'rate', 'created_at', 'modified_at']
    search_fields = ['author', 'restaurant']
    ordering = ['-id', 'rate', 'created_at']


class PostImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'post']


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
