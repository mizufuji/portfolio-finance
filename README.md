```plaintext
PythonのDjangoフレームワークを用いて、金融資産の損益状況とチャートを表示します。
CRUD操作が可能で、
Create・・・金融資産の登録
Read・・・・金融資産の情報の詳細表示（過去1ヶ月間のレート推移）
Update・・・金融資産の情報の更新（保有数の変更等）
Delete・・・金融資産の削除
ができます。

## ■構成
・ログイン画面
・会員登録画面
・トップページ（全銘柄の情報とチャート表示）
・資産追加画面（Create処理）
・資産詳細画面（Read処理）
・資産編集画面（Update処理）
・資産削除画面（Delete処理）
・管理者専用画面（Admin保有者のみ閲覧可能）


## ■フレームワーク:Django(Python)

## ■UI:HTML/CSS

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


