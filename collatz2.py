# This program is essentially a copy of collatz.py
# However, in this version, the program starts at n=2
# and in an open-ended loop tests each incremented integer
# in turn.

# The data returned from each iteration for n returns:
# - The integer tested
# - The number of iterations in the test
# - The time to complete the test for n

# In addition, the program will inform the user of an
# approximate expected end time for the completion of the next test

# This code programmatically tests the Collatz Conjecture
# by asking the user for a positive integer and processing
# this number such that if the number is even, it is divided
# by two, if it is odd, it is multiplied by three and then one
# is added. This process is reiterated with the iteration only
# ending if the resultant number equals 1

import os # to expose the method for clearing the screen
os.system('cls')

# This clears the screen

n=2 # create the pointer for the starting integer to be tested

import keyboard # imports the method to listen for key press
import datetime # imports the method for date difference

# create the loop break flag (boolean) and set to false
# the flag must be raised to exit loop and will only be raised 
# when a positive integer is provided by the user and the
# Collatz Conjecture is true for this number

isPos=False

# start a count of iterations
iCount=0

# start the loop
while not isPos:
    # this code (error trapping to enforce correct data entry)
    # sourced from https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
    try:
        n=int(input("Please enter a positive integer: "))
        # if an error isn't raised (i.e. an integer - positive or negative
        # is supplied) then check if the integer is positive
        if n > 0:
            # start the iterative processing of the number provided
            originalNumber=n
            while n>1:
                # provide feedback to the user
                print("The current value being processed= ",n)
                # check if the number is even
                # i.e. the modulus of the number and two is zero
                if n % 2 == 0:
                    # divide the number by 2
                    n //= 2 # yeah, I like the shortened version  :-)
                else:
                    # it's an odd number
                    n = (n * 3 ) + 1
                iCount+=1
            isPos=True
        else:
            # provide feedback to the user
            print("The integer MUST be positive!!")
            print() # print an empty line for ease of reading
    except ValueError:
        # this error is raised when conversion to an int is tried
        # on a value that is not an integer
        print("You can only enter a positive integer")
        print() # print an empty line for ease of reading
print(".. and finally we reached ",n, " after ", iCount, " iterations!")
print()
print("Therefore, the Collatz Conjecture is true for the positive integer", originalNumber)
