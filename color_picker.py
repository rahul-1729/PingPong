import cv2 as cv 
import numpy as np
x =0
y=0
evt =0
def callback(event,x_pos,y_pos,flag,param):
    global x ,y , evt
    x =x_pos
    y = y_pos
    evt = event

cap = cv.VideoCapture(0)
height = 1080
width= 1920
cap.set(cv.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv.CAP_PROP_FPS,30)
cap.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))
cv.namedWindow('Video')
cv.setMouseCallback('Video',callback)
while True:
    ret,frame=cap.read() 
    if evt ==1:
        fig = np.zeros((256,256,3),np.uint8)
        clr = frame[y][x]
        fig[:,:]= clr
        cv.putText(fig,str(clr),(0,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
        cv.imshow('fig',fig)
        cv.moveWindow('fig',width,0)
        evt=0

    
    cv.imshow('Video',frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
