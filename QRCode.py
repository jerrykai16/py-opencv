import numpy as np
import cv2
from pyzbar import pyzbar

p = cv2.VideoCapture(0)

while True:
    a , b = p.read()
    if a == True:
        r = pyzbar.decode(b)
        for d in r:
            x,y,w,h = d.rect
            cv2.rectangle(b,(x,y),(x+w,y+h),(0,0,255),(2))
            print("辨識到的文字:",d.data.decode("utf-8"))
        
        cv2.imshow("test",b)
        if cv2.waitKey(42) != -1:
            break
    else:
        break

cv2.destroyAllWindows()