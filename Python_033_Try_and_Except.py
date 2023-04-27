# Title: Python Try and Except blocks
# Author: C. S. Germany 01/15/2022

# Try and Except keywords: 
# try =     block lets you test a block of code for errors.
# except =  block lets you handle errors.
# else =    block lets you execute code when there is no error.
# finally = block lets you execute code, regardless of the result of the try and except blocks.
# raise =   used to throw your own custom exceptions.

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def Example_No_Errors():
    print("\nA. Inside function Example_No_Errors.");
    MESSAGE_1 = "Four score and seven years ago our fathers brought forth";
    MESSAGE_2 = " on this continent, a new nation, conceived in Liberty.";
    print(MESSAGE_1 + "\n" + MESSAGE_2);
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


def Example_Make_An_Error():
    print("\nA. Inside function Example_Make_An_Error.");
    MESSAGE_1 = "Four score and ";
    MESSAGE_2 = 7;
    MESSAGE_3 = " on this continent, a new nation, conceived in Liberty.";
    print(MESSAGE_1 + "\n" + MESSAGE_2 + MESSAGE_3);
    #Throws a TypeError exception cause MESSAGE_2 needs to be cast to a str() but it's an int
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


def Example_Catch_ANY_GENERIC_Error():
    print("\nA. Inside function Example_Catch_ANY_GENERIC_Error.");
    MESSAGE_1 = "Four score and ";
    MESSAGE_2 = 7;
    MESSAGE_3 = " on this continent, a new nation, conceived in Liberty.";

    try:
        print(MESSAGE_1 + "\n" + MESSAGE_2 + MESSAGE_3);    
    except:  
        print("There was a problem printing.");  
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


def Example_Catch_A_SPECIFIC_Error_01():
    print("\nA. Inside function Example_Catch_A_SPECIFIC_Error_01.");
    MESSAGE_1 = "Four score and ";
    MESSAGE_2 = 7;
    MESSAGE_3 = " on this continent, a new nation, conceived in Liberty.";

    try:
        print(MESSAGE_1 + "\n" + MESSAGE_2 + MESSAGE_3); 
       
    except TypeError:  
        print("A TypeError has occurred.");
    
    except:
        print("An unknown error has occurred.");      
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


def Example_Catch_A_SPECIFIC_Error_02():
    print("\nC. Inside function Example_Catch_A_SPECIFIC_Error_02:");
    
    try:
           print("  ",Un_Declared_Variable);
    
    except NameError:
           print("   A NameError exception has occurred.");

    except TypeError:  
           print("A TypeError has occurred.");    
    
    except:
           print("   Something wrong but it wasn't a NameError.");       
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#Using try and except with ELSE
def Try_and_Except_With_ELSE():
    print("\nD. Inside function Try_and_Except_With_ELSE:");

    MESSAGE = "Four Score and Seven Years Ago";

    try:
           print("  ",MESSAGE);
    except:
           print("   EXCEPTION: ERROR! A generic exception occurred.");
    else:
           print("   No exceptions thrown. Everything is A-OK.");       
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#   Using finally with try and except
def Try_Except_With_FINALLY():
    print("\nE. Inside function Try_Except_With_FINALLY:");

    MESSAGE = "Four Score and Seven Years Ago";
    try:
           print("  ",MESSAGE);
    except:
           print("   ERROR! Exception occurred.");
    finally:
           print("   FINALLY! Whether an exception was thrown or not? We are at the END here.");       
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#Throwing your own exceptions with "raise"
def Throwing_Custom_Exceptions_With_RAISE_01():
    print("\nF. Inside function Throwing_Custom_Exceptions_With_RAISE_01.");
    
    try: 
         print("  ",MESSAGE);
         raise Exception("Gettysburg_Error");

    except Exception as Gettysburg_Error:
           print("   DANGER Will Robinson! Alert Mr. Lincoln!");
           print("   A Gettysburg_Error has been triggered!\n");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Another example with raise, without try and except to catch it so displays direct to console output
def Throwing_Custom_Exceptions_With_RAISE_02():
    print("\nG. Inside function Throwing_Custom_Exceptions_With_RAISE_02:");

    AGE = "Puff the Magic Dragon";

    if not type(AGE) is int:
       raise TypeError("Only numbers (int) are allowed and SuperClalaFrajalIstic! :-p");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#-----Invocations-----
#Example_No_Errors();
#Example_Make_An_Error();
#Example_Catch_ANY_GENERIC_Error();
#Example_Catch_A_SPECIFIC_Error_01();
#Example_Catch_A_SPECIFIC_Error_02();
#Try_and_Except_With_ELSE();
#Try_Except_With_FINALLY();
#Throwing_Custom_Exceptions_With_RAISE_01();
Throwing_Custom_Exceptions_With_RAISE_02();


