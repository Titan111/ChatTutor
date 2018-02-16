# このレポジトリについて
後輩にチャットづくりを教えるために作成したレポジトリ

# チャットづくりの課題

## websocket動作確認 
websocketディレクトリ内のサーバとクライエントを
起動し動作を確認する

pythonはインストールされているものとする
まず、以下のコマンドでサーバのライブラリをインストールする

```
sudo pip install git+https://github.com/Pithikos/python-websocket-server
```

次にコマンドからサーバを起動する

```
python chat_server.py
```

ブラウザでclient.htmlを開くとチャットが開始できる
