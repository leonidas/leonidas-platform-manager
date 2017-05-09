from django.db import models


class Server(models.Model):
    paid_for_by = models.ForeignKey('cmdb.Customer')

    hostname = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # REVERSE: services = ManyToMany('cmdb.Service')
