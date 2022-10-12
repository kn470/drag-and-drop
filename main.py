import cv2
from cvzone.HandTrackingModule import HandDetector
from circle_object import Circle
import cvzone
import numpy as np


def mid(a,b):
    ax,ay,bx,by = a[0],a[1],b[0],b[1]
    return (ax+(bx-ax)//2, ay+(by-ay)//2)
detector = HandDetector(maxHands=1)
cap = cv2.VideoCapture(0)
run = True
hold = False
x = (100,100)
while run:
    ret, frame = cap.read()
    flipped = cv2.flip(frame,1)
    flipped = cv2.resize(flipped, (1000,700))
    hands, flipped = detector.findHands(flipped,flipType=False)
    circle = Circle(pos=(100,100),img="square.png", back_img=flipped)
    
    
    
    #cv2.imshow("frame", flipped)
    if hands:
        
        hand = hands[0]
        lmList = hand["lmList"]
        #cv2.circle(flipped, (lmList[8][0],lmList[8][1]), 10, (255,255,255), 3)
        #cv2.circle(flipped, (lmList[4][0],lmList[4][1]), 10, (255,255,255), 3)
        length, info, flipped = detector.findDistance(lmList[4][0:2], lmList[8][0:2], flipped)
        mid_point = mid(lmList[4][0:2], lmList[8][0:2])
        dist = (abs(mid_point[0]-(x[0]))+abs(mid_point[1]-(x[1])))**0.5

        if length < 50 and dist < 10:
            #print(length, dist)
            print("picked")
            #hold==True
            if 50 < mid_point[0] < 950 and 50 < mid_point[1] < 650:
                x = (mid_point[0], mid_point[1])

        #while hold:    
            
                
                #cv2.imshow("frame", flipped)
        """ if length > 40:
             hold==False """
            
        

        
        
    
    
        
    flipped[x[1]-50:x[1]+50, x[0]-50:x[0]+50] = np.zeros((100,100,3), dtype=np.uint8)
    cv2.imshow("frame", flipped)

    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        run == False

    #cv2.waitKey(0)
    

cv2.destroyAllWindows()