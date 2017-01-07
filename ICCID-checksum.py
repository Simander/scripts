import sys
#Calculates a checksum for an ICCID, using Luhn algorithm, or validating ICCID+checksum.

def calc_checksum(number):
        id = number
        sum=0                                   #temporary value used to store the sum of the ICCID numbers
        count = 0                               #counts the numbers in the ICCID
        for x in reversed(id):                  #loops through the numbers in the ICCID backwards


                if count%2 == 0:                                #if count mod 2 (every other number)
                        val=int(x)*2                                    #Double the digit
                        if val > 9:                                     #if result is double digits
                                tmp = str(val)                          #cast the value to string
                                val = int(tmp[0])+int(tmp[1])           #get the sum of the value's two digits
                        sum+=val                                        #adds the resulting digit to the sum
                else:                                           #else
                        sum+=int(x)                                     #adds digit to the sum
                count+=1                                        #increase count

        checksum = (sum*9)%10                                   #checksum = the sum times 9 mod 10
        return checksum

def is_checksum_valid(number_with_checksum):
        print(calc_checksum(number_with_checksum))
        return calc_checksum(number_with_checksum) == 0


ARGS = len(sys.argv)


if(ARGS == 1):
        print("argument1: ICCID, argument2 is optional set to 1 for human-readable output." )

elif ARGS >= 2:
        print("ARGS eq 2")
        arg1 = sys.argv[1]
        ICCID = arg1
        CHECKSUM = calc_checksum(arg1)
        if ARGS == 3:
                print("ARGS eq 3")
                arg2 = sys.argv[2]


                if len(arg1) == 19:
                        print("length is 19")
                        #using the above functions to calculate the checksum and validating it
                        
                        ICCID_PLUS_CHECKSUM = int(str(arg1)+str(CHECKSUM))
                        VALID_CHECKSUM=is_checksum_valid(str(ICCID_PLUS_CHECKSUM))
                        print(ICCID_PLUS_CHECKSUM)
                        print(VALID_CHECKSUM)
                        if arg2 == '1':
                                #printing result as human readable
                                print("*******USING LUHN ALGORITHM********")
                                print("****CALCULATING ICCID CHECKSUM*****")
                                print("ICCID:              | CHECKSUM:    ")
                                print(str(arg1)+" | "+str(CHECKSUM))
                                if VALID_CHECKSUM:
                                        print("////////VALID CHECKSUM/////////////")
                                else:
                                        print("////////INVALID CHECKSUM///////////")
        elif len(arg1) == 19:
                print(str(arg1)+"\t"+str(CHECKSUM))

        elif len(arg1) == 20:
                print(is_checksum_valid(str(arg1)))
