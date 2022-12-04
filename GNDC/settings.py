"""
Django settings for Proyecto project.
Generated by 'django-admin startproject' using Django 3.0.6.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from pathlib import Path
from lib2to3.pgen2.driver import Driver
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

###RUTA DEL MODELO
from os.path import join
RUTA_MODELO = join(BASE_DIR, 'prediccion_Total_venta.py')
RUTA_MODELO2 = join(BASE_DIR, 'prediccion_precio_ipc.py')
RUTA_MODELO3 = join(BASE_DIR, 'prediccion_cantidad_total.py')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '93l(+vpmkg)t3yeu4(^v09$%h5172e7moc!glr5-tkm2j1judn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]
#DEBUG_PROPAGATE_EXCEPTIONS = True


MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

#login

LOGIN_REDIRECT_URL = '/usuarios/index'
LOGOUT_REDIRECT_URL = '/accounts/login'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'GNDC.urls'

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

WSGI_APPLICATION = 'GNDC.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        #'ENGINE': 'sql_server.pyodbc',
        'NAME': 'GNDC',
        'USER': 'GNDC',
        'PASSWORD':'Admin123',
        'HOST':'misqlservidorgndc.database.windows.net',
        'PORT': '',
        'OPTIONS': {
             'driver': 'ODBC Driver 17 for SQL Server',
         }
    }
}
USE_TZ = False

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

#STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATIC_URL = '/static/'  
# para los ccs y todo lo demas 
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'GNDC/static'),)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#################################################
AUTH_USER_MODEL = 'usuarios.Usuario' 
#################################################

# Config demo mail

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'gndc.dataknights@gmail.com'
EMAIL_HOST_PASSWORD = 'huulxpzskxzhluvy'
CSRF_TRUSTED_ORIGINS = ['https://gestion-negocio-donna-clarita.azurewebsites.net']



