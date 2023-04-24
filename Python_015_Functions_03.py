# Title: Python Functions 3 - Default parameters
# Author: C. S. Germany 01/15/2022

#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Comments here
def Functions_04(Char_Name="Anonymous",Char_Age=42):
    print("\n     Inside Functions_04 now ...");
    print("     Hello,",Char_Name,". You are",Char_Age,"years old.");
    print("     Leaving function now ...");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#-----Invocations-----
print("\n---------------------------------------------------------------------------------------------------------------------");

print("\nD. Example 4 - Calling methods with no arguments supplies to trigger defaults:");
print("\nI am in the main global program space now.");
Functions_04();
print("\nI am back in the main global program space now.");

print("\n---------------------------------------------------------------------------------------------------------------------");

print("\nD. Example 4 - Passing in a string and an integer with parameters that override defaults:");
print("\nI am in the main global program space now.");
Functions_04("Carly Salali Germany",53);
print("\nI am back in the main global program space now.");


