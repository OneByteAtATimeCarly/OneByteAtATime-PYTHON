# Title: Classes 4 - Manipulating class objects and writing constructors that take DEFAULT arguments/parameters
# Author: C. S. Germany 01/15/2022

#Imports
from os import system,name;
import random,math;
import time;

#Globals
Player_One = None;
Player_Two = None;


#Class-------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Monster:
      #Class Attributes
      Monster_Name = "Anonymous Generic Base Class Monster";
      Monster_Health = 1000;
      Monster_Defense = 1000;
      Monster_Attack = 1000;
      Monster_Dexterity = 1000;
      Monster_Class = "Generic Monster";

      #Member Methods
      def Display_Monster(self):
          print("  ","--------------------Stats--------------------");
          print("  ","Name:",self.Monster_Name);
          print("  ","Health:",self.Monster_Health);
          print("  ","Defense:",self.Monster_Defense);
          print("  ","Attack:",self.Monster_Attack); 
          print("  ","Dexterity:",self.Monster_Dexterity);
          print("  ","Class:",self.Monster_Class ); 
 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Example: CHILD (derived) Class that inherits from PARENT (base) class of Monster
#Class-------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Reptilian(Monster):
      #Reptilian Class Attributes
      Scale_Armor = 3000;
      Nuclear_Lightning = 4500;

      #Constructor sets PARENT (base) class values for this derived CHILD class
      def __init__(self,Name="Generic Reptilian"):
          self.Monster_Name = Name;
          self.Monster_Health = 9000;
          self.Monster_Defense = 2000;
          self.Monster_Attack = 4000;
          self.Monster_Dexterity = 950;
          self.Monster_Class = "Reptilian";

      def Display_Reptilian_Abilities(self):
          print("\n  ","--------------Special Abilities--------------");
          print("  ","Scale Armor:",self.Scale_Armor);
          print("  ","Nuclear Lightning:",self.Nuclear_Lightning);    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Example: CHILD (derived) Class that inherits from PARENT (base) class of Monster
#Class-------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Winged_Insect(Monster):
      #Reptilian Class Attributes
      Evasive_Bilocation = 2000;
      Hurricane_Strike = 5000;

      #Constructor sets PARENT (base) class values for this derived CHILD class
      def __init__(self,Name="Generic Winged Insect"):
          self.Monster_Name = Name;
          self.Monster_Health = 7000;
          self.Monster_Defense = 1500;
          self.Monster_Attack = 2000;
          self.Monster_Dexterity = 9000;
          self.Monster_Class = "Winged Insect";

      def Display_Winged_Insect_Abilities(self):
          print("\n  ","--------------Special Abilities--------------");
          print("  ","Evasive Bilocation:",self.Evasive_Bilocation);
          print("  ","Hurricane Strike:",self.Hurricane_Strike);    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Create_Players():   

    print("\n1. Instantiating a Player_One object");
    Player_1 = Reptilian("Godzilla"); #This time passes name as argument into class CONSTRUCTOR
    Player_1.Display_Monster();
    Player_1.Display_Reptilian_Abilities();
    globals()['Player_One'] = Player_1;

    print("\n2. Instantiating a Player_Two object");
    Player_2 = Winged_Insect("Mothra"); #This time passes name as argument into class CONSTRUCTOR
    Player_2.Display_Monster();
    Player_2.Display_Winged_Insect_Abilities();
    globals()['Player_Two'] = Player_2;

    ContinueIT = input("\nENTER to continue:");
    system('cls');
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Display_Combat_Stats():
    print("\n");
    print ("{:<14} {:<8} {:<9} {:<8} {:<11} {:<20}".format("Name","Monster_Health","Defense","Attack","Dexterity","Class"));
    print("---------------------------------------------------------------------------");
    print ("{:<14} {:<8} {:<9} {:<8} {:<11} {:<20}".format(Player_Two.Monster_Name,Player_Two.Monster_Health,Player_Two.Monster_Defense,Player_Two.Monster_Attack,Player_Two.Monster_Dexterity,Player_Two.Monster_Class));
    print ("{:<14} {:<8} {:<9} {:<8} {:<11} {:<20}".format(Player_One.Monster_Name,Player_One.Monster_Health,Player_One.Monster_Defense,Player_One.Monster_Attack,Player_One.Monster_Dexterity,Player_One.Monster_Class));
    print("\n");
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Monster_Combat():
    MinDammage = 500;
    MaxDammage = 10000;
    CurrentPlayer = "Nobody"; 
    RoundCounter = 1;
    ClearCounter = 0;

  #1.Display names of instantiated class objects engaging in combat using pointers to globals
    print("\nMagic Battle!!!",Player_One.Monster_Name,"vs.",Player_Two.Monster_Name,"!");
    Display_Combat_Stats();                  
    time.sleep(2); 

  #2.Determine by random LUCK who gets 1st attack in sequence
    print("Flip a coin for who gets first attack. (HEADS = Heroine. TAILS = Antagonist.)");
    BlindChance = random.randint(1,2);

    if BlindChance == 1:
       CurrentPlayer = "Player_One"; 
       print("Result = Heads! What GOOD LUCK! Player_One gets 1st attack!");
    elif BlindChance == 2:
         CurrentPlayer = "Player_Two";
         print("Result = Tails! Such BAD luck. Player_Two gets 1st attack!"); 
    else: print("\nERROR. This should never happen.");  
    
    time.sleep(4);
    system('cls');

  #3.Begin iterating through combat sequence. If either player's Monster_Health = 0, combat over.
    while Player_One.Monster_Health > 0 and Player_Two.Monster_Health > 0:      
          
          print("\nBeginning combat sequence round #:",RoundCounter); 
          time.sleep(2);

          #If player is Player_One
          if CurrentPlayer == "Player_One":
             #Don't allow player any post-mortem attacks if lost combat sequence
             if Player_One.Monster_Health > 0:
                print("\n------------------------------------------------------------------------------------");
                print(Player_One.Monster_Name,"attacks",Player_Two.Monster_Name,"\b!");
                time.sleep(2);
                DAMMAGE = random.randint(MinDammage,MaxDammage);
                print(Player_One.Monster_Name,"generates",DAMMAGE,"dammage.");
                time.sleep(2);
                ATK_Points = random.randint(10,Player_One.Monster_Attack);
                print(Player_One.Monster_Name,"'s attack skills add",ATK_Points,"to this magic dammage!");
                time.sleep(2);
                DAMMAGE = DAMMAGE + ATK_Points;
                DEF_Points = random.randint(10,Player_Two.Monster_Defense);
                print("But",Player_Two.Monster_Name,"defends themselves, blocking",DEF_Points,"dammage.");
                time.sleep(2);
                DAMMAGE = DAMMAGE - DEF_Points;
                print("The total resulting dammage dealt by",Player_One.Monster_Name,"for this combat round is:",DAMMAGE);
                time.sleep(2);
                #prevent negative values of dammage which would actually ADD Monster_Health to opponent
                if DAMMAGE < 0: DAMMAGE = 0;
                if (Player_Two.Monster_Health - DAMMAGE) < 0:
                   Player_Two.Monster_Health = 0;
                else:
                   Player_Two.Monster_Health = Player_Two.Monster_Health - DAMMAGE;
                CurrentPlayer = "Antagonist";
             else: print("\n",Player_One.Monster_Name,"cannot attack anymore. She has LOST!");

          #If player is Player_Two
          elif CurrentPlayer == "Player_Two":
               #Don't allow player any post-mortem attacks if lost combat sequence
               if Player_Two.Monster_Health > 0:
                  print("\n------------------------------------------------------------------------------------");
                  print(Player_Two.Monster_Name,"attacks",Player_One.Monster_Name,"\b!");
                  time.sleep(2);
                  DAMMAGE = random.randint(MinDammage,MaxDammage);
                  print(Player_Two.Monster_Name,"generates",DAMMAGE,"dammage.");
                  time.sleep(2);
                  ATK_Points = random.randint(10,Player_Two.Monster_Attack);
                  print(Player_Two.Monster_Name,"'s attack skills add",ATK_Points,"to this magic dammage.");
                  time.sleep(2);
                  DAMMAGE = DAMMAGE + ATK_Points;
                  DEF_Points = random.randint(10,Player_One.Monster_Defense);
                  print("But",Player_One.Monster_Name,"defends themselves, blocking",DEF_Points,"dammage.");
                  time.sleep(2);
                  DAMMAGE = DAMMAGE - DEF_Points;
                  print("The total resulting dammage dealt by",Player_Two.Monster_Name,"for this combat round is:",DAMMAGE);
                  time.sleep(2);
                  #prevent negative values of dammage which would actually ADD Monster_Health to opponent
                  if DAMMAGE < 0: DAMMAGE = 0;
                  if (Player_One.Monster_Health - DAMMAGE) < 0:
                      Player_One.Monster_Health = 0;
                  else:
                      Player_One.Monster_Health = Player_One.Monster_Health - DAMMAGE;
                  CurrentPlayer = "Heroine";
               else: print("\n",Player_Two.Monster_Name,"cannot attack anymore. They have LOST!");
         
          else: print("\nERROR. This should never happen."); 

          ClearCounter = ClearCounter + 1;
          RoundCounter = RoundCounter + 1;
          Display_Combat_Stats();
          time.sleep(3); 
          if ClearCounter == 2: 
            ClearCounter = 0;
            system('cls');

    print("\nMagic Battle Complete!");

    if Player_One.Monster_Health > 0: print("\n",Player_One.Monster_Name,"is victorious! They defeat",Player_Two.Monster_Name,"\b!");
    else: print("\n",Player_Two.Monster_Name,"is victorious! They defeat",Player_One.Monster_Name,"\b!");

    Display_Combat_Stats();
          
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 


#-----Invocations-----
Create_Players();
#Display_Combat_Stats();
Monster_Combat();




