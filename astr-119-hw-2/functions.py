#Python Functions

import numpy as np
import sys

#define a function that returns a value
def expo(x):
	#return the np e^x function
	return np.exp(x)

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		#call the expo function
		print(expo(float(i))) 

#define a main function
def main():
	#provide a default function for n
	n = 10

	#check if there is a command line for n
	if(len(sys.argv) > 1 ):
		#if an argument was provided, use it for n
		n = int(sys.argv[1]) 

	#call the show_expo subroutine
	show_expo(n) 

#run the main function
if __name__ == "__main__":
	main()