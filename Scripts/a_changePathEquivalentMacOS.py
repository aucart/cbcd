import os
import pathlib

# Here is the syntax to define paths on MacOC (for example, to your desktop) - thank you Louisa!
# /Users/yourUserName/Desktop
filePath = "/Users/yourUserName/Desktop/filename.csv"
# filePath = "C:/Users/yourUserName/Desktop/filename.csv" # on windows


# If you don't want to define your path file by file, nor use your current/default path as root (for the relative paths such as: ./data/), you can change 
# your current working directory with os.chdir:

os.chdir(pathlib.Path("/Users/yourUserName/Desktop"))

# Note: pathlib.Path is not necessary, aka:
# os.chdir("/Users/yourUserName/Desktop") # This commented line would be the classical way to go: define a str with the path of your file ...
# ... But using this 'pathlib' library prevents any 'slash' issue if you share code between macOS / windows / Unix
