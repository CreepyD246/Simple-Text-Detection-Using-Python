import cv2
from pytesseract import pytesseract

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("ur_mom.png")
height, width, c = img.shape

letter_boxes = pytesseract.image_to_boxes(img)
print(letter_boxes)

for box in letter_boxes.splitlines():
	box = box.split()
	print(box)
	x,y,w,h = int(box[1]),int(box[2]),int(box[3]),int(box[4])
	cv2.rectangle(img,(x,height-y),(w,height-h), (0,0,255),3)
	cv2.putText(img,box[0],(x,height-h+32),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

cv2.imwrite('eeeeee.png', img)
cv2.imshow("window", img)
cv2.waitKey(0)