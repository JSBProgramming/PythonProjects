
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:09:55 2024


Let me read and write using a GUI - it has indicator light 

@author: Laitram LLC
"""





from pylogix import PLC
import tkinter as tk
from tkinter import ttk
import threading

def read_tag(plc, tag_name):
    return plc.Read(tag_name).Value

def write_tag(plc, tag_name, value):
    plc.Write(tag_name, value)

class PLCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PLC Tag Monitor and Control")
        
        # PLC connection settings
        self.plc = PLC()
        self.plc.IPAddress = '192.168.10.10'
        
        # Define tag names
        #self.tags = [f'Tag{i+1}' for i in range(5)]  # Example with 5 tags
        
        self.tags = [                       'MCP_START_LT',
                                            'Axis_AGS1L.OutputPower',
                                            'DWS_RUNNING',
                                            'MCP_PWR_LT',
                                            'MCP_ESTOP_LT'  ]  # Example with 5 tags
        
        # Create UI elements
        self.create_widgets()
        
        # Start updating the tags
        self.update_tags()

    def create_widgets(self):
        self.entries = {}
        self.values = {}
        
        # Connection status indicator
        self.status_label = tk.Label(self.root, text="Status: ")
        self.status_label.grid(row=0, column=0)
        self.status_indicator = tk.Canvas(self.root, width=20, height=20)
        self.status_indicator.grid(row=0, column=1)
        self.indicator = self.status_indicator.create_oval(5, 5, 20, 20, fill="red")

        for i, tag in enumerate(self.tags):
            label = tk.Label(self.root, text=tag)
            label.grid(row=i+1, column=0)

            entry = tk.Entry(self.root)
            entry.grid(row=i+1, column=1)
            self.entries[tag] = entry

            button = tk.Button(self.root, text="Write", command=lambda t=tag: self.write_tag_value(t))
            button.grid(row=i+1, column=2)

            value_label = tk.Label(self.root, text="", width=10)
            value_label.grid(row=i+1, column=3)
            self.values[tag] = value_label

    def write_tag_value(self, tag):
        value = self.entries[tag].get()
        try:
            # Convert value to appropriate type (int/float)
            if '.' in value:
                value = float(value)
            else:
                value = int(value)
            write_tag(self.plc, tag, value)
        except ValueError:
            print("Invalid input")

    def update_tags(self):
        try:
            # Check connection status
            if self.plc.Read(self.tags[0]).Status == 'Success':
                self.status_indicator.itemconfig(self.indicator, fill="green")
            else:
                self.status_indicator.itemconfig(self.indicator, fill="red")
                
            for tag in self.tags:
                value = read_tag(self.plc, tag)
                self.values[tag].config(text=str(value))
        except Exception as e:
            print(f"Error reading tags: {e}")
            self.status_indicator.itemconfig(self.indicator, fill="red")

        # Schedule the next update
        self.root.after(1000, self.update_tags)  # Update every second
        
        

def main():
    root = tk.Tk()
    app = PLCApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
