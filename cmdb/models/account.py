from django.db import models

from .common import CommonFields


TYPE_CHOICES = [
    ('aws', 'Amazon Web Services'),
    ('digitalocean', 'DigitalOcean'),
    ('linode', 'Linode'),
    ('ramnode', 'Ramnode'),
]


class Account(models.Model):
    """
    Represents an account in a cloud service.
    """
    slug = models.CharField(unique=True, **CommonFields.slug)
    name = models.CharField(max_length=63)
    type = models.CharField(
        max_length=max(len(key) for (key, label) in TYPE_CHOICES),
        default=TYPE_CHOICES[0][0],
    )
    email = models.EmailField(verbose_name='E-mail address', help_text='E-mail address of the Root Account Credentials')
    managed_by = models.ForeignKey('cmdb.Customer', related_name='accounts')

    @classmethod
    def get_or_create_dummy(cls):
        from .customer import Customer

        managed_by, unused = Customer.get_or_create_dummy()

        return cls.objects.get_or_create(
            slug='leonidas-aws',
            defaults=dict(
                name='Leonidas AWS',
                email='it@leonidasoy.fi',
                managed_by=managed_by,
            )
        )
