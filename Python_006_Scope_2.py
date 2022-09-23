# Title: Python Scope 2 - Using the globals() method
# Author: C. S. Germany 01/15/2022

#Variables declared outside a function are autmatically GLOBAL and available to all functions

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Default scope
def Scope_01():
    
    #Declared in parent function scope
    My_Name = "Carly Salali Germany";

    print("\nA. Variable declared inside a function is no longer available when the function ends:\n");
    print("   Inside function: My_Name = ",My_Name);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#Outside function - My_Name doesn't exist. ERROR in IDE because of SCOPE. My_Name only exists inside of scope of function above
#print("   Inside function: My_Name = ",My_Name); 


# Another example: declaring a variable outside functions in the global namespace
print("\nB. Using the globals() method:\n");

Player_Name = "Twilight Sparkle";

print("   Outside function, GLOBAL Player_Name value is:",Player_Name);

def Change_Global():
    Player_Name = "Rarity";
    print("   Inside function local Player_Name value is:",Player_Name);
    print("   Inside function GLOBAL Player_Name value is:",globals()['Player_Name']);
    print("   Changing GLOBAL from inside function:");
    globals()['Player_Name'] = "Rainbow Dash";

Change_Global();

print("\n   Back outside of function, GLOBAL Player_Name value is now:",Player_Name);



#-----Invocations-----
#Scope_01();

