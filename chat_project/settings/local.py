from .base import *

DEBUG = True

DATABASES = {
    'default': env.dj_db_url('DATABASE_URL', default="postgres://postgres@db/postgres")
}
