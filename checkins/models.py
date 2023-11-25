import uuid
from django.db import models


class Checkin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    employee_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='checkins')
