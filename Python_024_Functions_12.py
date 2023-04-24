# Title: Functions 12 - Recursion. 
# Author: C. S. Germany 01/15/2022

# This is where a function calls itself. It's something you can do in lots of languages like C++, Java and PowerShell.
# It can be a powerful tool, but use cautiously or you can end up with memory fork bomba and infinite loops.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 
def Recursion_Recursion(Z):
    print("-----------------------------------------------------------------------"); 
    print("Inside function. Received",Z,"as argument.");

    if(Z > 0):
       result = Z + Recursion_Recursion(Z - 1);
       print("Inside function after recursive call. Result = ",result);
    else:
       print("-----------------------------------------------------------------------");
       print("Inside function. Reached ZERO.");
       print("-----------------------------------------------------------------------");
       result = 0;
      
    return result;
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#-----Invocations-----
print("\n\nOutside function. Calling it 1st time and passing in 3.\n");
Recursion_Recursion(3);




