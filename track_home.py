import cv2 as cv 

def callback1(val):
 global x 
 x=val
def callback2(val):
 global y
 y=val
def callback3(val):
 global size
 size=val
 
cam = cv.VideoCapture(0)
size = 1
 
x=0
y=0

cv.namedWindow('track1')
cv.resizeWindow('track1',400,100)
cv.moveWindow('track1',size*192,0)
cv.createTrackbar('x','track1',x,1920,callback1)
cv.createTrackbar('y','track1',y,1080,callback2)
cv.createTrackbar('size','track1',1,10,callback3)
 
while True:
    cam.set(cv.CAP_PROP_FRAME_WIDTH,size*192)
    cam.set(cv.CAP_PROP_FRAME_HEIGHT,size*108)
    cam.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))
    _,frame= cam.read()
    
    cv.imshow('img',frame)
    cv.moveWindow('img',x,y)
    if(cv.waitKey(1)&0xff)==ord('q'):
        break
cam.release()
cv.destroyAllWindows()