from django.db import models
import datetime

class MyWatchList(models.Model):
    watched = models.BooleanField(null=True)
    title = models.CharField(max_length=255)
    rating = models.IntegerField(blank=True, null=True)
    release_date = models.DateField(blank=True, default=datetime.date.today)
    review = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title}"