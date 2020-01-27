import numpy as np
import cv2 as cv
import time

#Make Sure to Download Video and save in same file.
#Right is RED   Left is Blue
#Download from here:
# https://drive.google.com/file/d/1z6BuP-3aWjBk1BytTAX321AhPltbf_lc/view?usp=sharing
#Credit: OpenCV2020

#Also, make sure to do: "python3.8 Main.py" for running and displaying.

time.sleep(1)
print('-------------')
print('Demonstration')
print('  Beginning  ')
print('-------------')
print('')

print(cv.displayOverlay)


cap = cv.VideoCapture(cv.samples.findFile("vtest.avi"))

ret, frame1 = cap.read()
prvs = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
while(1):
    ret, frame2 = cap.read()
    next = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)
    flow = cv.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
    bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
    cv.imshow('Example of Video with Optical Flow',bgr)
    k = cv.waitKey(30) & 0xff
    
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('Video without Optical Flow',frame)
            
    if cv.waitKey(25) & 0xFF == ord('q'):
      break

    if k == 27:
        break
    elif k == ord('s'):
        cv.imwrite('opticalfb.png',frame2)
        cv.imwrite('opticalhsv.png',bgr)
    prvs = next

x = input('Would you like to end the demonstration?')
print('"y" or "n"')
if(x == 'y'): 
    quit()
if(x == 'n'):
    print('...')
  # Break the loop
   
 
# When everything done, release the video capture object
cap.release()
