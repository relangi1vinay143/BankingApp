from pathlib import Path
import os

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")
MEDIA_DIR = BASE_DIR / "media"

# Security
SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret")
DEBUG = os.environ.get("DEBUG", "False") == "True"

# Hosts
DEFAULT_ALLOWED_HOSTS = ["localhost", "127.0.0.1", "bankingapp-1.onrender.com"]
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS")
if ALLOWED_HOSTS:
    ALLOWED_HOSTS = ALLOWED_HOSTS.split(",")
else:
    ALLOWED_HOSTS = DEFAULT_ALLOWED_HOSTS


# CSRF trusted origins
DEFAULT_CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "https://bankingapp-1.onrender.com",
]

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS")
if CSRF_TRUSTED_ORIGINS:
    CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS.split(",")
else:
    CSRF_TRUSTED_ORIGINS = DEFAULT_CSRF_TRUSTED_ORIGINS

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "application1",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # only once!
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "application1.middleware.AuthMiddleware",
]

ROOT_URLCONF = "Bank.urls"
WSGI_APPLICATION = "Bank.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # PythonAnywhere free tier
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
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

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
