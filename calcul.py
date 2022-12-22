import cv2
import mediapipe as mp
import time
def outpt(num1, num2, res):
    num1 = str(num1)
    num2 = str(num2)
    res =  str(res)
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        sucess, img = cap.read()
        cv2.putText(img, ("number 1  : "+ num1), (50,  50),  cv2.FONT_HERSHEY_SIMPLEX, 2, (55, 10, 40), 10)
        cv2.putText(img, ("number 2  : "+ num2), (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (155, 80, 40), 10)
        cv2.putText(img, ("result    : "+ res),  (50, 450),  cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 160, 40), 10)
        cv2.imshow('img', img)
        if cv2.waitKey(1) == ord('q'):
           break