"""
Django settings for config project - Staging environment.

開発検証環境 (Staging) 専用の設定を定義します。
本番環境に近い状態で動作検証を行うための環境です。
"""

from .production import *  # noqa: F403

# Debug mode (必要に応じて True に変更可能)
DEBUG = env("DEBUG", default=False)  # noqa: F405

# ALLOWED_HOSTS は環境変数から取得
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])  # noqa: F405

# セキュリティ設定は production より緩め (HTTPでもアクセス可能にする場合)
SECURE_SSL_REDIRECT = False  # staging では HTTP も許可する場合が多い
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
