# Title: Python Algorithm Tricks
# Author: C. S. Germany 01/15/2022


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# The slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.
def Reversing_A_String():
    
    Text_to_Reverse = "I wonder how this text looks like backwards?";

    Reversed_Text = Text_to_Reverse [::-1];

    print("\nOriginal text:",Text_to_Reverse);
    print("Reversed text:",Reversed_Text);

#-------------------------------------------------------------------------------------------------------------------------------------------------------------  





#-----Invocations-----
Reversing_A_String();

