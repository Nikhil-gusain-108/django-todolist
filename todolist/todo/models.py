from django.db import models
from django.utils.timezone import localtime
# Create your models here.
class todoses(models.Model):
    task = models.CharField(max_length=100)
    checked = False
    time = localtime
    def __str__(self):
        return self.task