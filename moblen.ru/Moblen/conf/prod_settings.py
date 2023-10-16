import os

DEBUG = False

ALLOWED_HOSTS = ['moblen.ru', 'www.moblen.ru']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/var/www/u2258032/data/www/moblen.ru/templates'],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER_NAME"),
        'PASSWORD': os.getenv("DB_ADMIN_PASSWORD"),
        'HOST': 'localhost'
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CORS_ALLOW_ALL_ORIGINS = False  # Запретить все источники (по умолчанию)
CORS_ALLOW_CREDENTIALS = True  # Разрешить передачу куки и аутентификацию

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Укажите здесь нужные источники, с которых разрешены запросы
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",  # Добавьте OPTIONS для обработки предварительных запросов CORS
]