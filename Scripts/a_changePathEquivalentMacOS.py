# Here is the syntax to change your path in Mac (for example, to your desktop)
# /Users/yourUserName/Desktop (thank you Louisa!)

import pathlib
# filename = "/Users/yourUserName/Desktop"           # This commented line would be the classical way to go: define a str with the path of your file ...
filename = pathlib.Path("/Users/yourUserName/Desktop/filename.csv") # ... But using this 'pathlib' library prevents any 'slash' issue if you share code between macOS / windows / Unix
