import cv2
import os

class img_gray():
    def grayscale(self, img_name):
        #ファイル名を取得
        im_file = os.path.basename(img_name)
        #画像を読み込み
        im = cv2.imread(f'./{im_file}',cv2.IMREAD_GRAYSCALE)
        #書き込み-
        cv2.imwrite(f'./imageprocessing/grayscale/out_{im_file}',im)
