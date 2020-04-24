# Here is the syntax to change your path in Mac (for example, to your desktop) - thank you Louisa!
# /Users/yourUserName/Desktop

import os
import pathlib

os.chdir(pathlib.Path("/Users/yourUserName/Desktop"))

# Note: pathlib.Path is not necessary, aka:
# os.chdir("/Users/yourUserName/Desktop") # This commented line would be the classical way to go: define a str with the path of your file ...
# ... But using this 'pathlib' library prevents any 'slash' issue if you share code between macOS / windows / Unix
