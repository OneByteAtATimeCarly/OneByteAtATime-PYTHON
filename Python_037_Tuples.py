# Title: Python Tuples 
# Author: C. S. Germany 01/15/2022

# CHANGEABLE.  NO. UNCHANGEABLE. Cannot [ADD] or [REMOVE] items once created. To do so, you must convert a Tuple to a List first.
# INDEXED:     YES. First item = [0], second item = [1] and so on.
# ORDERED:     YES. Items have a defined order, and that order will not change. If you add new items to a List they are placed at the end. (some List methods can change order)
# DUPLICATES:  YES. Tuples can have items with the same value.
# USE:         To store multiple items in single container.
# SIMILIAR:    Similiar structures in Python are: List, Set, and Dictionary. 
# CREATED:     Created with parentheses (  ).
# MULTIPLE:    Unlike C++ arrays, members of a Tuple can be of different data types.
# METHODS:     len(), count(), index()


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Tuples - Instantiating
def Tuples_0l():
    Tuple_MLP_Main_Chars = ("Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie");

    print("\nA. An entire Tuple object:\n\n  ",Tuple_MLP_Main_Chars);
    
    print("\nB. Tuple one item at a time:\n");
    
    Char_Counter = 0;
    for x in Tuple_MLP_Main_Chars:
        Char_Counter = Char_Counter + 1;
        print("   ",Char_Counter,". ",x,sep='');

    print("\nC. Accessing one particular element in a Tuple via its index:\n");    
    print("  ","The MLP FIM main character at position 0 is:",Tuple_MLP_Main_Chars[0]);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Tuples - len() method gives number of objects stored in a Tuple
def Tuples_02():
    MLP_FIM_Main_Chars = ("Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie");

    Num_Tuple_Objects = len(MLP_FIM_Main_Chars);

    print("\n Number of objects in Tuple =",Num_Tuple_Objects);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Unlike ARRAYS, to create a Tuple with only ONE item you must leave it with a trailing comma like below. If not? It's not a Tuple.
def Tuples_03():
    MLP_FIM_Main_Chars_No_Trailing_Comma = ("Twilight Sparkle");
    MLP_FIM_Main_Chars_With_Trailing_Comma = ("Twilight Sparkle",);

    print("\nData type for \"MLP_FIM_Main_Chars_No_Trailing_Comma\" = ",type(MLP_FIM_Main_Chars_No_Trailing_Comma));
    print("Data type for \"MLP_FIM_Main_Chars_With_Trailing_Comma\" = ",type(MLP_FIM_Main_Chars_With_Trailing_Comma));
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Demonstrating that Python Tuples, unlike C++ ARRAYS, can hold multiple different data types. 
# Example: Tuples can hold strings, integers and booleans all at once.
# Here we use the format() method and <> to align output into columns.
def Tuples_04():
    Disorganized_Chaotic_Loosey_Goosey_Objects_With_Dif_DataTypes = ("Twilight Sparkle",42,True,"Rainbow Dash",444,False);

    print("\nA. Tuples can hold multiple different data types, like strings, integers and booleans all at once.:\n\n  ",Disorganized_Chaotic_Loosey_Goosey_Objects_With_Dif_DataTypes);
    
    print("\nB. Tuple one item at a time:\n");
    
    Char_Counter = 0;
    for X in Disorganized_Chaotic_Loosey_Goosey_Objects_With_Dif_DataTypes:
        Char_Counter = Char_Counter + 1;
        MESSAGE1 = "   " + str(Char_Counter) + ". Value: " + str(X);
        MESSAGE2 = "Data Type:" + str(type(X));
        print('{:<35}{:>0}'.format(MESSAGE1,MESSAGE2));

    print("\nC. Accessing one particular element in a Tuple via its index:\n");    
    print("  ","The MLP FIM main character at position 0 is:",Disorganized_Chaotic_Loosey_Goosey_Objects_With_Dif_DataTypes[0]);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# As Tuples are immutable/unchanageable, you must convert them to a List and then back again to add or remove elements.
def Tuples_05():
    Tuple_MLP_FIM_Chars = ("Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie");
    print("\nA. Tuple before conversion and adding member:\n\n  ",Tuple_MLP_FIM_Chars);

    List_MLP_FIM_Chars = list(Tuple_MLP_FIM_Chars);
    List_MLP_FIM_Chars.append("Princess Celestia");
    Tuple_MLP_FIM_Chars = tuple(List_MLP_FIM_Chars);

    print("\nB. Tuple after conversion and adding member:\n\n  ",Tuple_MLP_FIM_Chars);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# UNPACKING: Tuples can be UNPACKED into individual variables.
def Tuples_06():
    MLP_FIM_Main_Chars = ("Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie");

    (p1, p2, p3, p4, p5, p6) = MLP_FIM_Main_Chars;

    print("p1 =",p1);
    print("p2 =",p2);
    print("p3 =",p3);
    print("p4 =",p4);
    print("p5 =",p5);
    print("p6 =",p6);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# UNPACKING: Tuples can be UNPACKED into individual variables.
def Tuples_07():
    MLP_FIM_Main_Chars = ("Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie");
    print("\nUnpacking = retrieving each value.\n");

    for x in MLP_FIM_Main_Chars:
        print(x);    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#8. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# JOINING: Joining Tuples together
def Tuples_08():
    MLP_FIM_Main_Chars = ("Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie");
    MLP_FIM_Main_Antagonists = ("Discord","Lord Tirak","Nightmare Moon","King Sombra","Queen Chrysalis","Sonata Dusk");
    
    print("\nJoining two Tuples together.\n");
    MLP_FIM_Full_Cast = MLP_FIM_Main_Chars + MLP_FIM_Main_Antagonists;

    print("\nFull cast:",MLP_FIM_Full_Cast);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#9. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# MULTIPLYING: Multiplying Tuples together
def Tuples_09():
    MLP_FIM_Main_Chars = ("Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie");
    
    print("\nBEFORE: Tuple is:\n",MLP_FIM_Main_Chars);
    RESULT = MLP_FIM_Main_Chars * 2;
    print("\nAFTER: (*2) Tuple is:\n",RESULT);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#10. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# The count() method returns number of times a specified value exists in a Tuple. 
def Tuples_10():
    MLP_FIM_Main_Chars = ("Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie");
    Num_Rainbow_Dashes = MLP_FIM_Main_Chars.count("Rainbow Dash");
    print("Number of Rainbow Dashes in MLP = ",Num_Rainbow_Dashes);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#11. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# The index() method returns index of 1st occurence of a specified value that exists in a Tuple. 
def Tuples_11():
    MLP_FIM_Main_Chars = ("Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie");
    Index_of_Rainbow_Dash = MLP_FIM_Main_Chars.index("Rainbow Dash");
    print("Index of Rainbow Dash = ",Index_of_Rainbow_Dash);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



# Summary of Tuple methods:
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found


#-----Invocations-----
#Tuples_0l();
#Tuples_02();
#Tuples_03();
#Tuples_04();
#Tuples_05();
#Tuples_06();
#Tuples_07();
#Tuples_08();
#Tuples_09();
#Tuples_10();
Tuples_11();
