import cv2
import imutils

def import_img():
    img = cv2.imread("iphone.jpeg")
    img = imutils.resize(img,width=1080)
    cv2.imshow("original image",img)
    cv2.waitKey(0)
    return img
    
def averaging_blur(img):
    blur = cv2.blur(img,(5,5))
    cv2.imshow("averaging blur",blur)
    cv2.waitKey(0)

def gaussian_blur(img):
    gaussian_blur = cv2.GaussianBlur(img,(5,5),0)
    cv2.imshow("gaussian_blur",gaussian_blur)
    cv2.waitKey(0)

def median_blur(img):
    median = cv2.medianBlur(img,5)
    cv2.imshow("median_blur",median)
    cv2.waitKey(0)

IMG=import_img()
gaussian_blur(IMG)
median_blur(IMG)
averaging_blur(IMG)


