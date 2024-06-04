# モジュールのインポート
import socket
# グローバル変数
HOST = "localhost" # 接続先ホストの名前
PORT = 55515 # ポート番号
BUFSIZE = 4096 # 受信バッファの大きさ
# ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# サーバとの接続
client.sendto(b"Request",(HOST,PORT))
data = client.recv(BUFSIZE)
print(data.decode("UTF-8"))
# コネクションのクローズ
#client.close()