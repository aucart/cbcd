# CBCD Python learning group 

### Summary / Github content

- **Memos**

  |_ PDFs:  really good 'Cheat sheets' from datacamp + equivalent functions Matlab <-> Python

  |_ a01_generalImports.py: *recommend to copy it at the start of every script, to save time*

  |_ debugging

  ​		importing_xxx.py: As mentioned during the session last week, different syntax to import various things. Make sure you have dowloaded the whole folder 'debugging'

  ​        *For now you'll probably find this uninteresting and/or confusing. But come back here whenever you face an import problem, and hopefully going it will help make sense of it and solve your problem*

- **Scripts**

|_ After you've been through the fundamentals (see tutorials below), you can play with the scripts in there.



### Useful links/external ressources:
There are many great ressources online, I keep running into new ones and will update accordingly. 
- **Tutorials**:

  - [update 15/4/2020] I don't want to overwhelm you but this looks like an extremely relevant list, well-organized! https://github.com/openlists/PythonResources If you don't know what to choose in there, start with one of these:
    - https://www.oreilly.com/library/view/a-whirlwind-tour/9781492037859/ seems very complete yet concise (from the table of contents)
    - For a shorter overview: https://cogs18.github.io/materials/03-Variables (this is part '03-Variables' of the course) and continue until 07

  - [OR] after learning about the 'core' language, main modules you need to learn about: **numpy** and **pandas** (manipulating data: in brief, numpy is working like matrices, and datafame is build on top of numpy and is more convenient because it allows to call cells by name, handles input, output, etc.), **matplotlib** for plots **scipy** for stats etc.
    - https://www.dataquest.io/course/python-for-data-science-fundamentals/

    - https://www.dataquest.io/course/pandas-fundamentals/
- great search engine for coding: https://duckduckgo.com/ (but obviously google will work fine)
- some reasons why people prefer Python over Matlab: https://pyzo.org/python_vs_matlab.html

# Session-by-session comments

## Week 1 (9/4/2020) - Installation & demo environment
I'm not expecting you to do any before the session, as one of the points is that you set time aside for Python over the sessions (and obviously because 'who am i to "expect you" to do anything!!), BUT for this time it would be great that you **just downloaded** one thing before[1] (helpful in case you have a bad connection that would suffer if you download & videoconference simultaneously). 

What to download? **Anaconda Installer**, here https://www.anaconda.com/distribution/.

What it that? In Matlab, you install the language and the IDE (Integrated Development Environment = environment where you code) all together (you have no choice and you may have never thought about it). However there are many ways to use Python (a bit like the difference R/Rstudio). Also, with Python you will need several packages (even for simple things), but there's a convenient way not to have to worry about it: installing the Anaconda distribution. When you install Anaconda, you are installing Python + many useful packages for data analysis + an IDE (environment) called Spyder. If that's the first time you hear about all that, can be confusing but I will explain everything and you'll see, once that familiarisation phase has passed, Python is (at least) as intuitive as Matlab!


[1] If you already have Anaconda, or you already have Python installed and you are comfortable with installing packages, no need to do this.

/!\ I should give a **warning** here, *if you already have an install of Python on your laptop*, this can possibly mess things up *with your Python-related stuff*. And sadly I'm not an expert in debuging install/Python conflict issues if they arise. If you don't have any Python on your system, it's totally safe!


#### Installation
If you feel in a mood of installing it, go for it! As far as I can remember, you should simply follow the steps like a classical installation. If you have any doubts, please feel free to message me beforehand, or wait for the session.


###### 'Testing' the installation
Start 'Spyder' (it should be somewhere if you have successfully installed Anaconda). No need to run Anaconda, or Python, or anything. Python (more preciseley, a conda environment) will be by default in your Spyder.
Download, then try and run the code 'testInstall.py' from within Spyder. If it plots a curve, it means the install went well! 



## Getting started with Python

#### Option A : start learning _Without installaing anything on your computer_!

https://www.datacamp.com/

#### Option B : 

- https://www.dataquest.io/course/python-for-data-science-fundamentals/

  - followed by: https://www.dataquest.io/course/pandas-fundamentals/
  
## Week 2 (17/4/2020)
1. Video intro (catch up or reminder) & go at your own pace :)
https://youtu.be/DDf_qfcYR6w

2. Less essential but will be helpful at some point: imports
https://youtu.be/kSws93m-OZo

