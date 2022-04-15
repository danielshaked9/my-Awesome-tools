import numpy as np
import cv2 as cv
import os
import shutil #for deleting directory and its content
from loading_bar import loading_bar
def Canny(directory_list,min_threshold,max_thershold): #gets a list of directories
    for directory in directory_list:
        print("Starting Canny Edge Detection on " + str(directory))
        print()
        file_count=0
        # iterate over files in
        # that directory
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                file_count+=1
        #print (r"iterations for " + str(directory) + " with " + str(file_count) + " files\n")

        new_name = "_results"
        # mode
        mode = 0o666
        # new directory path
        new_path = os.path.join(directory, new_name)
        #delete the directory if exists
        if os.path.isdir(new_path):
            shutil.rmtree(new_path)
        # Create the directory
        # with mode 0o666
        os.mkdir(new_path, mode)
        i=1
        #print (f"iterations for " + str(directory) + " with " + str(file_count) + " files\n")
        
        for filename in os.listdir(directory):
            
            f = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(f):
                img = cv.imread(f,0)
                edges = cv.Canny(img,min_threshold,max_thershold)
                new_file=new_path + '\\' + str(i) + ".png"
                cv.imwrite(new_file, edges)
                i=i+1
                loading_bar(i,file_count+1)
        print()
Canny([r"C:\Users\danie\Documents\rune-detection\data\down",r"C:\Users\danie\Documents\rune-detection\data\left",r"C:\Users\danie\Documents\rune-detection\data\right",r"C:\Users\danie\Documents\rune-detection\data\up"],100,200)

