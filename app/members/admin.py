from django.contrib import admin

from posts.models import Post
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'is_staff', 'date_joined',]
    search_fields = ['username',]
    ordering = ['-id', 'date_joined',]


admin.site.register(User, UserAdmin)
