from django.db import models
from datetime import date, datetime

Priorities = (
    (1, 'High'),
    (2, 'Medium'),
    (3, 'Low'),
)

class Boards(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    priority = models.IntegerField(choices=Priorities)
    completed = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def deadline(self):
        if self.finished_at:
            self.finished_at = datetime.date(self.finished_at)
            return date.today() > self.finished_at
        else:
            return False