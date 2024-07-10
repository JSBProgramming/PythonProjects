# -*- coding: utf-8 -*-
"""
Author: Charlie Escude
Date: August 16th, 2023
Version: 2
Description: HOPS Bin Check code. Dedicated to Black Ops!!

"""
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

global sort_plan_dict
global sort_plan_loaded

sort_plan_dict = {}
sort_plan_loaded = False

# loads the sort plan from file browser
def load_sort_button_event():
	global sort_plan_dict

	try:
		root = tk.Tk()
		root.withdraw()
		currdir = os.getcwd()
		file_location = filedialog.askopenfilename(initialdir=currdir, title='Please select a directory')
		sort_plan = pd.read_csv(file_location)
		try:
			sort_plan_dict = AuditSortPlan(sort_plan)
			print(f"Sort Plan {file_location} Load Successful")
			sort_plan_loaded = True
			# loadfile = "MissortData/loadfile.txt"
			# with open(loadfile, 'w') as file:
			# 	loadfile = file.write(file_location)
		except Exception as e:
			print(str(e) + " ERROR: Failed to audit sort plan", "Error")

		
	except Exception as e:
		print(str(e) + " ERROR: Invalid File", "Error")

# audits sort plan to extract which zips belong in which bin
def AuditSortPlan(audit_file):
	audit_file = audit_file.drop(['RecordType', ' Day', ' Ain', ' MailType', ' Container', ' Route Name', ' Sort Group'], axis=1)
	first_zip = list(audit_file.iloc[:,0])
	last_zip = list(audit_file.iloc[:,1])
	discharge = list(audit_file.iloc[:,2])
	code_range = []
	zipcodes = []

	#Get the range of zipcodes and flatten them out
	for i in range(len(first_zip)):
	    code_range.append(range(first_zip[i], last_zip[i]+1))
	for j in code_range:
	    zipcodes.append([*j])

	#just the bin numbers from the header name
	temp = []
	for bins in discharge:
	    temp.append((bins[5:8]))
	discharge = temp
	sample_mapping = list(zip(discharge, zipcodes))

	#make a dictionary of the of the bins to zipcodes. ONE-TO-ONE mapping
	refined_mapping = {}
	for mapping in sample_mapping:
	    key = mapping[0]
	    value = mapping[1]
	    if key in refined_mapping:
	        refined_mapping[key].extend(value)
	    else:
	        refined_mapping[key] = value
	return refined_mapping

# extracted out missort check logic
def missort_check(scanBarcode = ""):
	global sort_plan_dict
	package_found = False
	# handler for manual codes
	if len(scanBarcode) < 23:
		manual_zip = input("Manual Enter Zipcode: ")
		try:
			if len(manual_zip) == 5 and manual_zip.isdigit():
				scanBarcode = '420' + manual_zip + '0000'
			else:
				print("ZIPCODE must be a 5-digit number. Try again. ", "Error")
		except:
			pass	# try to read zipcode

	try:
		zipcode_int = int(scanBarcode[3:8])
	except Exception as e:
		zipcode_int = 0
	zipcode_str = str(zipcode_int)
	print(f"got {zipcode_str} string, searching......")
	# determine success if zipcode is in bin dict entry
	for key, value in sort_plan_dict.items():
		if zipcode_int in value:
			print("Package should be in bin: " + str(key))
			package_found = True

	if not package_found:
		print("Zipcode not found in sort plan")

# main
def main():
	global sort_plan_dict
	global sort_plan_loaded
	try:
		sortplan = load_sort_button_event()
		sort_plan_loaded = True
	except:
		print("Failed to load sort plan")

	while sort_plan_loaded:
		print("-------------------------------")
		missort_check(input("Enter Zipcode: "))
		print()


if __name__ == '__main__':
	main()