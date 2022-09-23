# Title: Project - Banker Roulette
# Author: C. S. Germany 01/06/2022 

#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#1. Using Array of fixed size
def Banker_Roulette1():
    import random;
    from os import system;
    system("cls"); 

    List_of_Names = ["Carly",
                     "Eric",
                     "Kyle",
                     "Roland",
                     "Justin"];
    
    Number_of_Tries = 5;
    Try_Counter = 0;
    Person_Who_Pays = None;

    print("\nBanker Roulette1 1.0");
    print("Number of names in list: ",(len(List_of_Names)));

    while(Number_of_Tries > 0):
          Person_Who_Pays = random.randint(0,(len(List_of_Names)-1));
          Try_Counter = Try_Counter + 1;
          print("\n     Try #",Try_Counter,": ",end='');
          print("Random number:",Person_Who_Pays,"  ",List_of_Names[Person_Who_Pays],"pays for lunch today.");
          Number_of_Tries = Number_of_Tries - 1;      

#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#2. Using Dynamic Array and Append (List)
def Banker_Roulette2():
    import random;
    from os import system;
    system("cls"); 

    PersonName = None;
    List_of_Names = [];

    print("\nBanker Roulette2 1.0");

    while(PersonName != "0"):
          PersonName = input("Enter name: (0 to quit) : ");
          if(PersonName != "0"):
             List_of_Names.append(PersonName);
    
    Number_of_Tries = 5;
    Try_Counter = 0;
    Person_Who_Pays = None;

    print("\nNumber of names in list: ",(len(List_of_Names)),"\n");

    while(Number_of_Tries > 0):
          Person_Who_Pays = random.randint(0,(len(List_of_Names)-1));
          Try_Counter = Try_Counter + 1;
          print("\n     Try #",Try_Counter,": ",end='');
          print("Random number:",Person_Who_Pays,"  ",List_of_Names[Person_Who_Pays],"pays for lunch today.");
          Number_of_Tries = Number_of_Tries - 1; 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#3. Using split() method to parse string and store in array. Default separator is whitespace. You can also SPECIFY the separator.
def Banker_Roulette3():
    import random;
    from os import system;
    system("cls"); 

    The_Names = input("Enter names separated by comma and space: "); 

    List_of_Names = The_Names.split(", ");

    Number_of_Tries = 5;
    Try_Counter = 0;
    Person_Who_Pays = None;

    print("\nNumber of names in list: ",(len(List_of_Names)),"\n");

    while(Number_of_Tries > 0):
          Person_Who_Pays = random.randint(0,(len(List_of_Names)-1));
          Try_Counter = Try_Counter + 1;
          print("\n     Try #",Try_Counter,": ",end='');
          print("Random number:",Person_Who_Pays,"  ",List_of_Names[Person_Who_Pays],"pays for lunch today.");
          Number_of_Tries = Number_of_Tries - 1;     
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#4. Using the Python choice function. The built-in choice() method returns a random item from a list, tuple, or string.
def Banker_Roulette4():
    import random;
    from os import system;
    system("cls");   

    List_of_Names = ["Carly",
                     "Eric",
                     "Kyle",
                     "Roland",
                     "Justin"];

    print(random.choice(List_of_Names));
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#-----Invocations-----
#Banker_Roulette1();
#Banker_Roulette2();
#Banker_Roulette3();
Banker_Roulette4();

