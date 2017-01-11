#!/usr/bin/python

# A Python script for calculating the CHECK-digit of an ICCID or
# validating the ICCID with CHECK-digit.
# Included is my implementation of the luhn algorithm
#	
#	coreLuhn(number, count=0)
#	|
#	|_______calc_checkdigit(number)
#	|_______valid_number(number)
#
# Author simander 10/1/2016

import sys

#the core Luhn algorithm
def coreLuhn(number, count=0):
    sum = 0
    for x in reversed(number):
        if count%2 == 0:
            val = int(x)*2
            if val > 9:
                tmp = str(val)
                val = int(tmp[0])+int(tmp[1])
            sum+=val
        else:
            sum+=int(x)
        count+=1
    checksum = (sum*9)%10
    return checksum;

#takes a number without the checkdigit, and calculates the check-digit
def calc_checkdigit(number):
    return coreLuhn(number)

#takes a number with check-digit included and returns true if the number is valid.
def valid_number(number):
    return coreLuhn(number, 1) == 0

if len(sys.argv) == 1:
	print("**help:")
	print("\tusage: \'ICCID_check_validate.py <ICCID>\' returns \'ICCID+CHECK-DIGIT\'")
	print("\tusage: \'ICCID_check_validate.py <ICCID+CHECK-DIGIT>\' returns \'True if number is valid\'")

elif len(sys.argv) >=2:
	NUMBER = sys.argv[1]

	if len(NUMBER) == 19:
		CHECK_DIGIT = str(calc_checkdigit(NUMBER))
		print(NUMBER + "\t" + CHECK_DIGIT)
	elif len(NUMBER) == 20:
		VALID_NUMBER = valid_number(NUMBER)
		print(VALID_NUMBER)
	else:
		print("ICCID must be 19 or 20 digits");
