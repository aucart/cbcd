""" Some batch renaming and copying to a different folder with a new structure.

! Be careful because if misused, this can delete files permanently. Always make a backup of the file you are working on before trying to batch rename/move them.


Imagine you have saved your data participant by participant, with all files types in the same folder named after the participant ID:

FoldersSrc
    |_sub001
        |_20200101_rec.csv
        |_20200101_video.avi
    |_sub002
        |_ ...


This script will:

1) De-identify the data (here removing dates but it can easily be adapted)- Assuming you still have the date/time information somewhere in your filenames and want to remove for full anonymization.

2) Copy, move and re-organize the data by file type:

FoldersTgt
    |_data
        |_sub001.csv
        |_sub002.csv
        |_ ...
    |_videos
        |_ sub001.avs
    ...
"""


import pathlib
import os

rootSrc = pathlib.Path("./data/dummyFoldersSrc/")
rootTgt = pathlib.Path("./data/dummyFoldersTgt/")
slashSyst = pathlib.Path("/")                       # keeping it cross-OSs

typesToSeparateInFolders = ['.csv','.avi']          # define types of files that will be handled

# Create target arborescence
diFoldersExtensions = {'.csv':'data', '.avi':'videos'} # dictionnaries are convenient to link parameters etc..
for ext in diFoldersExtensions.keys():
    folderName = diFoldersExtensions[ext]              #.. select the name of folder that will host the type of file
    tgtFold = pathlib.Path( str(rootTgt) + str(slashSyst) + folderName + str(slashSyst) ) # define full path (mix of str & Path because can concatenates strings easily (with +) but not Path)

    if not os.path.exists(tgtFold): # the 2 lines could be replaced by: os.makedirs(rootTgt, exist_ok=True) -that creates folder if doesn't exist already- but the other way is better for demo
        os.makedirs(tgtFold)


# 1) adapt this to your file naming convention
# find a way to identify the date pattern to remove - should be manageable by using separation by a marker (here '_' but it could by any string) and/or using the nb of char


subfoldersList = os.listdir(rootSrc)

for sub in subfoldersList:
    path =  pathlib.Path( str(rootSrc) + str(slashSyst) + sub )
    for files in os.listdir(path):
        for ext in typesToSeparateInFolders:
            if files.endswith(ext):
                pathTgt = str(rootTgt) + str(slashSyst)  +diFoldersExtensions[ext]+ str(slashSyst)
                fullPathTgt =  pathlib.Path(pathTgt + files)

                fullPathSrc = pathlib.Path( str(rootSrc) + str(slashSyst) + sub  + str(slashSyst)+ files )
                os.rename(fullPathSrc,fullPathTgt)  # moves the file from Src to Tgt


                newFilename = str(fullPathTgt).split(str(slashSyst))[-1]
                newFilename = sub + "_" + newFilename.split('_')[-1]

                os.rename(pathTgt + files,pathTgt + newFilename) # actual file renaming
