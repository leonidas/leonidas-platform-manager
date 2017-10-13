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


ENVIRONMENT_CHOICES = [
    ('staging', 'Staging'),
    ('production', 'Production'),
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
    project = models.ForeignKey('cmdb.Project', related_name='projects')
    name = models.CharField(max_length=255)
    slug = models.CharField(**CommonFields.slug)
    canonical_name = models.CharField(unique=True, **CommonFields.slug)

    grid = models.ForeignKey('cmdb.Grid', blank=True, related_name='services')
    role = models.CharField(
        max_length=max(len(key) for (key, label) in ROLE_CHOICES),
        choices=ROLE_CHOICES,
        default=ROLE_CHOICES[0][0],
    )
    environment = models.CharField(
        max_length=max(len(key) for (key, label) in ENVIRONMENT_CHOICES),
        choices=ENVIRONMENT_CHOICES,
        default=ENVIRONMENT_CHOICES[0][0],
    )

    hostname = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    depends_on = models.ManyToManyField('self', blank=True, related_name='depended_on_by')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('project', 'slug')]

    def __str__(self):
        return self.name

    @classmethod
    def get_or_create_dummy(cls, role='backend'):
        from .project import Project
        from .grid import Grid

        project, unused = Project.get_or_create_dummy()
        grid, unused = Grid.get_or_create_dummy()

        defaults = dict(
            grid=grid,
            **DUMMY_DEFAULTS_BY_ROLE[role]
        )

        return cls.objects.get_or_create(
            project=project,
            role=role,
            defaults=defaults,
            environment='production',
        )
