import cv2

cap = cv2.VideoCapture(0) # 카메라 장치 열기
face_cascade = cv2.CascadeClassifier('./xml/face.xml')
img = cv2.imread('avengers.jpg')

if not cap.isOpened():
    print('Camera open failed')
    exit()

# fourxx(four character code) : DVIX(mp4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*"DIVX") 

out = cv2.VideoWriter("output.avi", fourcc, 30, (640, 480))

#동영상 촬영
while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    #1000-> 1초 10->0.01초
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
    # 원본 이미지 얼굴 위치 표시
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 13:
        break

cv2.waitKey(0)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllwindows()

