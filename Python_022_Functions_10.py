# Title: Functions 10 - Passing in a List (Array) as an argument
# Author: C. S. Germany 01/15/2022

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 
def Function_That_Takes_An_Array(PONIES):
    
    for x in range(len(PONIES)):
        print("   ",(x+1),". ",PONIES[x],sep='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#-----Invocations-----

print("\nA. Some MLP FIM Characters:");
Some_Ponies = ["Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie","Princess Celstia"];
Function_That_Takes_An_Array(Some_Ponies);



