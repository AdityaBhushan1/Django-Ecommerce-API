from pathlib import Path
from datetime import timedelta
from dotenv import dotenv_values
import stripe

env_vars = dotenv_values()

IS_UNDER_DEVELOPMENT = env_vars.get("under_development")

BASE_DIR = Path(__file__).resolve().parent.parent

# CUSTOM SETTINGS BASED ON DEVELOPMENT ENVIROMENT
if IS_UNDER_DEVELOPMENT == 'True':
    # SITE_DOMAIN = env_vars.get("test_frontend_site_domain")
    # PAYPLA_CLIENT_ID = env_vars.get("paypal_sandbox_client_id")
    # PAYPLA_SECRET_KEY = env_vars.get("paypal_sandbox_secret_key")
    # CORS_ALLOWED_ORIGINS = [
        # str(env_vars.get("test_frontend_site_domain")),
        # str(env_vars.get("test_frontend_site_ip"))
    # ]
    # INSTAMOJO_API_KEY = env_vars.get("instamojo_private_test_api_key")
    # INSTAMOJO_AUTH_TOKEN = env_vars.get("instamojo_private_test_auth_token")
    # INSTAMOJO_SALT = env_vars.get("instamojo_private_test_salt")
    STRIPE_PUBLIC_KEY = env_vars.get("stripe_api_publishable_key_test")
    STRIPE_SECRET_KEY = env_vars.get("stripe_api_secret_key_test")
    STRIPE_WEBHOOK_SECRET = env_vars.get("stripe_webhook_secret_test")
    DATABASES = {
        'default': {
            'ENGINE': env_vars.get("db_engine"),
            'NAME': env_vars.get("name"),
            'USER': env_vars.get("user_test"),
            'PASSWORD': env_vars.get("password_test"),
            'HOST': env_vars.get("host_test"),
            'PORT': env_vars.get("port_test"),
        }
    }
    SECRET_KEY = env_vars.get("secret_key_test")
else:
    # SITE_DOMAIN = env_vars.get("frontend_site_domain")
    # PAYPLA_CLIENT_ID = env_vars.get("paypal_live_client_id")
    # PAYPLA_SECRET_KEY = env_vars.get("paypal_live_secret_key")
    # CORS_ALLOWED_ORIGINS = [
    #     str(env_vars.get("frontend_site_domain")),
    #     str(env_vars.get("frontend_site_ip"))
    # ]
    # INSTAMOJO_API_KEY = env_vars.get("instamojo_private_live_api_key")
    # INSTAMOJO_AUTH_TOKEN = env_vars.get("instamojo_private_live_auth_token")
    # INSTAMOJO_SALT = env_vars.get("instamojo_private_live_salt")
    STRIPE_PUBLIC_KEY = env_vars.get("stripe_api_publishable_key_live")
    STRIPE_SECRET_KEY = env_vars.get("stripe_api_secret_key_live")
    STRIPE_WEBHOOK_SECRET = env_vars.get("stripe_webhook_secret_live")
    DATABASES = {
        'default': {
            'ENGINE': env_vars.get("db_engine"),
            'NAME': env_vars.get("name"),
            'USER': env_vars.get("user"),
            'PASSWORD': env_vars.get("password"),
            'HOST': env_vars.get("host"),
            'PORT': env_vars.get("port"),
        }
    }
    # SECRET_KEY = env_vars.get("secret_key")

DEBUG = env_vars.get("under_development")

stripe.api_key = STRIPE_SECRET_KEY

IPINFO_TOKEN = env_vars.get("ipinfo_token")


ALLOWED_HOSTS = [
    'localhost',
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # "django.contrib.staticfiles",
    'rest_framework',
    'Users',
    # 'Cart',
    # 'Orders',
    # 'Products',
    # 'Payments',
    # 'Wishlist',
    'rest_framework_simplejwt',
    "corsheaders",
    # 'Shipping',
    # 'Webhooks'
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
    'ipinfo_django.middleware.IPinfoMiddleware',
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


AUTH_USER_MODEL = 'Users.Users'

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
EMAIL_HOST = env_vars.get("email_host")
EMAIL_USE_TLS = env_vars.get("email_use_tls")
EMAIL_PORT = env_vars.get("email_port")
EMAIL_HOST_USER = env_vars.get("email_host_user")
EMAIL_HOST_PASSWORD = env_vars.get("email_host_password")

SITE_NAME = env_vars.get("company_name")

STATIC_URL = None

DEFAULT_CURRENCY = 'INR'
