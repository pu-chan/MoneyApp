from django.db import models
from django.urls import reverse

class Task(models.Model):
    message = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('todo:index')
