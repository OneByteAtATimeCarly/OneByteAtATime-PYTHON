# Title: Python Regular Expressions (RegEx) 
# Author: C. S. Germany 01/15/2022

# Sequences of characters that form a search pattern. Python use the re module for RegEx.

# Methods of re Module
# findall =	Returns a list containing all matches
# search  =	Returns a Match object if there is a match anywhere in the string
# split   =	Returns a list where the string has been split at each match
# sub     = Replaces one or many matches with a string

# The search() method itself has these functions and attributes
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match


#----------------------------------------------------------------------------------------------------------------------------------------------
   # Metacharacters for RegEx
   # Character | Description	                                       | Example	
   # []	         Set of characters	"[a-m]"	
   # \	         Signals special sequence (also escapes spec. chars)	 "\d"	
   # .	         Any character (except newline character)	             "he..o"	
   # ^	         Starts with	                                         "^hello"	
   # $	         Ends with	                                             "planet$"	
   # *	         Zero or more occurrences	                             "he.*o"	
   # +	         One or more occurrences	                             "he.+o"	
   # ?	         Zero or one occurrences	                             "he.?o"	
   # {}	         Exactly the specified number of occurrences	         "he.{2}o"	
   # |	         Either or                                               "falls|stays"	
   # ()	         Capture and group	 
#----------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------
   # Special Sequences for RegEx
   # Character | Description	                                                                              |  Example	
   # \A	         Returns match if the specified characters are at the beginning of the string	                 "\AThe"	
   # \b          Returns match where the specified characters are at the beginning or at the end of a word       r"\bain"
   #             ("r" in beginning is making sure string is being treated as "raw string")	                     r"ain\b"	
   # \B          Returns match where specified chars present but NOT at beginning or end word                    r"\Bain"
   #             ("r" in beginning is making sure that string is being treated as "raw string")	                 r"ain\B"	
   # \d	         Returns match where the string contains digits (numbers from 0-9)	                             "\d"	
   # \D	         Returns match where the string DOES NOT contain digits	                                         "\D"	
   # \s	         Returns match where the string contains a white space character	                             "\s"	
   # \S	         Returns match where the string DOES NOT contain a white space character	                     "\S"	
   # \w	         Returns match where string contains any word chars (A to Z), digits 0-9 and the underscore _)	 "\w"	
   # \W	         Returns match where the string DOES NOT contain any word characters	                         "\W"	
   # \Z        	 Returns match if the specified characters are at the end of the string	                         "Spain\Z"
#----------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------
   # Sets for RegEx
   #  Character  | Description	                                                                              	
   #  [arn]	       Returns a match where one of the specified characters (a, r, or n) are present	
   #  [a-n]	       Returns a match for any lower case character, alphabetically between a and n  
   #  [^arn]	   Returns a match for any character EXCEPT a, r, and n	
   #  [0123]	   Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
   #  [0-9]	       Returns a match for any digit between 0 and 9	
   #  [0-5][0-9]   Returns a match for any two-digit numbers from 00 and 59	
   #  [a-zA-Z]	   Returns a match for any character alphabetically between a and z, lower case OR upper case	
   #  [+]	       In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
#----------------------------------------------------------------------------------------------------------------------------------------------


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   SEARCH Method - Searches for strings of text that match a specified pattern. specify start and end portions of string
def Regular_Expressions_Search_0l():
    import re;
    txt = "The rain in Spain";

    x = re.search("^The.*Spain$", txt);  #search string that starts with "The" and ends with "Spain"  

    print("\nValue of x is:",x);
    print("Value of x.group() is:",x.group());
    print("Value of x.span() is:",x.span());
    print("Value of x.string is:",x.string);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   SEARCH Method - Any words beginning with uppercase letter
def Regular_Expressions_Search_02():
    import re;
    txt = "The rain in Spain";

    x = re.search(r"\bS\w+", txt); #search for any words staring with uppercase "S"   

    print("\nValue of x is:",x);
    print("Value of x.group() is:",x.group());
    print("Value of x.span() is:",x.span());
    print("Value of x.string is:",x.string);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   SEARCH Method - search for whitespace
def Regular_Expressions_Search_03():
    import re;
    txt = "The rain in Spain";

    x = re.search("\s", txt); #search for 1st whitespace char

    print("\nValue of x is:",x);
    print("Value of x.group() is:",x.group());
    print("Value of x.span() is:",x.span());
    print("Value of x.string is:",x.string);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   SEARCH Method - start, gives starting positoin of match
def Regular_Expressions_Search_04():
    import re;
    txt = "The rain in Spain";

    x = re.search("\s", txt); #search for 1st whitespace char

    print("\nValue of x is:",x);
    print("Value of x.start() is:",x.start());
    print("Value of x.group() is:",x.group());
    print("Value of x.span() is:",x.span());
    print("Value of x.string is:",x.string);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Findall Method - returns a list containing all matches
def Regular_Expressions_FindAll_01():
    import re;

    txt = "The rain in Spain";
    RESULT = re.findall("ai", txt);
    
    print("\nRaw value of RESULT is:",RESULT)

    for x in range(len(RESULT)):
        print("Value of element ",x," is: ",RESULT[x],sep='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Split Method - returns a list where the string has been split at each match.
def Regular_Expressions_Split_01():
    import re;

    txt = "The rain in Spain";
    RESULT = re.split("\s", txt);
    
    print("\nRaw value of RESULT is:",RESULT);

    for x in range(len(RESULT)):
        print("Value of element ",x," is: ",RESULT[x],sep='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Split Method - returns a list where the string has been split at each match.
def Regular_Expressions_Split_02():
    import re;

    txt = "The rain in Spain";
    RESULT = re.split("\s", txt, 1);
    
    print("\nRaw value of RESULT is:",RESULT);

    for x in range(len(RESULT)):
        print("Value of element ",x," is: ",RESULT[x],sep='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Sub Method - replaces any matches with specififed text
def Regular_Expressions_Sub_01():
    import re;

    txt = "The rain in Spain";
    RESULT1 = re.sub("\s", "9", txt);
    RESULT2 = re.sub("\s", "9", txt, 2);
    
    print("\nRaw value of RESULT1 is:",RESULT1);
    print("\nRaw value of RESULT2 is:",RESULT2);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#-----Invocations-----
#Regular_Expressions_Search_0l();
#Regular_Expressions_Search_02();
#Regular_Expressions_Search_03();
#Regular_Expressions_Search_04();
#Regular_Expressions_FindAll_01();
#Regular_Expressions_Split_01();
#Regular_Expressions_Split_02();
Regular_Expressions_Sub_01();




