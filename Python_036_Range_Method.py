# Title: Python Range Method 
# Author: C. S. Germany 01/15/2022 

# Syntax = range(start, stop, step)

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number. EXAMPLE:
# x = range(6)
# for n in x:
#  print(n);


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Create sequence of numbers from 0 to 5. Starts at 0, not 1. Fencepost. Also, only 1 argument specified so start at 0 assumed. 
def Range_01():
    x = range(6);
    for n in x:
        print(n);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Create sequence of numbers from 440 to 444. Here Start and Stop are specified. 
def Range_02():
    x = range(440,445);
    for n in x:
        print(n);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Create sequence of numbers from 440 to 444. Here Start and Stop are specified as well as Step. So starts at 1, counts by 2's to give odd number between 1 and 10.
def Range_03():
    x = range(1,10,2);
    for n in x:
        print(n);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Create sequence of numbers from 440 to 444. Here Start and Stop are specified as well as Step. So starts at 1, counts by 2's to give even number between 1 and 10.
def Range_04():
    x = range(0,10,2);
    for n in x:
        print(n);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#-----Invocations-----
#Range_01();
#Range_02();
#Range_03();
Range_04();

