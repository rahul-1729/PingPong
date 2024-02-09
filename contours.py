import cv2 as cv 
import numpy as np 
low_hue=0
low_sat=0
low_val=0
high_hue=0
high_sat=0
high_val=0
def call1(val):
    global low_hue
    low_hue = val
def call2(val):
    global high_hue
    high_hue = val
def call3(val):
    global low_sat
    low_sat = val
def call4(val):
    global high_sat
    high_sat = val
def call5(val):
    global low_val
    low_val = val
def call6(val):
    global high_val
    high_val = val
cam = cv.VideoCapture(0)
width = 640
height = 320
cam.set(cv.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv.CAP_PROP_FPS,30)
cam.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))
cv.namedWindow('track')
cv.moveWindow('track',width,0)
cv.createTrackbar('low hue','track',0,179,call1)
cv.createTrackbar('high hue','track',10,179,call2)
cv.createTrackbar('low sat','track',0,255,call3)
cv.createTrackbar('high sat','track',10,255,call4)
cv.createTrackbar('low val','track',0,255,call5)
cv.createTrackbar('high val','track',10,255,call6)
while True:
    _,frame = cam.read()
   
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    low_range = np.array([low_hue,low_sat,low_val])
    high_range = np.array([high_hue,high_sat,high_val])
    my_mask = cv.inRange(hsv,low_range,high_range)
    final = cv.bitwise_and(frame,frame,mask = my_mask)
    cv.imshow('final',final)
    cv.resizeWindow('final',320,160)
    cv.moveWindow('final',width,2*height)
    contours,junk = cv.findContours(my_mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(frame,contours,-1,(255,0,0),3)
    x=0
    y=0
    for contour in contours:
        area = cv.contourArea(contour)
        if area >=500:
            # cv.drawContours(frame,contours,-1,(255,0,0),3)
            x,y,w,h=cv.boundingRect(contour)
            cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)



    cv.imshow('img',frame)
    cv.moveWindow('img',x,y)  #camera window moves aacord to the position 

    cv.imshow('mask',my_mask)
    cv.resizeWindow('mask',320,160)
    cv.moveWindow('mask',0,2*height)
    
    if cv.waitKey(1)&0xff == ord('q'):
        break
cam.release()
cv.destroyAllWindows()