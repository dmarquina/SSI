from django.db import models
from tasks.models import Task

class Progress(models.Model):
	value = models.IntegerField(default=0)
	date = models.DateField(auto_now=False, auto_now_add=False,null=True, verbose_name='fecha')
	task = models.ForeignKey(Task,verbose_name='tarea')

	def __str__(self):
		return '%s' % (self.task.name)

	class Meta:
		ordering = ('id',)
