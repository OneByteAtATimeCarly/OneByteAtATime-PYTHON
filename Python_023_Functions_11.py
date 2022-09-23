# Title: Functions 11 - Returning values from a function with "return".
# Author: C. S. Germany 01/15/2022

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 
def Function_That_Takes_An_Array(PONIES):
    
    for x in range(len(PONIES)):
        print("   ",(x+1),". ",PONIES[x],sep='');
        
    Num_Ponies = len(PONIES);
    return Num_Ponies;
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#-----Invocations-----

print("\nA. Some MLP FIM Characters:");
Some_Ponies = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie","Princess Celstia"];

HowManyPonies = Function_That_Takes_An_Array(Some_Ponies);

print("\nNumber of ponies is:",HowManyPonies);




