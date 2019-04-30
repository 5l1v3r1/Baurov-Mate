import numpy as np
import cv2

img = cv2.imread('input/data.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sayi = 0

ret,thresh = cv2.threshold(gray,127,255,1)

contours,h = cv2.findContours(thresh,1,2)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.04*cv2.arcLength(cnt,True),True)    
    if len(approx)==4:
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
        sayi +=1
        print(sayi)

file = open("sonuc/kare.txt","w")
file.write(str(sayi))


cv2.imwrite('output/datas.png', img)
cv2.destroyAllWindows()