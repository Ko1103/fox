# 土壌水分量の空間分布を計測するシステム

## 開発環境 Development environment
Python 3.5.2
pyenv, pyenv-virtualenvを利用

## 使い方 Usage

1. 仮想環境を立ちあげる
予め仮想環境を構築する。その際、Pythonは3.5.2にする。ここではfoxという名の仮想環境を構築する。

```
$ pyenv activate fox 
```

2. サーバを立ち上げる run server
予め、今いるディレクトリの中にmanage.pyというファイルがあるかを確認する。このファイルはDBのマイグレートやサーバの起動などのコマンドが記述されている。

```
$ python3 manage.py runserver
```

3. ブラウザに表示
基本的には<http://127.0.0.1:8000/>がサーバのリンクとなる。このシステムでは'/mapping'が空間分布を計測するシステムのURLとなっているので、<http://127.0.0.1:8000/mapping>を開くとsigfoxクラウドからデータを取得する。

## ソースコード
このシステムではPythonのwebアプリ構築フレームワークであるDjangoを用いている。

- map
    - map
        - setting.py *
    - mapping
        - admin.py
        - urls.py *
        - apps.py
        - models.py
        - tests.py 
        - views.py *
        - その他

本システムで変更したファイルは*がついている3つのファイルである。
それぞれについて説明する。

### map/setting.py
利用するDBやアプリケーションを設定するファイルである。本システムではmappingというアプリを作成しているので、そのアプリを利用するために利用するアプリとして追記している。

### mapping/urls.py
views.pyに定義されている関数と、ブラウザで叩かれるURLを紐づける役割をしている。

### mapping/views.py
リクエストに対する処理を行う関数を定義している