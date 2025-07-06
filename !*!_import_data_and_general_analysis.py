#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 13:10:45 2025

@author: Jeff
"""
import math
import statistics as stat
#from Pathlib import Path

# Below code is for reference and trial during the build. 
#flight_coords.csv
#'/Users/Jeff/Downloads/flight_coords.csv'

file_1 = ""
file_1_path = ""

# Need to rethink the usage and applicaiton of the below function. 
def extract_file_name():
    global file_1
    file_1 = file_entry.get().strip()
    main_screen.destroy()
# For last line, perhaps there is a tk. function that parses the name of the widget?
# Should utilize that if possible. Will leave for now. 

import pandas as pd
import numpy as np
import os
import tkinter as tk

main_screen = tk.Tk()
main_screen.title("File Finder")
main_screen.geometry("250x150")

file_entry = tk.StringVar()

ms_entry_label = tk.Label(main_screen, 
                          text = "Enter the file you wish to access:",
                          font = ("Arial", 14),
                          justify = "left").pack(pady = 5)

# File entry box, need to designate a string entry
ms_entry = tk.Entry(main_screen,
                    textvariable = file_entry,
                    width = 22).pack(pady = 5)

# Terminate the window and continue button
ms_button = tk.Button(main_screen,
                      text = "Close and Find File",
                      command = extract_file_name).pack(pady = 10)

main_screen.mainloop()
# End of widget interface

#file_1 = file_entry.get().strip() <-- Moved to function at beginning. 

#df1 = pd.read_csv(file_1)
#print(df1.head())
print(df1.info())
# .info is a method, therefore needs to have () at the end
 # Attributes in pandas do not require a () at the end. 
 # .info also provides the # of entries (rows), # of columns, column name, 
  # the non-null count, and the data tpe (decimal # (float64), 
  # integer (int64), string (object), etc...)
   # I think .info may be a better way for understanding what is in a dataframe
    # than the function .head(). 
shape_1 = df1.shape
print (shape_1)
# .shape is an ATTRIBUTE and does not require ()
 # this yields: (rows, columns) as an output when printed

#result_fp = []

def find_file(file_name, file_path):
    for root, dirs, files in os.walk(file_path):
        if file_name in files:
            return os.path.join(root, file_name)
        return None
        
        global file_1
        global result_fp
        file_to_find = file_1
    
        file_path = os.path.expanduser("~")
        
        
        result = find_file(file_to_find)
        
        global file_1_path
        file_1_path = find_file(file_path)
        
    
        if result:
            print(f"File found: {result}")
            return file_1_path
        else:
            print("File not found.")
            return file_1_path
        
find_file(file_1, file_1_path)

df1 = pd.read_csv(file_1_path)

df2 = pd.DataFrame(df1)

# Haversine Formula --> d = 2 * R * arcsin(sqrt(sin^2((lat2 - lat1) / 2 ) + cos(lat1) * cos(lat2) * sin^2((lon2 - lon1) / 2 ) ) )
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    lat_diff = lat2 - lat1 
    long_diff = lon2 - lon1 
    a = np.sin(lat_diff / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(long_diff / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    r = 3956 
    return c * r

# Below two are for testing different pandas functions and code types.
#import pandas as pd
df1 = pd.read_csv(file_1)

# Utilizing the Haversine function to convert lat/long differences into distance in miles. 
df2['distance_miles'] = df2.apply(lambda row: haversine(row['oasis_template_transport → ref_latitude'], 
                                                        row['oasis_template_transport → ref_longitude'], 
                                                        (33.37), (-81.96)), axis=1)

#print(df2)

# file_path_1 = Path('/Users/Jeff/Downloads/output.csv')
# file_path_1.parent.mkdir(parents=True, exist_ok=True)  
#df2.to_csv('output.csv', index=False, sep='\t')

# Choose name for output file below. Will want this as a tkinter input window in the future. 
name_for_file = 'trial_1.csv'

# This took way more work than I was expecting, will have to review 
 # os directory. 
def out_to_csv(dfl):
    global name_for_file
    final_file_path = '{file_1_path}' , '{name_for_file}' # Need to double check this format, want export into same directory as input. 
    os.makedirs(os.path.dirname(final_file_path), exist_ok=True) 
    dfl.to_csv(final_file_path, sep='\t', index = False)  
    print(f"Save output file path is: ", "{final_file_path}")
    return
out_to_csv(df2)

# More efficient and interchangeable (for different data sets) to have the below to be in a function.
# output = pd.DataFrame(df2)
# output_path = os.path.join(os.path.dirname(output), "coordinate_output.txt")
# output.to_csv(output_path, index=False, sep='\t')


