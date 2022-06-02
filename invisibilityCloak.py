import cv2
import time
import numpy as np

fourcc=cv2.VideoWriter_fourcc(*"XVID")
outputFile = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))

capture = cv2.VideoCapture(0)

time.sleep(2)
bg = 0

for i in range(60):
    ret,bg=capture.read()

bg = np.flip(bg,axis = 1)

while(capture.isOpened()):
    ret,img = capture.read()
    if not ret:
        break
    
    img = np.flip(img,axis=1)

    #converting your bg to hsv
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #GENERATING THE  MASK TO DETECT RED COLOR
    lowerRed=np.array([0,120,50])
    upperRed=np.array([10,255,255])
    mask1=cv2.inRange(hsv,lowerRed,upperRed)

    lowerRed=np.array([170,120,70])
    upperRed=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lowerRed,upperRed)

    mask1=mask1+mask2

    #EXPANDING AND OPENING THE IMAGE WHERE THERE IS MASK 1 (RED COLOUR)
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    #SELECTING ONLY THE PART THAT DOESNT HAVE RED COLOUR
    mask2=cv2.bitwise_not(mask1)

    #STORING OR SAVING ONLY THE PART OF IMAGES WITHOUT THE RED COLOR
    result1=cv2.bitwise_and(img,img,mask=mask2)

    #Storing only the part of image with red colour from background
    result2=cv2.bitwise_and(bg,bg,mask=mask1)

    #Generating the final output by merging result one and two
    finalOutput = cv2.addWeighted(result1,1,result2,1,0)
    outputFile.write(finalOutput)

    #Displaying the output
    cv2.imshow("magic",finalOutput)
    cv2.waitKey(1)

capture.release()
out.release(img,csv,class,display,finalOutput,outputFile)
cv2.destroyAllWindows()



