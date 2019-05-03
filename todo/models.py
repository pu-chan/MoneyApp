from django.db import models
from django.urls import reverse

class Task(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('todo:index')
