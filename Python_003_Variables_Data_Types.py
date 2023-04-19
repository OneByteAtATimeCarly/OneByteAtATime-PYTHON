#Title: Python Programming 003 - Variables and Data Types
#Author: Carly S. Germany
#Created: 01/15/2022
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Implicitly declaring variables
def Variables_01():
    #To specify the data type of a variable, CAST it to a specific type
    x = "444";    # x will be STRING "444"
    y = 444;      # y will be INTEGER 444
    z = 444.13;   # z will be FLOAT 444.0

    print("\nA. IMPLICITLY setting the data type of a variable (Python chooses):\n");
    print("    x = ",x,"      TYPE:",type(x));
    print("    y = ",y,"      TYPE:",type(y));
    print("    z = ",z,"   TYPE:",type(z));
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 





#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Explicitly declaring variables
def Variables_02():
    #To specify the data type of a variable, CAST it to a specific type
    x = str(444)    # x will be STRING "444"
    y = int(444)    # y will be INTEGER 444
    z = float(444)  # z will be FLOAT 444.0

    print("\nB. EXPLICITLY setting the data type of a variable (You choose):\n");
    print("    x = ",x,"     TYPE:",type(x));
    print("    y = ",y,"     TYPE:",type(y));
    print("    z = ",z,"   TYPE:",type(z));
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#Integer and Float variables can be used in expressions
def Variables_03():
    
    x = 42
    y = 7
    z = 444;
    INT_RESULT = x * y * z;

    a = 3.14;
    b = 9.543;
    c = 10.672;
    FLOAT_RESULT = a * b * c;

    print("\nC. Using variables in an expression:\n");
    print("    x(",x,") * y(",y,") * z(",z,") = INT_RESULT(",INT_RESULT,").",sep='');
    print("    a(",a,") * b(",b,") * c(",c,") = FLOAT_RESULT(",FLOAT_RESULT,").",sep='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Concatenating string variables
def Variables_04():

    First_Name = "Carly";
    Middle_Name = "Salali";
    Last_Name = "Germany";
    Full_Name = First_Name + " " + Middle_Name + " " + Last_Name;

    print("\nD. Concatenating string variables together:\n");
    print("   First Name:",First_Name,"\n   Middle Name:",Middle_Name,"\n   Last Name:",Last_Name);
    print("   Full Name:",Full_Name);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#Casting One Variable Data Type to Another
MyAge = 42;
MyTemperature = 98.5638;

#print("\nMy age is",MyAge);
#print("\nMy temperature is",MyTemperature);

#Code below creates: TypeError: can only concatenate str
#print("\nMy age is " + MyAge,sep='');
#print("\nMy temperature is " + MyTemperature,sep='');

#To concatenate int and float variables to a string we must implement type-casting
print("\nMy age is " + str(MyAge),sep='');
print("\nMy temperature is " + str(MyTemperature),sep='');

#----------------------------------------------------------------------------------------------------------------------------------------------------------------


#-----Invocations-----
Variables_01();
Variables_02();
Variables_03();
Variables_04();




