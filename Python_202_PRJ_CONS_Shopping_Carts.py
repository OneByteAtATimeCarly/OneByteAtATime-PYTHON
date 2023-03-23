#Title: Carly's Calzones - a Puffy Purple Python Pizza Parlor (shopping cart using Lists)
#Author: Carly S. Germany
#Created: 01/06/2022 
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0

#GLOBALS --------------------------------------------------------------------------------------------------------------------------------------
from os import system,name;
Order_Choice = [];
Order_Cost = [];   
Order_Toppings = [];
Order_Toppings_Cost = [];


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Display_Order():

    system('cls');
    
    Items_Total = 0;
    Toppings_Total = 0;
    Item_Number = 0;
    Topping_Number = 0;

    print("\nItems in cart:");

    for x in Order_Choice:    
        Topping_Number = 0;
        print("\n---------------------------------------------------------------");     
        print("ITEM: ",(Item_Number+1),"\b.",x,"  Cost:",Order_Cost[(Item_Number)]);
        Items_Total = Items_Total + Order_Cost[Item_Number];

        NumToppings = len(Order_Toppings[Item_Number]);
        print("\n         ","There are",NumToppings,"toppings for this item:\n");

        for y in Order_Toppings[Item_Number]:
            print("         ",(Topping_Number+1),"\b.",y,"  Cost:",Order_Toppings_Cost[Item_Number][Topping_Number]);
            Toppings_Total = Toppings_Total + Order_Toppings_Cost[Item_Number][Topping_Number]; 
            Topping_Number = Topping_Number + 1;  
       
        Item_Number = Item_Number + 1; 
    
    Total_Cost = Items_Total + Toppings_Total;
    print("\n---------------------------------------------------------------"); 
    print("\nRunning Item Total:","$",Items_Total);
    print("Running Toppings Total:","$",Toppings_Total);
    print("Total Cost:","$",Total_Cost);        

    ContinueIT = input("\nENTER anything to continue:");
    ContinueIT = " ";
#----------------------------------------------------------------------------------------------------------------------------------------------      



#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Carlys_Calzones_Toppings():
    
    Toppings_Complete = "FALSE";
    Current_Toppings_Selection = [];
    Current_Toppings_Cost = [];

    while Toppings_Complete != "TRUE":
          print("\n--------------Toppings Menu---------------");
          print("|                                        |");
          print("|       (E)xtra Cheese         ($1)      |");
          print("|       (X)tra Sauce           ($0)      |");
          print("|       (B)lasphemous Pinapple ($5)      |");
          print("|       (T)omatoes             ($1)      |");
          print("|       (O)lives               ($1)      |");
          print("|       (G)reen Peppers        ($1)      |");
          print("|       (J)alapeños            ($1)      |");     
          print("|       (P)epperoni            ($2)      |");
          print("|       (S)ausage              ($2)      |");
          print("|       (H)am                  ($2)      |");
          print("|       (C)hicken              ($2)      |");
          print("|       (A)nchovies            ($2)      |");
          print("|       (Q)uit [Finished Toppings]       |");
          print("|                                        |");
          print("------------------------------------------","\n");
          CHOICE = input("Your choice: ");
          CHOICE = CHOICE.upper();

          if CHOICE == 'E': 
               Current_Toppings_Selection.append("Extra Cheese");
               Current_Toppings_Cost.append(1);
               print("Extra Cheese."); 
          elif CHOICE == 'X': 
               Current_Toppings_Selection.append("EXTRA Sauce");
               Current_Toppings_Cost.append(0);
               print("EXTRA Sauce");               
          elif CHOICE == 'B': 
               Current_Toppings_Selection.append("Blasphemous Pinapple");
               Current_Toppings_Cost.append(5);
               print("Blasphemous Pinapple.");
          elif CHOICE == 'T': 
               Current_Toppings_Selection.append("Tomatoes");
               Current_Toppings_Cost.append(1);               
               print("Tomatoes.");  
          elif CHOICE == 'O': 
               Current_Toppings_Selection.append("Olives");
               Current_Toppings_Cost.append(1);               
               print("Olives.");
          elif CHOICE == 'G': 
               Current_Toppings_Selection.append("Green Peppers");
               Current_Toppings_Cost.append(1);
               print("Green Peppers");
          elif CHOICE == 'J': 
               Current_Toppings_Selection.append("Jalapeños");
               Current_Toppings_Cost.append(1);
               print("Jalapeños.");
          elif CHOICE == 'P': 
               Current_Toppings_Selection.append("Pepperoni");
               Current_Toppings_Cost.append(2);               
               print("Pepperoni.");  
          elif CHOICE == 'S': 
               Current_Toppings_Selection.append("Sausage");
               Current_Toppings_Cost.append(2);               
               print("Sausage.");
          elif CHOICE == 'H': 
               Current_Toppings_Selection.append("Ham");
               Current_Toppings_Cost.append(2);
               print("Ham");
          elif CHOICE == 'C': 
               Current_Toppings_Selection.append("Chicken");
               Current_Toppings_Cost.append(2);               
               print("Chicken.");
          elif CHOICE == 'A': 
               Current_Toppings_Selection.append("Anchovies");
               Current_Toppings_Cost.append(2);
               print("Anchovies");               
          elif CHOICE == 'Q': 
               print("Toppings complete.");
               
               if len(Current_Toppings_Selection) < 1:
                  print("No toppings selected for this item.");
                  Current_Toppings_Selection.append("No toppings selected for this item.");
                  Current_Toppings_Cost.append(0);

               Toppings_Complete = "TRUE";                  
          else: 
               print("That choice was invalid. Please choose again.");

    Order_Toppings.append(Current_Toppings_Selection);
    Order_Toppings_Cost.append(Current_Toppings_Cost);       

#----------------------------------------------------------------------------------------------------------------------------------------------     

#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Carlys_Calzones_Main():
    
    system('cls');

    Order_Complete = "FALSE";   

    print("\nWelcome to Carly's Calzones!","\n");

    while Order_Complete != "TRUE":
          print("\n----------Product Menu------------");
          print("|                                   |");
          print("|       (S)mall Pizza               |");
          print("|       (M)edium Pizza              |");
          print("|       (L)arge Pizza               |");
          print("|       (B)read Sticks              |");
          print("|       (C)alzones                  |");
          print("|       (D)isplay Order             |");
          print("|       (Q)uit (complete order)     |");
          print("|                                   |");
          print("-------------------------------------","\n");
          CHOICE = input("Your choice: ");
          CHOICE = CHOICE.upper();

          if CHOICE == 'S': 
               Order_Choice.append("SMALL Pizza");
               Order_Cost.append(15);
               print("SMALL Pizza.");
               Carlys_Calzones_Toppings(); 
          elif CHOICE == 'M': 
               Order_Choice.append("MEDIUM Pizza");
               Order_Cost.append(20);
               print("MEDIUM Pizza.");
               Carlys_Calzones_Toppings(); 
          elif CHOICE == 'L': 
               Order_Choice.append("LARGE Pizza");
               Order_Cost.append(25);               
               print("LARGE Pizza.");
               Carlys_Calzones_Toppings();   
          elif CHOICE == 'B':   
               Order_Choice.append("Breadsticks");
               Order_Cost.append(5);               
               NO_Toppings_Selection = [];
               NO_Toppings_Cost = [];          
               NO_Toppings_Selection.append("Breadsticks have NO toppings.");
               NO_Toppings_Cost.append(0);
               Order_Toppings.append(NO_Toppings_Selection);
               Order_Toppings_Cost.append(NO_Toppings_Cost);             
               print("Breadsticks.");
          elif CHOICE == 'C': 
               Order_Choice.append("Calzone");
               Order_Cost.append(10);
               Order_Toppings.append("Breadsticks have NO toppings.");
               Order_Toppings_Cost.append(0);  
               print("Calzone");
               Carlys_Calzones_Toppings(); 
          elif CHOICE == 'D': 
               Display_Order();             
          elif CHOICE == 'Q': 
               Display_Order();
               print("\nOrder is complete. Exiting program.\n");
               Order_Complete = "TRUE";                 
          else: 
               print("That choice was invalid. Please choose again.") 


    print("\nThank you for choosing Carly's Calzones!\n");

#----------------------------------------------------------------------------------------------------------------------------------------------

#-----Function Invocations-----
Carlys_Calzones_Main();
#Carlys_Calzones_Toppings();