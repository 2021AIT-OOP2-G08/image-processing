import cv2
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from imageprocessing.grayScale import img_gray

cascade_path = "imageprocessing/haarcascade_frontalface_default.xml"
class facedetect():
    def __init__(self):
        
        img = cv2.imread("test.jpg")

        #グレースケール変換
        image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #カスケード分類器の特徴量を取得する
        cascade = cv2.CascadeClassifier(cascade_path)
        
        #物体認識（顔認識）の実行
        #image – CV_8U 型の行列．ここに格納されている画像中から物体が検出されます
        #objects – 矩形を要素とするベクトル．それぞれの矩形は，検出した物体を含みます
        #scaleFactor – 各画像スケールにおける縮小量を表します
        #minNeighbors – 物体候補となる矩形は，最低でもこの数だけの近傍矩形を含む必要があります
        #flags – このパラメータは，新しいカスケードでは利用されません．古いカスケードに対しては，cvHaarDetectObjects 関数の場合と同じ意味を持ちます
        #minSize – 物体が取り得る最小サイズ．これよりも小さい物体は無視されます
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

        #print(facerect)
        color = (255, 255, 255) #白
        # 検出した場合
        if len(facerect) > 0:
            #検出した顔を囲む矩形の作成
            for rect in facerect:
                cv2.rectangle(img, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

        #認識結果の保存
        
        cv2.imwrite("out_face.jpg", img)


#画像のパスの文字列を引数にとる
class CannyProcess:
    th1 = 80
    th2 = 80
    #画像のパスの文字列を引数にとる 
    def fCanny(self,img) :
        self.img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        self.canny_img = cv2.Canny(self.img,self.th1,self.th2)
        return self.canny_img
        

if __name__ == "__main__":
    #ロギングの設定
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'    #監視対象のpathを設定
    event_handler = LoggingEventHandler()   #イベントハンドラ生成
    observer = Observer()       #監視オブジェクト生成
    observer.schedule(          #監視設定
        event_handler,
        path,
        recursive=True
        )
    observer.start()            #監視開始
    try:
        while True:             #ctrl-Cが押されるまで実行
            time.sleep(1)       #1秒停止
    except KeyboardInterrupt:   #ctrl-C実行時
        observer.stop()         #監視修了
    observer.join()
    
    facedetect()　#顔検出

img_gray(filepath)
