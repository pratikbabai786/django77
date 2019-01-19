from django.db import models

# Create your models here.
class Task(models.Model):
    taskname=models.CharField(max_length=30)
    deadline=models.DateField()
    completed=models.BooleanField()
