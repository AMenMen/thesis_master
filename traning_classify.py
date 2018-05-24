# -*- coding: utf-8 -*-
"""
Created on Sun May 20 21:15:12 2018

@author: Kiet Tram
"""

# Importing the libraries
import cv2 			# OpenCV library
import glob			# Glob library
import random as rd # Random library
import numpy as np	# Numpy library

# Create a list of emotions
emotions = ["neutral", "anger", "contempt", "disgust",
			"fear", "happy", "sadness", "surprise"]

# Using Fisher Face Classifier for recognizing
fisher_face = cv2.face.createFisherFaceRecognizer() 

# Create an empty data dictionary
data = {} 

# Define function to get file list, randomly shuffle is and split 80/20 ratio
# 80 for training and 20 for classification
def get_files(emotion):
	files = glob.glob("dataset\\%s\\*" % emotion)
	rd.shuffle(files)
	
	# Getting the first 80% number of files in list
	training = files[:int(len(files) * 0.8)]
	
	# Getting the last 20% number of files in list
	predicting = files[-int(len(files) * 0.2)]
	
	return training, predicting
	
# Difine function to create the sets
def create_sets():
	training_data = []
	training_lables = []
	prediction_data = []
	prediction_labels = []
	
	for emotion in emotions:
		training, prediction = get_files(emotion)
		
		for item in training:
		
			# Open image
			image = cv2.imread(item)
			
			# Convert image to grayscale
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			
			# Append image array to training data list
			training_data.append(gray)
			
			# Append its label respectively
			training_labels.append(emotions.index(emotion))
		
		for item in prediction:
			
			# Open image
			image = cv2.imread(item)
			
			# Convert image to gray scale
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			
			# Add image to prediction data
			prediction_data.append(gray)
			
			# Add its respectively label
			prediction_labels.append(emotions.index(emotion))
		
	return training_data, training_labels, prediction_data, prediction_label
	
# Run recognizer
def run_recognizer():
	training_data, training_labels, prediction_data, prediction_labels = make_sets()
	
	# Printing
	print("Training fisher face classifier: ")
	print("The size of the training set is: ", len(training_labels), " images.")
	
	# Convert training_labels array into numpy array
	np_training_labels = np.asarray(training_labels)
	
	# Training
	fisher_face.train(training_data, np_training_labels)
	
	# Prediting
	print("Predicting classification set: ")
	cnt = 0
	correct = 0
	incorrect = 0
	for img in prediction_data:
		pred, conf = fisher_face.predict(img)
		if pred == prediction_labels[cnt]:
			correct += 1
			cnt += 1
		else:
			incorrect += 1
			cnt += 1
	# Return the ratio of correct prediction
	return ((100 * correct)/(correct + incorrect))
	
# Run the MAIN program
metascore = []
for i in range(0, 10):
	correct = run_recognizer()
	# Printing
	print("Got ", correct, " percent correct.")
	
	metascore.append(correct)
	
# Printing the medium correct ratio
print("\n\n End score: ", np.mean(metascore), " percent correct.")