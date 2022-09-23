# Introduction - C. S. Germany 2022

# History: Python was originally developed by Guido van Rossum in the late 1980's and officially released in 1991. It is the offspring of 
#          the "ABC programming language". Guido remained Python's lead developer until July 12, 2018, when he stepped down. In 2019, Python's
#          core developers elected a 5-member Steering Council to lead the project. Python owes its name in some part as a hommage paid to
#          the British comedy group "Monty Python". As a result, Python used spam and eggs in place of foo and bar. :-)

# Uses: Python's uses include distributed development, server and client-side scripting, web development, mathematical applications, robotics and more.

# Platform: Python is platform independent, like Java. It's interpreted so it doesn't need to be recompiled when modified. 
#           It can, however, package bytecode with dependencies into executables and binaries with package managers like PIP. 
#           Some tools for this are "auto-py-to-exe" and "PyInstaller". (https://www.geeksforgeeks.org/convert-python-script-to-exe-file/)

# Versions: The most recent version of Python at the time of this writing is 3.10.7. I personally prefer installing the "Anaconda" version of Python.
#           Its latest implementation of Python is version 3.9 at the time I'm writing this. So it's not the latest and the greatest, but it's stable.
#           You may obtain Anaconda and install it here: (https://www.anaconda.com/). In addition to a version of Python on your computer or device, 
#           you will also want an IDE (Integrated Development Environment). There are many, and each has its uses and particular set of features.
#           My two favorites for Python development are Netbeans (https://netbeans.apache.org/download/) and Visual Studio Code (https://code.visualstudio.com/). 
#           Both are free IDEs and offer powerful features like autocomplete and step-by-step debugging that really help with coding and testing Python projects. 

# Indentation: Unlike other languages such as C++, Java and PowerShell, which use curly braces to define blocks of code and scope, Python relies exclusively
#              on INDENTATION for this. Get your indentations even a single whitespace off in a script with thousands of lines of code? And your application
#              quickly becomes a tangle of spaghetti seething with syntax and logic errors! If you are new to Python and coming from other languages where
#              indentation is not as important, this takes some getting used to. If anything, it will force you to write neatly defined functions, classes,
#              decision and repetition structures in your code. Programming with Python will do wonders for developers who have the bad habit of writing
#              sloppy, poorly-indented code in other languages. :-)

# Garbage Colletion: Like Java, Python performs garbage collection to assist with memory management. So objects that are no longer used return their memory
#                    and resources back to the system, reducing the effect of "memory leaks" that can occur with languages that don't do garbage collection.

# Reference Counting: Like C++ that employs pointers and references to manage objects on the heap (free store), Python also supports "reference counting".

# POINTERS ?: If you have developed in C++, one of the things you will appreciate about Python is that it too makes use of passing by reference instead of value
#             for greater efficiency and speed. Whereas C++ gives you explicit control over how this is done with Pointers and References, Python hides much of
#             the implementation of and existence of these structures "under the hood". Though hidden from the developer, the functionality is still there, and
#             you will find that many things you could do in C++ development, you can also do with Python. For instance, when creating GUI interfaces with tkinter,
#             you can setup your GUI in a separate class. You can also create an inheritance hierarchy of classes to organize, encapsulate and reuse your code
#             in the inheritance chain. You can then setup objects external to the local scope and namespace of all your different classes, and initialize them to
#             "None", like C++'s "null". You may then instantiate objects from your classes that persist in memory, existing outside the scope and namespace of 
#             static and non-static classes and functions. You may then pass these objects efficently by reference both to internal methods in your classes, and
#             external functions - just as you could with C++ Pointers and References! We will look at doing this in many projects to come that use tkinter GUI
#             interfaces. This "C++-like" functionality is implemented in Python without C++ operators like "->" and "&" and "*". But it's still there, tucked away,
#             out of sight. Occasionally, this C++-like functionality becomes visible when Python outwardly uses the dereference operator "*" to dereference objects.

# Object-Oriented: Python provides classes, inheritance hierarchies, polymorphic structures, encapsulation and code-reuse structures, and exception handling. 
#                  All the features required and expected of a truly object-oriented language exist within Python.

# Structural: Although OOP is the path to the future, Python can also be adapted for Structural Programming.

# Semicolons?: You don't have to use semicolons at the end of statements in Python, as you do with C++ and Java. Neither do you have to use them in languages 
#              like PowerShell. However, you can use them in both languages, if you want to. It won't hurt anything. I use semicolons for consistency as my         
#              personal choice. When I go back and forth from C++ and Java, which require semicolons, to languages like Python and PowerShell, that do not?
#              Semicolons provide familiarity, consistency and organization for me. As well as the ability to put more than 1 statment of code on a single
#              line when desired.

# Development Environment: All these examples were created and tested using Anaconda 3 using Python version 3.9 (64-bit) and Visual Studio Code as an IDE.
#                          BOTH are FREE downloads. It will cost you NOTHING to learn and start developing in Python.

#                          Download the latest ANACONDA: https://www.anaconda.com/
#                          Download the latest Visual Studio Code: https://code.visualstudio.com/download     


# PIP = package manager for Python
#    Link for packages = https://pypi.org/
#    Example: Check if PIP is installed and get version  = pip --version
#    Example: Download package - pip install camelcase
#    Example: Using a package once installed = import *
#    Example: Uninstall package = pip uninstall camelcase
#    Example: List packages = pip list


# Our Very First Python Program!

#Function Definition------------------------------------------------------------------------------------------------------------------------------------------

def Topic_0l():
    print("\n");
    print("Hello World! \n");
    print("   1: Using semicolons at the end of statements is optional."); 
    print("   2. Completely unnecessary in Python. It may even be \"unpythonic\"?"); 
    print("   3. But it provides me with an organizational consistency I like that's compatible with other languages like C++ and Java."); 
    print("   4. It is a personal choice."); print("      You may, or may not wish to terminate your Python statements with a semicolon.");
    print("   5. Semicolons also allow me to place multiple statements of code on a single line, as in the line above. :-)"); 
    print("   6. Pythonistas may abhor this optional personal particular style.");
    print("   7. But there is never truly \"one way to do it\", is there?");
    print("   8. Perhaps innovation comes by constantly questioning \"Is there another way?\" For better, or for worse.");
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#----------Function Invocations----------
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