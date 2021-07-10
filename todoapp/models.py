from django.db import models


# Create your models here.
class Task(models.Model):
    taskname = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
