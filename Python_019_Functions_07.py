# Title: Functions 7 - Arbitrary Arguments (Taking arguments as an ARRAY)
# Author: C. S. Germany 01/15/2022

# Add a * before the parameter name in the function definition and it can take an unknown number of arguments.
# To do this, the * acts somewhat like C++'s dereference operator and the arguments are passed in as elements of an array type object.
# This allows them to be accessed and referenced using array subscript syntax and an index value.
# See below how flexible a function written this way can be? Reusing the same code over and over to list any number of different things. Viva Python! 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 
def Functions_05(*CAST_CHARACTERS):
    
    for x in range(len(CAST_CHARACTERS)):
        print("   ",(x+1),". ",CAST_CHARACTERS[x],sep='');

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#-----Invocations-----

print("\nA. The cast of \"My Little Pony - Friendship is Magic (MLP FIM)\"");
Functions_05("Fluttershy","Twilight Sparkle","Rainbow Dash","Rarity","Pinkie Pie","Apple Jack");

print("\nB. The cast of \"Battle Star Galactica (BSG)\"");
Functions_05("Gaius Baltar","William Adama","Kara Thrace (Starbuck)","Sharon Valerii (Boomer)","Laura Roslin","Number Six","Saul Tigh");

print("\nC. The cast of \"Naruto\"");
Functions_05("Naruto Uzumaki","Sasuke Uchiha","Kakashi Hatake","Sakura Haruno","Jiraiya","Lady Tsunade","Gaara","Rock Lee","Orochimaru","Shikamaru");

print("\nD. The cast of \"One Piece\"");
Functions_05("Luffy MonkeyD","Zoro Roronoa","Nami Akemi","Sanji Vinsmoke","Robin Nico","Usopp Yamaguchi","Chopper Tony");

print("\nE. The cast of \"Star Trek TNG\"");
Functions_05("Jean-Luc Picard","William T Riker","Beverly Crusher","Worf Mogh","DATA Soong","Geordi LaForge","Deanna Troi");



