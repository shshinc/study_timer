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

video = cv2.VideoCapture(0)
def infer():
    ret, img = video.read()

    height, width, channels = img.shapee
    scale = ROBOFLOW_SIZE / max(height, width)
    img = cv2.resize(img, (round(scale * width), round(scale * height)))
    
    retval, buffer = cv2.imencode('.jpg', img)
    img_str = base64.b64encode(buffer)
    
    resp = requests.post(upload_url, data=img_str, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    }, stream=True).raw
    
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image

while 1:
    if(cv2.waitKey(1) == ord('q')):
        break
    start = time.time()
    image = infer()
    cv2.imshow('image', image)
    
video.release()
cv2.destroyAllWindows()