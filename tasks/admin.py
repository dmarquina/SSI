from django.contrib import admin
from .models import Task

@admin.register(Task)
class AdminTask(admin.ModelAdmin):
	list_display = ('id','name','component','actions','responsable')
# Register your models here.
