"""
Project: Sample Project from Projects Repo - Find e to the Nth Digit
Author: Nicholas Kier
Date: 10/09/15
Problem: Just like the previous problem, but with e instead of Pi.
Enter a number and have the program generate e up to that many decimal places. 
Keep a limit to how far the program will go.
References: http://mathworld.wolfram.com/e.html; https://docs.python.org/2/library/decimal.html
"""
import decimal # The decimal module is imported since it performs better than float()
factorial = 1 # The factorial is defined as 1 in order to find e from a nested series.
e = 2 # e is defined as 2 in order to begin the sequence of 2.xxxx.
for x in range(2,50): # The larger the range, the higher degree of accuracy for euler's number.
	# The two lines below perform the nested series calculation in order to find e.
	factorial *= x
	e += decimal.Decimal(1.0)/decimal.Decimal(factorial)

# Now that e has been determined, it can be used in a way that allows the user to determine the number of decimal places.

result = int(raw_input("Please enter how many decimal places you would like returned for e:"))
while result > 20:
	print "Sorry, cannot compute numbers greater than 20."
	# The code below lets the user enter another number, although it does seem wasteful.
	result = int(raw_input("Please enter how many decimal places you would like returned for e:"))
else:
	# The line below prints e as a string and slices the output using the result variable. '+2' is used as a quick trick to 
	# incorporate the beginning two characters of '2.'
	print str(e)[0:result+2]
