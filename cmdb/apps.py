from django.apps import AppConfig


class CmdbAppConfig(AppConfig):
    name = 'cmdb'
    verbose_name = 'Configuration Management Database'

    def ready(self):
        from . import handlers  # noqa
