import cv2
import os

class img_gray():
    def grayscale(self, img_name):
        im_file = os.path.basename(img_name)
        im = cv2.imread(f'./imageprocessing/input/{im_file}',cv2.IMREAD_GRAYSCALE)    

        cv2.imwrite(f'./imageprocessing/grayscale/out_{im_file}',im)

if __name__ == '__main__':
    a = img_gray()
    #a.grayscale('./input/a.png')
