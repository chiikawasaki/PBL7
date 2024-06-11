import socket
import sys


HOST = "localhost" # 接続先ホストの名前
PORT = 55515 # ポート番号

filename = sys.argv[1]
try:
    with open(filename, 'r',encoding="utf-8") as f:
        content=f.read()
except FileNotFoundError:
    print("file not found.")
    sys.exit(1)
except IOError:
    print("reading file error")
    sys.exit()
# ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバとの接続
client.connect((HOST, PORT))
client.sendall(content.encode('utf-8'))

# サーバからのメッセージの受信
# コネクションのクローズ
client.close()