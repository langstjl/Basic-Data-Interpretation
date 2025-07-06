#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 13:10:45 2025

@author: Jeff
"""

#%% - Imports
import math
import statistics as stat
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *
from Pathlib import Path
import matplotlib.pyplot as plt

#%% - Build 2.0

# Need to be able to potentially format the program so that it creates a list
 # of all files that need to be utilized and can save the file path to another 
 # list to pull from those. Possibly make my own pandas database?
 
# Additionally, goal is to create a single customized .ttk window that allows 
 # me to input/choose/select all files pertaining to what I want, choose a 
 # function(.head, .shape, etc...) to get a quick look at the data and then
 # use .columns (or similar method) to choose how to join the data.

# I want an interface with a dropdown 'select' feature that allows me to choose
 # built-in functions below to peform analysis. 

file_1 = ""
file_1_path = ""
name_entry_for_file = ""

# Future variables
files_selected = []
files_selected_file_paths = []

def csv_check_for_input_file(fi):
    if fi.lower().endswith(".csv"):
        return fi
    else:
        tk.messagebox.showerror(title = "WARNING:", 
                                  message = "Please select a .csv file")
        return False

def select_file():
    root = tk.Tk()
    root.title("File Name Creator")
    root.geometry("400x300")
    global file_1_path 
    file_1_path = filedialog.askopenfilename(title="Select a .csv file") # Much easier for me than .os search.
    entry_string = tk.StringVar()
    # if csv_check_for_input_file(file_1_path): # Redundant. Modified for use later in code. 
    #     #root.destroy()
    #     return file_1_path
    def submit_function():
        root.destroy()
            
    root_label = tk.Label(root, 
                              text = "Enter the name for the new file:",
                              font = ("Arial", 14),
                              justify = "left")
    root_label.pack(pady = 5)
    
    root_entry = tk.Entry(root, textvariable = entry_string, width = 22)
    root_entry.pack(pady = 5)

    root_button = tk.Button(root, text = "Close and Submit", 
              command =  submit_function)
    root_button.pack(pady = 10)
    
    root.mainloop()
    
    name_entry_for_file = entry_string.get().strip()
    
    if not name_entry_for_file.lower().endswith(".csv"):
        name_entry_for_file += ".csv"
        
    return file_1_path, name_entry_for_file

file_1_path, name_entry_for_file = select_file()
# End 1st window, file selected, and output file named.

df1 = pd.read_csv(file_1_path)

df1_columns = list(df1.columns)
columns_for_window = { 'File Columns' : df1_columns }
column_position_for_window = { 'Column Position' : datafile_column_position_list }

def enter_columns_for_analysis():
    global entry1_string, entry2_string
    def submit_function_for_column():
        column_entry.destroy()
        
    column_entry = tk.Tk()
    column_entry.geometry("300x250")
    column_entry.title("Enter the column positions you wish to analyze.")

    tk.Label(column_entry, 
             text = "The column names and positions are displayed below:",
             font = ("Arial", 16)).pack(pady = 10)
    tk.Label(column_entry, 
             text = f"{columns_for_window}",
             font = ("Arial", 12)).pack(pady = 8)
    tk.Label(column_entry, 
             text = f"{column_position_for_window}",
             font = ("Arial", 12)).pack(pady = 8)

    tk.Label(column_entry, 
             text = f"Column positions are between 0 and {max_column}",
             font = ("Arial", 16)).pack(pady = 10)
 # Most likely can combine the above, definitely needs some filtering for the columns. 
 # Just want it added for now. 
    
    entry1 = tk.IntVar()
    entry2 = tk.IntVar()
    
    column_entry1 = tk.Entry(column_entry, 
                             textvariable = entry1,
                             font = ("Arial", 14),
                             justify = "left",
                             width = 10
                             )
    column_entry1.pack(pady = 10)
    
    column_entry2 = tk.Entry(column_entry, 
                             textvariable = entry2,
                             font = ("Arial", 14),
                             justify = "left",
                             width = 10
                             )
    column_entry2.pack(pady = 10)
        
    column_entry_button = tk.Button(text = "Submit",
                              command = submit_function_for_column
                              )
    column_entry_button.pack(pady = 20)
    
    column_entry.mainloop()
    
    entry1_integer = entry1.get()
    entry2_integer = entry2.get()
    
    return entry1_integer, entry2_integer

entry1_integer = int()
entry2_integer = int()

#analysis_file_column1 = df1.columns[column_position1]
#analysis_file_column2 = df1.columns[column_position2]

entry1_str, entry2_str = enter_columns_for_analysis()
column_position1 = int(entry1_str)
column_position2 = int(entry2_str)

# Haversine Formula --> d = 2 * R * arcsin(sqrt(sin^2((lat2 - lat1) / 2 ) + cos(lat1) * cos(lat2) * sin^2((lon2 - lon1) / 2 ) ) )
# Haversine function for converting lat/long coordinates to distance in miles.
# Modified to allow for designation from GUI for which rows to utilize. 
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    lat_diff = lat2 - lat1 
    long_diff = lon2 - lon1 
    a = np.sin(lat_diff / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(long_diff / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    r = 3956 
    return c * r

df1['distance_miles'] = df1.apply(
    lambda row: haversine(row[column_position1], row[column_position2], 33.37, -81.96),
    axis=1)

# There must be something I can use other than .os, above utilizes 'filedialog' within tkinter. Look into this.
def out_to_csv(dfl):
    global name_entry_for_file
    final_file_path = os.path.join(os.path.dirname(file_1_path), 
                                   name_entry_for_file)
    dfl.to_csv(final_file_path, sep='\t', index = False)  
    print(f"Output file path is: {final_file_path}")
    return
out_to_csv(df1)






