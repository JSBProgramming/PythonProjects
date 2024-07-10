# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:33:16 2024

@author: Laitram LLC
"""

from pylogix import PLC

def test_plc_connection():
    plc = PLC()
    plc.IPAddress = "192.168.10.10"  # Replace with your PLC IP address

    try:
        response = plc.Read( 'FaultArray[8].1')  # Replace with an actual tag name from your PLC
        if response.Status == "Success":
            print(f"Connected to PLC. Tag value: {response.Value}")
        else:
            print(f"Failed to read tag: {response.Status}")
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        plc.Close()

if __name__ == "__main__":
    test_plc_connection()