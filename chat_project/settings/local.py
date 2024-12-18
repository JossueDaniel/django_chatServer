from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# DATABASES = {
#     'default': env.dj_db_url('DATABASE_URL', default="postgres://postgres@db/postgres")
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
