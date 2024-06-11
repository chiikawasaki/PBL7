# モジュールのインポート
import socket
import datetime
# グローバル変数
PORT = 55515 # ポート番号
BUFSIZE = 4096 # 受信バッファの大きさ
# メイン実行部
# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ポート再利用指定
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# アドレスの設定
server.bind(("", PORT))
# 接続の待ち受け
server.listen()
# クライアントへの対応処理
try:
    while True: # 対応の繰り返し
        client, addr = server.accept() # 通信用ソケットの取得
        d = datetime.datetime.now() # 現在時刻の取得
        fname = d.strftime("%m%d%H%M%S"+".log") # 文字列へ変換
        print("conncted from:", client) # 接続先を端末に表示
        fout = open(fname, mode="w", encoding="utf-8") # 書き込みファイルオープン
        while True:
            data = client.recv(BUFSIZE) # クライアントより受信
            print(data.decode("UTF-8")) # 受信内容の出力
            print(data.decode("UTF-8"), file = fout) # ファイルへの書き込み
 
            if not data: # 受信するものがないなら
                 break ; # 受信終了
        # print(data.decode("UTF-8")) # 受信内容の出力
        # print(data.decode("UTF-8"), file = fout) # ファイルへの書き込み
        client.close() # コネクションのクローズ
        fout.close() # ファイルのクローズ
        print("connection closed. file is saved as ", fname, ".")
except KeyboardInterrupt:
    server.close()
