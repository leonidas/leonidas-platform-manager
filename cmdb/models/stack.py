from django.db import models

from .common import CommonFields


ENVIRONMENT_CHOICES = [
    ('staging', 'Staging'),
    ('production', 'Production'),
]


class Stack(models.Model):
    project = models.ForeignKey('cmdb.Project', related_name='stacks')
    grid = models.ForeignKey('cmdb.Grid', blank=True, related_name='stacks')

    slug = models.CharField(unique=True, **CommonFields.slug)
    name = models.CharField(max_length=255)

    environment = models.CharField(
        max_length=max(len(key) for (key, label) in ENVIRONMENT_CHOICES),
        choices=ENVIRONMENT_CHOICES,
        default=ENVIRONMENT_CHOICES[0][0],
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def customer(self):
        return self.project.customer if self.project else None

    def admin_get_customer(self):
        return self.customer
    admin_get_customer.short_description = 'Customer'
    admin_get_customer.admin_order_field = 'project__customer'

    @classmethod
    def get_or_create_dummy(cls):
        from .project import Project
        from .grid import Grid

        project, unused = Project.get_or_create_dummy()
        grid, unused = Grid.get_or_create_dummy()

        return cls.objects.get_or_create(
            slug='cmdb-staging',
            defaults=dict(
                project=project,
                grid=grid,
                name='Leonidas Platform Manager',
                description='Documenting our resources',
            )
        )
