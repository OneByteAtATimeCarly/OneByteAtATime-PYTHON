# Title: Python Try and Except blocks
# Author: C. S. Germany 01/15/2022

# Try and Except keywords: 
# try =     block lets you test a block of code for errors.
# except =  block lets you handle errors.
# else =    block lets you execute code when there is no error.
# finally = block lets you execute code, regardless of the result of the try and except blocks.
# raise =   used to throw your own custom exceptions.

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   A basic try and except block
def Try_and_Except_01():
    
    print("\nA. Inside function Try_and_Except_01:");
    MESSAGE = "Four Score and Seven Years Ago";
    try:
           print("  ",MESSAGE);
    except:
           print("ERROR! Exception occurred.");
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Code that throws an exception
def Try_and_Except_02_Error():

    print("\nB. Inside function Try_and_Except_02_Error:");
    try:
           print("  ",MESSAGE);
    except:
           print("   EXCEPT: ERROR! Exception occurred.");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Code that throws an exception and catches multiple types of exceptions
def Try_and_Except_03_Handling_Different_Exceptions():

    print("\nC. Inside function Try_and_Except_03_Handling_Different_Exceptions:");
    try:
           print("  ",MESSAGE);
    except NameError:
           print("   EXCEPT: ERROR! Exception occurred.");
    except:
           print("   EXCEPT: Something wrong but not a NameError.");       
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Using else with try and except
def Try_and_Except_04_Try_Except_ELSE():

    print("\nD. Inside function Try_and_Except_04_Try_Except_ELSE:");
    MESSAGE = "Four Score and Seven Years Ago";
    try:
           print("  ",MESSAGE);
    except:
           print("   EXCEPT: ERROR! Exception occurred.");
    else:
           print("   ELSE: No exceptions thrown. Everything is A-OK.");       
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Using finally with try and except
def Try_and_Except_05_Try_Except_FINALLY():

    print("\nE. Inside function Try_and_Except_05_Try_Except_FINALLY:");
    MESSAGE = "Four Score and Seven Years Ago";
    try:
           print("  ",MESSAGE);
    except:
           print("   ERROR! Exception occurred.");
    finally:
           print("   FINALLY: Whether an exception was thrown or not? We are at the END.");       
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Throwing your own exceptions with "raise"
def Try_and_Except_06_Throwing_Custom_Exceptions_RAISE():

    print("\nF. Inside function Try_and_Except_06_Throwing_Custom_Exceptions_RAISE:");
    
    try: 
         print("  ",MESSAGE);
         raise Exception("Gettysburg_Error");
    except Exception as Gettysburg_Error:
           print("   DANGER Will Robinson! Alert! A Gettysburg_Error has been triggered!");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Another example with raise, without try and except to catch it so displays direct to console output
def Try_and_Except_07_Throwing_Custom_Exceptions_RAISE2():

    print("\nG. Inside function Try_and_Except_07_Throwing_Custom_Exceptions_RAISE2:");
    AGE = "Puff the Magic Dragon";
    if not type(AGE) is int:
       raise TypeError("Only numbers (int) are allowed");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#-----Invocations-----
#Try_and_Except_01();
#Try_and_Except_02_Error();
#Try_and_Except_03_Handling_Different_Exceptions();
#Try_and_Except_04_Try_Except_ELSE();
#Try_and_Except_05_Try_Except_FINALLY();
#Try_and_Except_06_Throwing_Custom_Exceptions_RAISE();
Try_and_Except_07_Throwing_Custom_Exceptions_RAISE2();


