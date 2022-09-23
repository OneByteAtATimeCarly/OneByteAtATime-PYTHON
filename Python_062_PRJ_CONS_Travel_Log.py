# Title: Project - Travel Log
# Author: C. S. Germany 01/06/2022 

import random;
from os import system;
system("cls");

#Globals

D_Countries = { "China" : 2,
                "Japan" : 3,
                "Argentina" : 1,
              };

D_Cities = {    "China" : ["Beijing","Shanghai"],
                "Japan" : ["Tokyo","Okinawa"],
                "Argentina" : ["Buenos Aires"],
           };
         
L_Travel_Log = [ D_Countries, D_Cities ];



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
def add_new_country(Country,NumVisits,Cities):
    print("\nReceived:");
    print("Country:",Country);
    print("Num Visits:",NumVisits);
    print("Cities:",Cities);

    D_Countries.update({Country : NumVisits});
    D_Cities.update({Country : Cities});

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#Invocations
add_new_country("United Kingdom",3,["Winchester","London","Liverpool"]);
add_new_country("Israel",5,["Jerusalem","Tel Aviv","Nazareth"]);
add_new_country("Russia",2,["Moscow", "Saint Petersburg"]);

print("\nAfterwards:");

print("\nDictionary Countries:");
print(D_Countries);

print("\nDictionary Cities:");
print(D_Cities);

print("\nList Travel Log:");
print(L_Travel_Log);


