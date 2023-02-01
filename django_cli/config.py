DJANGO_REST_FRAMEWORK = "djangorestframework"
CORSHEADER = "django-cors-headers"


# Libs to install (ask user)
LIBRARIES_OPTIONAL = [
    DJANGO_REST_FRAMEWORK,
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
}

# Linked Installation
LINKED_LIBRARY = {
    DJANGO_REST_FRAMEWORK: CORSHEADER,
}

VERSION = '1.0'

POSTGRES = "postgresql"
MYSQL = "mysql"
SQLITE = "sqlite3"

# Database LIBS / Drivers
DATABASE_DRIVERS = {
    POSTGRES: "psycopg2-binary",
    MYSQL: "mysqlclient",
}

DBEngine = {
    POSTGRES: 'django.db.backends.postgresql',
    MYSQL: 'django.db.backends.mysql',
    SQLITE: 'django.db.backends.sqlite3',
}

PY_MEM_CACHE = "pymemcache"
REDIS = "redis"


CACHE_BACKED = {
    PY_MEM_CACHE: 'django.core.cache.backends.memcached.PyMemcacheCache',
    REDIS: 'django.core.cache.backends.redis.RedisCache',
}
