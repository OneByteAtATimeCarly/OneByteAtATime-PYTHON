# Scope: Different scopes and different ways of hansdling scope in Python

#Variables declared outside a function are autmatically GLOBAL and available to all functions
My_Name = "Carly Salali Germany";
print("\nOutside all functions: GLOBAL My_Name = ",My_Name);

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Default scope. Variables local to a funciton take precedence over glbals by default
def Scope_0l():
    My_Name = "Your FACE!";
    print("\nA. Inside Scope_0l function. My_Name = ",My_Name);
    print("   Notice by default inside the function, the LOCAL My_Name overrides the GLOBAL My_Name.");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   If a local variable is absent, the global variable is accessed by default
def Scope_02():
    print("\nB. Inside Scope_02 function. My_Name = ",My_Name);
    print("   Notice by default inside the function, if no LOCAL My_Name exists, GLOBAL My_Name is accessed.");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#-----Invocations-----
Scope_0l();
Scope_02();

