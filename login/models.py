from django.db import models
from django import forms

# Create your models here.
"""
class our_users(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length = 40,null=True)
	email = models.EmailField()

	class Meta:
		ordering = ['username']

	def __str__(self):
		return f"{self.username}"
"""