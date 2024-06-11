# モジュールのインポート
import socket
# グローバル変数
HOST = "localhost" # 接続先ホストの名前
PORT = 55515 # ポート番号
BUFSIZE = 4096 # 受信バッファの大きさ
# ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバとの接続
client.connect((HOST, PORT))
while True:
    #サーバにメッセージを送信
    message = input()
    client.sendall(message.encode("UTF-8"))
    if message == "bye":
        break
# サーバからのメッセージの受信
# コネクションのクローズ
client.close()