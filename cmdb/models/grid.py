from django.db import models

from .common import CommonFields


TYPE_CHOICES = [
    ('kontena', 'Kontena Grid'),
    ('aws-ess', 'AWS ElasticSearch Service'),
    ('aws-rds', 'AWS RDS'),
    ('bunch', 'Just a bunch of nodes'),
]


class Grid(models.Model):
    """
    A Grid is a collection of Nodes. It may or may not use some fancy cluster management software,
    such as Kontena.
    """

    slug = models.CharField(unique=True, **CommonFields.slug)
    name = models.CharField(max_length=255)
    description = models.TextField()

    type = models.CharField(
        max_length=max(len(key) for (key, label) in TYPE_CHOICES),
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES[0][0],
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_or_create_dummy(cls):
        from .node import Node

        grid, created = cls.objects.get_or_create(
            slug='plat2-grid',
            defaults=dict(
                name='Plat2',
                description='Leonidas Platform Revision 2',
                type='kontena',
            )
        )

        for node_name in [
            'spring-butterfly-50',
            'muddy-rain-28',
            'autumn-river-15',
        ]:
            Node.get_or_create_dummy(name=node_name, grid=grid)

        return grid, created
