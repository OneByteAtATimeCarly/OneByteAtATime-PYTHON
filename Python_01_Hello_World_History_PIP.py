# A. Introduction - C. S. Germany 2022

# History: Python was originally developed by Guido van Rossum in the late 1980's and officially released in 1991. It is the offspring of the "ABC programming language".
#          Guido remained Python's lead developer until 12 July 2018, when he stepped down. In 2019, Python core developers elected a 5-member Steering Council to lead the project.
#          Python owes its name in some part as a hommage paid to the British comedy group "Monty Python". As a result, Python used spam and eggs in place of foo and bar. :-)

# Uses: Python uses include distributed development, server and cleint-side scripting, web development and mathematical applications.

# Platform: Python is platform independent, like Java. And interpreted so it doesn't need to be recompiled when modified. It can, however, be packaged with dependencies. 

# Versions: The most recent version of Python at the time of this writing is 3.10.4.

# Indentation: Unlike other languages such as C++, Java and PowerShell which use curly braces to define blocks of code and scope, Python relies exclusively on INDENTATION for this.

# Garbage Colletion: Like Java, Python performs garbage collection to asisst with memory management. 

# Reference Counting: Like C++ that employs pointers and references to manage objects on the heap (free store) and stack, Python also supports this "reference counting".
# Python hides the internals of pointers -> and references &, but occasionally they become visible as Python outwardly uses the dereference operator "*" to dereference objects.

# Object-Oriented: Python provides classes, inheritance hierarchies, polymorphic structures, code reuse and exception handling for true OOP.

# Structural: Python can also be adapted for Structural Programming as well.

# Semicolons?: You don't have to use semicolons at the end of statements in Python, as in PowerShell. But I you can use them if you want to. Won't hurt anything.  
#              I use semicolons for consistency as my personal choice. 
#              As I go back and forth from C++ and Java, which require semicolons, to languages like Python and PowerShell that do not - semicolons provide
#              familiarity and organization for me. 


# Development Environment: All these examples were created and tested using Anaconda 3 Python version 3.9 64-bit and Microsoft Visual Studio Code.
# BOTH are FREE dowloads. It will cost you NOTHING to learn and start developing in Python.

# Download latest ANACONDA Python 3.9: https://www.anaconda.com/products/distribution
# Download latest Visual Studio Code: https://code.visualstudio.com/download     


# PIP = package manager for Python

#    Link for packages = https://pypi.org/
#    Check if PIP is installed and get version  = pip --version
#    Download package - pip install camelcase
#    Using a package once installed = import *
#    Uninstall package = pip uninstall camelcase
#    List packages = pip list


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# 
def Topic_0l():
    print("\n   1: Using semicolons at the end of statements is optional"); print("   2. and unncessary in Python. It may even be \"unpythonic\"!"); 
    print("   3. But it provides me an organizational consistency I like compatible with other languages like C++ and Java."); print("   4. It is a personal choice.");
    print("   5. It also allows me to place multiple statements of code on a single line, as coded above. :-)"); print("   6. Pythonistas may abhor my personal style.");
    print("   7. But there is never truly \"one way to do it\". Innovation comes by constantly questioning \"Is there another way, for better or worse?\"");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#-----Invocations-----
Topic_0l();














#Anaconda Troubleshooting Notes:

#Step A: Get CONDA cmd to work in Windows 10
#
#         1. To get the conda cmd to work, must add to Windows PATH:
#            conda.bat  =  "C:\Users\germanc\Anaconda3\Library\bin\conda.bat"
#            conda.exe = "C:\Users\germanc\Anaconda3\Scripts\conda.exe"
#
#         2. In Windows
#            A. Goto  Control Panel -> System -> Advanced System Settings
#            B. Click the "Advanced" tab
#            C. Select "Environment Variables"
#            D. Under "User varibles for germanc" select "Path" and click "Edit". Add:
#               C:\Users\germanc\Anaconda3
#               C:\Users\germanc\Anaconda3\Scripts
#               C:\Users\germanc\Anaconda3\Library\bin
#
#            E. Verify path change by closing and reopening prompt and type: PATH
#            F. Verify Python version: python --version
#            G. Verify conda version: conda --version
#
#            H. Type: conda install anaconda-navigator
#               Note: Anaconda Navigator is a desktop graphical user interface (GUI) included in Anaconda® distribution
#                    that allows you to launch applications and easily manage conda packages, environments, and channels
#                    without using command-line commands. Navigator can search for packages on Anaconda.org or in a local
#                    Anaconda Repository.
#
#            I. Close and reopen Visual Studio Code
#            J. Switch VS Code to use cmd.exe as the default integrated terminal shell by:    
#               1. opening the command palette (Control-Shift-P)
#               2. search for Terminal: Select Default Profile
#               3. select Command Prompt
#               4. Close current terminal
#               5. Open new terminal  
#
#            K. To return to POSH mode, do above but select:
#               Powershell: Enable ISE Mode

