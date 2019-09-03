from django.db import models

class Boards(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    finished_at = models.DateTimeField()