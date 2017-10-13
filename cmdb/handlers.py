from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Customer, Grid, Project, Service
from .utils import slugify


for model in [
    Customer,
    Grid,
    Project,
    Service,
]:
    @receiver(pre_save, sender=model, weak=False)
    def set_slug_from_name(sender, instance, **kwargs):
        if instance.name and not instance.slug:
            instance.slug = slugify(instance.name)


@receiver(pre_save, sender=Service)
def set_canonical_name(sender, instance, **kwargs):
    if instance.slug and instance.project and instance.project.slug and not instance.canonical_name:
        instance.canonical_name = f'{instance.project.slug}/{instance.slug}'
