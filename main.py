import tkinter as tk
from loginform import login
from menubar import menu
import cv2
import mediapipe as mediapipe
from PIL import Image, ImageTk
from threading import Thread
import os
from math import hypot
from toolbarmovement import start_drag, move_window

def main():
    translationlist=[">"]
    mediapipeHands = mediapipe.solutions.hands
    Lhands = mediapipeHands.Hands()
    Rhands = mediapipeHands.Hands()
    mediapipeDraw = mediapipe.solutions.drawing_utils

    def shutter():
        if booleanshutter.get() == True:
            cameracontainer.grid_forget()
            cameracover.grid(row=0, column=0, padx=10, pady=15, columnspan=2)
            booleanshutter.set(value=False)
        else:
            cameracover.grid_forget()
            cameracontainer.grid(row=0, column=0, padx=10, pady=15, columnspan=2)
            booleanshutter.set(value=True)

    def show_frame():
        success, frame = capture.read()
        if not success:
             print("Ignoring empty camera frame.")
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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
                                height, width, depth = frame.shape
                                cx, cy = int(lm.x * width), int(lm.y * height)
                                LlmList.append([id, cx, cy])
                                mediapipeDraw.draw_landmarks(cv2image, handlandmark, mediapipeHands.HAND_CONNECTIONS)
                    if lbl =="Right":
                        for handlandmark in Rfinish.multi_hand_landmarks:
                            for id, lm in enumerate(handlandmark.landmark):
                                    height, width, depth = frame.shape
                                    cx, cy = int(lm.x * width), int(lm.y * height)
                                    RlmList.append([id, cx, cy])
                                    mediapipeDraw.draw_landmarks(cv2image, handlandmark, mediapipeHands.HAND_CONNECTIONS)

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

            Alength=hypot(Rx8-Lx4, Ry8-Ly4)
            Elength = hypot(Rx8-Lx8, Ry8-Ly8)
            Ilength = hypot(Rx8-Lx12, Ry8-Ly12)
            Olength = hypot(Rx8-Lx16, Ry8-Ly16)
            Ulength = hypot(Rx8-Lx20, Ry8-Ly20)
            Llength = hypot(Rx8-Lx0, Ry8-Ly0)
            Xlength = hypot(Rx7-Lx7, Ry7-Ly7)
            Blength = hypot(Rx12-Lx12, Ry12-Ly12)

            if Alength<25:
                cv2.putText(cv2image, "A",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
                if translationlist[-1]!="A":
                    translationlist.append("A")
            elif Elength<25:
                cv2.putText(cv2image, "E",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
            elif Ilength<25:
                cv2.putText(cv2image, "I",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
                if translationlist[-1]!="I":
                    translationlist.append("I")
            elif Llength<75:
                cv2.putText(cv2image, "L",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
                if translationlist[-1]!="L":    
                    translationlist.append("L")
            elif Olength<25:
                cv2.putText(cv2image, "O",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
                if translationlist[-1]!="O":   
                    translationlist.append("O")
            elif Ulength<25:
                cv2.putText(cv2image, "U",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
                if translationlist[-1]!="U":    
                    translationlist.append("U")
            elif Xlength<50:
                cv2.putText(cv2image, "X",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
                if translationlist[-1]!="X":
                    translationlist.append("X")
            elif Blength<50:
                cv2.putText(cv2image, "B",(100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 4, cv2.LINE_4)
                if translationlist[-1]!="B":    
                    translationlist.append("B")
        translation.set(value=translationlist)
        cv2image = Image.fromarray(cv2image)
        tkimage = ImageTk.PhotoImage(image=cv2image)
        cameracontainer.imgtk = tkimage
        cameracontainer.configure(image=tkimage)
        cameracontainer.after(1, show_frame)

    root = tk.Tk()
    width, height = 800, 600
    x, y = (int(((root.winfo_screenwidth())/2)-((width+75)/2))), (int(((root.winfo_screenheight())/2)-(height/2)))

    root.geometry('{}x{}+{}+{}'.format(width+75, height, x, y))
    root.title("BSL Comprehension")
    root.resizable(False, False)
    root.overrideredirect(True)
    root.configure(background="lightgray")

    root.bind("<Escape>", lambda e: root.quit())
    root.bind("<Button-1>", lambda e: start_drag(e))
    root.bind("<B1-Motion>", lambda e:move_window(e, root))

    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    cameracontainer = tk.Label(root, relief='sunken',bg="#3676d1", bd=5)
    cameracontainer.grid(row=0, column=0, padx=10, pady=15, columnspan=2)
    cameracover = tk.Label(root, bg="#000000",fg="#ffffff", text="PAUSED", height=32, width=121)

    translation = tk.StringVar()
    translationresult = tk.Entry(root, textvariable=translation, relief="sunken",width=68, font=(18))
    translationresult.grid(row=1, column=0, ipady=20, padx=2)

    booleanshutter = tk.BooleanVar(value=True)
    shutterbutton = tk.Button(root, text="Shutter",bg="#3676d1",fg="#ffffff",font=("bold"),height=2,width=6 ,command=lambda:shutter())
    shutterbutton.grid(row=1, column=1, ipady=3)
    filepath = "./savefile.txt"
    if os.path.isfile(filepath):
        savefile = open("savefile.txt", "r")
        translation.set(value=f"{savefile.read()}")
        savefile.close()
    showframeThread= Thread(target=show_frame)
    showframeThread.start()
    menu(root, translation)
    root.mainloop()
    
login()
main()
