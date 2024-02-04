from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    choice_priority = [
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'High'),
    ]

    status_mark = [
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='task_images', default='Image')
    due_date = models.DateTimeField()
    priority = models.CharField(
        max_length=10, choices=choice_priority, default='1')
    status = models.CharField(
        max_length=10, choices=status_mark, default='incomplete')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
