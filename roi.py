import cv2 as cv 
cam = cv.VideoCapture(0)
width=640
height=320
boxh = 100
boxw = 200
cc= width//2
rc=height//2
jump_row =1
jump_column =1
cam.set(cv.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv.CAP_PROP_FPS,30)
cam.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))

while True:
    _,frame = cam.read()
    roi = frame[rc-(boxh//2):rc+(boxh//2),cc-(boxw//2):cc+(boxw//2)]
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    frame = cv.cvtColor(frame,cv.COLOR_GRAY2BGR)
    frame[rc-(boxh//2):rc+(boxh//2),cc-(boxw//2):cc+(boxw//2)]=roi
    
    if(rc-(boxh//2)<=0) or rc+(boxh//2) >height:
        jump_row = jump_row*(-1)
         
    if(cc-(boxw//2)<=0) or cc+(boxw//2) >=width:
        jump_column = jump_column*(-1)
      
    rc =rc+jump_row
    cc=cc+jump_column
    print(rc+(boxh//2))
    print(cc+(boxw//2))
    cv.imshow('img',frame)
    cv.moveWindow('img',0,0)
    if cv.waitKey(1)& 0xff ==ord('q'):
        break
cam.release()
cv.destroyAllWindows()