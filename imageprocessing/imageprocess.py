import cv2
#画像のパスの文字列を引数にとる
class CannyProcess:
    #画像のパスの文字列を引数にとる 
    def fCanny(img,self) :
        self.img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        canny_img = cv2.Canny(self.img,80,80)
        return canny_img

img = CannyProcess.fCanny('らっだぁ.jpg')
cv2.imshow(img,'test')
        
