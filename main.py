import cv2 as cv
import winsound

cam = cv.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv.absdiff(frame1, frame2)

    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv.threshold(blur, 20, 255,cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        if cv.contourArea(c) < 1500:
            continue
        x, y, w, h = cv.boundingRect(c)
        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 3)
        winsound.PlaySound('police.wav', winsound.SND_ASYNC)
        #winsound.Beep(5000, 1000)
        


    if cv.waitKey(10) == ord('q'):
        break
    #cv.imshow('Awesome cam', frame1)
    cv.imshow('Awesome cam', diff)

