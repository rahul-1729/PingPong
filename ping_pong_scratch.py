 
import cv2 as cv 
class mpHands:
    import mediapipe as mp
    def __init__(self,static=False,maxhands=2,tol1=1,tol2=0.5):
        self.static =static 
        self.maxhands =maxhands
        self.tol1= tol1
        self.tol2=tol2
        self.hands = self.mp.solutions.hands.Hands(self.static,self.maxhands,self.tol1,self.tol2)
    def Marks(self,frame,height,width):
        hand_marks=[]
        framergb= cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        result = self.hands.process(framergb)
        if result.multi_hand_landmarks!=None:
         for hands in result.multi_hand_landmarks:
            hand_mark=[]
            for mark in hands.landmark:
               hand_mark.append((mark.x*width,mark.y*height))
            hand_marks.append(hand_mark)
        return hand_marks
    def h_type(self,frame):
       hand_types =[]
       framergb= cv.cvtColor(frame,cv.COLOR_BGR2RGB)
       result = self.hands.process(framergb)
       if result.multi_handedness != None:
        for hand_type in result.multi_handedness:
          hand_types.append(hand_type.classification[0].label)
       return hand_type
           

cam = cv.VideoCapture(0)
width = 1920
height = 1080
cam.set(cv.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))
cam.set(cv.CAP_PROP_FPS,30)
my_hand = mpHands(False,2,1,0.5)
while True:
    _,frame = cam.read()
    cv.imshow('ping pong',frame)
    # my_hand.Marks(frame,height,width)
    my_hand.h_type(frame)
    cv.moveWindow('ping pong',0,0)

    if cv.waitKey(1)&0xff==ord('q'):
        break
cam.release()
cv.destroyAllWindows()