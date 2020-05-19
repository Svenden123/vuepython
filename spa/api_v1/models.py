import uuid

from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=128)
    email = models.CharField(max_length=128, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    description = models.TextField(max_length=4096)
    url = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'event'
        verbose_name_plural = 'events'
