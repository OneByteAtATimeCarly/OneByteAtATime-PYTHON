# Title: Python Scope 2 - Using the globals() method
# Author: C. S. Germany 01/15/2022

#Variables declared outside a function are autmatically GLOBAL and available to all functions

#Another example: declaring a variable outside functions in the global namespace
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

