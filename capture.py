import cv2
import numpy as np
import datetime

real_study_time = 0
total_time = 0
count = 1
def get_study_time():
    global real_study_time, count, total_time
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("yolo.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    study_time = 30
    play_time = 0
    img = cv2.imread("D:/download/image (" + str(count) + ").jpg")
    if img is None:
        return '0:00:00', '0:00:00'
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
            print(label)
            if label == 'cell phone':
                play_time = 30

    study_time -= play_time
    real_study_time += study_time
    study_time = str(datetime.timedelta(seconds=real_study_time, microseconds=0))
    total_time += 30
    total_time_tmp = str(datetime.timedelta(seconds=total_time, microseconds=0))
    count += 1
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return (study_time[:7], total_time_tmp[:7])
 
