from django.db import models
from datetime import date, datetime

Priorities = (
    (1, 'High'),
    (2, 'Normal'),
    (3, 'Low'),
)

class Boards(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    priority = models.IntegerField(choices=Priorities)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def test(self):
        self.finished_at = datetime.date(self.finished_at)
        return date.today() > self.finished_at