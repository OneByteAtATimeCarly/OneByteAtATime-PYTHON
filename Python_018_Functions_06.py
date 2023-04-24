# Title: Python Functions 6 - Command line part 3
# Author: C. S. Germany 01/15/2022

# Calling individual functions from command line.

 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 
import sys, getopt;

def Meaning_of_Life():
    print("\nThe Meaning of Life = 42");

def What_Time_Is_It():
    print("\nThe time is 4:44");  

def SuperCala():
    print("\nSuperCalaFrajalIsticExpeAlaDocius!");   

if __name__ == '__main__':
   Meaning_of_Life();    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#-----Invocations-----

# To run, do not hit "debug" or F5. Rather, from a CMD PROMPT go the the sctipt directory and run from cmd line: 
# cd to "D:\Carlys_Scripts_2023\Carlys_PYTHON_Scripts_2023\Python\Programming_CONSOLE\Complete", change to D:

#------ 1. Call function from main within script
# python "Python_018_Functions_06.py"

#------ 2. Call functions from cmd line using the -c command argument option
# python -c "import Python_018_Functions_06; Python_018_Functions_06.What_Time_Is_It()"




