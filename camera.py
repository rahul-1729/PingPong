# launcing open cv and camera
import cv2 as cv 
print(cv.__version__)
#heights and width of camera
width = 1920
height=1080
cap = cv.VideoCapture(0) #if you are in windows use CAP_DSHOW to quickly open web_cam
cap.set(cv.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv.CAP_PROP_FPS,30)
cap.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,frame = cap.read()
    #. grey = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #.............creating multiple windows...........
    cv.imshow('my webcam',frame)
    cv.moveWindow('my webcam',0,0)
    # cv.imshow('my webcam 2',grey)
    #...........for moving window to a particular location......
    # cv.moveWindow('my webcam 2',700,0)
    if(cv.waitKey(1) & 0xff)==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
