import cv2

class img_gray():
    def grayscale(self, img_name):
        im = cv2.imread(f'{img_name}',cv2.IMREAD_GRAYSCALE)

        cv2.imwrite(f'./imageprocessing/grayscale/out.png',im)
