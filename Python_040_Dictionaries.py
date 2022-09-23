# Title: Python Dictionaries
# Author: C. S. Germany 01/15/2022

# Store data values in key:value pairs.

# CHANGEABLE.  YES. You CAN both [ADD] and [REMOVE] items in a Dictionary using the methods update() and pop(). 
# INDEXED:     YES, BUT indexed by KEYS rather than numerically
# ORDERED:     YES. Items have defined order that will not change. If add new items to a Dictionary they are placed at end. (Python version 3.7, earlier versions Dictionaries were unordered)
# DUPLICATES:  NO. Dictionaries can NOT have any two items with the same value. Duplictes will OVERWRITE previous keys with same name.
# USE:         To store multiple items in single container.
# SIMILIAR:    Similiar structures in Python are: Tuple, Set, and List. 
# CREATED:     Created with curly braces {  } and key-value pairs separated with semicolons : followed by commas ,
# MULTIPLE:    Unlike C++ arrays, members of a Dictionary can be of different data types.
# METHODS:     len(), update(), pop()


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Dictionaries - Instantiating. Can hold objects of different data types in a single Dictionary.
def Dictionaries_0l():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    print("\nNumber of items in Dictionary:",len(DCT_Twilight));

    print("\nEntire Dictionary: ",DCT_Twilight);
    print("\nDictionary value at KEY Name:",DCT_Twilight["Name"]);
    print("Dictionary value at KEY Species:",DCT_Twilight["Species"]);
    print("Dictionary value at KEY Age:",DCT_Twilight["Age"]);
    print("Dictionary value at KEY Magic User:",DCT_Twilight["Magic User"]);
    print("Dictionary value at KEY Flight Capable:",DCT_Twilight["Flight Capable"]);
    print("Dictionary value at KEY Powers:",DCT_Twilight["Powers"]);    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Dictionaries - Creation. Holding different data types.
def Dictionaries_02():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    print("\nData Type of Dictionary itself:",type(DCT_Twilight));

    print("\nData Type of value at KEY Name:",type(DCT_Twilight["Name"]));
    print("Data Type of value at KEY Species:",type(DCT_Twilight["Species"]));
    print("Data Type of value at KEY Age:",type(DCT_Twilight["Age"]));
    print("Data Type of value at KEY Magic User:",type(DCT_Twilight["Magic User"]));
    print("Data Type of value at KEY Flight Capable:",type(DCT_Twilight["Flight Capable"]));
    print("Data Type of value at KEY Powers:",type(DCT_Twilight["Powers"]));    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# get() method - Retrieving values using get() method and without
def Dictionaries_03():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    print("\nUsing get() to retreive value of KEY Name:",DCT_Twilight.get("Name"));
    print("Retreiving value of KEY Name directly without get():",DCT_Twilight["Name"]);
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# keys() method - Return list of all KEYS in Dictionary
def Dictionaries_04():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    print("\nKEYS in Dictionary are:",DCT_Twilight.keys());
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# values() method - Return list of all VALUES in Dictionary
def Dictionaries_05():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    print("\nVALUES in Dictionary are:",DCT_Twilight.values());
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# items() method - Returns each item in a Dictionary as Tuples in a List
def Dictionaries_06():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    print("\nVALUES in Dictionary are:",DCT_Twilight.items());
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# To check if KEY exists in Dictionary use "in" keyword
def Dictionaries_07():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    if("Flight Capable" in DCT_Twilight):
       print("\nThis KEY exists in this Dictionary.");
    else: print("\nThis KEY does NOT exist in this Dictionary."); 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#8. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# CHANGING items in a Dictionary
def Dictionaries_08():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    if("Flight Capable" in DCT_Twilight):
       print("\nThis KEY exists in this Dictionary.");
    else: print("\nThis KEY does NOT exist in this Dictionary."); 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#9. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# CHANGING items in a Dictionary
def Dictionaries_09():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    print("\nBEFORE: ",DCT_Twilight);

    DCT_Twilight["Name"] = "Rainbow Dash";

    print("\nAFTER: ",DCT_Twilight);
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#10. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# update() method - modifies Dictionary based on given KEY and VALUE pair
def Dictionaries_10():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    print("\nBEFORE: ",DCT_Twilight);

    DCT_Twilight.update({"Name" : "Apple Jack"});

    print("\nAFTER: ",DCT_Twilight);
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#11. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Adding new key pairs to Dictionaries - Just postfix the key-value pair to the end of the Dictionary
def Dictionaries_11():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    print("\nBEFORE: ",DCT_Twilight);

    DCT_Twilight["Color"] = "Purple";

    print("\nAFTER: ",DCT_Twilight);
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#12. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# update() method - Can also add new key pairs to Dictionaries. If the KEY exists, it will modify the value. If not, it will add a new KEY-VALUE pair.
def Dictionaries_12():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    print("\nupdate() with KEY that already exists:");
    print("BEFORE: ",DCT_Twilight);
    DCT_Twilight.update({"Name": "Rarity"});
    print("AFTER: ",DCT_Twilight);                     

    print("\nupdate() with KEY that does not exist:");
    print("BEFORE: ",DCT_Twilight);
    DCT_Twilight.update({"Color": "White"});
    print("AFTER: ",DCT_Twilight);
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#13. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# pop() method - Removes item specified by KEY from Dictionary
def Dictionaries_13():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"]};   

    print("\nBEFORE: ",DCT_Twilight);

    DCT_Twilight.pop("Powers");

    print("AFTER: ",DCT_Twilight);                     
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#14. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# popitem() method - Removes last KEY-VALUE pair item in the Dictionary
def Dictionaries_14():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"],
                      "Color": "Purple"};   

    print("\nBEFORE: ",DCT_Twilight);

    DCT_Twilight.popitem();

    print("AFTER: ",DCT_Twilight);                     
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#15. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# clear() method - Clears Dictionary without deleting/destroying it
def Dictionaries_15():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"],
                      "Color": "Purple"};   

    print("\nBEFORE: ",DCT_Twilight);

    DCT_Twilight.clear();

    print("AFTER: ",DCT_Twilight);                     
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#16. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# del() method - removes KEY-VALUE pair in Dictionary by specified KEY name
def Dictionaries_16():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"],
                      "Color": "Purple"};   

    print("\nBEFORE: ",DCT_Twilight);

    del DCT_Twilight["Powers"];

    print("AFTER: ",DCT_Twilight);                     
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#17. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# del() method - Can also completely destroy a Dictionary
def Dictionaries_17():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"],
                      "Color": "Purple"};   

    print("\nBEFORE: ",DCT_Twilight);

    del DCT_Twilight;

    #Code below will produce ERROR as Dictionary no longer exists
    print("AFTER: ",DCT_Twilight);                     
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#18. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# LOOPING 1 - Accessing KEYS, VALUES, BOTH and FORMATTING output into columns
def Dictionaries_18():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"],
                      "Color": "Purple"};   

    print("\nA. Display all KEYS in Dictionary.");
    for X in DCT_Twilight:
        print("  KEY:",X);

    print("\nB. Display all VALUES in Dictionary.");
    for Y in DCT_Twilight:
        print("  VALUE:",DCT_Twilight[Y]);  

    print("\nC. Display both KEYS and VALUES in Dictionary.\n");
    for Z in DCT_Twilight:
        #print("  KEY:",X,"  VALUE:",DCT_Twilight[X]);
        COLUMN_1 = "   KEY: " + Z;
        COLUMN_2 = "  VALUE: " + str(DCT_Twilight[Z]);
        print('{:<23}{:>0}'.format(COLUMN_1,COLUMN_2));                 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#19. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# LOOPING 2 - using methods keys(), values() and items()
def Dictionaries_19():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"],
                      "Color": "Purple"};   

    print("\nA. Looping with keys() method to get dictionary KEYS:");
    for X in DCT_Twilight.keys():
        print("  KEY:",X);

    print("\nB. Looping with values() method to get dictionary VALUES:");
    for Y in DCT_Twilight.values():
        print("  VALUE:",Y);

    print("\nC. Looping with items() method to get dictionary KEYS:");
    for A,B in DCT_Twilight.items():
        #print("  KEY:",X,"  VALUE:",DCT_Twilight[X]);
        COLUMN_1 = "   KEY: " + A;
        COLUMN_2 = "  VALUE: " + str(B);
        print('{:<23}{:>0}'.format(COLUMN_1,COLUMN_2));                 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#20. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# COPYING: - You cannot copy a Dictionary using: Dictionary2 = Dictionary1. Doing this doesn't copy the Dictionary to another. 
# Rather, it effectively sets up Dictionary2 to be a C++ type POINTER that references Dictionary1, so any changes made to Dictionary2 are made to Dictionary1.
# The copy() method will let you copy an entire Dictionary to another as a separate duplicate, element by element.
def Dictionaries_20():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"],
                      "Color": "Purple"}; 

    DCT_Twilight_evil_Clone = DCT_Twilight.copy();                 

    print("\nA. Original dictionary DCT_Twilight:",DCT_Twilight);
    print("B. Copied dictionary DCT_Twilight_evil_Clone:",DCT_Twilight_evil_Clone);
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#21. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# COPYING: - You can also copy a Dictionary using its constructor dict()
def Dictionaries_21():

    DCT_Twilight = {  "Name": "Twilight Sparkle",
                      "Species": "Alicorn",
                      "Age": 444,
                      "Magic User": True,
                      "Flight Capable": True,
                      "Powers": ["Friendship","Love","Kindness","Forgiveness"],
                      "Color": "Purple"}; 

    DCT_Twilight_evil_Clone = dict(DCT_Twilight);                 

    print("\nA. Original dictionary DCT_Twilight:",DCT_Twilight);
    print("B. Copied dictionary DCT_Twilight_evil_Clone:",DCT_Twilight_evil_Clone);
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#22. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# NESTED DICTIONARIES 1: - You can NEST Dictionaries inside other Dictionaries. Like multpile records/rows with columns
# In the exampe below each Dictionary itself contains a Dictionary with multiple KEY-VALUE pairs.
def Dictionaries_22():

    DCT_MLP_Chars = {  "Pony1" : { "Name": "Twilight Sparkle",
                                   "Species": "Alicorn",
                                   "Age": 444,
                                   "Magic User": True,
                                   "Flight Capable": True,
                                   "Powers": ["Friendship","Love","Kindness","Forgiveness"],
                                   "Color": "Purple" 
                                 },
                       "Pony2" : { "Name": "Rainbow Dash",
                                   "Species": "Pegasus",
                                   "Age": 205,
                                   "Magic User": True,
                                   "Flight Capable": True,
                                   "Powers": ["Sonic Rainboom","20% More Awesomeness"],
                                   "Color": "Blue" 
                                 },
                       "Pony3" : { "Name": "Rarity",
                                   "Species": "Unicorn",
                                   "Age": 302,
                                   "Magic User": True,
                                   "Flight Capable": False,
                                   "Powers": ["Fashionista Vista","Super-Style","Telekinesis"],
                                   "Color": "White" 
                                 }                                                                  
                    }; 

    print("\nEntire Nested Dictionary:",DCT_MLP_Chars);
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#23. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# NESTED DICTIONARIES 2: - Creating inner dictionaries FIRST. Then placing them into an outer Dictionary.
def Dictionaries_23():

    DCT_Pony1 = { "Name": "Twilight Sparkle",
                  "Species": "Alicorn",
                  "Age": 444,
                  "Magic User": True,
                  "Flight Capable": True,
                  "Powers": ["Friendship","Love","Kindness","Forgiveness"],
                  "Color": "Purple" };

    DCT_Pony2 = { "Name": "Rainbow Dash",
                  "Species": "Pegasus",
                  "Age": 205,
                  "Magic User": True,
                  "Flight Capable": True,
                  "Powers": ["Sonic Rainboom","20% More Awesomeness"],
                  "Color": "Blue" };

    DCT_Pony3 = { "Name": "Rarity",
                  "Species": "Unicorn",
                  "Age": 302,
                  "Magic User": True,
                  "Flight Capable": False,
                  "Powers": ["Fashionista Vista","Super-Style","Telekinesis"],
                  "Color": "White" };                                      

    DCT_MLP_Chars = { "Pony1" : DCT_Pony1, 
                      "Pony2" : DCT_Pony2, 
                      "Pony3" : DCT_Pony3}; 

    print("\nEntire Nested Dictionary:",DCT_MLP_Chars);
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#24. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# LOOPING NESTED DICTIONARIES 1: 
def Dictionaries_24():

    DCT_MLP_Chars = {  "Pony1" : { "Name": "Twilight Sparkle",
                                   "Species": "Alicorn",
                                   "Age": 444,
                                   "Magic User": True,
                                   "Flight Capable": True,
                                   "Powers": ["Friendship","Love","Kindness","Forgiveness"],
                                   "Color": "Purple" 
                                 },
                       "Pony2" : { "Name": "Rainbow Dash",
                                   "Species": "Pegasus",
                                   "Age": 205,
                                   "Magic User": True,
                                   "Flight Capable": True,
                                   "Powers": ["Sonic Rainboom","20% More Awesomeness"],
                                   "Color": "Blue" 
                                 },
                       "Pony3" : { "Name": "Rarity",
                                   "Species": "Unicorn",
                                   "Age": 302,
                                   "Magic User": True,
                                   "Flight Capable": False,
                                   "Powers": ["Fashionista Vista","Super-Style","Telekinesis"],
                                   "Color": "White" 
                                 }                                                                  
                    }; 

    print("\nLooping Outer Nested Dictionary:");
    for X in DCT_MLP_Chars:
        print(X);
        print(DCT_MLP_Chars[X]);
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



# Summary of Dictionary Methods
# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()    Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary


#-----Invocations-----
#Dictionaries_0l();
#Dictionaries_02();
#Dictionaries_03();
#Dictionaries_04();
#Dictionaries_05();
#Dictionaries_06();
#Dictionaries_07();
#Dictionaries_08();
#Dictionaries_09();
#Dictionaries_10();
#Dictionaries_11();
#Dictionaries_12();
#Dictionaries_13();
#Dictionaries_14();
#Dictionaries_15();
#Dictionaries_16();
#Dictionaries_17();
#Dictionaries_18();
#Dictionaries_19();
#Dictionaries_20();
#Dictionaries_21();
#Dictionaries_22();
#Dictionaries_23();
Dictionaries_24();

