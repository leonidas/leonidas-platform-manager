from django.db import models


class Service(models.Model):
    project = models.ForeignKey('cmdb.Project')
    hostname = models.CharField(max_length=255)

    servers = models.ManyToManyField('cmdb.Server', related_name='services', blank=True)
    grid = models.ForeignKey('cmdb.Grid', blank=True)

    name = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
