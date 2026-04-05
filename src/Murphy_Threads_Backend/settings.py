from pathlib import Path
from datetime import timedelta
from dotenv import dotenv_values

env_vars = dotenv_values()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env_vars.get("secret")

DEBUG = env_vars.get("under_development")

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",
    "Users",
    # 'Cart',
    # 'Orders',
    # 'Products',
    # 'Payments',
    # 'Payments.Stripe',
    # 'Payments.Paypal',
    # 'Payments.Cashfree',
    # 'Wishlist',
    # 'Shipping',
    # 'Shipping.Shiprocket',
    # 'Shipping.Ithinklogistics',
    # 'Coupons',
    "drf_spectacular",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "ipinfo_django.middleware.IPinfoMiddleware",
]

ROOT_URLCONF = "Murphy_Threads_Backend.urls"

WSGI_APPLICATION = "Murphy_Threads_Backend.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-in"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

# STATIC_URL = '/static/'


AUTH_USER_MODEL = "Users.Users"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
}

PASSWORD_RESET_TIMEOUT = 900

CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]

# if DEBUG == False:
#     REST_FRAMEWORK.update(
#         {
#             'DEFAULT_RENDERER_CLASSES': 'rest_framework.renderers.JSONRenderer'
#         }
#     )

# email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env_vars.get("email_host")
EMAIL_USE_TLS = env_vars.get("email_use_tls")
EMAIL_PORT = env_vars.get("email_port")
EMAIL_HOST_USER = env_vars.get("email_host_user")
EMAIL_HOST_PASSWORD = env_vars.get("email_host_password")


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_CURRENCY = "INR"

# database
DATABASES = {
    "default": {
        "ENGINE": env_vars.get("db_engine"),
        "NAME": env_vars.get("name"),
        "USER": env_vars.get("user"),
        "PASSWORD": env_vars.get("password"),
        "HOST": env_vars.get("host"),
        "PORT": env_vars.get("port"),
    }
}

IPINFO_TOKEN = env_vars.get("ipinfo_token")


SPECTACULAR_SETTINGS = {
    "TITLE": "Django E-Commerce API",
    "DESCRIPTION": "A reusable production-style e-commerce backend built with Django REST Framework.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}