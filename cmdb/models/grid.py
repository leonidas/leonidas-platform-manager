from django.db import models


TYPE_CHOICES = [
    ('kontena', 'Kontena Grid'),
    ('swarm', 'Docker Swarm'),
]


class Grid(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    type = models.CharField(max_length=max(key for (key, label) in TYPE_CHOICES), choices=TYPE_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
