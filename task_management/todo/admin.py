from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.ToDoModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['title','description','status']