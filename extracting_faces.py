# -*- coding: utf-8 -*-
"""
Created on Wed May 23 21:19:14 2018

@author: Kiet Tram
"""

# Importing libraries
import glob
import cv2

# Creating a list of emotions
emotions = ["neutral", "anger", "contempt","disgust",
            "fear",    "happy", "sadness", "surprise"]

# Four pre-trained classifiers
faceDet = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faceAlt = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
faceAlt2 = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
faceAltTree = cv2.CascadeClassifier("haarcascade_frontalface_alt_tree")

# Detecting face function
def detect_faces(emotion):
	# Get a list of all images by emotions
	files = glob.glob("sorted_set\\%s\\*" % emotion)
	
	file_number = 0
	
	for f in files:
	
		# Open image
		frame = cv2.imread(f)
		
		# Convert image to gray scale, saved as gray attribute
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		# Detect faces using four different classifiers for more exactly performance
		face_one = faceDet.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 10, minSize = (5, 5), flags = cv2.CASCADE_SCALE_IMAGE)
		face_two = faceAlt.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 10, minSize = (5, 5), flags = cv2.CASCADE_SCALE_IMAGE)
		face_three = faceAlt2.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 10, minSize = (5, 5), flags = cv2.CASCADE_SCALE_IMAGE)
		face_four = faceAltTree.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 10, minSize = (5, 5), flags = cv2.CASCADE_SCALE_IMAGE)
		
		# Go over detected faces, stop at first detected face, return empty if no face found
		if len(face_one) == 1:
			face_features = face_one
		elif len(face_two) == 1:
			face_features = face_two
		elif len(face_three) == 1:
			face_features = face_three
		elif len(face_four == 1):
			face_features = face_four
		else:
			face_feaures = ""
			
		# After detected, crop and save face
		# Get coordinates and size of rectangle containing face
		for (x, y, w, h) in face_features:
		
			# Printing for announcement
			print("Face is found in file: %s" %f)
			
			# Cut the frame to size
			gray = gray[y:y+h, x:x+w]
			
			# Excute the exception
			try:
				# Resize the face so all images have the same size
				out = cv2.resize(gray, (350, 350))
				
				# Write image
				cv2.imwrite("dataset\\%s\\%s.jpg" % (emotion, file_number), out)
			except:
				# If error, pass the file
				pass
		file_number += 1
	
for emotion in emotions:
	# Call and detect the face
	detect_faces(emotion)