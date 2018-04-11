"""
===================   TASK 2   ====================
* Name:  Euclidean algorithm
*
* Write a function `gcd` that will calculate
* greatest common divisor for two integer values.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

def nzd(a,b):

    a = abs(a)
    b = abs(b)
    z = (a-b)

    if z == 0:
        return min(a,b)

    else:
        return nzd(z,min(a,b))

print (nzd(-24,6))