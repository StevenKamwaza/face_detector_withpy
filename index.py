import cv2;

facecasd = cv2.CascadeClassifier("casd/haarcascade_frontalface_default.xml");

img =cv2.imread("Resoures/che/chedp.png")
imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces =facecasd.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)


cv2.imshow("Face detector",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
