# Title: Python Scope 4 - Using the globals keyword
# Author: C. S. Germany 01/15/2022

#Variables declared outside a function are autmatically GLOBAL and available to all functions

#Using the "global" keyword


#1. Define Function----------------------------------------------------------------------------------------------------------------------------------------------
#   Default scope
def Scope_01():
    #Declared in parent function scope
    global My_Name;
    My_Name = "Carly Salali Germany";
    print("\n   A. Inside function: My_Name = ",My_Name);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#2. Call Function----
Scope_01();


#3. Access a variable declared global inside a function when outside the function
print("   B. Outside function: My_Name = ",My_Name);

