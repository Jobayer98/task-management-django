from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    priority_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=priority_choices)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class TaskPhoto(models.Model):
    task = models.ForeignKey(Task, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='task_photos/', null=True, blank=True)

    def __str__(self):
        return f'{self.task.title} - Photo {self.id}'