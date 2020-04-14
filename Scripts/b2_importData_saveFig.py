""" The dummy data simulates average performance (say, percentage correct responses) in condition A and B of participants aged 3 to 7 years old
with one row per subject"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime
import os
import math
import scipy
import itertools
import statsmodels.api as sm
import statsmodels.stats.stattools as stools
import statsmodels.stats as stats
import scipy.stats as scipystats
from functools import partial
import random
# As mentionned - I'm including a bunch of stuff, even if I won't use it, so that I don't have to import every single module every time



# -*-*-*-*-*-*-*-*-*-*-*-*-*- Load dummy data -*-*-*-*-*-*-*-*-*-*-*-*-*-
src = "C:/Users/acarteron/PycharmProjects/autres/pals/pyCbcd/"          # on windows you can write the path either with this slash "/"...
src = "C:\\Users\\acarteron\\PycharmProjects\\autres\\pals\\pyCbcd\\"   # ... or with this one double "\\"


try:    #the try except is a way to 'bypass' errors in Python. Here I'm trying to load to a given location (src), but if you haven't changed src, you will get an error because this path doesn't exist in your computer...
    df = pd.read_csv(src+"dummyData_b1.csv")
except: #.. Because the line above cannot run without error, instead, it will what's following except:
    df = pd.read_csv("dummyData_b1.csv")  #this creates the file "dummyData.csv" in your current path/directory

print(df)   #just watching the variable



# -*-*-*-*-*-*-*-*-*-*-*-*-*- Look at the data -*-*-*-*-*-*-*-*-*-*-*-*-*-

y = df["DV_cdtA"]                   # take the data from condition A
x = df["age"]

plt.plot(x,y)                       # plots the average performance (in cdtA) as a function of age



# -*-*-*-*-*-*-*-*-*-*-*-*-*- Correlation -*-*-*-*-*-*-*-*-*-*-*-*-*-

rho, p = scipy.stats.pearsonr(x,y)   # correlation between age and average perfromance (in cdtA)

print(rho)
print(p)


# -*-*-*-*-*-*-*-*-*-*-*-*-*- Re-plot the data and save the figure -*-*-*-*-*-*-*-*-*-*-*-*-*-

plt.figure()                             # create a separate figure (new windows)

plt.plot(x,y, "o")                       # points instead of a line

plt.xlabel("Age")

plt.ylabel("Average performance in condition A ")

annotationStr = "Pearson r = %.3f, p = %.3f" % (rho, p)
plt.title(annotationStr)

tgt = "C:/Users/acarteron/PycharmProjects/autres/pals/pyCbcd/"
plt.savefig(tgt+"dummyFig.png")
#plt.savefig(tgt+"dummyFig.png", dpi = 75) # save with low resolution