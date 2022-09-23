# Title: Project - Add Even Numbers
# Author: C. S. Germany 01/06/2022


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# range() function returns sequence of numbers starting from 0 (by default) and increments by 1 (by default) and stops before a specified number.
# Syntax: range(start, stop, step)
def Add_Even_Numbers():
    import random;
    from os import system;
    system("cls"); 

    Accumulator = 0;

    for x in range(2,100,2):
        print(x,"+ ",end='');
        Accumulator = Accumulator + x;

    print("\n\n  Total sum of all numbers is:",Accumulator);    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------   


Add_Even_Numbers();

