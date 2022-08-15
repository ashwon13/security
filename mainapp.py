import cv2
import numpy as np
import matplotlib.pyplot as plt
data=int(input("What is your Blood- glucose level"))
if(data<=80):
    print("you need some suguar-try pancakes with syrup")

elif(80<data<100):
    print("try some oatmeal with fruits")

elif(data>=100):
    print("Skip breakfast today")

print("Show plate to webcam")
img = cv2.imread("test.png")
video_capture = cv2.VideoCapture(0)