"""
Django settings for SAPDAPI project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from datetime import timedelta
from pathlib import Path
import os

import dj_database_url
from dotenv import load_dotenv
load_dotenv()

import cloudinary

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
MEDIA_URL = '/photos/'
MEDIA_ROOT = os.path.join(BASE_DIR, "photos")

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y^b@(80rf_ewviwl*)e6aqn6i9_o44)o_23nwz5wb=arei_lfh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = "users.User"
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'drf_yasg',
    'rest_framework_simplejwt',
    'rest_framework',
    'corsheaders',

    'users',
    'posts',
    'comments',
    'facial_recognition',
    'emergency_contact',
]

CORS_ORIGIN_ALLOW_ALL = True


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'drxn8xsyi',
    'API_KEY': '785413883832964',
    'API_SECRET': 'FOiok4tpbRm3obrJ56EintpBlG8'
}


cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=CLOUDINARY_STORAGE['API_KEY'],
    api_secret=CLOUDINARY_STORAGE['API_SECRET']
)




MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SAPDAPI.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'users.jwt.JWTAuthentication',
    )
}


SIMPLE_JWT = {

    'ALGORITHM': 'HS256',  # O algoritmo de assinatura JWT
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),  # Tempo de vida do refresh token
    'SLIDING_TOKEN_LIFETIME': timedelta(days=7),  # Tempo de vida do access token
    'SLIDING_TOKEN_REFRESH_LIFETIME_ALLOW_REFRESH': True,  # Permite atualização do refresh token
}


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

WSGI_APPLICATION = 'SAPDAPI.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

import pymysql
pymysql.install_as_MySQLdb()
# DATABASES = {
#     'default': {
#         'NAME': 'apisapd',
#         'ENGINE': 'mysql.connector.django',
#         'HOST': 'localhost',
#         'PORT': 3300,
#         'USER': 'root',
#         'PASSWORD': '',
#
#         'OPTIONS': {
#            'autocommit': True,
#         },
#     }
# }

# DATABASES = {
#     'default': {
#         'NAME': 'railway',
#         'ENGINE': 'mysql.connector.django',
#         'HOST': 'mysql.railway.internal',
#         'PORT': 3306,
#         'USER': 'root',
#         'PASSWORD': 'krWqeEJmNELbiAwXBECJgHpdqjAchPrd',
#
#         'OPTIONS': {
#            'autocommit': True,
#         },
#     }
# }

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,  # Tempo para manter a conexão aberta

    )
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Maputo'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
