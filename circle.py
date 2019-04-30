import cv2
import numpy as np

img = cv2.imread('input/data.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
sayi = 0

file = open("sonuc/yuvarlak.txt","w")

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,40,
                            param1=50,param2=35,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    sayi +=1
    
    
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
print(sayi)
file.write(str(sayi))
cv2.imwrite("output/datac.png", cimg )
cv2.waitKey(0)

cv2.destroyAllWindows()