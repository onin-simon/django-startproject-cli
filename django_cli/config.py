DJANGO_REST_FRAMEWORK = "djangorestframework"
GRAPHENE_DJANGO = "graphene-django"
CHANNELS = "django-channels"
LOCALFLAVOR = "django-localflavor"
CELERY = "celery"
WHITENOISE = "whitenoise"
DJANGO_FILTER = "django-filter"
DJANGO_EXTENSIONS = "django-extensions"
DJANGO_STORAGES = "django-storages"
CORSHEADER = "django-cors-headers"
CHANNELS_REDIS = "channels_redis"

# Libs to install (ask user)
LIBRARIES_OPTIONAL = [
    DJANGO_REST_FRAMEWORK,
    GRAPHENE_DJANGO,
    CHANNELS,
    LOCALFLAVOR,
    CELERY,
    WHITENOISE,
    DJANGO_FILTER,
    DJANGO_EXTENSIONS,
    DJANGO_STORAGES
]
# INSTALLED APP LIST
INSTALLED_APP = {
    DJANGO_REST_FRAMEWORK: "'rest_framework'",
    CORSHEADER: "'corsheaders'"
}

MIDDLEWARE = {
    CORSHEADER: """'corsheaders.middleware.CorsMiddleware'"""
}

EXTRA = {
    CORSHEADER: """# Django Cors Header Settings,
CORS_ALLOWED_ORIGINS = ['http://localhost:8080','http://127.0.0.1:8000',]""",
    CHANNELS: """
# Add REDIS_URL To Env Variable    
CHANNEL_LAYERS = {
     'default': {
         'BACKEND': 'channels_redis.core.RedisChannelLayer',
         'CONFIG': {'hosts': [os.environ.get('REDIS_URL', 'redis://localhost:6379')]},
     },     
}
ASGI_APPLICATION = "$PROJECT_NAME.routing.application"
"""
}

# Linked Installation
LINKED_LIBRARY = {
    DJANGO_REST_FRAMEWORK: CORSHEADER,
}

LINKED_FILES = {
    CHANNELS: {
        "name": "routing",
        "dj_loc": "$APP_LOC",
        "data": "",
        "extension": ".py",
        "suffix": ""
    }
}

VERSION = '1.0'

POSTGRES = "postgresql"
MYSQL = "mysql"

# Database LIBS / Drivers
DATABASE_DRIVERS = {
    POSTGRES: "psycopg2-binary",
    MYSQL: "mysqlclient",
}

DBEngine = {
    POSTGRES: 'django.db.backends.postgresql',
    MYSQL: 'django.db.backends.mysql',
}

PY_MEM_CACHE = "pymemcache"
REDIS = "redis"


CACHE_BACKED = {
    PY_MEM_CACHE: 'django.core.cache.backends.memcached.PyMemcacheCache',
    REDIS: 'django.core.cache.backends.redis.RedisCache',
}
