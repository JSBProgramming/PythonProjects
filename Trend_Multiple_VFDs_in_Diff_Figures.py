# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:26:08 2024

LCS Control - Intralox LLC
The goal of this scrip is to trend the VFDs on HOPS and collect data sets. This code will not trend live but create plots once duration is completed.

@author: Jhonatas Bastos - LCS Controls 
"""

# Required Libraries 

from pylogix import PLC
import matplotlib.pyplot as plt
import os 
import time
import pandas as pd
import csv
import numpy as np

# create a function to read the tags and 
def read_tags(plc, tags):
    results = plc.Read(tags)
    return {result.TagName: result.Value for result in results}

# Define PLC IP address and tags to read

plc_ip = '192.168.10.10' # conveyor PLC Ip

# All the Tags related with VFDs

#Uncommment or comment to get specific resutls. 

tags = [     'Axis_IFS1.OutputPower', 'Axis_IFS2.OutputPower', 'Axis_IFS3.OutputPower', 'Axis_IFS4.OutputPower', 'Axis_IFS5.OutputPower',
             'Axis_SMS0.OutputPower', 'Axis_SMS1A.OutputPower', 'Axis_SMS1B.OutputPower',  'Axis_SMS1C.OutputPower', 'Axis_SMS2A.OutputPower', 
             'Axis_SMS2B.OutputPower', 'Axis_SMS3.OutputPower', 'Axis_SMS3L.OutputPower', 'Axis_SMS3R.OutputPower', 'Axis_SMS5L.OutputPower', 'Axis_SMS5R.OutputPower', 'Axis_SMS6L.OutputPower', 'Axis_SMS6R.OutputPower', 
             'Axis_AGS1L.OutputPower', 'Axis_AGS1R.OutputPower', 'Axis_AGS2.OutputPower','Axis_AGS3L.OutputPower', 'Axis_AGS3R.OutputPower',
             'Axis_CF1.OutputPower','Axis_CF2.OutputPower','Axis_CF3.OutputPower', 'Axis_CF4.OutputPower', 'Axis_CF5.OutputPower', 'Axis_CF6A.OutputPower', 'Axis_CF6B.OutputPower', 'Axis_CF6C.OutputPower',
             'Axis_CF7.OutputPower', 'Axis_CF8.OutputPower', 'Axis_CF9.OutputPower', 'Axis_CF10.OutputPower', 'Axis_CF11.OutputPower', 'Axis_CF12A.OutputPower', 'Axis_CF12B.OutputPower', 'Axis_CF12C.OutputPower',
             'Axis_KFS1.OutputPower','Axis_KFS2.OutputPower','Axis_KFS3.OutputPower','Axis_KFS4.OutputPower', 'Axis_KFS5.OutputPower', 'Axis_KFS6.OutputPower', 'Axis_KFS7.OutputPower', 'Axis_KFS8.OutputPower', 'Axis_KFS9.OutputPower',
             'Axis_SLS1.OutputPower', 'Axis_SLS2.OutputPower', 'Axis_SLS3.OutputPower', 'Axis_SLS4.OutputPower', 'Axis_SLS5.OutputPower',
             'Axis_NMO1.OutputPower', 'Axis_RJ1.OutputPower',
        ]

# Initialize a dictionary to store tag data
data = {tag: [] for tag in tags}
timestamps = []

with PLC() as comm:
    comm.IPAddress = plc_ip

    # Collect data for a specified duration
    
    duration = 10 #300 #3600 = 1 hour # 30 1800  # seconds x*60                      I need to implement a Break function 
    interval = 1  # seconds

    start_time = time.time()
    while time.time() - start_time < duration: 
        timestamp = time.time()
        tag_values = read_tags(comm, tags)
        print(" Time Counter: " + str(int(time.time()-start_time)) + " for " + str(duration) + " secs time duration") # This wll create a counter 
             
        
        # user_input = input("Type exit to stop: ")

        # if user_input.lower() == 'exit':
        #     print("Exinting the loop")
        #     break
        #     print(f"You entered: {user_input}")
        
        for tag in tags:
            data[tag].append(tag_values[tag])
        timestamps.append(timestamp - start_time)

        time.sleep(interval)
        
       # print(data) # for troubleshooting purpose 


# Plot the collected data, each tag in its own figure

   # folder_path = "HOPS_Figures_1005_2" # Name your folder here - The folder will be created on your directory 
    #os.makedirs(folder_path, exist_ok=True)


    for tag in tags:
    #figsize : (float, float), default: :rc:`figure.figsize`
    # Width, height in inches.
    # dpi : float, default: :rc:`figure.dpi`
    # The resolution of the figure in dots-per-inch.
    
       #  plt.figure(dpi = 300)
       #  plt.plot(timestamps, data[tag], linewidth = 0.5, label=tag)
       #  plt.xlabel('Time (s)')
       #  plt.ylabel('Value')
       #  plt.title(f'{tag} Values Over Time')
       #  plt.legend()
       #  plt.grid(True)
       # #plt.show()
        
       #  plt.savefig(os.path.join(folder_path, f'{tag}.png'), dpi=300)
       #  plt.close()
        
#------------------------------------------------------------------------------

        # Using Pandas to collect the data: 
            
        df = pd.DataFrame(data)
        # Save to CSV file
        df.to_csv("HOPS_Output_ Data_1005_3.csv", index=False) # Name your data set here
        
    print("\n")
    print("Plots and data has been completed - check your directory")
        
        
      
        
        
        
        



