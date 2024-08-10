from django.contrib import admin
from .models import Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('completed',)
    raw_id_fields = ('user',)

