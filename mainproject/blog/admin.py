from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "assigned_to")
    list_filter = ("status", "assigned_to")
    search_fields = ("title", "description")