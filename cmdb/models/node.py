from django.db import models


ROLE_CHOICES = [
    ('general', 'General purpose'),
    ('lb', 'Load Balancer'),
    ('bastion', 'Bastion Host'),
    ('app', 'Application Node'),
]


class Node(models.Model):
    grid = models.ForeignKey('cmdb.Node', related_name='nodes')
    paid_for_by = models.ForeignKey('cmdb.Customer', related_name='nodes')

    hostname = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    role = models.CharField(
        max_length=max(len(key) for (key, label) in ROLE_CHOICES),
        choices=ROLE_CHOICES,
        default=ROLE_CHOICES[0][0],
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hostname

    @classmethod
    def get_or_create_dummy(cls):
        from .customer import Customer
        from .grid import Grid

        paid_for_by, unused = Customer.get_or_create_dummy()
        grid, unused = Grid.get_or_create_dummy()

        return cls.objects.get_or_create(
            hostname='restless-haze-25.plat2.leonidasoy.fi',
            defaults=dict(
                grid=grid,
                paid_for_by=paid_for_by,
            )
        )
