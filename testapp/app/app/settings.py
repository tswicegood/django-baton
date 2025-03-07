"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm5%-jr^27gr893xb%ey^%+2de#y844-oi5y1_!%h%^+1*bz5gj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
INSTALLED_APPS = [
    'app',
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'easy_thumbnails',
    'admin_auto_filters',
    'rangefilter',
    'import_export',
    'filer',
    'tinymce',
    'mptt',
    'news',
    'baton.autodiscover',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
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

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

BATON = {
    'SITE_HEADER': 'Baton Test App',
    'SITE_TITLE': 'Baton Test App',
    'INDEX_TITLE': 'Baton administration',
    'SUPPORT_HREF': 'mailto:mail@otto.to.it',
    'COPYRIGHT': 'copyright © 2020 <a href="https://www.otto.to.it">Otto srl</a>',  # noqa
    'POWERED_BY': 'Otto srl',
    'CONFIRM_UNSAVED_CHANGES': False,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'COLLAPSABLE_USER_AREA': False,
    'MENU_ALWAYS_COLLAPSED': False,
    'MESSAGES_TOASTS': ['success'],
    'GRAVATAR_DEFAULT_IMG': 'robohash',
    'LOGIN_SPLASH': '/static/app/bg.jpg',
    'SEARCH_FIELD': {
        'label': 'Search news',
        'url': '/admin/search/',
    },
    'MENU': (
        {
            'type': 'title',
            'label': 'System',
            'apps': ('auth', ),
        },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
        {
            'type': 'title',
            'label': 'Resources',
            'apps': ('filer', ),
        },
        {
            'type': 'app',
            'name': 'filer',
            'label': 'File explorer',
            'icon': 'fa fa-file'
        },
        {
            'type': 'title',
            'label': 'News',
            'apps': ('news', ),
            'default_open': True,
            'children': [
                {
                    'type': 'free',
                    'label': 'Categories',
                    'url': '/admin/news/category/',
                    're': '^/admin/news/category/(\d*)?'
                },
                {
                    'type': 'model',
                    'label': 'News',
                    'name': 'news',
                    'app': 'news'
                },
            ]
        },
        {
            'type': 'title',
            'label': 'Tools',
            'children': [
                {
                    'type': 'free',
                    'label': 'Password generator',
                    'url': 'https://passwordsgenerator.net/',
                    'perms': ('auth.add_user', 'auth.change_user')
                },
                {
                    'type': 'free',
                    'label': 'Google search',
                    'url': 'http://www.google.it'
                },
                # {
                #     'type': 'free',
                #     'label': 'Dalla change form',
                #     'url': '/admin/newschange/3'
                # },
            ]
        },
    ),
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
