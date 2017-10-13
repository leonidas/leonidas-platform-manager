from django.db import models

from .common import CommonFields


class Customer(models.Model):
    slug = models.CharField(unique=True, **CommonFields.slug)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    is_internal = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_or_create_dummy(cls):
        return cls.objects.get_or_create(
            slug='leonidas',
            defaults=dict(
                name='Leonidas Oy',
                description='An agile software company at the forefront of XR technologies',
                is_internal=True,
            )
        )
