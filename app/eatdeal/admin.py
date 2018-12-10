from django.contrib import admin

from .models import Eatdeal, EatdealImage


class EatdealAdmin(admin.ModelAdmin):
    list_display = ['id', 'restaurant', 'deal_name', 'created_at', 'modified_at',]
    search_fields = ['restaurant', 'deal_name']
    ordering = ['-id', 'restaurant', 'created_at']

admin.site.register(Eatdeal, EatdealAdmin)
admin.site.register(EatdealImage)

