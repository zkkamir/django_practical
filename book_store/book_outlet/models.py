from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.IntegerField()

    def __str__(self):
        return self.title
