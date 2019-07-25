from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=30)
    userName = models.CharField(max_length=30)
    contents = models.TextField()
    lookup = models.IntegerField(default=0)

    def __str__(self):
        return self.title