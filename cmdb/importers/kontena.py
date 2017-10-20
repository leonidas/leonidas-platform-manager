import logging

from ..models import Stack, Service
from ..utils import log_get_or_create


logger = logging.getLogger(__name__)


ROLE_GUESSES = dict(
    postgres='database',
    sql='database',
    mariadb='database',
    mongo='database',
    memcache='cache',
    redis='cache',
    celery='worker',
    worker='worker',
    api='backend',
    frontend='frontend',
    web='backend',
)

DEFAULT_ROLE = 'backend'


def guess_role_from(item):
    """
    >>> guess_role_from('registry.plat2.leonidasoy.fi/leonidas2017-mariadb')
    'database'
    """
    for role_guess, guessed_role in ROLE_GUESSES.items():
        if role_guess in item:
            return guessed_role


def guess_role(service_slug, service_dict, default_role=DEFAULT_ROLE):
    """
    Tries to guess role first from service_slug and then service_dict['image'].
    """
    role = guess_role_from(service_slug)
    if role:
        return role

    role = guess_role_from(service_dict.get('image', ''))
    if role:
        return role

    return default_role


def env_list_to_dict(env_list):
    """
    >>> env_list_to_dict(['KONTENA_LB_MODE=http', 'KONTENA_LB_VIRTUAL_HOSTS=leonidasoy.fi'])
    {'KONTENA_LB_MODE': 'http', 'KONTENA_LB_VIRTUAL_HOSTS': 'leonidasoy.fi'}
    """
    return dict(env_item.split('=', 1) for env_item in env_list)


def get_service_env(service_dict, env_name, default=None):
    environment = service_dict.get('environment', dict())

    if isinstance(environment, list):
        environment = env_list_to_dict(environment)

    return environment.get(env_name, default)


def import_stack(stack_slug, stack_dict, project, grid, environment='staging'):
    stack, created = Stack.objects.get_or_create(
        slug=stack_slug,
        defaults=dict(
            name=stack_slug,
            project=project,
            grid=grid,
            environment=environment,
            description=stack_dict.get('description', ''),
        )
    )

    log_get_or_create(logger, stack, created)

    for service_slug, service_dict in stack_dict['services'].items():
        role = guess_role(service_slug, service_dict)
        hostnames = get_service_env(service_dict, 'KONTENA_LB_VIRTUAL_HOSTS', '').split()
        hostname = hostnames[0] if hostnames else ''

        service, created = Service.objects.get_or_create(
            stack=stack,
            slug=service_slug,
            defaults=dict(
                name=service_slug,
                description=service_dict.get('description', ''),
                role=role,
                hostname=hostname,
            )
        )

        log_get_or_create(logger, service, created)

    return stack
