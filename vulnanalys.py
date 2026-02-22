#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
def menu():
	try:
		while True:
			os.system("figlet VULNERABILITY ANALYSIS")
			print(""" 
VULNERABILITY ANALYSIS
			""")
			os.system("lynis audit system")
			break
			print("""
RESULT
			 """)
	except KeyboardInterrupt:
		print(" Exiting...")		 
if __name__ == "__main__":
	menu()
