from django.db import models

from .common import CommonFields


class Project(models.Model):
    customer = models.ForeignKey('cmdb.Customer', related_name='projects')
    slug = models.CharField(unique=True, **CommonFields.slug)
    name = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_or_create_dummy(cls):
        from .customer import Customer

        customer, unused = Customer.get_or_create_dummy()

        return cls.objects.get_or_create(
            slug='cmdb',
            defaults=dict(
                customer=customer,
                name='Leonidas Platform Manager',
                description='Documenting our resources',
            )
        )
