from django.db import models
from datetime import datetime as dt
from django.utils import timezone

class posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=dt.now, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Posts'

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

class comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=500)
    def __str__(self):
        return self.name