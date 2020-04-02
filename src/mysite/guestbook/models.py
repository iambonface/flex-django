from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    name    = models.CharField(max_length=35)
    comment = models.TextField(max_length=300)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Name: {}, ID: {}, Created: {}'.format(self.name, self.id, self.created)
