# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 11:52:21 2018

@author: Kiet Tram
"""

import cv2
import numpy as np
import os

def main():

    # WebCam capture
    capWebcam = cv2.VideoCapture(0)

    # OpenCV Classifiers
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    # Check WebCam is open
    if capWebcam.isOpened() == False:
        #Error: WebCam is unavailable
        print("Error: WebCam is unavailable \n\n")         
        
        # Pause until the uses press a Key
        os.system("Pause")  
                                        
        return ""

    while cv2.waitKey(1) != 27 and capWebcam.isOpened():
        # Get each frame
        blnFrameReadSuccessfully, imgOriginal = capWebcam.read()    

        # Error: We can't read the next frame
        if not blnFrameReadSuccessfully or imgOriginal is None:     
            print("Error: We can't read the next frame\n")
            os.system("pause")
            break


        # Process 
        # Convert into grayscale
        imgGrayscale = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)    
        
        # Face classifier in the grayscale image
        faces = face_cascade.detectMultiScale(imgGrayscale, 1.3, 5)     
        
        # Draw the rectangle in the face area
        i = 0
        for (x,y,w,h) in faces:             
             # RGB: Green                          
             cv2.rectangle(imgOriginal,(x,y),(x+w,y+h),(0,255,0),2)     
                                   
             
             # Once we detect the face, we obtain a ROI (Region of Interest) 
             # so, we looking for eyes inside the ROI
             roi_imgGrayscale = imgGrayscale[y:y+h, x:x+w]
             roi_color = imgOriginal[y:y+h, x:x+w]
             
             # Save image
             i += 1
             cv2.imwrite("face-" + str(i) + ".jpg",roi_imgGrayscale)
             
             
             # Eyes classifier inside the roi_grayscale image
             eyes = eye_cascade.detectMultiScale(roi_imgGrayscale) 
             
             # CMY: Cyan
             for (ex,ey,ew,eh) in eyes:             
                 cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)

        cv2.imshow("Detected face", imgOriginal)


    cv2.destroyAllWindows()

    return

if __name__ == "__main__":
    main()




