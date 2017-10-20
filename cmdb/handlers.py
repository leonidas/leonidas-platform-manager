from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Customer, Grid, Project, Service, Stack
from .utils import slugify


for model in [
    Customer,
    Grid,
    Project,
    Stack,
    Service,
]:
    @receiver(pre_save, sender=model, weak=False)
    def set_slug_from_name(sender, instance, **kwargs):
        if instance.name and not instance.slug:
            instance.slug = slugify(instance.name)


@receiver(pre_save, sender=Service)
def set_canonical_name(sender, instance, **kwargs):
    if instance.slug and instance.stack and instance.stack.slug and not instance.canonical_name:
        instance.canonical_name = f'{instance.stack.slug}/{instance.slug}'
