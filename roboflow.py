import cv2
import base64
import numpy as np
import requests
import time
import json
with open('model.json') as f:
    config = json.load(f)