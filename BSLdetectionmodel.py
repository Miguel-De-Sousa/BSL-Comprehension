import cv2
import mediapipe as mp
from math import hypot

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

mphands=mp.solutions.hands
Lhands=mphands.Hands()
Rhands=mphands.Hands()
mpdraw=mp.solutions.drawing_utils

while True:
    success, image = capture.read()
    image = cv2.flip(image, 1)
    cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    Lfinish = Lhands.process(cv2image)
    Rfinish= Rhands.process(cv2image)
    LlmList = []
    RlmList = []
    if Lfinish.multi_hand_landmarks:
        for handlandmark in Lfinish.multi_hand_landmarks:
            for id, lms  in enumerate(Lfinish.multi_hand_landmarks):
                 lbl=Lfinish.multi_handedness[id].classification[0].label
                 if lbl == "Left":
                    for id, lm in enumerate(handlandmark.landmark):
                            height, width, depth = image.shape
                            cx, cy = int(lm.x * width), int(lm.y * height)
                            LlmList.append([id, cx, cy])
                            mpdraw.draw_landmarks(image, handlandmark, mphands.HAND_CONNECTIONS)
                 if lbl =="Right":
                    for handlandmark in Rfinish.multi_hand_landmarks:
                        for id, lm in enumerate(handlandmark.landmark):
                                height, width, depth = image.shape
                                cx, cy = int(lm.x * width), int(lm.y * height)
                                RlmList.append([id, cx, cy])
                                mpdraw.draw_landmarks(image, handlandmark, mphands.HAND_CONNECTIONS)
    if LlmList != [] and RlmList!=[]:
        Lx4, Ly4 = LlmList[4][1], LlmList[4][2]
        Lx8, Ly8 = LlmList[8][1], LlmList[8][2]
        Lx12, Ly12 = LlmList[12][1], LlmList[12][2]
        Lx16, Ly16 = LlmList[16][1], LlmList[16][2]
        Lx20, Ly20 = LlmList[20][1], LlmList[20][2]
        Lx0, Ly0 = LlmList[0][1], LlmList[0][2]
        Lx7, Ly7 = LlmList[7][1], LlmList[7][2]

        Rx12, Ry12 = RlmList[12][1], RlmList[12][2]
        Rx11, Ry11 = RlmList[11][1], RlmList[11][2]
        Rx8, Ry8 = RlmList[8][1], RlmList[8][2]
        Rx7, Ry7 = RlmList[7][1], RlmList[7][2]

        #print(LlmList[4])
        #print(RlmList[4])
        
        #for i in range(len(LlmList)):
        #    cv2.putText(image, "id: {} ".format(LlmList[i]), (LlmList[i][1], LlmList[i][2]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        

        #cv2.line(image, (Lx4, Ly4), (Rx8, Ry8), (255, 0, 0), 2)
        #cv2.line(image, (Rx8, Ry8), (Lx8, Ly8), (255, 0, 0), 2)

        Alength=hypot(Rx8-Lx4, Ry8-Ly4)
        Elength = hypot(Rx8-Lx8, Ry8-Ly8)
        Ilength = hypot(Rx8-Lx12, Ry8-Ly12)
        Olength = hypot(Rx8-Lx16, Ry8-Ly16)
        Ulength = hypot(Rx8-Lx20, Ry8-Ly20)
        Llength = hypot(Rx8-Lx0, Ry8-Ly0)
        Xlength = hypot(Rx7-Lx7, Ry7-Ly7)
        Blength = hypot(Rx12-Lx12, Ry12-Ly12)
       
        if Alength<25:
            cv2.putText(image, "A",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)  
        elif Elength<25:
             cv2.putText(image, "E",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
        elif Ilength<25:
            cv2.putText(image, "I",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
        elif Llength<75:
             cv2.putText(image, "L",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
        elif Olength<25:
            cv2.putText(image, "O",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
        elif Ulength<25:
            cv2.putText(image, "U",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
        elif Xlength<50:
            cv2.putText(image, "X",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
        elif Blength<50:
            cv2.putText(image, "B",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
    
    cv2.imshow("Image", image)
    key = cv2.waitKey(1)
    if key == ord("p"):
         break