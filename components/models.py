from django.db import models

class Component(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('id',)

