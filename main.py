import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import webbrowser


myEquation = ''
delayCounter = 0

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:

        lmList = hands[0]['lmList']

        length, _, img = detector.findDistance(lmList[4], lmList[8], img)

        if length < 10 and delayCounter == 0:
            webbrowser.open('https://dzen.ru/', new=2)

            sleep(3)

        length2, _, img = detector.findDistance(lmList[4], lmList[12], img)

        if length2 < 10 and delayCounter == 0:
            webbrowser.open('https://youtube.com', new=2)

            sleep(3)

        length3, _, img = detector.findDistance(lmList[4], lmList[16], img)

        if length3 < 10 and delayCounter == 0:
            webbrowser.open('https://vk.com', new=2)

            sleep(3)

        length4, _, img = detector.findDistance(lmList[4], lmList[20], img)

        if length4 < 10 and delayCounter == 0:
            webbrowser.open('https://translate.yandex.ru/', new=2)

            sleep(3)

    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0

    cv2.putText(img, myEquation, (810, 130), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 0, 0), 3)

    key = cv2.waitKey(1)
    cv2.imshow("Image", img)
    if key == ord('c'):
        myEquation = ''
