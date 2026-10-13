from split_settings.tools import include
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Settings live in djgame/settings/, so the project root is three levels up.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

#-------------------------------------------------------------------------------
# CHOOSE ENVIRONMENT AND INCLUDE SETTINGS
#-------------------------------------------------------------------------------
ENVIRONMENT = os.environ.get('DJGAME_ENVIRONMENT', 'dev')
include(
    'env_{}.py'.format(ENVIRONMENT),
    scope=globals()
)


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djgame.apps.base',
    'djgame.apps.account',
    'djgame.apps.game',
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

ROOT_URLCONF = 'djgame.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djgame.wsgi.application'
ASGI_APPLICATION = 'djgame.asgi.application'


# Password validation
# https://docs.djangoproject.com/en/6.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.1/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']


# Uploaded files (game thumbnails)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Authentication
# https://docs.djangoproject.com/en/6.1/topics/auth/default/
LOGIN_URL = 'account:login'
LOGIN_REDIRECT_URL = 'game:index'
LOGOUT_REDIRECT_URL = 'game:index'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
