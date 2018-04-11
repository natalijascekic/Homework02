"""
===================   TASK 1   ====================
* Name: Rectangular To Polar
*
* Write a function `rect2polar` that will convert
* rectangular complex number notation to polar
* notation. 
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

import math

def rect2polar(x,y):

    r = math.sqrt(x**2 + y**2)

    if x > 0:
        angle = math.atan(y/x)

    elif x < 0:
        angle = 3.14 + math.atan(y/x)

    else:
        if y > 0:
            angle = 3.14/2

        else:
            angle = -(3.14/2)

    angle = angle * (180 / 3.14)

    return "("+ str(r)+","+str(angle)+")"

def main():

     print(rect2polar(4,5))

main()