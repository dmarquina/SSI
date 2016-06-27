from django.contrib import admin
from .models import Component

@admin.register(Component)
class AdminComponent(admin.ModelAdmin):
	list_display = ('id','name')