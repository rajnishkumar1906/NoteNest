"""
Django settings for Hello project.
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages

# -------------------------------------------------------------------
# BASE DIRECTORY
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# -------------------------------------------------------------------
# SECURITY SETTINGS
# -------------------------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret-key")  # ✅ use env variable in production
DEBUG = os.getenv("DEBUG", "False") == "True"

# ✅ Allow Render/Heroku host + localhost for local dev
ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".onrender.com"]


# -------------------------------------------------------------------
# APPLICATION DEFINITION
# -------------------------------------------------------------------
INSTALLED_APPS = [
    # Local apps
    'NotesApp.apps.NotesappConfig',

    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # ✅ Whitenoise for static files
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Hello.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # global templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Hello.wsgi.application'


# -------------------------------------------------------------------
# DATABASE CONFIGURATION
# -------------------------------------------------------------------
# Default: SQLite (fine for dev, not ideal for production)
# You can switch to PostgreSQL easily later.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -------------------------------------------------------------------
# PASSWORD VALIDATION
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -------------------------------------------------------------------
# INTERNATIONALIZATION
# -------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -------------------------------------------------------------------
# STATIC FILES (CSS, JS, Images)
# -------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# ✅ For production (collectstatic will gather here)
STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ Whitenoise: serve compressed static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# -------------------------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# -------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
