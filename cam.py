import numpy as np
import cv2
import math



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
			
		

	#cv2.imshow('img',img)
    # Display the resulting frame
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
