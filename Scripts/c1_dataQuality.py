""" To make very quick data inspection.
Say you have pilot data from an experiment for one subject. You want to see if the data look reasonable
We'll take real data from a switching task, where in block 1 the subject did task1, in block2 task2 and in block 3 an alternance of task 1 and 2

Here the data is short enough so that you could inspect it visually but you might as well do 3 more lines of code to check most of it is fine (and learn this for when you have many subjects / bigger data files!)

Data coding:
------------
 Phase
  0: practise trials, 1: block task1, 2: block task2, 3: block alternating task 1&2

"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime
import os
import math
import scipy

filename = 'data/demoSwitch00.csv'

df = pd.read_csv(filename)


# Inspecting shape, number of trial per phase, values for each discrete variable (missing data will appear):

print( df.shape )


for phaseN in df['phase'].unique():

    subdf = df[df['phase']==phaseN]

    print( 'N trials in phase %i:' %phaseN )
    print( subdf.shape[0] )

    print( subdf.shape[0] == subdf.trial.unique()[-1]+1 ) # no trial is missing (e.g. will be False if you have 0 1 3 4 5...)


for var in ['trial', 'imgID', 'phase', 'resp',  'correct', 'keysID']:

    print( df[var].unique() )


# Counting number of suspicious RTs - datawise:

print( (df['RT'] <= 0).sum() )

# Counting number of suspicious RTs - psychologywise:

print( df['RT'] <= 200 )


# Obviously instead of print you can create the variables, loop over participants and export everything

