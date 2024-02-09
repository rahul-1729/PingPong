import cv2 as cv 

cam = cv.VideoCapture(0)
width = 640
height = 320
evt =0
def mouseClick(event,x_pos,y_pos,flags,params):
    global evt ,x,y
    evt = event
    x = x_pos
    y = y_pos




cam.set(cv.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))
cv.namedWindow('webcam')
cv.setMouseCallback('webcam',mouseClick)
flag = True
flag2 = False
 
 
while True:
    _,frame=cam.read()

    if evt ==1 and flag:
       x1 = x
       y1=y
       flag = False
      

    if evt == 4 and (not flag) and x1!=x and y1!=y:
       x2= x
       y2=y
       flag = True
       flag2 = True
       cv.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),3)
     
      
    if flag2:
       roi = frame[y1:y2,x1:x2]
       cv.imshow('roi',roi)
       cv.moveWindow('roi',width,0)
       cv.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),3)
    
    if evt ==5 and flag2:
        cv.destroyWindow('roi')
        evt =0
        flag2 = False
    print (evt)
    cv.imshow('webcam',frame)
    cv.moveWindow('webcam',0,0)
    if cv.waitKey(1)&0xff==ord('q'):
        break
cam.release()
cv.destroyAllWindows()
