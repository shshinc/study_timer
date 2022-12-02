import cv2
import base64
import numpy as np
import requests
import time
import json
with open('model.json') as f:
    config = json.load(f)

    ROBOFLOW_API_KEY = json.config["ROBOFLOW_API_KEY"]
    ROBOFLOW_MODEL = json.config["ROBOFLOW_MODEL"]
    ROBOFLOW_SIZE = json.config["ROBOFLOW_SIZE"]