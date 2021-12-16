import cv2

class img_gray():
    def grayscale(self):
        im = cv2.imread('./imageprocessing/',cv2.IMREAD_GRAYSCALE)

        cv2.imwrite('./imageprocessing/',im)
