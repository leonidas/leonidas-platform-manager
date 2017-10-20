from django.db import models

from .common import CommonFields


ROLE_CHOICES = [
    ('backend', 'Web backend or API'),
    ('frontend', 'Web frontend'),
    ('database', 'Database'),
    ('queue', 'Message queue'),
    ('cache', 'Cache or auxiliary database'),
    ('worker', 'Background worker'),
]


DUMMY_DEFAULTS_BY_ROLE = dict(
    backend=dict(
        name='Backend',
        description='Python 3, Django',
    ),
    frontend=dict(
        name='Frontend',
        description='TypeScript, React, Redux isomorphic web app',
        hostname='cmdb.leonidasoy.fi',
    ),
    database=dict(
        slug='postgres',
        name='PostgreSQL',
        description='PostgreSQL 10',
    ),
    queue=dict(
        name='RabbitMQ',
    ),
    cache=dict(
        name='Redis',
    ),
    worker=dict(
        name='Worker',
        description='Python 3, Celery',
    )
)


class Service(models.Model):
    stack = models.ForeignKey('cmdb.Stack', related_name='services')
    name = models.CharField(max_length=255)
    slug = models.CharField(**CommonFields.slug)
    canonical_name = models.CharField(unique=True, **CommonFields.slug)

    role = models.CharField(
        max_length=max(len(key) for (key, label) in ROLE_CHOICES),
        choices=ROLE_CHOICES,
        default=ROLE_CHOICES[0][0],
    )

    hostname = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    depends_on = models.ManyToManyField('self', blank=True, related_name='depended_on_by')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('stack', 'slug')]

    def __str__(self):
        return self.name

    @property
    def project(self):
        return self.stack.project if self.stack else None

    def admin_get_project(self):
        return self.project
    admin_get_project.short_description = 'Project'
    admin_get_project.admin_order_field = 'stack__project'

    @property
    def customer(self):
        return self.project.customer if self.project else None

    def admin_get_customer(self):
        return self.customer
    admin_get_customer.short_description = 'Customer'
    admin_get_customer.admin_order_field = 'stack__project__customer'

    @classmethod
    def get_or_create_dummy(cls, role='backend'):
        from .stack import Stack

        stack, unused = Stack.get_or_create_dummy()

        return cls.objects.get_or_create(
            stack=stack,
            role=role,
            defaults=DUMMY_DEFAULTS_BY_ROLE[role],
        )
