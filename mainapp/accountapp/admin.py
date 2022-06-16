from django.contrib import admin
from .models import User


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at' ]

admin.site.register(User)
