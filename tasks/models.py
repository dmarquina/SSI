from django.db import models
from userprofiles.models import Userprofile
from components.models import Component

class Task(models.Model):
	name = models.CharField(max_length=255)
	actions = models.CharField(max_length=255)
	observations = models.CharField(max_length=255)
	responsable = models.ForeignKey(Userprofile,verbose_name='responsable')
	component = models.ForeignKey(Component,verbose_name='componente')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('id',)

