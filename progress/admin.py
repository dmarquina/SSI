from django.contrib import admin
from .models import Progress

@admin.register(Progress)
class AdminProgress(admin.ModelAdmin):
	list_display = ('id','value','date','task')
