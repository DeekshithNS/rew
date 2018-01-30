import numpy as np
import cv2
import math

human_cascade = cv2.CascadeClassifier("cascadeH5.xml")	

cap = cv2.VideoCapture(0)
frameRate = cap.get(5)
while(True):
	frameId = cap.get(1)
    # Capture frame-by-frame
	ret,img = cap.read()

    # Our operations on the frame come here
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	if (frameId % math.floor(frameRate)== 0):
		strng = "images/img1_"+str(int(frameId))+".jpg"
		cv2.imwrite(strng,gray)
			
	heads = human_cascade.detectMultiScale(gray,1.3,5)	
	for(x,y,w,h) in heads :
		img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h,x:x+w]
		roi_color = img[y:y+h,x:x+w]
	cv2.imshow('frame',gray)
    # Display the resulting frame
	#cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
