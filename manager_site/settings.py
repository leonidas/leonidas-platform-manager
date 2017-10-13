import os
from email.utils import parseaddr

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
    'ADMINS',
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

DEBUG = env.bool('DEBUG', default=False)

ADMINS = [parseaddr(addr) for addr in env('ADMINS', default='').split(',') if addr]
ALLOWED_HOSTS = env('ALLOWED_HOSTS', default='*' if DEBUG else '').split()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = dict(default=env.db('DATABASE_URL', default='psql://'))
MANAGERS = ADMINS
SECRET_KEY = env('SECRET_KEY', default='secret' if DEBUG else '')
SOCIAL_AUTH_GITHUB_ORG_KEY = env('GITHUB_KEY', default='')
SOCIAL_AUTH_GITHUB_ORG_NAME = env('GITHUB_ORG_NAME', default='')
SOCIAL_AUTH_GITHUB_ORG_SECRET = env('GITHUB_SECRET', default='')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
TIME_ZONE = env('TZ', default='Europe/Helsinki')
