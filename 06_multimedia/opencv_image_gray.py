import cv2

#image 파일 추가
img = cv2.imread("Karina.jpg")
#img2 = cv2.resize(img, (600, 400))
#img = cv2.resize(img, (1000, 1000))

#Edge선 추출하기
edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

#색상변환하기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#이미지 파일읽기
cv2.imshow("Karina", img)
cv2.imshow("edge1", edge1)
cv2.imshow("edge2", edge2)
cv2.imshow("edge3", edge3)

#키보드입력을 기다림 (millisecond)
#기본값 0,ㅡ 0인 경우 키보드 입력이 있을 때까지 계속 기다림
#ENTER:13, ESC:27
while True:
    if cv2.waitLKey() == ord('q'):
        break

#파일로 저장하기
cv2.imwrite("Karina_GRAY.jpg", gray)
cv2.imwrite("Karina_EDGE.jpg", edge1)

#열려있는 모든 창 닫기 
cv2.destroyAllWindows()