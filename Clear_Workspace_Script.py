# -*- coding: utf-8 -*-
"""
Created on Fri May 17 19:56:01 2024

@author: Laitram LLC
"""

import os
import sys

def clear_console():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def clear_all_variables():
    globals_to_clear = [name for name in globals() if not name.startswith('__') and name not in {'clear_console', 'clear_all_variables'}]
    for name in globals_to_clear:
        del globals()[name]


clear_console()
clear_all_variables()

# This will raise a NameError if executed because the variables have been cleared.
# try:
#     print(f"After clearing: x={x}, y={y}, z={z}")
# except NameError as e:
#     print(f"Variables have been cleared: {e}")
