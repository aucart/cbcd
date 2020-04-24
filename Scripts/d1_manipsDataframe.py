import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import os
import math
import scipy
import pathlib

#filename = "./data/dummyData_b1.csv"           # This commented line would be the classical way to go: define a str with the path of your file ...
filename = pathlib.Path("./data/dummyData3.csv")# ... But using this 'pathlib' library should solve the slash issue (always write with the '/', and it will convert it for your OS, e.g. if you are using macOS I believe the above row wouldn't have worked.

df = pd.read_csv(filename)                      # Creates the file "dummyData.csv" in your current path/directory
print(df)                                       # It was the dummy dataset created in b1 and used in b2 (assuming one row represents one participant who did two conditions); i've just added more participants and shuffled them
print(df.columns)                               # Reminder: this is how your access the row names

# ---------------------------------------------------------------
# Let's say I want to average the two conditions within each subject - average of columns 1 and 2:
ave = (df["DV_cdtA"] + df["DV_cdtB"])/2

# NB. Another way to do it:
subsetDf = df[ ["DV_cdtA","DV_cdtB"] ].copy()   #  list the columns columns names to select from the df
print(subsetDf)

ave = subsetDf.mean(axis=1)

print(subsetDf.mean())                          # Note that without the 'axis=1' this is what we would have had (the default argument is axis=0)

# ---------------------------------------------------------------
# Now I want to make a discrete age category with a median split

medianAge = df.age.median()
df['medianSplit'] = df['age']>medianAge       # Create an indicator column - will be True if older than median age
df['medianSplit'] = df['medianSplit']*1       # Tip if you want to convert into 0/1s
print(df)

# ---------------------------------------------------------------
# 3 ways get the the average & standard deviation per group
# (1)
print(df.describe())


# (2)
print(df.groupby(['medianSplit']).mean())
print(df.groupby(['medianSplit']).std())


# (3)
cdt = 'cdtA'
diResults = {'ageGroup0':[], 'ageGroup1':[]} # Will store results in a dictionnary
diResults

for i in range(2):                           # Note that if you hadn't converted the bool into int, you could do: for i in range [True, False]
    subset = df[df['medianSplit']==i]
    av = subset['DV_'+cdt].mean()
    sd = subset['DV_'+cdt].std()
    diResults['ageGroup'+str(i)] = [av, sd]

print(diResults)



# ---------- exporting the results
res = df.describe()

del res['age']
del res['medianSplit']

res = res.T
res = res[['mean','std','50%']]

save = False  #todo: Change to True if you want the file created in your current directory
if save:
    res.to_csv('resManipsDf.csv')
