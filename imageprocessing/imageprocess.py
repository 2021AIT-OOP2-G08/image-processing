import cv2
#画像のパスの文字列を引数にとる
class CannyProcess:
    th1 = 80
    th2 = 80
    #画像のパスの文字列を引数にとる 
    def fCanny(self,img) :
        self.img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        self.canny_img = cv2.Canny(self.img,self.th1,self.th2)
        return self.canny_img
        
