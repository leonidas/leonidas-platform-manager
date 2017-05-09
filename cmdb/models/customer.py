from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    is_internal = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
