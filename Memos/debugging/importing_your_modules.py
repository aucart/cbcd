"""Remember: I recommend using as (root) current directory (path)- from where you run the scripts / code in the console - as the 'highest' Python folder in hierarchy

Here I am assuming that the root is at the level of 'debugging' (which contains the folder 'own_fcts')
"""

#if the python file (module) to import in the same folder as your current directory

#some equivalents

import myFunctions1
myFunctions1.just_print_stuff(10)


from myFunctions1 import *
just_print_stuff(20)


from myFunctions1 import just_print_stuff
just_print_stuff(30)


#-----------------------------------
#if the python file (module) is 'one folder below'

import own_fcts.myFunctions2
own_fcts.myFunctions2.just_print_stuff(40)

