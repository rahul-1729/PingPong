import cv2 as cv 
import mediapipe as mp
print(cv.__version__)
 
width = 720
height=340
cap = cv.VideoCapture(0) 
cap.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv.CAP_PROP_FPS,30)
cap.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))
my_hand = mp.solutions.hands.Hands(False,2,1,0.5)
mpDraw = mp.solutions.drawing_utils
while True:
    total_hands=[]
    ignore,frame = cap.read()
    frame = cv.flip(frame,1)
    frame = cv.resize(frame,(width,height))
    frame_rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results = my_hand.process(frame_rgb)
    if results.multi_hand_landmarks != None:
        for handLandmarks in results.multi_hand_landmarks: #results.multi_hand_landmarks --> no of hands : handLandmarks --> each hands nodes landmark (x,y,z)
            co_ordinates = []
            mpDraw.draw_landmarks(frame,handLandmarks,mp.solutions.hands.HAND_CONNECTIONS)
            for marks in handLandmarks.landmark:
                co_ordinates.append((int(marks.x*width),int(marks.y*height)))
            cv.circle(frame,co_ordinates[12],25,(255,0,0),3)   
            total_hands.append(co_ordinates)
         
              
           
        print(total_hands)
    cv.imshow('my webcam',frame)
    cv.moveWindow('my webcam',0,0)
     
    if(cv.waitKey(1) & 0xff)==ord('q'):
        break
cap.release()
cv.destroyAllWindows()