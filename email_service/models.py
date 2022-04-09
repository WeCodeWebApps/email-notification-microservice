from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Model(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)


class EmailTemplate(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    template_name = models.CharField(max_length=30)
    args = models.JSONField(default=list)
    text = models.TextField()

    def __str__(self) -> str:
        return self.template_name
