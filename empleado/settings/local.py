from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'postgres',
        'PASSWORD': 'MedinA120482',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
#añadimos una ruta para acceder a la carpeta creada 'static'
STATICFILES_DIRS = [BASE_DIR / 'static']

#añadimos una ruta a la carpeta 'media' - configuración extra
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'media'