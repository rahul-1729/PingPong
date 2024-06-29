import imp_hand_module as hm 
import cv2 as cv 
import time 

width =1240
height=720
cap = cv.VideoCapture(0)  
cap.set(cv.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv.CAP_PROP_FPS,30)
cap.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))
hand1 = hm.mpHands(False,1,1,0.5)
boxw = 200
boxh = 20
color = (0,255,0)

x = width//2
y=  height//2
radius =25
life =3
delta =0
incr_x = 0
incr_y =0
ticket =1
print('Welcome to ping pong')
user = int(input("1: easy\n2:medium\n3:hard\n"))
if (user ==1):
  delta =1
  incr_x = 7
  incr_y =-7
elif (user ==2):
  delta =2
  incr_x = 9
  incr_y =-9
elif (user ==3):
  delta =5
  incr_x = 15
  incr_y =-15
else:
   ticket =0
points = 0
movex = incr_x
movey = incr_y
while True and ticket:
    ignore,frame = cap.read()
    frame= cv.resize(frame,(width,height))
    frame = cv.flip(frame,1)
    data = hand1.Marks(frame,width,height)
    if x+movex>width or x+movex<0:
        movex = - movex
    if y+movey<0:
        movey = - movey
    x = x+movex
    y = y+movey
    cv.circle(frame,(x,y),radius,(255,0,255),-1)
    cv.putText(frame,'life : ' +str(life),(50,50),cv.FONT_HERSHEY_PLAIN,3,(0,0,255),6)
    if len(data)!=0:
       
        cv.rectangle(frame,(data[0][8][0]-(boxw//2),height-boxh),(data[0][8][0]+(boxw//2),height),color,-1)
        if (x>=(data[0][8][0]-(boxw//2))) and (x<=data[0][8][0]+(boxw//2)) and ((y + radius)>=(height-boxh))and((y + radius)<(height)):
            movey = -movey
            points = points+delta
    cv.putText(frame,str(points),(width-100,50),cv.FONT_HERSHEY_PLAIN,2,(255,0,0),6)
    if (y>height-boxh):
        life=life-1
        if life!=0:
          x = width//2
          y=  height//2
          movex = incr_x
          movey = incr_y
    if life==0:
        break
    
    
    cv.imshow('my webcam',frame)
    cv.moveWindow('my webcam',0,0)
  
    
    if(cv.waitKey(1) & 0xff)==ord('q'):
        break
print ('your points ',points)
cap.release()
cv.destroyAllWindows()
