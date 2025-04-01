import os
import cv2
cap=cv2.VideoCapture(0)
directory='Image/'
while True:
    _,frame=cap.read()
    count = {
             'left': len(os.listdir(directory+"/LEFT")),
             'right': len(os.listdir(directory+"/RIGHT")),
             'up': len(os.listdir(directory+"/UP")),
             'down': len(os.listdir(directory+"/DOWN")),
             }
    
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('left'):
        cv2.imwrite(directory+'LEFT/'+str(count['a'])+'.png',frame)
    if interrupt & 0xFF == ord('right'):
        cv2.imwrite(directory+'RIGHT/'+str(count['b'])+'.png',frame)
    if interrupt & 0xFF == ord('up'):
        cv2.imwrite(directory+'UP/'+str(count['c'])+'.png',frame)
    if interrupt & 0xFF == ord('down'):
        cv2.imwrite(directory+'DOWN/'+str(count['c'])+'.png',frame)


cap.release()
cv2.destroyAllWindows()
