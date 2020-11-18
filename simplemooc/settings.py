"""
Django settings for simplemooc project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e25$i2m@h4+fiv!ichgz5cm3_e=1*hpdq+m896fl#_ry!l_a9m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition: The CoreConfig class is in the core/apps.py. Now Django knows to include the polls app.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'core.apps.CoreConfig',
    'accounts.apps.AccountsConfig',
	'courses.apps.CoursesConfig',
]

#digite python manage.py makemigrations polls

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'simplemooc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            'libraries':{
                        'courses_tags': 'courses.templatetags.courses_tags',
                        }
        },
    },
]

WSGI_APPLICATION = 'simplemooc.wsgi.application'


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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'simplemooc', 'media')
MEDIA_URL = '/media/' #A URL basica para arquivos estaticos do usuario

#E-mails
#EMAIL_BACKEND = 'django.core.mail.smtp.EmailBackend'
#smtpé o padrão do django
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#vamos usar o  console para apenas printar no terminal p email
DEFAULT_FROM_EMAIL = 'Dina <dina.contact.us@gmail.com>'

# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = 'x@gmail.com '
# EMAIL_HOST_PASSWORD = 'xxx!'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

CONTACT_EMAIL = 'x@gmail.com'

#Auth
LOGIN_URL = '/entrar'
LOGIN_REDIRECT_URL = '/home'
LOGOUT_URL = '/home'
AUTH_USER_MODEL = 'accounts.User' #apartir disso o django sabe q o model é o nosso e não oq ele dá
#o usuário não serámais o padrão do django
#após isso (accounts.models.py e novo user) apague o banco de dados e todas as pastas migrations nos apps
#https://stackoverflow.com/questions/26207022/custom-user-in-django-raises-valueerror

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Heroku settings

import dj_database_url

DATABASES = {
    'default':  dj_database_url.config(),
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
#simplemooc2020.herokuapp.com

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

try:
    from simplemooc.local_settings import *
except ImportError:
    pass