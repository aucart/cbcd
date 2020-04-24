# Scripts d1_ and d2_ show you how to do similar operations with two modules: Numpy and Pandas (Pandas is the name of the module that has DataFrames object- it was inspired from R's dataframes)
# it's useful to be able to *understand* both as both are commonly used. For using it's a matter of preference
# I personally use numpy (arrays) only when dealing with one-dimension vectors,
# and use Dataframe most of the time, because there's less risk of errors when you call columns names instead of indices (if you're wondering, I sometimes use it for 1-dim array because find it more convenient and then tend to remember better the df commands)


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime
import os
import math
import scipy
import pathlib

try:
    filename = pathlib.Path("/Users/yourUserName/Desktop/dummyData3.csv") # ... But using this 'pathlib' library prevents any 'slash' issue if you share code between macOS / windows / Unix
    arr = np.genfromtxt(filename, delimiter=',') # This genfromtxt is not specific for CSV so it doesn't know that by defintions a CSV file's delimiter is a common
except: # when you're a windows user,...
    try: # either write your entire path like this
        filename = pathlib.Path("C:/Users/yourUserName/Desktop/dummyData3.csv")
        arr = np.genfromtxt(filename, delimiter=',') # This genfromtxt is not specific for CSV so it doesn't know that by defintions a CSV file's delimiter is a common

    except: # or the relative folder
        filename = pathlib.Path("./data/dummyData3.csv")
        arr = np.genfromtxt(filename, delimiter=',') # This genfromtxt is not specific for CSV so it doesn't know that by defintions a CSV file's delimiter is a common

# For more on changing path: see 'a_changePathEquivalentMacOS.py"
# If you're wondering what is this strange syntax in genfromtxt (why not: np.genfromtxt(filename, ',') - go see: snipets_fcts.py)

# ----------------------------------------------------------------
# The first row contained strings and numpy only handles number so it replaced the str by 'nan' (Not A Number)
arr = arr[1:,:] #to remove the first row, selecting all rows from index 1 (aka the second line as indexing starts at 0) until the end

print(arr)
print(arr.shape)


# -------------------------
# Selecting rows or column
rowNb = 0
print(arr[rowNb,:])

colNb = 2
print(arr[:,colNb])
print(arr[:,-1])    # same as calling -1 = last column


# ---------------------------------------------------------------
# Let's say I want to average the two conditions within each subject - average of columns 1 and 2:
ave = (arr[:,0] + arr[:,1]) / 2

print( np.mean(arr[:,0:1], axis=1 ) )

# careful, if you don't specify any axis it will make the average of rows AND columns:
print(np.mean(arr[:,0:1]))


# ---------------------------------------------------------------
# Now I want to make a discrete age category with a median split

medianAge = np.median( arr[:,-1] )

arrAges = arr[:,2]
ageIndicator = arrAges<medianAge


# ---------------------------------------------------------------
# Get the the average & standard deviation per group

diMatchCdtIdx = {'cdtA':0, 'cdtB':1}
cdt = 'cdtA'
idxToSelect = diMatchCdtIdx[cdt] # this line of code (& the two above) don't seem useful here as it's not hard to keep track of what column is what, but for bigger project where these lines are separated, or to automatize more, this 'trick' can be handy
print(idxToSelect)

arrCdt = arr[ :,idxToSelect] #select the column
print(arrCdt)

diResults = {'ageGroup0':[], 'ageGroup1':[]} # Will store results in a dictionnary

for i in range(2):                           # Note that if you hadn't converted the bool into int, you could do: for i in range [True, False]
    subset = arrCdt[ ageIndicator ] #select the rows for which ageIndicator is True
    av = subset.mean()
    sd = subset.std()
    diResults['ageGroup'+str(i)] = [av, sd]

print(diResults)


# ---------------------------------------------------------------
# Exporting the results
res = pd.DataFrame.from_dict(diResults) # trick to format and save the results quickly: go through a dataframe

save = False  #todo: Change to True if you want the file created in your current directory
if save:
    res.to_csv('resManipsDf.csv')

