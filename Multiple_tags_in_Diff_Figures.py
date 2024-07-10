# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:26:08 2024

@author: Laitram LLC
"""






from pylogix import PLC
import matplotlib.pyplot as plt
import os 
import time
import pandas as pd
import csv
import numpy as np


def read_tags(plc, tags):
    results = plc.Read(tags)
    return {result.TagName: result.Value for result in results}

# Define PLC IP address and tags to read
plc_ip = '192.168.10.10'

#tags = [f'Tag{i+1}' for i in range(20)]  # List of 20 tags
tags = [   #'Axis_IFS1.OutputPower', 'Axis_IFS2.OutputPower', 'Axis_IFS3.OutputPower', 'Axis_IFS4.OutputPower', 'Axis_IFS5.OutputPower',
           # 'Axis_SMS0.OutputPower', 'Axis_SMS1A.OutputPower', 'Axis_SMS1B.OutputPower',  'Axis_SMS1C.OutputPower', 'Axis_SMS2A.OutputPower',
           # 'Axis_SMS2B.OutputPower', 'Axis_SMS3.OutputPower', 'Axis_SMS3L.OutputPower', 'Axis_SMS3R.OutputPower', 'Axis_SMS5L.OutputPower', 'Axis_SMS5R.OutputPower', 'Axis_SMS6L.OutputPower', 'Axis_SMS6R.OutputPower', 
           # 'Axis_AGS1L.OutputPower', 'Axis_AGS1R.OutputPower', 'Axis_AGS2.OutputPower','Axis_AGS3L.OutputPower', 'Axis_AGS3R.OutputPower',
           'Axis_CF1.OutputPower','Axis_CF2.OutputPower','Axis_CF3.OutputPower', 'Axis_CF4.OutputPower', 'Axis_CF5.OutputPower', 'Axis_CF6A.OutputPower', 'Axis_CF6B.OutputPower', 'Axis_CF6C.OutputPower',
           'Axis_CF7.OutputPower', 'Axis_CF8.OutputPower', 'Axis_CF9.OutputPower', 'Axis_CF10.OutputPower', 'Axis_CF11.OutputPower', 'Axis_CF12A.OutputPower', 'Axis_CF12B.OutputPower', 'Axis_CF12C.OutputPower' 
           # 'Axis_KFS1.OutputPower','Axis_KFS2.OutputPower','Axis_KFS3.OutputPower','Axis_KFS4.OutputPower', 'Axis_KFS5.OutputPower', 'Axis_KFS6.OutputPower', 'Axis_KFS7.OutputPower', 'Axis_KFS8.OutputPower', 'Axis_KFS9.OutputPower',
           # 'Axis_NMO1.OutputPower', 'Axis_RJ1.OutputPower',
        ]

# Initialize a dictionary to store tag data
data = {tag: [] for tag in tags}
timestamps = []

with PLC() as comm:
    comm.IPAddress = plc_ip

    # Collect data for a specified duration
    
    duration = 3600 #300 3600 # 30 1800  # seconds x*60                      I need to implement a Break function 
    interval = 1  # seconds

    start_time = time.time()
    while time.time() - start_time < duration: 
        timestamp = time.time()
        tag_values = read_tags(comm, tags)
        print(" Time Counter: " + str(int(time.time()-start_time)) + " for " + str(duration) + " secs time duration")
             
        
        # user_input = input("Type exit to stop: ")

        # if user_input.lower() == 'exit':
        #     print("Exinting the loop")
        #     break
        #     print(f"You entered: {user_input}")
        
        for tag in tags:
            data[tag].append(tag_values[tag])
        timestamps.append(timestamp - start_time)

        time.sleep(interval)
        
       # print(data)

# Plot the collected data using subplots

# num_tags = len(tags)
# num_cols = 4  # Number of columns for subplots
# num_rows = (num_tags + num_cols - 1) // num_cols  # Calculate number of rows needed

# fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 2.5 * num_rows), constrained_layout=True)

# for i, tag in enumerate(tags):
#     row = i // num_cols
#     col = i % num_cols
#     ax = axs[row, col]
#     ax.plot(timestamps, data[tag], label=tag)
#     ax.set_xlabel('Time (s)')
#     ax.set_ylabel('Value')
#     ax.set_title(tag)
#     ax.legend()
#     ax.grid(True)

# plt.suptitle('PLC Tag Values Over Time')
# plt.show()


# Plot the collected data, each tag in its own figure


#def save_figures(self):
    folder_path = "HOPS_Figures_1014_7"
    os.makedirs(folder_path, exist_ok=True)

   # timestamps = list(range(60))  # Example timestamps
  #  data = {tag: [i for i in range(60)] for tag in tags}  # Example data

    for tag in tags:
    #figsize : (float, float), default: :rc:`figure.figsize`
    #Width, height in inches.

    # dpi : float, default: :rc:`figure.dpi`
    # The resolution of the figure in dots-per-inch.
    
        plt.figure(dpi = 300)
        plt.plot(timestamps, data[tag], linewidth = 0.5, label=tag)
        plt.xlabel('Time (s)')
        plt.ylabel('Value')
        plt.title(f'{tag} Values Over Time')
        plt.legend()
        plt.grid(True)
       #plt.show()
        
        plt.savefig(os.path.join(folder_path, f'{tag}.png'), dpi=300)
        plt.close()
        
#------------------------------------------------------------------------------

        # Using Pandas to collect the data: 
            
        df = pd.DataFrame(data)
        # Save to CSV
        df.to_csv("HOPS_Output_7.csv", index=False)
        
        
        # Using numpy to calculate the average
    
        # def average():
        #     return np.mean()


"""
# 

# for tag in tags:
#     plt.figure(figsize=(10, 6))
#     plt.plot(timestamps, data[tag], label=tag)
#     plt.xlabel('Time (s)')
#     plt.ylabel('Value')
#     plt.title(f'{tag} Values Over Time')
#     plt.legend()
#     plt.grid(True)
#     #plt.show()
    
    
    
# def main():
#     save_figures()

# if __name__ == "__main__":
#     main()
    
"""
