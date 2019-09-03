from django.db import models

Priorities = (
    (1, 'High'),
    (2, 'Normal'),
    (3, 'Low'),
)

class Boards(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    priority = models.IntegerField(default=1, choices=Priorities)
    created_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(null=True, blank=True)