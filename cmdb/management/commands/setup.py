from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = ''
    help = 'Setup all the things'

    def handle(self, *args, **options):
        call_command('migrate')

        if settings.DEBUG:
            from django.contrib.auth import get_user_model
            User = get_user_model()

            superuser, created = User.objects.get_or_create(
                username='admin',
                first_name='Admin',
                last_name='Admin',
                email='admin@example.com',
                is_staff=True,
                is_superuser=True,
            )

            if created:
                superuser.set_password('secret')
                superuser.save()
