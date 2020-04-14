# As mentionned - I'm including a bunch of stuff, even if I won't use it, so that I don't have to import every single module every time
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


# -*-*-*-*-*-*-*-*-*- Generate dummy data -*-*-*-*-*-*-*-*-*-

simulated_participants_age = [3,4,5,6,7]
sigma = 2
invDiff = 10 #5
diSubj = {"DV_cdtA":{},"DV_cdtB":{}, "age":{}}                                 # initialising the dictionnary, itself containing dictionnaries

subjID = 0

for cur_age in simulated_participants_age:

    mu = 50 * (1 - (5-cur_age)/ invDiff)                     # changing the mu to generate different data according to age

    simulated_data_points =  np.random.normal(mu, sigma, (2,1))

    # Note that you will sometimes see the names of the argumenti in the function as below:
    simulated_data_points =  np.random.normal(loc=mu, scale=sigma,size=(1,2)) # this does exactly the same thing, except that you could  have only a few arguments, for ex:
    #simulated_data_points =  np.random.normal(size=(1,2))                    # this would leave the loc and scale parameters as their defaults (that you can find in the documentation: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.normal.html)

    diSubj["DV_cdtA"][subjID] = simulated_data_points[0][0]
    diSubj["DV_cdtB"][subjID] = simulated_data_points[0][1]
    diSubj["age"][subjID] = cur_age

    subjID += 1                                               # same as : subjID = subjID + 1

print(diSubj) #just watching the variable

df = pd.DataFrame.from_dict(diSubj)                           # transform the dictionnary into a dataframe- because dataframes are easy to export

print(df)   #just watching the variable



# -*-*-*-*-*-*-*-*-*- Export the dummy data -*-*-*-*-*-*-*-*-*-

# You can save export this df variable (a dataframe object) to a csv file simply with the command below:
df.to_csv("dummyData_b1.csv")

# you can also export it to excel:
df.to_excel("dummyData_b1.xls")
#df.to_excel("dummyData_b1.xlsx") #chose xls or xlsx just by changing the extension in the file name as here.



# Now the same but:

tgt = "C:/Users/acarteron/PycharmProjects/autres/pals/pyCbcd/"        #on windows you can write the path either with this slash "/"
tgt = "C:\\Users\\acarteron\\PycharmProjects\\autres\\pals\\pyCbcd\\" #... or with this one double "\\"


try:
#the try except is a way to 'bypass' errors in Python. Here I'm trying to save to a given location (tgt), but if you haven't changed it, you will get an error because this path doesn't exist in your folder...

    path_save_file = tgt+"dummyData_b1.csv"  # using a "+" between two strings is a way to concatenate them

    df.to_csv(path_save_file, index=None)

except:
#.. Because the line above cannot run without error, instead, it will what's following except:

    path_save_file = "dummyData_b1.csv"

    df.to_csv(path_save_file, index=None)           # this creates the file "dummyData.csv" in your current path/directory

print("Saved data in: " + path_save_file)
