import sys
#import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    #ファイルやフォルダが作成された場合の処理
    def on_created(self, event):
        filepath = event.src_path
        #filename = os.path.basename(filepath)
        print('%sを作成しました。' % filepath)
        #ここに引数filepathでクラスを呼び出すよよ

if __name__ == "__main__":
    #ロギングの設定
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'    #監視対象のpathを設定
    event_handler = ChangeHandler()   #イベントハンドラ生成
    observer = Observer()       #監視オブジェクト生成
    observer.schedule(          #監視設定
        event_handler,
        path,
        recursive=True
        )
    print("監視開始")
    observer.start()            #監視開始
    try:
        while True:             #ctrl-Cが押されるまで実行(1秒ごとに実行)
            time.sleep(1)       #1秒停止
    except KeyboardInterrupt:   #ctrl-C実行時
        observer.stop()         #監視修了
    observer.join()
    print("監視終了")