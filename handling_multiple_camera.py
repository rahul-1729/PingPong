import cv2 as cv 

x = int(input('Boss how many rows do you want'))
y = int(input('Boss how many columns do you want'))
width=1920//x
height=1080//x
cam= cv.VideoCapture(0)
cam.set(cv.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv.CAP_PROP_FPS,30)
cam.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))

while True:
    _,img = cam.read()
    i=0
    j=0
    for i in range(0,x):
        for j in range(0,y):
            name = 'x'+str(i)+'y'+str(j)
            cv.imshow(name,img)
            cv.moveWindow( name,0+i*(width),0+j*(height))

        
    
    
    if(cv.waitKey(1)&0xff)==ord('q'):
        break
cam.release()
cv.destroyAllWindows()