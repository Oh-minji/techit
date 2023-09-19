from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9g_+lvqef!d*tffh6305jk23%(%+5n5-7dgg*3u8ngn3iu&2an"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mariadb",
        "USER": "dhalswl94",
        "PASSWORD": "dhalswl94",
        "HOST": "mariadb",
        "PORT": "3306",
    }
}
