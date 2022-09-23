# Title: Project - Prime Numbers
# Author: C. S. Germany 01/06/2022



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#Prime Numbers - Using a FLAG
def Prime_Numbers1():
    import random;
    from os import system;
    system("cls");

    print("\nPrime Numbers 1.0");

    Target_Number = int(input("Please enter a number: "));
    
    FLAG = False;

    #Prime numbers are greater than 1
    if Target_Number > 1:
       #check for factors
       for i in range(2, Target_Number):
           if (Target_Number % i) == 0:
               #if factor is found, set FLAG to true
               FLAG = True;
               break;

    #check if FLAG is true
    if FLAG:
       print(Target_Number, "is not a prime number");
    else:
         print(Target_Number, "is a prime number");
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#Prime Numbers - Using a for-else loop and range, In For-else loops the "else" clause runs ONLY if we don't BREAK out the for loop.
def Prime_Numbers2():
    import random;
    from os import system;
    system("cls");

    print("\nPrime Numbers 2.0");

    Target_Number = int(input("Please enter a number: "));
    
    #prime numbers are greater than 1
    if Target_Number > 1:
       #check for factors
       for i in range(2,Target_Number):
           if(Target_Number % i) == 0:
              print(Target_Number,"is NOT a prime number.");
              print(i,"times",int(Target_Number/i),"is",Target_Number); #int() method to truncate decimals
              print("Shorthand using // = ",i,"times",Target_Number//i,"is",Target_Number); #// shorthand for int() method to truncate decimals
              break;
       else:
             print(Target_Number,"IS a prime number.");
       
    #if input number is less than or equal to 1, it is not prime
    else:
         print("Number was:",Target_Number,". Numbers <= 1 are NOT prime numbers.");
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#-----Invocations-----
#Prime_Numbers1();
Prime_Numbers2();