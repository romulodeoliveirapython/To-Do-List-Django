from django.db import models
from django.contrib.auth.models import User
import uuid


class ToDo(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) # UUID, parecido com Java
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    comment = models.TextField(blank = True)
    isComplete = models.BooleanField(default = False)

    def __str__(self):
        return self.title