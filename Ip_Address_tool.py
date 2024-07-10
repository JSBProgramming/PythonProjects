# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:25:25 2024

@author: Laitram LLC
"""
import requests
import re
import socket
import subprocess

# Display my Host machine IP address

def get_host_ip():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to an external server (we don't actually send any data)
        s.connect(("8.8.8.8", 80))
        # Get the socket's local address, which is our host's IP address
        host_ip = s.getsockname()[0]
        # Close the socket
        s.close()
        return host_ip
    except Exception as e:
        return "An error occurred: {}".format(str(e))

if __name__ == "__main__":
    host_ip = get_host_ip()
    print("Your host machine's IP address is:", host_ip, "\n")



# Display my Public IP address

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            return "Failed to fetch IP. Status code: {}".format(response.status_code)
    except Exception as e:
        return "An error occurred: {}".format(str(e))

if __name__ == "__main__":
    public_ip = get_public_ip()
    print("Your public IP address is:", public_ip, "\n")


#


def get_public_ipv4():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            ip_info = response.json()
            return ip_info.get('ip', 'IPv4 address not found')
        else:
            return "Failed to fetch IP. Status code: {}".format(response.status_code)
    except Exception as e:
        return "An error occurred: {}".format(str(e))

if __name__ == "__main__":
    public_ipv4 = get_public_ipv4()
    print("Your public IPv4 address is:", public_ipv4)


# To ping a specific IP address 

def ping_ip(ip_address):
    try:
        # Run the ping command
        result = subprocess.run(['ping', '-c', '4', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Check if the ping was successful
        if result.returncode == 0:
            return result.stdout
        else:
            return result.stderr
    except Exception as e:
        return "An error occurred: {}".format(str(e))

if __name__ == "__main__":
    ip_address = input("Enter the IP address to ping: ")
    ping_result = ping_ip(ip_address)
    print(ping_result)
