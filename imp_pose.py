import cv2 as cv 
import time 
import imp_PoseModule as pm 
cap = cv.VideoCapture(0)
pTime=0
detector = pm.PoseDetector()
width= 1920
height = 1080
cap.set(cv.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv.CAP_PROP_FPS,30)
cap.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))
while True :
    x,img =cap.read()
    img = detector.findPose(img)
    lmList = detector.getPosition(img)
    print(lmList)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime= cTime

    cv.putText(img,str(int(fps)),(50,50),cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3);
   
    cv.imshow('image',img)
    cv.moveWindow('image',0,0)
    time.sleep(0) #to increase latency increase the number
                  #this will increase its processing time

    if cv.waitKey(1) &0xFF ==ord('q') or x==False:
        break

cap.release()
cap.destroyAllWindows()

