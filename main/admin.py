from django.contrib import admin
from .models import Cont

@admin.register(Cont)
class ContAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'content', 'created_time', 'tag')
    search_fields=('tag', 'title')
    ordering = ('tag', 'created_time')
