""" Importing Anaconda modules(or other modules you have created)

Numpy is a module, that is a set of functions
Here I am using two of its functions: arange and flipud

To understand well how module import work in practise, run those bits of code independently (that is :
 - either run bit by bit in the console, restarting the kernel everytime in between
 - or copy paste into different scripts and execute the scripts
"""

#----------------------------------------
import numpy

x = numpy.arange(10)
print(x)
reversed_x = numpy.flipud(x)
print(reversed_x)

#----------------------------------------
import numpy as np #this is the common way to do it

x = np.arange(10)
print(x)
reversed_x = np.flipud(x)
print(reversed_x)

#----------------------------------------
from numpy import arange

x = arange(10)
print(x)
reversed_x = flipud(x) # Gives an error here because I only imported one function from numpy!
print(reversed_x)

#----------------------------------------
from numpy import arange, flipud

x = arange(10)
print(x)
reversed_x = flipud(x)
print(reversed_x)

#----------------------------------------
from numpy import * # Imports all the functions from numpy. May seem tempting but not recommended, for two reasons
# 1) you may overwrite some numpy function if you create functions/variables with the same name (you wouldn't know if as you probably don't know all numpy functions by heart!)
# 2) when you use some functions (like arange), it helps to read 'np.arange' rather than 'arange' because then you know directly that x is a numpy object

x = arange(10)
print(x)
reversed_x = flipud(x)
print(reversed_x)
