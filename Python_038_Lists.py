# Title: Python Lists (Arrays)
# Author: C. S. Germany 01/15/2022

# CHANGEABLE.  YES. You CAN both [ADD] and [REMOVE] items in a List using the methods append() and remove(). 
# INDEXED:     YES. First item = [0], second item = [1] and so on.
# ORDERED:     YES. Items have a defined order, and that order will not change. If you add new items to a List they are placed at the end. (some List methods can change order)
# DUPLICATES:  YES. Lists can have items with the same value.
# USE:         To store multiple items in single container.
# SIMILIAR:    Similiar structures in Python are: Tuple, Set, and Dictionary. 
# CREATED:     Created with square braces [  ].
# MULTIPLE:    Unlike C++ arrays, members of a List can be of different data types.
# METHODS:     len(), append(), remove(), extend(), insert(), index(), pop(), clear(), sort(), copy().


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Lists - Instantiating
def Lists_0l():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nA. An entire List object:\n\n  ",MLP_FIM_Main_Chars);
    
    print("\nB. List one item at a time:\n");
    
    Char_Counter = 0;
    for x in MLP_FIM_Main_Chars:
        Char_Counter = Char_Counter + 1;
        print("   ",Char_Counter,". ",x,sep='');

    print("\nC. Accessing one particular element in a List via its index:\n");    
    print("  ","The MLP FIM main character at position 0 is:",MLP_FIM_Main_Chars[0]);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Lists - len() method gives number of objects stored in a List
def Lists_02():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    Num_List_Objects = len(MLP_FIM_Main_Chars);

    print("\n Number of objects in List =",Num_List_Objects);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Unlike TUPLES, you don't have to use a trailing COMMA to create a List with only 1 element. You can see below that BOTH examples are data type class 'list'.
def Lists_03():
    MLP_FIM_Main_Chars_No_Trailing_Comma = ["Twilight Sparkle"];
    MLP_FIM_Main_Chars_With_Trailing_Comma = ["Twilight Sparkle",];

    print("\nData type for \"MLP_FIM_Main_Chars_No_Trailing_Comma\" = ",type(MLP_FIM_Main_Chars_No_Trailing_Comma));
    print("Data type for \"MLP_FIM_Main_Chars_With_Trailing_Comma\" = ",type(MLP_FIM_Main_Chars_With_Trailing_Comma));
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Demonstrating that Python Lists, unlike C++ ARRAYS, can hold multiple different data types. 
# Example: Lists can hold strings, integers and booleans all at once.
# Here we use the format() method and <> to align output into columns.
def Lists_04():
    Disorganized_Chaotic_Loosey_Goosey_Objects_With_Dif_DataTypes = ["Twilight Sparkle",42,True,"Rainbow Dash",444,False];

    print("\nA. Lists can hold multiple different data types, like strings, integers and booleans all at once.:\n\n  ",Disorganized_Chaotic_Loosey_Goosey_Objects_With_Dif_DataTypes);
    
    print("\nB. Lists, displaying one item at a time:\n");
    
    Char_Counter = 0;
    for X in Disorganized_Chaotic_Loosey_Goosey_Objects_With_Dif_DataTypes:
        Char_Counter = Char_Counter + 1;
        MESSAGE1 = "   " + str(Char_Counter) + ". Value: " + str(X);
        MESSAGE2 = "Data Type:" + str(type(X));
        print('{:<35}{:>0}'.format(MESSAGE1,MESSAGE2));

    print("\nC. Accessing one particular element in a List via its index:\n");    
    print("  ","The MLP FIM main character at position 0 is:",Disorganized_Chaotic_Loosey_Goosey_Objects_With_Dif_DataTypes[0]);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Lists are chanageable. No need to convert them to add or remove elements as is the case with Tuples.
# To [ADD] an element to a list, use append(). Adds item to the END of a List.
def Lists_05():
    List_MLP_FIM_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    print("\nA. BEFORE append() members to List:\n\n  ",List_MLP_FIM_Chars);

    List_MLP_FIM_Chars.append("Princess Celestia");
    List_MLP_FIM_Chars.append("Princess Luna");

    print("\nB. AFTER append() members to List:\n\n  ",List_MLP_FIM_Chars);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# To [REMOVE] an element, use remove().
def Lists_06():
    List_MLP_FIM_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie","Princess Celestia","Princess Luna"];
    print("\nA. BEFORE remove() members from List:\n\n  ",List_MLP_FIM_Chars);

    List_MLP_FIM_Chars.remove("Princess Celestia");
    List_MLP_FIM_Chars.remove("Princess Luna");

    print("\nB. AFTER remove() members from List:\n\n  ",List_MLP_FIM_Chars);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# To [INSERT] an element at a SPECIFIED index instead of the end, use insert().
def Lists_07():
    List_MLP_FIM_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie","Princess Celestia","Princess Luna"];
    print("\nA. BEFORE insert() members from List:\n\n  ",List_MLP_FIM_Chars);

    List_MLP_FIM_Chars.insert(0,"Princess Celestia"); #insert at beginning
    List_MLP_FIM_Chars.insert(4,"Princess Luna"); #insert before 4th element

    print("\nB. AFTER insert() members from List:\n\n  ",List_MLP_FIM_Chars);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#8. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Indexing a list with -1 wraps around to the last element in the list, -2 to the second to last and so on
def Lists_08():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    print("\n   At index -1 is the value:",MLP_FIM_Main_Chars[-1]);
    print("   At index -2 is the value:",MLP_FIM_Main_Chars[-2]);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#9. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# RANGE: You can specify a range for a List index using [2:6]. 
# Remember when indexing List, Tuples and Arrays that everything starts with 0, not 1. Be mindful of the fencepost error.
# Leaving start value out like [:3] returns from beginning (index 0) up to (index 2). Remember things start with 0.
# Leaving stop value out like [4:] returns from beginning (index 4) up to end (index 7). Remember things start with 0. 
def Lists_09():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie","Princess Celestia","Princess Luna"];
    print("\n   Number of elements in List is:",len(MLP_FIM_Main_Chars));
    print("   Index range [2:6] is:",MLP_FIM_Main_Chars[2:6]);
    print("   Index range [4:7] is the value:",MLP_FIM_Main_Chars[4:7]);
    print("   Index range [0:3] is the value:",MLP_FIM_Main_Chars[0:3]);
    print("   Index range [6:8] is the value:",MLP_FIM_Main_Chars[6:8]);
    print("   Index range [:3] is the value:",MLP_FIM_Main_Chars[:3]);
    print("   Index range [4:] is the value:",MLP_FIM_Main_Chars[4:]);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 





#10. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Can check if object exists in List using "in" keyword.
def Lists_10():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie","Princess Celestia","Princess Luna"];

    print("\nSearching for items in a List:\n");

    if("Rainbow Dash" in MLP_FIM_Main_Chars):
       print("    Yes! Sonic Rain Boom!");
    else: print("NOT in the List."); 

    if("Pinkie Pie" in MLP_FIM_Main_Chars):
        print("    Yes! Party time!");
    else: print("NOT in the List."); 

    if("Supercalafrajalistic" in MLP_FIM_Main_Chars):
        print("Yes! Party time!");    
    else: print("    NOT in the List.");  
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 





#11. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# EXTEND: the extend() method appends elements from one List to another. 
# This method works with any iterable object in Python. So can be used with: Tuples, Sets and Dictionaries too.
def Lists_11():
    List_MLP_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    List_MLP_Main_Antagonists = ["Discord","Lord Tirak","Nightmare Moon","King Sombra","Queen Chrysalis","Sonata Dusk"];

    List_MLP_Main_Chars.extend(List_MLP_Main_Antagonists);

    print("\nExtended characters adding List to List:\n   ",List_MLP_Main_Chars);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#12. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# EXTEND: the extend() method appends elements from one List to another. Also can append a Tuple to a List.
# This method works with any iterable object in Python. So can be used with: Tuples, Sets and Dictionaries too.
def Lists_12():
    List_MLP_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    Tuple_MLP_Main_Antagonists = ("Discord","Lord Tirak","Nightmare Moon","King Sombra","Queen Chrysalis","Sonata Dusk");

    List_MLP_Main_Chars.extend(Tuple_MLP_Main_Antagonists);

    print("\nExtended characters adding Tuple to List:\n   ",List_MLP_Main_Chars);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#13. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# JOINING: Joining Lists together (concatenation)
def Lists_13():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    MLP_FIM_Main_Antagonists = ["Discord","Lord Tirak","Nightmare Moon","King Sombra","Queen Chrysalis","Sonata Dusk"];
    
    print("\nJoining two Tuples together.\n");
    MLP_FIM_Full_Cast = MLP_FIM_Main_Chars + MLP_FIM_Main_Antagonists;

    print("\nFull cast:",MLP_FIM_Full_Cast);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#14. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# UNPACKING: Lists can be UNPACKED into individual variables.
def Lists_14():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    print("\nUnpacking = retrieving each value.\n");

    for x in MLP_FIM_Main_Chars:
        print(x);    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 





#15. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# MODIFYING: The values of objects in a list can be modified and manipulated by accessing the List's index.
def Lists_15():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nBEFORE modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);

    MLP_FIM_Main_Chars[0] = "Discord"; # Replace single value = Twilight Sparkle with Discord

    print("\nAFTER modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#16. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# MODIFYING: To modify a RANGE of List elements at once, define a range like [0:2] and insert a new List into it. Example: 
def Lists_16():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nBEFORE modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);

    MLP_FIM_Main_Chars[0:2] = ["Discord","Lord Tirek"]; # Replace range of multiple values at once

    print("\nAFTER modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#17. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# MODIFYING: When specifying a RANGE, if you insert MORE elements into the List than existed previously, the list is expanded and the elements shifted in place
# to accomodare your new elements as if you had added them with the append() method. Example: 
def Lists_17():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nBEFORE modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);

    MLP_FIM_Main_Chars[0:2] = ["Discord","Lord Tirek","King Sombra","Queen Chrysalis","Sonata Dusk"]; # Replace range of multiple values at once

    print("\nAFTER modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#18. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# insert() Method: Inserts an item at the specified index without replacing existing values. Example:
def Lists_18():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nBEFORE modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);

    MLP_FIM_Main_Chars.insert(2,"Discord");

    print("\nAFTER modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#19. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# pop() Method: Removes an item at the specified index. If called without specifying index, pop() removes last element in List. Example:
def Lists_19():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nBEFORE modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);

    MLP_FIM_Main_Chars.pop(2); #Remove 3rd element in List indexed by 2

    print("\nAFTER modifying List (pop index 2):");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);

    MLP_FIM_Main_Chars.pop(); #Remove last element in List since index not specified

    print("\nAFTER modifying List (pop no arguments):");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#20. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# del() Method: Removes List element at specified index. If index not specified, deleted entire list. Example:
def Lists_20():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nBEFORE modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);

    del MLP_FIM_Main_Chars[2]; #deletes only 2nd element in List

    print("\nAFTER modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);

    del MLP_FIM_Main_Chars; #deletes the ENTIRE List
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#21. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# clear() Method: Clears all elements in a List without deleting the List. Example:
def Lists_21():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nBEFORE modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);

    MLP_FIM_Main_Chars.clear(); 

    print("\nAFTER modifying List:");
    print("Number of elements in List =",len(MLP_FIM_Main_Chars),".");
    print(MLP_FIM_Main_Chars);

    del MLP_FIM_Main_Chars; #deletes the ENTIRE List
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#22. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# LOOPING 1: - Iterating through a list without using range( 0and len(). If using this method, it simplifies List looping. 
# But to count the List elements you must use a separate variable as an accumulator.
def Lists_22():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nLooping a List. One item at a time. With an accumulator:\n");
    
    Char_Counter = 0;
    for x in MLP_FIM_Main_Chars:
        Char_Counter = Char_Counter + 1;
        print("   ",Char_Counter,". ",x,sep='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#23. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# LOOPING 2: - Iterating through a list using each element's index number and the range() and len() functions.
# This variation makes Python List looping work the way looping Arrays works in C++, Java and PowerShell. 
# You can use the index value and add 1 to offset the "off-by-one" issue to number, and access List element value directly by its index.  
def Lists_23():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nLooping a List. One item at a time. Using range(), len() and index number:\n");
    
    for x in range(len(MLP_FIM_Main_Chars)):
        print("   ",(x+1),". ",MLP_FIM_Main_Chars[x],sep='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#24. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# LOOPING 3: - Iterating through a list using a WHILE TRUE loop.
def Lists_24():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    print("\nLooping a List. Using a WHILE TRUE loop and a sentinel value:\n");
    
    Sentinel_Value = 0; #used to determine when to exit while true loop

    while Sentinel_Value < len(MLP_FIM_Main_Chars):
          print("   ",(Sentinel_Value+1),". ",MLP_FIM_Main_Chars[Sentinel_Value],sep='');
          Sentinel_Value = Sentinel_Value + 1;
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#25. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# SHORTHAND 1: - Short-hand interation through Lists.
# Syntax: Result_List = [expression for item in iterable if condition == True]. Just iterates through list if the condition is omitted, as below.
def Lists_25():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    print("\nShort-hand iteration through List objects:\n");
    
    [print(x) for x in MLP_FIM_Main_Chars];
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#26. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# SHORTHAND 2: - Short-hand interation through Lists objects matching to a specified value. Compare the processes below. Both do the same thing.
# But the normal method of matching items in a List using a for loop is 4 lines of code. Whereas the shorthand methos which does the same is only 1 line of code.
def Lists_26():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    
    print("\nA. The normal way to iterate through List objects matching to a specified value.");
    print("\n   Looking for all MLP characters with letter \"y\" in their name. (4 lines of code using for loop)");

    Match_Results_Normal = [];
    for x in MLP_FIM_Main_Chars:
        if "y" in x:
           Match_Results_Normal.append(x);

    print("   Normal match results:",Match_Results_Normal);


    print("\nB. Short-hand iteration through List objects matching to a specified value.");
    print("\n   Looking for all MLP characters with letter \"y\" in their name. (1 line of code in shorthand)");
    
    Match_Results_Shorthand = [z for z in MLP_FIM_Main_Chars if "y" in z];

    print("   Shorthand match results:",Match_Results_Shorthand);

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#27. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# SHORTHAND 3: - Matching another condition type
def Lists_27():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    
    print("\nA. The entire List:\n  ",MLP_FIM_Main_Chars);
    
    Match_Results_Shorthand = [m for m in MLP_FIM_Main_Chars if m != "Fluttershy"];

    print("\nB. Items in List that match the condition:\n  ",Match_Results_Shorthand);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#28. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# SHORTHAND 4: - Using range() to create and populate a List
def Lists_28():
    
    List_Numbers = [A for A in range(10)];

    print("\nList of 10 numbers:",List_Numbers);

    List_Even_Numbers = [B for B in range(11) if B % 2 == 0];

    print("\nList of EVEN numbers:",List_Even_Numbers);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#29. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# SHORTHAND 5: - Setting all string chars in a List to uppercase
def Lists_29():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    
    print("\nBEFORE:",MLP_FIM_Main_Chars);

    Upper_MLP_FIM_Main_Chars = [C.upper() for C in MLP_FIM_Main_Chars];

    print("\nAFTER:",Upper_MLP_FIM_Main_Chars);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#30. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# SHORTHAND 6: - Setting all elements in a List to a specified value
def Lists_30():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    
    print("\nBEFORE:",MLP_FIM_Main_Chars);

    Modified_MLP_FIM_Main_Chars = ["BLANK" for D in MLP_FIM_Main_Chars];

    print("\nAFTER:",Modified_MLP_FIM_Main_Chars);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#31. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# SHORTHAND 7: - Setting all elements in a List to a specified value
def Lists_31():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    
    print("\nBEFORE:",MLP_FIM_Main_Chars);

    Modified_MLP_FIM_Main_Chars = [E if E == "Fluttershy" else "NOT Fluttershy" for E in MLP_FIM_Main_Chars];

    print("\nAFTER:",Modified_MLP_FIM_Main_Chars);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#32. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# sort() method: - Sorts a List alphanumerically and ascending by default. Example: alphanumerically ascending strings.
def Lists_32():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    
    print("\nBEFORE: (not sorted)",MLP_FIM_Main_Chars);

    MLP_FIM_Main_Chars.sort();

    print("\nAFTER: (sorted)",MLP_FIM_Main_Chars);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#33. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# sort() method: - Sorts numbers too, like a built-in Bubble sort! :-) Example:
def Lists_33():
    List_AGES = [205,96,444,37,505,29,102];
    
    print("\nBEFORE: (not sorted)",List_AGES);

    List_AGES.sort();

    print("\nAFTER: (sorted)",List_AGES);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#34. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# sort() method: - To specify a descending sort, include argument (reverse = True) Example:
def Lists_34():
    
    List_AGES = [205,96,444,37,505,29,102];  
    print("\nBEFORE: (not sorted)",List_AGES);
    List_AGES.sort(reverse = True);
    print("AFTER: (reverse sorted)",List_AGES);

    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];
    print("\nBEFORE: (not sorted)",MLP_FIM_Main_Chars);
    MLP_FIM_Main_Chars.sort(reverse = True);
    print("AFTER: (reverse sorted)",MLP_FIM_Main_Chars);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#35. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# COPYING: - You cannot copy a List using: List2 = List1. Doing this doesn't copy the List to another. 
# Rather it effectively sets up List2 to be a C++ type POINTER that references List1, so any changes made to List2 are made to List1.
# The copy() method will let you copy an entire List to another as a separate duplicate, element by element.

def Lists_35():
    MLP_FIM_Main_Chars = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"];

    print("\nMLP_FIM_Main_Chars:",MLP_FIM_Main_Chars);

    COPY_MLP_FIM_Main_Chars = MLP_FIM_Main_Chars.copy();

    print("COPY_MLP_FIM_Main_Chars:",COPY_MLP_FIM_Main_Chars);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



# Summary of List methods:
# append()	 Adds an element at the end of the list
# clear()	 Removes all the elements from the list
# copy()	 Returns a copy of the list
# count()	 Returns the number of elements with the specified value
# extend()	 Add the elements of a list (or any iterable), to the end of the current list
# index()	 Returns the index of the first element with the specified value
# insert()	 Adds an element at the specified position
# pop()	     Removes the element at the specified position
# remove()	 Removes the item with the specified value
# reverse()	 Reverses the order of the list
# sort()	 Sorts the list



#-----Invocations-----
#Lists_0l();
#Lists_02();
#Lists_03();
#Lists_04();
#Lists_05();
#Lists_06();
#Lists_07();
#Lists_08();
#Lists_09();
#Lists_10();
#Lists_11();
#Lists_12();
#Lists_13();
#Lists_14();
#Lists_15();
#Lists_16();
#Lists_17();
#Lists_18();
#Lists_19();
#Lists_20();
#Lists_21();
#Lists_22();
#Lists_23();
#Lists_24();
#Lists_25();
#Lists_26();
#Lists_27();
#Lists_28();
#Lists_29();
#Lists_30();
#Lists_31();
#Lists_32();
#Lists_33();
#Lists_34();
Lists_35();
