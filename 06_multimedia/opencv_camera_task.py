import cv2

cap = cv2.VideoCapture(0) # 카메라 장치 열기


if not cap.isOpened():
    print('Camera open failed')
    exit()

# fourxx(four character code) : DVIX(mp4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*"DIVX") 

out = cv2.VideoWriter("output.avi", fourcc, 30, (640, 480))

#동영상 촬영
while True:
    ret, frame = cap.read()
    edge1 = cv2.Canny(frame, 50, 100)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret:
        break
    cv2.imshow('frame', frame)
    cv2.imshow("edge1", edge1)
    cv2.imshow("gray", gray)
    out.write(frame)
    #1000-> 1초 10->0.01초
    if cv2.waitKey(10) == 13:
        break

cv2.waitKey(0)

#사용자 자원 해제 
cap.release()
out.release()
cv2.destroyAllWindows()