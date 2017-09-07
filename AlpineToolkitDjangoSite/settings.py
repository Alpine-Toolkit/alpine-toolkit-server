####################################################################################################
#
# Alpine Toolkit - 
# Copyright (C) 2017 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
####################################################################################################

####################################################################################################

"""Django settings for Alpine Toolkit project.

"""

####################################################################################################

import os

from django.conf import settings
# from django_jinja.builtins import DEFAULT_EXTENSIONS

####################################################################################################
#
# Debug
#

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

####################################################################################################

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

####################################################################################################

ROOT_URLCONF = 'AlpineToolkitDjangoSite.urls'

WSGI_APPLICATION = 'AlpineToolkitDjangoSite.wsgi.application'

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xfhm&=2i&y*$yuot#_5+lw6b5jx!!(^wg)*#b^6qzh#h)3xtv^'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

####################################################################################################
#
# Database
#

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'NAME': 'alpinetoolkit',
        # 'USER': 'alpinetoolkit',
        # 'PASSWORD': 'alpinetoolkit',
    }
}

####################################################################################################
#
# Application definition
#

INSTALLED_APPS = [
    # /!\ ordered list
    # 'django.contrib.sites',

    'easy_thumbnails',
    'filer', # https://github.com/darklow/django-suit/issues/484
    'mptt',

    'suit', # before admin
    'django.contrib.admin',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'rest_framework',
    # 'django_filters',
    # 'rest_framework_filters',
    'crispy_forms',
    'rest_framework_swagger',

    'reversion',

    'django_jinja', # to complete Jinja2 backend
    'django_jinja.contrib._humanize',

    'AlpineToolkitDjangoApplication',
]

MIDDLEWARE_CLASSES = [
    # /!\ ordered list
    'reversion.middleware.RevisionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # to setup translation
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # for CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware', # for messaging
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

####################################################################################################
#
# Template
#

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        # 'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'APP_DIRS': True, # looks for app/jinja2
        # 'DIRS': [
        #     os.path.join(BASE_DIR, 'AlpineToolkitDjangoApplication', 'jinja2'),
        # ],
        'OPTIONS': {
            # 'environment': 'AlpineToolkitDjangoApplication.jinja2.environment', # for standard backend

            "app_dirname": "jinja2",
            "match_extension": ".html",
            # "match_extension": ".jinja",

            "newstyle_gettext": True,

            "context_processors": [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # "django.template.context_processors.i18n",
                # "django.template.context_processors.media",
                # "django.template.context_processors.static",
                # "django.template.context_processors.tz",
            ],

            # "extensions": DEFAULT_EXTENSIONS + [
            "extensions": [
                "jinja2.ext.do",
                "jinja2.ext.loopcontrols",
                "jinja2.ext.with_",
                "jinja2.ext.i18n",
                "jinja2.ext.autoescape",
                "django_jinja.builtins.extensions.CsrfExtension",
                "django_jinja.builtins.extensions.CacheExtension",
                "django_jinja.builtins.extensions.TimezoneExtension",
                "django_jinja.builtins.extensions.UrlsExtension",
                "django_jinja.builtins.extensions.StaticFilesExtension",
                "django_jinja.builtins.extensions.DjangoFiltersExtension",
            ],

            "bytecode_cache": {
                "name": "default",
                "backend": "django_jinja.cache.BytecodeCache",
                "enabled": False,
            },
            "autoescape": True,
            "auto_reload": settings.DEBUG,
            "translation_engine": "django.utils.translation",
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

####################################################################################################
#
# Password validation
#

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

####################################################################################################
#
# Internationalization
#

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

####################################################################################################
#
# LOGIN URLs
#

# LOGIN_REDIRECT_URL = 'accounts.profile'
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'accounts.login'
LOGOUT_URL = 'accounts.logout'

####################################################################################################
#
# Django Suit configuration
#

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Alpine Toolkit',
    'HEADER_DATE_FORMAT': 'l, j F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,

    # 'MENU': (
    #     'sites',

    #     {'app': 'auth', 'models': ('user', 'group')},
    #     {'label': 'Alpine Toolkit',
    #      'app': 'AlpineToolkitDjangoApplication',
    #      'models': ('circuit',),
    #     },
    # ),

    'LIST_PER_PAGE': 15
}

####################################################################################################
#
# REST Framework
#

REST_FRAMEWORK = {
    # http://www.django-rest-framework.org/api-guide/permissions/
    # IsAdminUser
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework_filters.backends.DjangoFilterBackend',
    ),
}

SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_key': '',
    'api_version': '1.0',
    # 'api_path': '/',
    # 'base_path': '',
    'doc_expansion': 'none',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'info': {
        'title': 'Alpine Toolkit REST API',
        'description': '''
        This page provides an automatically generated documentation for the <a href="/about-rest-api">Alpine Toolkit REST API</a>.
        You can learn the data schemas and try it out.
        Data are licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/">CC BY-NC-SA 3.0.</a>
        ''',
        # 'contact': 'fabrice.salvaire@orange.fr',
        # 'license': 'CC BY-NC-SA 3.0',
        # 'licenseUrl': 'http://creativecommons.org/licenses/by-nc-sa/3.0/',
        # 'termsOfServiceUrl': '/mentions-legales',
    },
    'is_authenticated': False,
    'is_superuser': False,
    'permission_denied_handler': None,
    'resource_access_handler': None,
    # 'token_type': Token,
}

####################################################################################################
#
# Email
#

# Log to console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

####################################################################################################
#
# Thumbnail
#

# THUMBNAIL_HIGH_RESOLUTION = True

# THUMBNAIL_PROCESSORS = (
#     'easy_thumbnails.processors.colorspace',
#     'easy_thumbnails.processors.autocrop',
#     #'easy_thumbnails.processors.scale_and_crop',
#     'filer.thumbnail_processors.scale_and_crop_with_subject_location',
#     'easy_thumbnails.processors.filters',
# )

####################################################################################################
#
# Filer
#

# FILER_CANONICAL_URL = 'sharing/'
