from django.contrib import admin

from .models import Restaurant, Menu, MenuImage
# Register your models here.


admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(MenuImage)

