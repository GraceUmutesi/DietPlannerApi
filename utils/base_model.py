import uuid

from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='%(class)s_created_by', on_delete=models.PROTECT)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
