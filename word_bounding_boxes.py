import cv2
from pytesseract import pytesseract
from pytesseract import Output

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("ur_mom.png")

image_data = pytesseract.image_to_data(img, output_type=Output.DICT)

print(image_data['left'])

# Printing each word
# for word in image_data['text']:
# 	print(word)

for i, word in enumerate(image_data['text']):
	if word != '':
		x,y,w,h = image_data['left'][i],image_data['top'][i],image_data['width'][i],image_data['height'][i]
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
		cv2.putText(img,word,(x,y-16),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow("window", img)
cv2.waitKey(0)