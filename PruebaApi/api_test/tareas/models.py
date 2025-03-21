from django.db import models

class Homework(models.Model):
    title = models.TextField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
