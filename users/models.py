import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.DecimalField(max_digits=11, decimal_places=0, unique=True)
    first_name = models.CharField(max_length=1, null=True, editable=False)
    last_name = models.CharField(max_length=1, null=True, editable=False)
