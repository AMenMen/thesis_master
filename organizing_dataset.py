# -*- coding: utf-8 -*-
"""
Created on Sun May 20 21:15:12 2018

@author: Kiet Tram
"""

# Importing the libraries
import glob
from shutil import copyfile

# Create a list of emotions
emotions = ["neutral", "anger", "contempt", "disgust",
            "fear"   , "happy", "sadness" , "surprise"]

# Return a list of all folders with participant numbers
parts = glob.glob("source_emotion\\*")

for p in parts:
    # Store current participant number
    part = "%s" %p[-4 : ]
    
    # Store list of sessions for current participant 
    for sessions in glob.glob("%s\\*" %p):
        for files in glob.glob("%s\\*" %sessions):
            current_session = files[20 : -30]
            
            # Open file
            file = open(files, 'r')
            
            # Read emotion in each line
            emotion = int(float(file.readline()))
            
            # Two foldes source neutral and source emotions
            # Get path for first image in sequence, which contain the neutral
            source_neut = glob.glob("source_images\\%s\\%s\\*" %(part, current_session))[0]
            
            # Get path for last image in sequence, which contain the emotion
            source_emot = glob.glob("source_images\\%s\\%s\\*" %(part, current_session))[-1]
            
            
            # Generate path to put neutral image into
            dest_neut = "sorted_set\\neutral\\%s" % source_neut[25 : ]
            
            # Generate path to put emotion image into
            dest_emot = "sorted_set\\%s\\%s" % (emotions[emotion], source_emot[25 : ])
            
            # Copy file
            copyfile(source_neut, dest_neut)
            copyfile(source_emot, dest_emot)