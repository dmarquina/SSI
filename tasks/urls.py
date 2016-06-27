from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^tasks/create_task$', views.createTask, name="createtask"),
	url(r'^tasks/show_all_tasks$', views.showAllTasks, name="showalltasks"),
]