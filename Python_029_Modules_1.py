# Title: Python Modules 1
# Author: C. S. Germany 01/15/2022

# You can create your own modules and import them in Python.
# To do so, just save the code with a ".py" extension just as you would any other file.

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   This function is in a file saved as "Python_030_Modules_2_Synchronicity.py"
#   
#   def What_Time_Is_It():
#       print("   The time is 4:44"); 
#
#   The_Name = "Anonymous"; 
#   The_Age = 52;
#   The_Class = "Unicorn";   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


import Python_030_Modules_2_Synchronicity;

print("\nA. Import entire module and list all members with dir()");
print("  ",dir(Python_13_Synchronicity))

print("\nB. Call a function from an imported module");
Python_13_Synchronicity.What_Time_Is_It();

print("\nC. Import Module and rename it as an instance and call function from module");
import Python_13_Synchronicity as SYNC;
SYNC.What_Time_Is_It();

print("\nD. Access data members from an Imported Module");
T_Name = Python_13_Synchronicity.The_Name;
T_Age = Python_13_Synchronicity.The_Age;
T_Class = Python_13_Synchronicity.The_Class;
print("   Name:",T_Name);
print("   Age:",T_Age);
print("   Class:",T_Class);

