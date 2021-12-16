import cv2
import os

class img_gray():
    def grayscale(self, img_name):
        im = cv2.imread(f'{img_name}',cv2.IMREAD_GRAYSCALE)
        im_file = os.path.basename(img_name)

        cv2.imwrite(f'./imageprocessing/grayscale/out_{im_file}',im)
