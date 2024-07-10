# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:57:02 2024

Asking ChatGBT for a PLC GUI to see if the machine is running

@author: Laitram LLC
"""

import tkinter as tk
from pymodbus.client.sync import ModbusTcpClient

class PLCStatusApp:
    def __init__(self, master):
        self.master = master
        master.title("PLC Status")

        self.label = tk.Label(master, text="PLC Status:")
        self.label.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

        self.check_status_button = tk.Button(master, text="Check Status", command=self.check_status)
        self.check_status_button.pack()

    def check_status(self):
        PLC_IP = '192.168.10.10'  # Modify this with your PLC IP address
        PLC_PORT = 502  # Modify this with your PLC Modbus port

        try:
            client = ModbusTcpClient(PLC_IP, port=PLC_PORT)
            client.connect()
            # Read a register to check PLC status (modify according to your PLC configuration)
            result = client.read_holding_registers(0, 1, unit=1)
            client.close()

            if result:
                self.status_label.config(text="PLC is running")
            else:
                self.status_label.config(text="PLC is not running")
        except Exception as e:
            print("Error:", e)
            self.status_label.config(text="Error: " + str(e))

def main():
    root = tk.Tk()
    app = PLCStatusApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
