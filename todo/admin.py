from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_display_links = ('category',)

admin.site.register(Task, TaskAdmin)
