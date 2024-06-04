# モジュールのインポート
import socket
# グローバル変数
PORT = 55515 # ポート番号
BUFSIZE = 4096

# メイン実行部
# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# port reuse
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# アドレスの設定
server.bind(("", PORT))

rx_message, addr = server.recvfrom(BUFSIZE)
server.sendto(b"Hello Seikei University!", addr)
print(rx_message.decode("UTF-8"))



# 接続の待ち受け
#server.listen()
# クライアントへの対応処理
#client, addr = server.accept() # 通信用ソケットの取得
#client.sendall(b"Hello Seikei University!\n") # メッセージの送信
#client.close() # コネクションのクローズ
#server.close() # サーバソケットのクローズ