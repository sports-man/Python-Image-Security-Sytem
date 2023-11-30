import sys
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from playsound import playsound
import shutil
import winsound
import subprocess

path = 'img'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for i in myList:
    curImg = cv2.imread(f'{path}/{i}')
    images.append(curImg)
    classNames.append(os.path.splitext(i)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('resource\\Attendance.cvs', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime("%Y-%m-%d %H:%M:%S")
            f.writelines(f'\n{name}, {dtString}')

def markAttendanceUnknown(name):
    with open('resource\\Attendance.cvs', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        now = datetime.now()
        dtString = now.strftime("%Y-%m-%d %H:%M:%S")
        f.writelines(f'\n{name}, {dtString}')
        
encodeListKnown = findEncodings(images)
print(len(encodeListKnown)) 

cap = cv2.VideoCapture(0)
imgCount = 1 
check=0
nameTmp = ""
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)
        if faceDis[matchIndex]< 0.57:
            name = classNames[matchIndex].upper()
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
        else: 
            check=1
            name = 'Unknown'
            nameTmp = name
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            file_path = "resource\\imgSave\\captured_image.jpg"
            cv2.imwrite(file_path, img)
    cv2.imshow('CCTV', img)
    key = cv2.waitKey(1)
    if(key==113):
        break

# Đường dẫn tới thư mục chứa ảnh
folder_path = "resource\\Unknown"

# Đếm số lượng tệp ảnh trong thư mục
image_count = sum(1 for file in os.listdir(folder_path) if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif")))
if check==1:  
    markAttendanceUnknown(nameTmp)
    image = cv2.imread("resource\\imgSave\\captured_image.jpg")

    # Lấy ngày giờ hiện tại
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Vẽ văn bản lên ảnh
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_color = (0, 0, 255)  # Màu văn bản (đỏ)
    font_thickness = 1
    x, y = 10, 20  # Vị trí vẽ văn bản (góc trái)

    cv2.putText(image, formatted_time, (x, y), font, font_scale, font_color, font_thickness)

    # Lưu ảnh với ngày giờ đã vẽ
    cv2.imwrite("resource\\imgSave\\captured_image.jpg", image)
    # Đường dẫn đầy đủ tới tệp ảnh cần thêm
    image_path = "resource\\imgSave\\captured_image.jpg"
    folder_path = "resource\\Unknown"
    new_filename = f"Unknown{image_count+1}.jpg"
    destination_path = os.path.join(folder_path, new_filename)
    # Di chuyển hoặc sao chép tệp ảnh vào thư mục
    shutil.copy(image_path, destination_path)  # Để sao chép
cv2.destroyAllWindows()
