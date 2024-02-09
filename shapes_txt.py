import cv2 as cv 
import time
cam = cv.VideoCapture(0)
height = 1920
width = 1080
cam.set(cv.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv.CAP_PROP_FPS,30)
cam.set(cv.CAP_PROP_FOURCC,cv.VideoWriter.fourcc(*'MJPG'))
p_time =0
while True:
    _,frame = cam.read()
    # frame[140:250,230:300]=(0,0,0)
    # cv.rectangle(frame,(100,170),(170,300),(0,0,255),5) #if u put thickness as -1 it will fill the shape
    # cv.circle(frame,(130,130),40,(0,255,0),3)
    # cv.putText(frame,'my text',(120,120),cv.FONT_HERSHEY_COMPLEX,2,(0,0,255))

    c_time = time.time()
    fps = 1/(c_time-p_time)
    p_time = c_time
    cv.putText(frame,str(int(fps)),(50,50),cv.FONT_HERSHEY_SIMPLEX,2,(0,255,0))
    cv.imshow('web cam',frame)
    cv.moveWindow('web cam',0,0)
 
    if cv.waitKey(1)&0xff == ord('q'):
        break

cam.release()
cv.destroyAllWindows()