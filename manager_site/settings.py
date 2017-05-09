import os

import environ

from .settings_defaults import (
    AUTH_PASSWORD_VALIDATORS,
    AUTHENTICATION_BACKENDS,
    INSTALLED_APPS,
    LANGUAGE_CODE,
    MIDDLEWARE,
    ROOT_URLCONF,
    STATIC_URL,
    TEMPLATES,
    USE_I18N,
    USE_L10N,
    USE_TZ,
    WSGI_APPLICATION,
)


__all__ = [
    'ALLOWED_HOSTS',
    'AUTH_PASSWORD_VALIDATORS',
    'AUTHENTICATION_BACKENDS',
    'BASE_DIR',
    'DATABASES',
    'DEBUG',
    'INSTALLED_APPS',
    'LANGUAGE_CODE',
    'MIDDLEWARE',
    'ROOT_URLCONF',
    'SECRET_KEY',
    'STATIC_URL',
    'TEMPLATES',
    'TIME_ZONE',
    'USE_I18N',
    'USE_L10N',
    'USE_TZ',
    'WSGI_APPLICATION',
]


env = environ.Env()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
DEBUG = env.bool('DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY', default='secret' if DEBUG else '')
ALLOWED_HOSTS = env('ALLOWED_HOSTS', default='*' if DEBUG else '').split()
DATABASES = dict(default=env.db('DATABASE_URL', default='sqlite:///manager.sqlite3'))
TIME_ZONE = env('TZ', default='Europe/Helsinki')
SOCIAL_AUTH_GITHUB_ORG_KEY = env('GITHUB_KEY', default='')
SOCIAL_AUTH_GITHUB_ORG_SECRET = env('GITHUB_SECRET', default='')
SOCIAL_AUTH_GITHUB_ORG_NAME = env('GITHUB_ORG_NAME', default='')
