# Title: Python Functions 4 - Command line part 1
# Author: C. S. Germany 01/15/2022

# Python provides a getopt module that helps you parse command-line options and arguments.
# Basic command line script in GLOBAL namespace

import sys;
print("\nNumber of arguments:", len(sys.argv),"arguments.");
print("Argument List:", str(sys.argv));
print("\nBreak it down:");

print("Path and script name:",sys.argv[0]);
print("Arguments Passed In:",((len(sys.argv))-1),"\n");

#Note: Skip element 0 since that's file and path and start with 1
for x in range(1,(len(sys.argv))):
    print("   ",x,". ",str(sys.argv[x]),sep='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#-----Invocations-----

# To run, do not hit "debug" or F5. Rather, from a CMD PROMPT go the the sctipt directory and run from cmd line: 
# python "d:\Bills\Carlys_Python_Scripts_2022\Programming_CONSOLE\Python_10_Functions_D.py" Pony1 Pony2 Pony3 Pony4 Pony5 Pony6


