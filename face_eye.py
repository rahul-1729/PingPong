import cv2 as cv 
print(cv.__version__)
 
width = 1920
height=1080
cap = cv.VideoCapture(0)  
cap.set(cv.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv.CAP_PROP_FPS,30)
cap.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
eyecascade = cv.CascadeClassifier('haar/haarcascade_eye.xml')

while True:
    ignore,frame = cap.read()
    grey = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grey,1.3,5)
    eyes = eyecascade.detectMultiScale(grey,1.3,4)
    print(eyes)
    for i in eyes :
        cv.rectangle(frame,(i[0],i[1]),(i[0]+i[3],i[1]+i[2]),(0, 0, 255),4)
    for x,y,w,h in faces :
        cv.rectangle(frame,(x,y),(x+w,y+h),(0, 255, 255),4)
    cv.imshow('my webcam',frame)
    cv.moveWindow('my webcam',0,0)
    
    if(cv.waitKey(1) & 0xff)==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
