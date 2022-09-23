# Functions 8 - Keyword Arguments 
# Author: C. S. Germany 01/15/2022

# Normally when you define a function, parameters must be passed into the function in directly the same order as its arguments are defined.
# But if you define a function using keyword arguments, when you call the function later you can pass arguments into it using any order you please as long as you
# reference each variable by name.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 
def Functions_06(Pony1, Pony2, Pony3, Pony4):
    
    print("   Pony 1:",Pony1);
    print("   Pony 2:",Pony2);
    print("   Pony 3:",Pony3);
    print("   Pony 4:",Pony4);

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#-----Invocations-----

print("\nA. Some MLP FIM Characters:");
Functions_06(Pony4 = "AppleJack", Pony1 = "Twilight Sparkle", Pony3="Fluttershy", Pony2 = "Rainbow Dash");




