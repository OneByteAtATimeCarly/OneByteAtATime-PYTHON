# Title: Project - Pirate Treasure Map
# Author: C. S. Germany 01/06/2022  



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
def Pirate_Treasure_Map():
    from os import system;
    system("cls"); 

    Num_Rows = 7;
    Num_Columns = 10;
    Row_Counter = 0;
    Column_Counter = 0;
    Map_Char = "⬜️";

    print("\n A BLANK map with loops:");
    while(Row_Counter < Num_Rows):
          Row_Counter = Row_Counter + 1;
          print();
          Column_Counter = 0;
          while(Column_Counter < Num_Columns):
                Column_Counter = Column_Counter + 1;
                print(Map_Char,sep='',end='');


    MAP_Array = [ ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️",],
                  ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️",],
                  ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️",],
                  ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️",],
                  ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️",],
                  ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️",],
                  ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"]
                ];

    UserChoice = input("\n\n Place treasure. 1st digit = row. 2nd digit = column. : ");
    Treasure_ROW = int(UserChoice[0]); 
    Treasure_COLUMN = int(UserChoice[1]); 

    MAP_Array[(Treasure_ROW-1)][(Treasure_COLUMN-1)] = "XX";                

    print("\n A Treasure Map using a 2-D Array:"); 
    for x in MAP_Array:
        print();
        for y in x:
            print(y,sep='',end='');
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

Pirate_Treasure_Map();

