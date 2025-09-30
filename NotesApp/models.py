from django.db import models
from django.conf import settings

class Note(models.Model):
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    null=True,   
    blank=True)
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
