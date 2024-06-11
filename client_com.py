# モジュールのインポート
import socket
# グローバル変数
HOST = "localhost" # 接続先ホストの名前
PORT = 55515 # ポート番号
BUFSIZE = 4096 # 
# ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバとの接続
client.connect((HOST, PORT))
message = input("send message:")
client.sendall(message.encode("UTF-8"))
data = client.recv(BUFSIZE)
print(data.decode("UTF-8"))
# コネクションのクローズ
client.close()