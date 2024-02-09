import cv2 as cv 

def callback1(val):
 global x 
 x=val
def callback2(val):
 global y
 y=val
def callback3(val):
 global rad
 rad=val
def callback4(val):
 global thick
 thick=val
cam = cv.VideoCapture(0)
width = 1920
height =1080
x=0
y=0
rad = 3 
thick =1
cam.set(cv.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))
cv.namedWindow('track1')
cv.resizeWindow('track1',400,100)
cv.moveWindow('track1',width,0)
cv.createTrackbar('x','track1',x,1920,callback1)
cv.createTrackbar('y','track1',y,1080,callback2)
cv.createTrackbar('rad','track1',0,height//2,callback3)
cv.createTrackbar('thick','track1',0,10,callback4) 
while True:
    _,frame= cam.read()
    if thick ==0:
      thick =-1
    cv.circle(frame,(x,y),rad,(0,0,255),thick)
    cv.imshow('img',frame)
    cv.moveWindow('img',0,0)
    if(cv.waitKey(1)&0xff)==ord('q'):
        break
cam.release()
cv.destroyAllWindows()