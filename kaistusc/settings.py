"""
Django settings for kaistusc project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

import django_jinja.builtins
import pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_dcwta0d49azy*1##hy*j*g)s8d3&q88q(eushtfqrx&ff#auw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [u'143.248.234.160', u'localhost', u'student.kaist.ac.kr']

CSRF_TRUSTED_ORIGINS = [u'143.248.234.160', u'localhost', u'student.kaist.ac.kr']


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jinja',
    'apps.manager',
    'apps.ksso',
    'apps.board',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'middlewares.locale.SessionBasedLocaleMiddleware',
]

ROOT_URLCONF = 'kaistusc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'APP_DIRS': True,
        'OPTIONS': {
            'match_extension': '.jinja',
            'extensions': django_jinja.builtins.DEFAULT_EXTENSIONS
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

WSGI_APPLICATION = 'kaistusc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kaistusc',
        'USER': os.getenv('DB_ENV_MYSQL_USER'),
        'PASSWORD': os.getenv('DB_ENV_MYSQL_PASSWORD'),
        'HOST': os.getenv('MYSQL_HOST') or 'db',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

LANGUAGES = (
    ('ko', 'Korean'),
    ('en', 'English'),
)

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

MODELTRANSLATION_FALLBACK_LANGUAGES = ('ko', 'en')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static/dist"),
)

STATIC_ROOT = '/var/www/static'

MEDIA_URL = '/files/'

MEDIA_ROOT = '/var/www/media'


# Session Management

SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# Authentication

LOGIN_URL = '/user/login/'
