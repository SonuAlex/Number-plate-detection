import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np
import pytesseract
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = "D:/Program Files/Tesseract-OCR/tesseract.exe"
model = YOLO('model/best.pt')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture('carVideo/mycarplate.mp4')
my_file = open('coco1.txt', 'r')
data = my_file.read()
class_list = data.split('\n')
area = [(27, 417), (16, 456), (1015, 451), (992, 417)]
count = 0
list1 = []
processed_numbers = set()

with open('car_plate_data.txt', 'a') as file:
    file.write('NumberPlate\tDate\tTime\n')

while True:
    ret, frame = cap.read()
    count += 1
    if count % 3 != 0:
        continue
    if not ret:
        break

    frame = cv2.resize(frame, (1020, 500))
    result = model.predict(frame)
    a = result[0].boxes.data
    px = pd.DataFrame(a).astype('float')

    for index, row in px.iterrows():
        x1 = int((row[0]))
        y1 = int((row[1]))
        x2 = int((row[2]))
        y2 = int((row[3]))

        d = int(row[5])
        c = class_list[d]
        cx = int(x1 + x2) // 2
        cy = int(y1 + y2) // 2

    cv2.imshow('RGB', frame)
    if cv2.waitKey(0) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()