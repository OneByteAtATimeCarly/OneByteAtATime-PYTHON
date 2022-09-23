# Title: Project - FizzBuzz
# Author: C. S. Germany 01/06/2022 


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# range() function returns sequence of numbers starting from 0 (by default) and increments by 1 (by default) and stops before a specified number.
# Syntax: range(start, stop, step)
def Fizz_Buzz():
    import random;
    from os import system;
    system("cls"); 

    for x in range(1,101,1):
        print("Current # = ",x,end='');
        if(x % 3 == 0 and x % 5 == 0):
           print(" Divisible by BOTH 3 and 5 : FIZZBUZZ");
        elif(x % 3 == 0):
             print(" Divisible by 3 : FIZZ");
        elif(x % 5 == 0):
             print(" Divisible by 5 : BUZZ");   
        else:
              print();  
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  


Fizz_Buzz();
