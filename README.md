# SNS&マッチング　App

・デプロイ先→後ほど追記

・本番環境→後ほど追記

# セットアップ

ローカル環境構築について

・venvによる仮想環境を使用

・Django

## Step1.Install
```
git clone "URL"
```

## Step2.Set up environment
仮想環境を作成
```
cd [project dir]
python3 -m venv [newenvname]
```
仮想環境を有効化
```
source [newenvname]/bin/activate
```
もしくは
```
. [newenvname]/bin/activate
```
pipコマンドで必要なパッケージをインストール
```
pip install -r requirements.txt
```
MySQLは今度導入予定

## Step3.Run Django in development mode
ローカルサーバー起動
```
python manage.py runserver
```
You can access to http://127.0.0.1:8000/.
