"""
Django settings for ambientalismo project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pmmh*#d@a=71d&(b%cu1k(8$n&l%k^kn8m+^_8qa==zllo%#u_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['lugaresincreibles.herokuapp.com']#

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'webservices',
    'rest_framework',
    'gunicorn',
    'psycopg2',
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

ROOT_URLCONF = 'ambientalismo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'ambientalismo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#DATABASES = {
#   'default': {
#    'ENGINE': 'django.db.backends.mysql',
#    'NAME': 'ambientalismo3',
#    'USER': 'root',
#    'PASSWORD':'',
#    'HOST':'127.0.0.1',
#    'PORT':'3306',
#    }
#}

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd9qlrkinca6lum',#dfk1k8sl6val9i
        'USER': 'uvfnejvihssrzh',#jsxkvkloxqlitm
        'PASSWORD':'7579017b98864d97bc8fd8f541f5bb16cef5a381c77769426d965ec449e11ea3',#aa5add40cfbecec14d03c70702429dbdaf90dab4c2ae3f6dbe55cd0ecbe9916b
        'HOST':'ec2-54-152-185-191.compute-1.amazonaws.com',#ec2-54-166-167-192.compute-1.amazonaws.com
        'PORT':'5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

#STATICFILES_DIRS = [
#    BASE_DIR / "static",
#]

MEDIA_URL = '/media/'
MEDIA_ROOT="media"

STATIC_ROOT="static"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
