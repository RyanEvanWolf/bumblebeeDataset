#!/usr/bin/env python
import os
import cv2
import sys
import struct
import time
import numpy as np
import argparse

parser =argparse.ArgumentParser()
parser.add_argument("raw_video_file",help="Location of the binary video file recorded from the jetson")
parser.add_argument("--out_folder",help="Location of extracted ppm images with a forward slash, default='Raw/'",default="Raw/")
args=parser.parse_args()

###create directories


print("Reading from File =",args.raw_video_file)
totalBytes=os.path.getsize(args.raw_video_file)
bytesPerImage=2*768*1024

print("Total Bytes = "+str(totalBytes))
totalImages=int(totalBytes/bytesPerImage)
remainderBytes=totalBytes%bytesPerImage
print("total Images = "+str(totalImages))
print("Extra Bytes = "+str(remainderBytes))

print("saving to "+args.out_folder)
setFolders=[args.out_folder,
            args.out_folder+"Colour/left/",
            args.out_folder+"Colour/right/",
            args.out_folder+"Grey/left/",
            args.out_folder+"Grey/right/"]

for folder in setFolders:
    if(not os.path.exists(os.path.dirname(folder))):
        print("Creating Directory "+folder)
        os.makedirs(os.path.dirname(folder))


with open(args.raw_video_file,"rb") as f:
    for imageIndex in range(0,totalImages):
        '''
            -Create a numpy of all zeros with the correct datatype
            -Loop through the file byte at a time and unpack according to binary file format it was saved in
            -form it into the left and right bayer encoded image from the PointGrey camera
        '''
        image=np.zeros((1,bytesPerImage),np.uint8)
        for byteIndex in range(0,bytesPerImage):            
            by=struct.unpack("B",f.read(1))
            image[0,byteIndex]=by[0]
        image=image.reshape(2*768,1024)
        '''
            -split the image into the left and right image respectively
            -decode the image into a colour and black and white version for saving
            -save them into the premade folders as one large sequential set of images
            -display the image with the 15Hz frame rate
        '''


        imageColour=cv2.cvtColor(image,cv2.COLOR_BAYER_BG2RGB)
        imageColourLeft=imageColour[0:768,:]
        imageColourRight=imageColour[768:2*768,:]

        imageGreyscale=cv2.cvtColor(image,cv2.COLOR_BAYER_BG2GRAY)
        imageGreyLeft=imageGreyscale[0:768,:]
        imageGreyRight=imageGreyscale[768:2*768,:]

        cv2.imwrite(args.out_folder+"Colour/left/"+("%05d.png"%int(imageIndex)),imageColourLeft, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        cv2.imwrite(args.out_folder+"Colour/right/"+("%05d.png"%int(imageIndex)),imageColourRight, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        cv2.imwrite(args.out_folder+"Grey/left/"+("%05d.pgm"%int(imageIndex)),imageGreyLeft)
        cv2.imwrite(args.out_folder+"Grey/right/"+("%05d.pgm"%int(imageIndex)),imageGreyRight)
        print(imageIndex,totalImages)
       # cv2.imshow("dataset-Colour",imageColour)
       # cv2.waitKey(66)
        ##copy an image into a np array
    


