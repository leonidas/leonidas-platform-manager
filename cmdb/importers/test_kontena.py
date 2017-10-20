import pytest
import yaml
from pkg_resources import resource_string

from ..models import Project, Grid

from .kontena import import_stack


EXAMPLE_STACK_DICT = yaml.safe_load(resource_string(__name__, 'data/example_kontena_stack.yml'))


@pytest.mark.django_db
def test_import_stack():
    project, unused = Project.get_or_create_dummy()
    grid, unused = Grid.get_or_create_dummy()

    stack = import_stack('wordpress', EXAMPLE_STACK_DICT, project, grid)

    assert stack.services.count() == 2

    wordpress = stack.services.get(slug='wordpress')
    assert wordpress.hostname == 'example.com'
    assert wordpress.role == 'backend'

    mariadb = stack.services.get(slug='mariadb')
    assert mariadb.role == 'database'
