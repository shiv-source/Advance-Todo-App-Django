from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=100, blank=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at");
    completed_at = models.DateTimeField(verbose_name="completed at", blank=True , null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name