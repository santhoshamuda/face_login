# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    face_encoding = models.BinaryField(null=True, blank=True)
