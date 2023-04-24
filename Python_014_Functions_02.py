# Title: Python Functions 2 - Passing arguments and parameters
# Author: C. S. Germany 01/15/2022

#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Comments here
def Functions_02(Char_Name,Char_Age):
    print("\n     Inside Functions_02 now ...");
    print("     Hello,",Char_Name,". You are",Char_Age,"years old.");
    print("     Leaving function now ...");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Comments here
def Functions_03(Meaning_of_Life,Magic_Number):
    print("\n     Inside Functions_03 now ...");
    print("     Multiply",Meaning_of_Life,"by",Magic_Number,"and return result");
    RESULT = Meaning_of_Life * Magic_Number;
    print("     Leaving function now ...");
    return RESULT;
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 

"""
#-----Invocations-----
print("\n---------------------------------------------------------------------------------------------------------------------");
print("\nB. Example 2 - Passing in a string and an integer");
print("\nI am in the main global program space now.");
Functions_02("Carly Salali Germany",53);
print("\nI am back in the main global program space now.");
"""

print("\n---------------------------------------------------------------------------------------------------------------------");
print("\nC. Example 3 - Passing in 2 integers and returning a value");
print("\nI am in the main global program space now.");
Returned_Value = Functions_03(42,444);
print("\nI am back in the main global program space now.");
print("Returned_Value =",Returned_Value);
print("\n---------------------------------------------------------------------------------------------------------------------");

