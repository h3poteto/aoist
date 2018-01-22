from django.db import models

class Youtube(models.Model):
    movie_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

    def __str__(self):
        return self.title
