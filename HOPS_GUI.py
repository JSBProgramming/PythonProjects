# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:36:57 2024

@author: Laitram LLC
"""

import tkinter as tk
from tkinter import scrolledtext
from pylogix import PLC
import threading
import time

class PLCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PLC Live Tag Monitor")
        self.plc = PLC()
        self.plc.IPAddress = "192.168.10.10"  # Replace with your PLC IP address
        self.tags = ['DWS_RUNNING',
        'MCP_PWR_LT',
        #'MCP_RESET_LT',
        'MCP_ESTOP_LT',
        'FaultArray[8].1',
        #'BeltRunningThreshhold_mm_s', 
        'FaultActive_EM01',
        'FaultActive_EM02',
        'FaultActive_EM03',
        'FaultActive_EM04', 
        'FaultActive_EM05',
        'FaultActive_UM01',
        'FaultArray[8]' ]  # Example tags to monitor
        
        self.log_file = "plc_log.txt"

        # Connection Status
        self.connection_status_label = tk.Label(root, text="Connection Status: Disconnected", fg="red")
        self.connection_status_label.pack()

        # Tags Display
        self.tags_display = scrolledtext.ScrolledText(root, width=50, height=15)
        self.tags_display.pack()

        # Start Monitoring Button
        self.start_button = tk.Button(root, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack()

        # Stop Monitoring Button
        self.stop_button = tk.Button(root, text="Stop Monitoring", command=self.stop_monitoring)
        self.stop_button.pack()

        self.monitoring = False

    def connect_plc(self):
        try:
            self.plc.Close()  # Ensure previous connection is closed
            self.plc = PLC()
            self.plc.IPAddress = "192.168.10.10"  # Replace with your PLC IP address
            response = self.plc.Read('FaultArray[8].1')  # Replace with an actual tag name from your PLC
            if response.Status == "Success":
                self.connection_status_label.config(text="Connection Status: Connected", fg="green")
                return True
            else:
                print(f"Failed to connect: {response.Status}")
                self.connection_status_label.config(text="Connection Status: Disconnected", fg="red")
                return False
        except Exception as e:
            print(f"Connection error: {e}")
            self.connection_status_label.config(text="Connection Status: Disconnected", fg="red")
            return False

    def get_tag_info(self, tag):
        tag_value = None
        tag_data_type = None
        tag_description = None

        # Get the tag value
        value_response = self.plc.Read(tag)
        if value_response.Status == "Success":
            tag_value = value_response.Value
        else:
            print(f"Error reading value for {tag}: {value_response.Status}")

        # Get the tag data type and description
        try:
            tag_info_response = self.plc.GetTagList()
            for tag_info in tag_info_response:
                if tag_info.TagName == tag:
                    tag_data_type = tag_info.DataType
                    tag_description = tag_info.Description
                    break
        except Exception as e:
            print(f"Error getting tag info for {tag}: {e}")

        return tag_value, tag_data_type, tag_description

    def monitor_tags(self):
        while self.monitoring:
            if self.connect_plc():
                tag_info_list = []
                for tag in self.tags:
                    tag_value, tag_data_type, tag_description = self.get_tag_info(tag)
                    tag_info = f"Tag: {tag}, Value: {tag_value}, Data Type: {tag_data_type}, Description: {tag_description}"
                    tag_info_list.append(tag_info)
                    self.log_tag_info(tag_info)
                
                self.update_tags_display(tag_info_list)
            time.sleep(5)

    def start_monitoring(self):
        self.monitoring = True
        self.monitor_thread = threading.Thread(target=self.monitor_tags)
        self.monitor_thread.start()

    def stop_monitoring(self):
        self.monitoring = False
        if hasattr(self, 'monitor_thread'):
            self.monitor_thread.join()

    def update_tags_display(self, tag_info_list):
        self.tags_display.delete(1.0, tk.END)
        for tag_info in tag_info_list:
            self.tags_display.insert(tk.END, tag_info + "\n")

    def log_tag_info(self, tag_info):
        with open(self.log_file, "a") as file:
            file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {tag_info}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = PLCApp(root)
    root.mainloop()
