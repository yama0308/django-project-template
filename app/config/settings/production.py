"""
Django settings for config project - Production environment.

本番環境専用の設定を定義します。
- DEBUG = False
- セキュリティ設定の強化
"""

from .base import *  # noqa: F403

# Debug mode
DEBUG = False

# ALLOWED_HOSTS は環境変数から取得 (カンマ区切り)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])  # noqa: F405

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Static files (本番環境では collectstatic が必要)
STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa: F405
