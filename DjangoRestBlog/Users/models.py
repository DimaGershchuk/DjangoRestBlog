from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Чоловік'), ('female', 'Жінка'), ('other', 'Інший')], null=True, blank=True)

    def __str__(self):
        return self.username
