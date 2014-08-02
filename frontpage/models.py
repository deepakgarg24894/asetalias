from django.db import models

class messages(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	subject=models.CharField(max_length=100)
	message=models.CharField(max_length=200)
