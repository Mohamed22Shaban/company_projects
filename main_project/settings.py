"""
Django settings for main_project project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import django_heroku
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.

## path use in static
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = Path(__file__).resolve().parent.parent
#   git push heroku main
DISABLE_COLLECTSTATIC = True


## language settings
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'main_project/locale')
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3Ef5D3C5C5Eb8Bf1D3181410Bb646806A26B51D1C2B604D7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'project-django-show.herokuapp.com/','127.0.0.1'
    ]


# Application definition

INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'report',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
    'blog',
    'crispy_forms',
    
]


## language setting   => 'django.middleware.locale.LocaleMiddleware',
## heroku setting   => 'whitenoise.middleware.WhiteNoiseMiddleware',

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main_project.urls'

## language settings  => 'django.template.context_processors.i18n',
## email settings  => 'tasks.context_processors.recive_email',

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'tasks.context_processors.recive_email',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
#### waleed   ### mu2020

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8pr5n3187u3pb',
        'HOST': 'ec2-44-195-132-31.compute-1.amazonaws.com',
        'USER': 'mqbjyfjzqqropz',
        'PASSWORD': '2b3008755b60ee2c5122d61e212a45410e47027278e5c7e30327e025f28cad08',
        'PORT': '5432',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }






# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ar'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

## language settings

LANGUAGES = [
  ('ar', ('Arabic')),
  ('en', ('English')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main_project/static')
]



## heroku settings
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


CRISPY_TEMPLATE_PACK = 'bootstrap4'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login'


## email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mohamedtelb200@gmail.com'
EMAIL_HOST_PASSWORD = 'kijqgemazngrxrbv'
EMAIL_USE_TLS = True
EMAIL_PORT = '587'

#raheem2022#
## heroku settings
django_heroku.settings(locals())