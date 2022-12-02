import cv2
import base64
import numpy as np
import requests
import time
import json
with open('model.json') as f:
    config = json.load(f)

    ROBOFLOW_API_KEY = config["ROBOFLOW_API_KEY"]
    ROBOFLOW_MODEL = config["ROBOFLOW_MODEL"]
    ROBOFLOW_SIZE = config["ROBOFLOW_SIZE"]
    RAMERATE = config["FRAMERATE"]
    BUFFER = config["BUFFER"]
    COMMENT_1 = config["__comment1"]
    COMMENT_2 = config["__comment2"]
    
    
upload_url = "".join([
    "https://detect.roboflow.com/",
    ROBOFLOW_MODEL,
    "?api_key=",
    ROBOFLOW_API_KEY,
    "&format=image",
    "&stroke=5"
])