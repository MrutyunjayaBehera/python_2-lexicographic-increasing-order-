#TASK

#You are given three integers X, Y and Z, representing the dimensions of a cuboid along with an integer N.
#You have to print a list of all possible coordinates given by(i,j,k)  on a 3D grid where the sum of (i+j+k) is not equal to N . 
#here 0<=i<=X, 0<=j<=Y, 0<=k<=Z

#CODE

import math
import os
import random
import re
import sys

x = input("raw_input1: ")              
x = int(x)                              #converting input string to an integer 
y = input("raw_input2: ")
y = int(y) 
z = input("raw_input3: ")
z = int(z)
n = input("raw_input4: ")
n = int(n)

print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n])    #This prints all the combinations of a,b and c for their given ranges


#ENJOY
