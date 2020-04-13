"""Importing Anaconda modules/packages (or other modules you have created)

Terminology: a package is a set of modules.
It uses the folder hierarchy.
   You can picture 'matplotlib' as a folder containing many modules/python files.
   'Pyplot' is a file within this folder.
   Pyplot contains several functions included the function named 'plt'

I would recommend not using 'abbreviations'-like 'as np, as plt'- other than for the classical ones (the ones you will see in the code generalImports)
"""


import numpy as np
import scipy.stats

x = np.arange(10)
y  = np.flipud(x)
print(x)
print(y)
rho, p = scipy.stats.pearsonr(x,y)
print(rho)

#----------------------------------------
import numpy as np
import matplotlib.pyplot

x = np.arange(10)
y = np.exp(x)

matplotlib.pyplot.plot(x,y)

#NB: here you wouldn't be able to use other modules from matplotlib, say  matplotlib.rcsetup

#----------------------------------------
import numpy as np
import matplotlib.pyplot as plt         #recommended way to go

x = np.arange(10)
y = np.exp(x)

plt.plot(x,y)

#----------------------------------------
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(10)
y = np.exp(x)

plt.plot(x,y)

#----------------------------------------
import numpy as np
from matplotlib import pyplot

x = np.arange(10)
y = np.exp(x)

pyplot.plot(x,y)

#----------------------------------------
import numpy as np
from matplotlib.pyplot import *

x = np.arange(10)
y = np.exp(x)

plot(x,y)
#----------------------------------------
import numpy as np
import matplotlib.pyplot

x = np.arange(10)
y = np.exp(x)

pyplot.plot(x,y)

#----------------------------------------
# BELOW are what does NOT work:
#----------------------------------------
import numpy as np
import matplotlib.pyplot

x = np.arange(10)
y = np.exp(x)

pyplot.plot(x,y)  # Come back to the very top to see the correct way

#----------------------------------------
import numpy as np
from matplotlib import * # The '*' imports all the functions within one module (aka, the 'end' python file);
# whereas here you are trying to import all the modules (files) within the matpltlib folder. You can't do that

x = np.arange(10)
y = np.exp(x)

pyplot.plot(x,y)

