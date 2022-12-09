import cv2
import numpy as np
import datetime

def get_study_time():
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    return