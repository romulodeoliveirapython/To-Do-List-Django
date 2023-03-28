from django.db import models
from django.contrib.auth.models import User
import uuid


class Tasks(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) # UUID, parecido com Java
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    comment = models.TextField(blank = True)
    isComplete = models.BooleanField(default = False)

    def __str__(self):
        return self.title


# https://ohmycode.com.br/perfil-para-o-usuario-com-o-model-one-to-one-no-django/
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)