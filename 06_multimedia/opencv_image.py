import cv2

#image 파일 추가
img = cv2.imread("Karina.jpg")
#img2 = cv2.resize(img, (600, 400))
img = cv2.resize(img, (1000, 1000))

cv2.imshow("Karina", img)

#키보드입력을 기다림 (millisecond)
#기본값 0,ㅡ 0인 경우 키보드 입력이 있을 때까지 계속 기다림
cv2.waitKey(0)

#열려있는 모든 창 닫기 
cv2.destroyAllWindows()