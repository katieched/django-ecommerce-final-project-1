"""
Django settings for community_store_app project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import django_heroku
from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$a&_=q_(d8lk(@r*jaw!==#v!kb%bgv-xnqyr88$q8ovo!x@uf'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    '127.0.0.1',
    'https://jackpot-communities.herokuapp.com/'
]

# Application definition
# <appname>.apps.<AppConfigClass>
INSTALLED_APPS = [
    'cart',
    'members.apps.MembersConfig',
    "corsheaders",
    'communities.apps.CommunitiesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic'
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "corsheaders.middleware.CorsPostCsrfMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CORS_ALLOWED_ORIGINS = [
    "https://www.sandbox.paypal.com",
    "https://c.paypal.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]

CSRF_TRUSTED_ORIGINS = [
    "https://www.sandbox.paypal.com",
    "https://c.paypal.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]


ROOT_URLCONF = 'community_store_app.urls'

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
                'django.template.context_processors.media', #this line allows us to reference the MEDIA_URL variable in template directories
            ],
        },
    },
]

WSGI_APPLICATION = 'community_store_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbtest',
        'USER': 'postgres',
        'PORT': 5432,
        'HOST': 'localhost',
        'PASSWORD': 'password'
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

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


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Specifying the path to the media directory so that Django knows where it is located
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')
# MEDIA_URL is for scripts or various files in templates, so that when we reference MEDIA_URL, the script knows where
MEDIA_URL= "/media/"

PAYPAL_RECEIVER_EMAIL = 'zbchazach@gmail.com'

PAYPAL_TEST = True

#note: these might need to be strings ??
URL='http://localhost:8000'

LOGIN_URL = URL

LOGIN_REDIRECT_URL='communities/my-communities/'

LOGOUT_REDIRECT_URL=''

django_heroku.settings(locals())

AUTH_USER_MODEL = "members.Member"

