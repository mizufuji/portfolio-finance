PythonのDjangoフレームワークを用いて、金融資産の損益状況とチャートを表示します。

## ■言語:Python

## ■UI:HTML/CSS

## ■フレームワーク:Django(Python)

## ■Database:Sqlite3

## ■画像
![image](https://github.com/user-attachments/assets/7cb9e3d7-8652-49d5-bd7a-ac64ce04c147)
![image](https://github.com/user-attachments/assets/e61568c4-48ff-4739-b4f8-02c995321ab2)



## ■ディレクトリ構成
```plaintext
financial_asset
│   db.sqlite3
│   manage.py
│
├─accounts
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├─static
│   │   └─accounts
│   │       └─css
│   │               style.css
│   │
│   └─templates
│       └─registration
│               base.html
│               login.html
│               signup.html
│
├─asset
│   │   admin.py
│   │   apps.py
│   │   forms.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├─migrations
│   │       0001_initial.py
│   │       0002_asset_user.py
│   │       0003_asset_ticker_name.py
│   │       __init__.py
│   │
│   ├─static
│   │   └─asset
│   │       └─css
│   │               style.css
│   │
│   ├─templates
│   │   └─assets
│   │           asset_detail.html
│   │           asset_edit.html
│   │           base.html
│   │           new_asset.html
│   │           top.html
│   │
│   └─templatetags
│       │   custom_filters.py
│       │   __init__.py
│
└─financial_asset
    │   asgi.py
    │   settings.py
    │   urls.py
    │   wsgi.py
    │   __init__.py


