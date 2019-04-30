import numpy as np
import cv2

img = cv2.imread('input/data.png')
sayi = 0

for gray in cv2.split(img):
    canny = cv2.Canny(gray,50,200)
    

    contours,hier = cv2.findContours(canny,1,2)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.04*cv2.arcLength(cnt,True),True)
        if len(approx)==3:
            cv2.drawContours(img,[cnt],0,(0,255,0),2)
            tri = approx
            sayi +=1
        

for vertex in tri:
    cv2.circle(img,(vertex[0][0],vertex[0][1]),5,255,-1)
sayison= sayi//6
print(sayison)
file = open("sonuc/ucgen.txt","w")
file.write(str(sayison))


cv2.imwrite("output/datat.png", img)

cv2.destroyAllWindows()