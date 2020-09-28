import cv2
import time
import requests
cap = cv2.VideoCapture('vlc-record-2020-07-15-17h49m57s-rtsp___211.179.16.25_1125_4_stream1-.mp4')
count = 0
while(cap.isOpened()):
    print("change image")
    ret, frame = cap.read()
    cv2.imwrite(str(count) + '.jpg', frame)
    response = requests.post('http://192.168.0.43:9031/api/v1/sendTrajectory/singleImage/', data={'file_path' : str(count) + '.jpg'})
    count += 1
cap.release()
