#!/usr/bin/python

import fib
from fib import fib

print "Type the Fibonacci number you would like to see\n -1 to quit\n"

while 1:
	num = raw_input("Enter your Input: ")
	if(num<0 or not num.isdigit()):
	        print "Quiting..." 
        	break
	print "At ", num, " Fibonacci Number is ", fib(int(num))
