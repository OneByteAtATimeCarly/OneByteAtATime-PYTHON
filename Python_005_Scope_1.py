# Title: Python Scope 1 - Different scopes and different ways of handling scope in Python
# Author: C. S. Germany 01/15/2022


#Variables declared outside a function are automatically GLOBAL and available to all functions
My_Name = "Carly Salali Germany";
print("\nOutside all functions: GLOBAL My_Name = ",My_Name);


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Default scope. Variables local to a function take precedence over globals by default
def Scope_0l():
    My_Name = "Your FACE!";
    print("\nA. Inside Scope_0l function. My_Name = ",My_Name);
    print("   Notice by default inside the function, the LOCAL \"My_Name\" variable overrides the GLOBAL \"My_Name\" variable.");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   If a local variable is ABSENT, the global variable is accessed by default
def Scope_02():
    print("\nB. Inside Scope_02 function. My_Name = ",My_Name);
    print("   Notice by default inside the function, if no LOCAL My_Name exists, GLOBAL My_Name is accessed.");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#-----Invocations-----
#Scope_0l();
Scope_02();

