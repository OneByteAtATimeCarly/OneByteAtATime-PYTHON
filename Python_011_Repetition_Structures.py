# Python Repetition Structures
# Author: C. S. Germany 01/15/2022

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# A basic Python for loop
def Repetition_Structures_0l():

    Main_Char_Array = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nA. Loop method 1");
    Counter = 0;

    for W in Main_Char_Array:
        Counter = Counter + 1;
        print("   ",Counter,". ",W,sep='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# A Python for loop using range() and len() to make it syntactically more like C++,Java and POSH. 
# Note that you can use index and subscript array syntax with this type.
def Repetition_Structures_02():

    Main_Char_Array = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nB. Loop method 2 using range() and len()");

    for X in range(len(Main_Char_Array)):
        print("   ",(X+1),". ",Main_Char_Array[X],sep='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Using range() with for() to approximate loop syntax and behavior from C++, Java and Powershell

def Repetition_Structures_03():

    print("\nC. Using range() with for() to approximate loop syntax and behavior from C++, Java and Powershell.");
    print("   Here we want to count from 1 to 10. But note that the end of range is 1 less than desired.");
    print("   The range beginning is 1, but for the range end, we need make it 11, or to add 1 to 10.");

    for X in range(1,(10+1)):
        print("   X = ",X,"");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# While true loop
def Repetition_Structures_04():

    Main_Char_Array = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nD. Loop method 3 - a While-True loop");

    x = 0;

    while(x < len(Main_Char_Array)):
          print("   ",(x+1),". ",Main_Char_Array[x],sep='');
          x = x + 1;
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Another While true loop
def Repetition_Structures_05():

    Main_Char_Array = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nE. Loop method 4 - Another While-True loop");

    x = 0;

    while(x < 3):
          print("   ",(x+1),". ",Main_Char_Array[x],sep='');
          x += 1;
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# The break statement
def Repetition_Structures_06():

    Main_Char_Array = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nF. While-True loop with BREAK");

    x = 0;

    while(x < 6):
          print("   ",(x+1),". ",Main_Char_Array[x],sep='');
          if(x == 2):
             print("   Sentinel value attained! Breaking out of while true loop now."); 
             break;
          x += 1;
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# The continue statement. Causes loop to go to next iteration and skip code below it.
def Repetition_Structures_07():

    Main_Char_Array = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nG. While-True loop with CONTINUE");

    x = 0;

    while(x < 6):
          print("   ",(x+1),". ",Main_Char_Array[x],sep='');
          if(x == 2):
             print("   Target value triggered! Continuing with while true loop now. Skips code below so becomes infinite loop."); 
             continue;
          x += 1;
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#8. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Combining a while-true loop with else
def Repetition_Structures_08():

    Main_Char_Array = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nH. While-True loop with ELSE");

    x = 0;

    while(x < 6):
          print("   ",(x+1),". ",Main_Char_Array[x],sep='');
          x += 1;
    else: print("   Sentinel value attained so exited while-true loop.");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#9. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# There is no Do-While loop structure in Python
# We can approximate the structure, however, with a While-True loop
def Repetition_Structures_09():

    Main_Char_Array = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nI. Unlike C++, Java and Powershell, there is not Do-While loop structure in Python.");
    print("   You can, however, approximate the functionaility of a Do-While loop.");
    print("   To do so, just use a While-True loop. Set the initial condition to be TRUE.");
    print("   Then be sure you execute code in the loop BEFORE you check for the condition.\n");

    Pony_Count = len(Main_Char_Array);
    Pony_Counter = 0;

    while True:
          print("   ",(Pony_Counter+1),". ",Main_Char_Array[Pony_Counter],sep='');
          #Note: We have to offset for the fencepost/off-by-1 issue by subtracting 1 from Pony_Count
          if(Pony_Counter >= (Pony_Count-1)): 
             break;
          Pony_Counter += 1;
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#-----Invocations-----
#Repetition_Structures_0l();
#Repetition_Structures_02();
#Repetition_Structures_03();
#Repetition_Structures_04();
#Repetition_Structures_05();
#Repetition_Structures_06();
#Repetition_Structures_07();
#Repetition_Structures_08();
Repetition_Structures_09();



