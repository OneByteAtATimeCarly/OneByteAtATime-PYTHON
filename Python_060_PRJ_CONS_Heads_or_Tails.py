# Title: Project - Heads or Tails
# Author: C. S. Germany 01/06/2022 



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
def Heads_Or_Tails():
    import random;
    from os import system;
    system("cls");  
    
    Number_of_Coin_Tosses = 5;
    Toss_Counter = 0;
    Coin_Toss_Result = None;

    print("\nCoin Toss 1.0");

    while(Number_of_Coin_Tosses > 0):
          Coin_Toss_Result = random.randint(0,1);
          Toss_Counter = Toss_Counter + 1;
          print("\n     Coin toss #",Toss_Counter,": ",end='');

          if(Coin_Toss_Result == 0):
             print("HEADS");
          elif(Coin_Toss_Result == 1):
               print("TAILS");   
          else:
               print("Invalid value.");  

          Number_of_Coin_Tosses = Number_of_Coin_Tosses - 1;      
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



Heads_Or_Tails();
