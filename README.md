# Django Project Template

## 概要

Django プロジェクトにおける設定ファイルのテンプレートリポジトリです。

## 背景

最近、個人開発で Django を利用しており、今後設定ファイルを使い回しできるようにテンプレートの用意を行いました。

## 採用技術

- Python (3.13系)
- Django
  - django-environ (環境変数管理)
  - djangorestframework (django での REST API 開発用)
  - django-debug-toolbar (開発用デバッグツールバー)
- uv (パッケージ管理)
- ruff, mypy (リンター＆フォーマッタ)
- poethepoet (タスクランナー)
- docker (データベース実行環境)
- pre-commit (git hooks)
- vscode (エディタ)
- github actions (CI/CD)

## 各種解説

### Django

#### ディレクトリ構成

```
app/
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── local.py
│   │   ├── production.py
│   │   └── staging.py
│   └── urls.py
├── manage.py
```

#### django-environ

記述予定

#### djangorestframework

記述予定

#### django-debug-toolbar

記述予定

### uv

記述予定

### ruff, mypy

記述予定

### poethepoet

記述予定

### docker

記述予定

### pre-commit

記述予定

### vscode

記述予定

### github actions

記述予定
