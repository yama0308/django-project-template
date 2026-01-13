"""
Django settings for config project - Local development environment.

開発環境専用の設定を定義します。
- DEBUG = True
- Django Debug Toolbar
- 詳細なログ出力
"""

from .base import *  # noqa: F403

# Debug mode
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Django Debug Toolbar
INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405

MIDDLEWARE.insert(  # noqa: F405
    0, "debug_toolbar.middleware.DebugToolbarMiddleware"
)

INTERNAL_IPS = [
    "127.0.0.1",
]

# Logging - SQL queries を console に出力
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",  # SQL を出力
        },
    },
}
