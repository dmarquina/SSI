from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^progress/set_progress$', views.setProgress, name="setprogress"),
	url(r'^progress/show_progress$', views.showProgress, name="showprogress"),
]