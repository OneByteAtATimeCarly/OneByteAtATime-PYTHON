# Title: Python Strings
# Author: C. S. Germany 01/15/2022

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Different strings
def Strings_0l():
    
    Single_String = "Carly";

    Concatenated_String = "Carly" + "Salali" + "Germany";

    Multiline_String = """Beware the Jabberwock, my son! The jaws that bite, the claws that catch!
    Beware the Jubjub bird, and shun the frumious Bandersnatch!
    He took his vorpal sword in hand; long time the manxome foe he sought.
    So rested he by the Tumtum tree and stood awhile in thought.""";

    print("\nA. Single string:");
    print("  ",Single_String);

    print("\nB. Concatenated string:");
    print("  ",Concatenated_String);

    print("\nC.  Multiline string:");
    print("   ",Multiline_String);       
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   A string is really an array of type char, so it is always an iterable object
def Strings_02():
    
    print("\nD. A string is really an array of type char, so it is always an iterable object:\n");

    The_String = "Carly";

    for x in The_String:
        print("  ",x);

    print("\nE. Just like with any array type object, you can use len() to get the number of elements:");    
    print("   There are ",len(The_String)," characters in the string \"",The_String,"\".",sep='');
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Using decision structures with String objects
def Strings_03():
    
    print("\nF. Strings are accessible as substrings");

    Pokemon_Song = "I wanna be the very best like no one ever was. To catch them is my real test. To train them is my cause.";

    if("Pikachu" not in Pokemon_Song):
       print("   Pikachu is not here :-(");

    if("cause" in Pokemon_Song):
       print("   I found my CAUSE!");
#------------------------------------------------------------;----------------------------------------------------------------------------------------------------



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   upper() and lower() methods
def Strings_04():
    
    Lower_Case = "and in the streets the children screamed. the lovers cried and the poets dreamed.";
    Upper_Case = "BUT NOT A WORD WAS SPOKEN. THE CHURCH BELLS ALL WERE BROKEN.";

    print("------------------------------------------------------------------------------------");
    print("A. String Lower_Case by itself:\n  ",Lower_Case);
    print("\n   String Upper_Case by itself:\n  ",Upper_Case);
    print("------------------------------------------------------------------------------------");
    print("B. String Lower_Case with upper():\n  ",Lower_Case.upper());
    print("\n   String Upper_Case with lower():\n  ",Upper_Case.lower());
    print("------------------------------------------------------------------------------------");
#------------------------------------------------------------;----------------------------------------------------------------------------------------------------



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   replace() method
def Strings_05():
    
    Erroneous_Gettysburg = "Four score and three years ago";

    Correct_Gettysburg = Erroneous_Gettysburg.replace("three","seven");

    print("\nIncorrect Gettysburg address:",Erroneous_Gettysburg);
    print("Correct Gettysburg address:",Correct_Gettysburg,"\n");
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   split() method
def Strings_06():
    
    Main_Char_String = "Twilight Sparkle,Fluttershy,Rainbow Dash,Rarity,Apple Jack,Pinkie Pie";

    Main_Char_Array = Main_Char_String.split(",");

    #Loop method 1
    print("\nA. Using split() - Loop method 1");
    Counter = 0;
    for W in Main_Char_Array:
        Counter = Counter + 1;
        print("   ",Counter,". ",W,sep='');

    #Loop method 2 - Like C++.JAVA,POSH using range() and len()
    print("\nB. Using split() - Loop method 2");
    for X in range(len(Main_Char_Array)):
        print("   ",(X+1),". ",Main_Char_Array[X],sep='');
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   isdigit() method
def Strings_07():
    
    Pony_Ages = ["12","seven","19","thirteen","9","18","six"];

    for x in Pony_Ages:
        if(x.isdigit()):
           print("   \"",x,"\" is a number.",sep='');
        else:
           print("   \"",x,"\" is NOT a number.",sep='');   
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#-----Invocations-----
#Strings_0l();
#Strings_02();
#Strings_03();
#Strings_04();
#Strings_05();
#Strings_06();
Strings_07();



# String Methods
# capitalize()	     Converts the first character to upper case
# casefold()	     Converts string into lower case
# center()	         Returns a centered string
# count()	         Returns the number of times a specified value occurs in a string
# encode()	         Returns an encoded version of the string
# endswith()	     Returns true if the string ends with the specified value
# expandtabs()	     Sets the tab size of the string
# find()	         Searches the string for a specified value and returns the position of where it was found
# format()	         Formats specified values in a string
# format_map()	     Formats specified values in a string
# index()	         Searches the string for a specified value and returns the position of where it was found
# isalnum()	         Returns True if all characters in the string are alphanumeric
# salpha()	         Returns True if all characters in the string are in the alphabet
# isascii()	         Returns True if all characters in the string are ascii characters
# isdecimal()	     Returns True if all characters in the string are decimals
# isdigit()	         Returns True if all characters in the string are digits
# isidentifier()	 Returns True if the string is an identifier
# islower()	         Returns True if all characters in the string are lower case
# isnumeric()	     Returns True if all characters in the string are numeric
# isprintable()	     Returns True if all characters in the string are printable
# isspace()	         Returns True if all characters in the string are whitespaces
# istitle()	         Returns True if the string follows the rules of a title
# isupper()	         Returns True if all characters in the string are upper case
# join()	         Converts the elements of an iterable into a string
# ljust()	         Returns a left justified version of the string
# lower()	         Converts a string into lower case
# lstrip()	         Returns a left trim version of the string
# maketrans()	     Returns a translation table to be used in translations
# partition()	     Returns a tuple where the string is parted into three parts
# replace()	         Returns a string where a specified value is replaced with a specified value
# rfind()	         Searches the string for a specified value and returns the last position of where it was found
# rindex()	         Searches the string for a specified value and returns the last position of where it was found
# rjust()	         Returns a right justified version of the string
# rpartition()	     Returns a tuple where the string is parted into three parts
# rsplit()	         Splits the string at the specified separator, and returns a list
# rstrip()	         Returns a right trim version of the string
# split()	         Splits the string at the specified separator, and returns a list
# splitlines()	     Splits the string at line breaks and returns a list
# startswith()	     Returns true if the string starts with the specified value
# strip()	         Returns a trimmed version of the string
# swapcase()	     Swaps cases, lower case becomes upper case and vice versa
# title()	         Converts the first character of each word to upper case
# translate()	     Returns a translated string
# upper()	         Converts a string into upper case
# zfill()	         Fills the string with a specified number of 0 values at the beginning
