# Title: Python Sets
# Author: C. S. Germany 01/15/2022

# CHANGEABLE.  NO. You can not change the value of an item in a Set. But you can [ADD] and [REMOVE] items in a Set using the methods append() and remove(). 
# INDEXED:     NO. No indexing for a Set.
# ORDERED:     NO. Items are randomly rodered in a Set. They have no specific order and will randomly display.
# DUPLICATES:  NO. Sets can NOT have any two items with the same value.
# USE:         To store multiple items in single container.
# SIMILIAR:    Similiar structures in Python are: Tuple, List, and Dictionary. 
# CREATED:     Created with curly brackets { }
# MULTIPLE:    Unlike C++ arrays, members of a Set can be of different data types.
# METHODS:     len(), append(), remove(), extend(), insert(), index(), pop(), clear(), sort(), copy().


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Sets - Instantiating. Notice that when you display the items in the Set, they do not display in an ORDERED fashion. 
def Sets_0l():
    Set_MLP_FIM_Main_Chars = {"Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"};
    print(Set_MLP_FIM_Main_Chars);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Sets - Instantiating. Notice that when you display the items in the Set, they do not display in an ORDERED fashion. 
def Sets_02():
    Set_MLP_FIM_Main_Chars = {"Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"};
    print("\n  Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Sets - Instantiating. Notice that when you display the items in the Set, they do not display in an ORDERED fashion. 
def Sets_03():
    Set_Disorganized_Objects_With_Dif_DataTypes = {"Twilight Sparkle",42,True,"Rainbow Dash",444,False};

    print("\nA. Sets can hold multiple different data types, like strings, integers and booleans all at once.:\n\n  ",Set_Disorganized_Objects_With_Dif_DataTypes);
    
    print("\nB. A Set one item at a time:\n");
    
    Char_Counter = 0;
    for X in Set_Disorganized_Objects_With_Dif_DataTypes:
        Char_Counter = Char_Counter + 1;
        MESSAGE1 = "   " + str(Char_Counter) + ". Value: " + str(X);
        MESSAGE2 = "Data Type:" + str(type(X));
        print('{:<35}{:>0}'.format(MESSAGE1,MESSAGE2));
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# add() Method - This methos can only add a SINGLE ITEM to a Set. It can NOT add a Set to another Set. To do that, use the update() method.
def Sets_04():
    Set_MLP_FIM_Main_Chars = {"Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"};
    
    print("\n  BEFORE: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));

    Set_MLP_FIM_Main_Chars.add("Princess Celestia");
    Set_MLP_FIM_Main_Chars.add("Princess Luna");

    print("\n  AFTER: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# update() Method - This method can add an entire Set to another Set. It can also add other iterables like List, Dictionary or Tuple to a Set. 
def Sets_05():
    Set_MLP_FIM_Main_Chars = {"Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"};
    Set_MLP_Main_Antagonists = {"Discord","Lord Tirak","Nightmare Moon","King Sombra","Queen Chrysalis","Sonata Dusk"};

    print("\n  BEFORE: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));

    Set_MLP_FIM_Main_Chars.update(Set_MLP_Main_Antagonists);

    print("\n  AFTER: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# remove() Method - Removes a single item from a Set. Throws exception error if item does not exist.
def Sets_06():
    Set_MLP_FIM_Main_Chars = {"Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"};
    
    print("\n  BEFORE: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));

    Set_MLP_FIM_Main_Chars.remove("Rainbow Dash");
    Set_MLP_FIM_Main_Chars.remove("Twilight Sparkle");

    print("\n  AFTER: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# discard() Method - Removes a single item from a Set. Does not exception error if item does not exist.
def Sets_07():
    Set_MLP_FIM_Main_Chars = {"Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"};
    
    print("\n  BEFORE: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));

    Set_MLP_FIM_Main_Chars.discard("Rainbow Dash");
    Set_MLP_FIM_Main_Chars.discard("Twilight Sparkle");

    print("\n  AFTER: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#8. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# pop() Method - Since Sets are UNORDERED, you cannot specify index of item to remove. You can call pop() with no aruments on a Set however to remove the last random item.
def Sets_08():
    Set_MLP_FIM_Main_Chars = {"Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"};
    
    print("\n  BEFORE: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));

    Set_MLP_FIM_Main_Chars.pop();
    Set_MLP_FIM_Main_Chars.pop();

    print("\n  AFTER: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#9. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# clear() Method - Clears all items in a Set without deleting/destroying it.
def Sets_09():
    Set_MLP_FIM_Main_Chars = {"Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"};
    
    print("\n  BEFORE: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));

    Set_MLP_FIM_Main_Chars.clear();

    print("\n  AFTER: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#10. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# del() Method - Completely deletes/destroys a Set.
def Sets_10():
    Set_MLP_FIM_Main_Chars = {"Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"};
    
    print("\n  BEFORE: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));

    del Set_MLP_FIM_Main_Chars;

    #Code below will throw exception/create ERROR as the Set now no longer exists
    print("\n  AFTER: Set is:",Set_MLP_FIM_Main_Chars);
    print("  Number of Items in Set =",len(Set_MLP_FIM_Main_Chars));    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#11. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# LOOPING - Sets can be looped like other iterators.
def Sets_11():
    Set_MLP_FIM_Main_Chars = {"Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"};

    print("\n   Number of Items in Set =",len(Set_MLP_FIM_Main_Chars),"\n");
    
    for X in Set_MLP_FIM_Main_Chars:
        print("  ",X);

    print("");
    Char_Counter = 0;
    for Y in Set_MLP_FIM_Main_Chars:
        Char_Counter = Char_Counter + 1;
        MESSAGE1 = "   " + str(Char_Counter) + ". Value: " + str(Y);
        MESSAGE2 = "Data Type:" + str(type(Y));
        print('{:<35}{:>0}'.format(MESSAGE1,MESSAGE2));
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#12. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# JOINING: union() method - Returns a new set containing all items from both sets. Excludes duplicate items.
def Sets_12():
    Set_MLP_FIM_Main_Chars = {"Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie"};
    Set_MLP_Main_Antagonists = {"Discord","Lord Tirak","Nightmare Moon","King Sombra","Queen Chrysalis","Sonata Dusk"};

    Set_Total_Cast = Set_MLP_FIM_Main_Chars.union(Set_MLP_Main_Antagonists);

    print("\nCast of main characters:",Set_MLP_FIM_Main_Chars);
    print("Cast of antagonists:",Set_MLP_Main_Antagonists);
    print("Total cast of all characters:",Set_Total_Cast);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 

# Summary of Set methods:
# add()	                         Adds an element to the set
# clear()	                     Removes all the elements from the set
# copy()	                     Returns a copy of the set
# difference()	                 Returns a set containing the difference between two or more sets
# difference_update()	         Removes the items in this set that are also included in another, specified set
# discard()	                     Remove the specified item
# intersection()	             Returns a set, that is the intersection of two other sets
# intersection_update()	         Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                 Returns whether two sets have a intersection or not
# issubset()	                 Returns whether another set contains this set or not
# issuperset()	                 Returns whether this set contains another set or not
# pop()	                         Removes an element from the set
# remove()	                     Removes the specified element
# symmetric_difference()         Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	 Inserts the symmetric differences from this set and another
# union()	                     Return a set containing the union of sets
# update()	                     Update the set with the union of this set and others

#-----Invocations-----
Sets_0l();
#Sets_02();
#Sets_03();
#Sets_04();
#Sets_05();
#Sets_06();
#Sets_07();
#Sets_08();
#Sets_09();
#Sets_10();
#Sets_11();
#Sets_12();

