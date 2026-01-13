"""
Django settings for config project - Test environment.

テスト実行時専用の設定です。
- DBをSQLite (メモリ上) に変更して高速化&Docker依存を排除
- デバッグ無効化
- CI/CD環境での実行をサポート (環境変数はワークフローから渡される)
"""

from .base import *  # noqa: F403

DEBUG = False

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# DockerのPostgresではなく、Python標準のSQLite(メモリ)を使用
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# メール送信をコンソールやメモリに流す ※誤送信防止
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
