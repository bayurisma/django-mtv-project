from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    title = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f"{self.id}. {self.title}"
