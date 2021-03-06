from django.db import models


ROLE_CHOICES = [
    ('general', 'General purpose'),
    ('lb', 'Load Balancer'),
    ('bastion', 'Bastion Host'),
    ('app', 'Application Node'),
]


class Node(models.Model):
    """
    A Node is a virtual or physical server that runs one or more Services.
    """
    grid = models.ForeignKey('cmdb.Grid', related_name='nodes')
    paid_for_by = models.ForeignKey('cmdb.Customer', related_name='nodes')
    account = models.ForeignKey('cmdb.Account', related_name='accounts', null=True, blank=True)

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
    def get_or_create_dummy(cls, name='restless-haze-25', grid=None):
        from .account import Account
        from .customer import Customer
        from .grid import Grid

        paid_for_by, unused = Customer.get_or_create_dummy()
        account, unused = Account.get_or_create_dummy()

        if grid is None:
            grid, unused = Grid.get_or_create_dummy()

        return cls.objects.get_or_create(
            hostname=f'{name}.plat2.leonidasoy.fi',
            defaults=dict(
                grid=grid,
                paid_for_by=paid_for_by,
            )
        )
