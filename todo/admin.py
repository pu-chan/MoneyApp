from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('message','completed')
    list_display_links = ('message','completed')

admin.site.register(Task, TaskAdmin)
