from django.db import models

# Create your models here.I
class TodoItem(models.Model):
	content=models.CharField(max_length=200)