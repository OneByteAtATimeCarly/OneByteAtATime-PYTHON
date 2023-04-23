#Nested Repetition Structures
import os;
import random;

#---------------------------------------------------------------------------------------------------------------------------------------------------------
def Nesting_00():
    #A. Nested For loops with Lists NOT using range() and len()
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("A. Nested For loops with Lists NOT using range() and len()\n");

    Sizes = ["Small","Medium","Large"];
    Flavors = ["Orange","Grape","Cherry Coke","Peach","Strawberry","Vanilla Cream","Ginger"];

    Counter = 1;
    print("--------------------------------------------");
    for X in Sizes:
        Counter = 1;
        for Y in Flavors:
            print(Counter,". ",X," ",Y,sep='');
            Counter += 1;
        print("--------------------------------------------");
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Nesting_01():
    #B. Nested For loops with Lists USING range() and len()
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("B. Nested For loops with Lists USING range() and len()\n");

    Sizes = ["Small","Medium","Large"];
    Flavors = ["Orange","Grape","Cherry Coke","Peach","Strawberry","Vanilla Cream","Ginger"];

    print("--------------------------------------------");
    for X in Sizes:
        for Y in range(len(Flavors)):
            print((Y+1),". ",X," ",Flavors[Y],sep='');
        
        print("--------------------------------------------");
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Nesting_02():
    #C. Using Nested For Loops to Create a Multiplication Table
    os.system("cls");
    print("\nC. Using Nested For Loops to Create a Multiplication Table\n");

    for NUMBER in range(1,(10+1)):
        print("\n--------------------------------");
        print("Multipliers 1-12 for " + str(NUMBER));
        for MULTIPLIER in range(1,13):
            print(NUMBER, "*", MULTIPLIER, "=", (NUMBER*MULTIPLIER));
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Nesting_03():
    print("\nNesting FOR loops. 3 players get 3 6-sided dice rolls each.");
    
    for PLAYER in range(1,4):
        print("\n-----------------------------------------------");
        for ROLL in range(1,4):
            Lady_Luck = random.randint(1,6);
            print("Player " + str(PLAYER) + " rolls a " + str(Lady_Luck) + ".");
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Nesting_04():
    print("\nNesting WHILE TRUE loops. 3 players get 3 6-sided dice rolls each.");
    
    Num_Players = 3;
    Num_Rolls = 3;
    Player_Counter = 0;
    Roll_Counter = 0;

    while(Player_Counter < Num_Players):
        print("\n-----------------------------------------------");
        Player_Counter += 1;

        while(Roll_Counter < Num_Rolls):
              Lady_Luck = random.randint(1,6);
              print("Player " + str(Player_Counter) + " rolls a " + str(Lady_Luck) + ".");
              Roll_Counter += 1;
        
        Roll_Counter = 0; #MUST reset roll counter here for next iteration of Player_Counter
#---------------------------------------------------------------------------------------------------------------------------------------------------------



#Invocations
#Nesting_00();
#Nesting_01();
#Nesting_02();
#Nesting_03();
Nesting_04();


