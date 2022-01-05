#import libraries
import cv2
import imutils
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.3/bin/tesseract"
cv2.namedWindow('CV2', cv2.WINDOW_NORMAL)
#read image from file
image = cv2.imread("/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/utils/numberPlateHandler/23550-cam1.jpg")

#resize image to 500
image = imutils.resize(image, width=1000)

#display original image
cv2.imshow("Original Image", image)
cv2.waitKey(0)

#convert image to greystyle
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey", grey)
cv2.waitKey(0)

#smooth remove further noise
grey = cv2.bilateralFilter(grey, 11, 17, 17)
cv2.imshow("Smoother Image", grey)
cv2.waitKey(0)

#find the edges of the images

edged = cv2.Canny(grey, 170, 200)
cv2.imshow("Canny Image", edged)
cv2.waitKey(0)

#find the contours
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#copy of image
image1 = image.copy()
cv2.drawContours(image1, cnts, -1, (0,255,0),3)
cv2.imshow("After finding contours", image1)
cv2.waitKey(0)

#find the number plate related contours
cnts = sorted(cnts, key = cv2.contourArea, reverse= True)[:30]
NumberPlateCount = None

image2 = image.copy()
cv2.drawContours(image2, cnts, -1, (0,255,0),3)
cv2.imshow("Top 30", image2)
cv2.waitKey(0)

cv2.destroyAllWindows()

count = 0
name  = 0
for i in cnts:
    perimeter = cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, 0.02*perimeter, True)

    if(len(approx)==4):
        NumberPlateCount = approx
        x,y,w,h = cv2.boundingRect(i)
        crop_image = image[y:y+h, x:x+w]
        print('hello')
        cv2.imwrite(str(name)+'.png', crop_image)
        name +=1
        break

text = pytesseract.image_to_string(image, lang='ben')
print(text)