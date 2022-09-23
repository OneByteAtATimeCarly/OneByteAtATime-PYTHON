# Title: Project - Paint Area Calculator
# Author: C. S. Germany 01/06/2022 


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
def Paint_Area_Calculator():
    import random;
    from os import system;
    system("cls"); 

    Sq_Meters_Per_Can = 5;
    
    print("\nPaint Area calculator 1.0");

    Wall_HEIGHT = int(input("Please enter wall HEIGHT: "));
    Wall_WIDTH = int(input("Please enter wall WIDTH: "));

    print("\nWall HEIGHT = ",Wall_HEIGHT);
    print("Wall WIDTH = ",Wall_WIDTH);
    Surface_Area_to_Cover = Wall_HEIGHT * Wall_WIDTH;
    print("\nCurrent surface area to cover:",Surface_Area_to_Cover,"sq meters.");
    print("Current paint can capacity: 1 paint can covers",Sq_Meters_Per_Can,"sq meters.\n");
    Num_Paint_Cans = round((Surface_Area_to_Cover / Sq_Meters_Per_Can),0); #round since can buy fractions of paint cans
    Num_Paint_Cans = int(Num_Paint_Cans); #get rid of decimals
    print("Number of paint cans required:",Num_Paint_Cans);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


Paint_Area_Calculator();

