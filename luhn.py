# An implementation of the Luhn algorithm in Python.
# Written by Anders Simonsen
# 
# the calc_checkdigit(number): 
#       takes a number without the check-digit and calculates the check-digit
# the valid_number(number):
#       validates a number with the included check-digit and returns true if number is valid
#
# the two methods explained above rely on the coreLuhn(number, count=0)
#       Takes two parameters, a number, and a count value.
#       The default value of the count value is 0 which means it will calculate the numbers check-digit,
#       this can be altered to one to validate a number with a check-digit

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
    print("check digit: ")
    return coreLuhn(number)

#takes a number with check-digit included and returns true if the number is valid.
def valid_number(number):
    print("valid number: ")
    return coreLuhn(number, 1) == 0
