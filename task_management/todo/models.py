from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class ToDoModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    status = models.BooleanField()
    