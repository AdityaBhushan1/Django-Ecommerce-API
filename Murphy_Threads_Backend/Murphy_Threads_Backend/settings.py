from pathlib import Path
from datetime import timedelta
import os

IS_UNDER_DEVELOPMENT = os.environ.get("under_development")
BASE_DIR = Path(__file__).resolve().parent.parent

# CUSTOM SETTINGS BASED ON DEVELOPMENT ENVIROMENT
if IS_UNDER_DEVELOPMENT is True:
    SITE_DOMAIN = os.environ.get("test_frontend_site_domain")
    PAYPLA_CLIENT_ID = os.environ.get("paypal_sandbox_client_id")
    PAYPLA_SECRET_KEY = os.environ.get("paypal_sandbox_secret_key")
    CORS_ALLOWED_ORIGINS = [
        str(os.environ.get("test_frontend_site_domain")),
        str(os.environ.get("test_frontend_site_ip"))
    ]
    # INSTAMOJO_API_KEY = os.environ.get("instamojo_private_test_api_key")
    # INSTAMOJO_AUTH_TOKEN = os.environ.get("instamojo_private_test_auth_token")
    # INSTAMOJO_SALT = os.environ.get("instamojo_private_test_salt")
    STRIPE_API_KEY = os.environ.get("stripe_api_publishable_key_test")
    STRIPE_SECRET_KEY = os.environ.get("stripe_api_secret_key_test")
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get("db_engine"),
            'NAME': os.environ.get("name"),
            'USER': os.environ.get("user_test"),
            'PASSWORD': os.environ.get("password_test"),
            'HOST': os.environ.get("host_test"),
            'PORT': os.environ.get("port_test"),
        }
    }
    SECRET_KEY = os.environ.get("secret_key_test")
else:
    SITE_DOMAIN = os.environ.get("frontend_site_domain")
    PAYPLA_CLIENT_ID = os.environ.get("paypal_live_client_id")
    PAYPLA_SECRET_KEY = os.environ.get("paypal_live_secret_key")
    CORS_ALLOWED_ORIGINS = [
        str(os.environ.get("frontend_site_domain")),
        str(os.environ.get("frontend_site_ip"))
    ]
    # INSTAMOJO_API_KEY = os.environ.get("instamojo_private_live_api_key")
    # INSTAMOJO_AUTH_TOKEN = os.environ.get("instamojo_private_live_auth_token")
    # INSTAMOJO_SALT = os.environ.get("instamojo_private_live_salt")
    STRIPE_API_KEY = os.environ.get("stripe_api_publishable_key_live")
    STRIPE_SECRET_KEY = os.environ.get("stripe_api_secret_key_live")
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get("db_engine"),
            'NAME': os.environ.get("name"),
            'USER': os.environ.get("user"),
            'PASSWORD': os.environ.get("password"),
            'HOST': os.environ.get("host"),
            'PORT': os.environ.get("port"),
        }
    }
    SECRET_KEY = os.environ.get("secret_key")

DEBUG = os.environ.get("under_development")

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'users',
    'cart',
    # 'apps.extra',
    'orders',
    'products',
    'payments',
    'wishlist',
    'rest_framework_simplejwt',
    "corsheaders",
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
]

ROOT_URLCONF = "Murphy_Threads_Backend.urls"

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
            ],
        },
    },
]

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

}

AUTH_USER_MODEL = 'users.Users'

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=10),
}

PASSWORD_RESET_TIMEOUT = 900 

# if DEBUG == False:
#     REST_FRAMEWORK.update(
#         {
#             'DEFAULT_RENDERER_CLASSES': 'rest_framework.renderers.JSONRenderer'
#         }
#     )


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("email_host")
EMAIL_USE_TLS = os.environ.get("email_use_tls")
EMAIL_PORT = os.environ.get("email_port")
EMAIL_HOST_USER = os.environ.get("email_host_user")
EMAIL_HOST_PASSWORD = os.environ.get("email_host_password")

SITE_NAME = os.environ.get("company_name")