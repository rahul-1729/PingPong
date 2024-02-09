import cv2 as cv
evt =0
def mouseClick(event,xPos,yPos,flags,params):
    global evt,pnt
    if event ==cv.EVENT_LBUTTONDOWN:
        print('Mouse Event was ',event)
        print('at Position',xPos,yPos)
        pnt =(xPos,yPos)
        evt = event
    if event ==cv.EVENT_LBUTTONUP:
        print('Mouse Event was ',event)
        print('at Position',xPos,yPos)
        evt = event
        pnt =(xPos,yPos)






height =320
width = 640
cam = cv.VideoCapture(0)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv.CAP_PROP_FPS,30)
cam.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))
cv.namedWindow('webcam')
cv.setMouseCallback('webcam',mouseClick)
while True:
    _,frame=cam.read()

    if(evt==1 or evt ==4):
       cv.circle(frame,pnt,10,(0,0,255),-1)
    print (evt)
    cv.imshow('webcam',frame)
   
    if cv.waitKey(1)&0xff == ord('q'):
        break
cam.release()
cv.destroyAllWindows()