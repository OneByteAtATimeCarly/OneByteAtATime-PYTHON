#Title: Discord's Dungeon 02 - Coding Combat, Globals, Local vs. Global Scope in Functions and Classes
#Project: Discord's Dungeon - A Python Text-Based RPG
#Author: Carly Salali Germany
#Date: 01/19/2022
#Description: A project-based approach to teach the basic structures of Python by incorporating each new concept into a text-based RPG.


#Imports
from os import system,name;
import random,math;
import time;

#Globals
Player_Opponent = None;
Player_Heroine = None;


#Example: Basic Class with NO constuctor
#Class-------------------------------------------------------------------------------------------------------------------------------------------------------------------
class NPC:
      #Class Attributes
      NPC_Name = "Anonymous NPC";
      NPC_Health = 9000;
      NPC_Defense = 1000;
      NPC_Attack = 1000;

      #Member Methods
      def Display_NPC(self):
          print("\n     ","NPC Stats:");
          print("     ","NPC Name:",self.NPC_Name);
          print("     ","NPC Health:",self.NPC_Health);
          print("     ","NPC Defense:",self.NPC_Defense);
          print("     ","NPC Attack:",self.NPC_Attack); 

 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

#Another basic Class------------------------------------------------------------------------------------------------------------------------------------------------------
class Antagonist:
      #Class Attributes
      Antagonist_Name = "Anonymous Antagonist";
      Antagonist_Class = "Generic NPC";
      Antagonist_Health = 50;
      Antagonist_Defense = 5;
      Antagonist_Attack = 5;
      Antagonist_MP = 25;
      Antagonist_Ability_1 = "Warp SpaceTime";
      Antagonist_Ability_2 = "Improbability Materilization";
      Antagonist_Ability_3 = "Wish Projection";

      #Member Methods
      def Display_Antagonist(self):
          print("\n     ","Antagonist Stats:");
          print("     ","Name:",self.Antagonist_Name);
          print("     ","Class:",self.Antagonist_Class);
          print("     ","Health:",self.Antagonist_Health);
          print("     ","Defense:",self.Antagonist_Defense);
          print("     ","Attack:",self.Antagonist_Attack); 
          print("     ","MP:",self.Antagonist_MP);

      def Display_Abilities(self):
          print("\n     ","Antagonist Special Abilities:");
          print("     ","Ability 1:",self.Antagonist_Ability_1);
          print("     ","Ability 2:",self.Antagonist_Ability_2);
          print("     ","Ability 3:",self.Antagonist_Ability_3);     

 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 


#Example: PARENT (base) Class with CONSTRUCTOR (init method) and DEFAULT ARGUMENTS (can't overload constructors in Python)
#Class-------------------------------------------------------------------------------------------------------------------------------------------------------------------
class PONY:
      #Class Attributes
      PonyName = "Anonymous Pony";
      PonyClass = "Equestrian";
      Health = 100;
      Defense = 15;
      Attack = 10;
      MagicPower = 25;
   
      #Constructor (init method) with DEFAULT arguments
      def __init__(self, name=PonyName,pclass=PonyClass,health=Health,defense=Defense,attack=Attack,magicpower=MagicPower):
          self.PonyName = name;
          self.PonyClass = pclass;
          self.Health = health;
          self.Defense = defense;
          self.Attack = attack;
          self.MagicPower = magicpower;

      #Member Methods
      def Display_Pony(self):
          print("\n     ","PONY Stats:");
          print("     ","Name:",self.PonyName);
          print("     ","Class:",self.PonyClass);
          print("     ","Health:",self.Health);
          print("     ","Defense:",self.Defense);
          print("     ","Attack:",self.Attack);
          print("     ","MagicPower:",self.MagicPower);
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------      

#Example: CHILD (derived) Class that inherits from PARENT (base) class of PONY
#Class-------------------------------------------------------------------------------------------------------------------------------------------------------------------
class PRINCESS_PONY(PONY):
      #Class Attributes
      Princess_Power = 100;
      Princess_Charisma = 50;
      Princess_Ability_1 = "Telekinesis";
      Princess_Ability_2 = "Teleportation";
      Princess_Ability_3 = "Telepathy";
      Princess_Ability_4 = "Omni-Conversion";
      Princess_Ability_5 = "Friendship-casting";

      #Constructor sets PARENT (base) class values for this derived CHILD class
      def __init__(self):
          self.PonyClass = "Alicorn Princess Pony";
          self.Health = 32000;
          self.MagicPower = 32000;
          self.Defense = 500;
          self.Attack = 300;

      def Display_Abilities(self):
          print("\n     ","Princess Special Abilities:");
          print("     ","Ability 1:",self.Princess_Ability_1);
          print("     ","Ability 2:",self.Princess_Ability_2);
          print("     ","Ability 3:",self.Princess_Ability_3); 
          print("     ","Ability 4:",self.Princess_Ability_4); 
          print("     ","Ability 5:",self.Princess_Ability_5);     
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Create_Characters():   
    print("\n1. Instantiating an Opponent");
    Opponent = Antagonist();
    Opponent.Antagonist_Name = "Discord";
    Opponent.Antagonist_Class = "Supreme Agent of Chaos";
    Opponent.Antagonist_Health = 32000;
    Opponent.Antagonist_Defense = 300;
    Opponent.Antagonist_Attack = 500;
    Opponent.Antagonist_MP = 32000;
    Opponent.Display_Antagonist();
    Opponent.Display_Abilities();  
    globals()['Player_Opponent'] = Opponent;

    print("\n2. Instantiating a Heroine");
    Heroine = PRINCESS_PONY();
    Heroine.PonyName = "Celestia";
    Heroine.Display_Pony();
    Heroine.Display_Abilities();
    globals()['Player_Heroine'] = Heroine;

    ContinueIT = input("\nENTER anything to continue:");
    system('cls');
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Display_Combat_Stats():
    print("\n");
    print ("{:<14} {:<7} {:<7} {:<8} {:<11} {:<20}".format("Name","Health","Attack","Defense","MagicPower","Class"));
    print("---------------------------------------------------------------------------");
    print ("{:<14} {:<7} {:<7} {:<8} {:<11} {:<20}".format(Player_Opponent.Antagonist_Name,Player_Opponent.Antagonist_Health,Player_Opponent.Antagonist_Attack,Player_Opponent.Antagonist_Defense,Player_Opponent.Antagonist_MP,Player_Opponent.Antagonist_Class));
    print ("{:<14} {:<7} {:<7} {:<8} {:<11} {:<20}".format(Player_Heroine.PonyName,Player_Heroine.Health,Player_Heroine.Attack,Player_Heroine.Defense,Player_Heroine.MagicPower,Player_Heroine.PonyClass));
    print("\n");
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Pony_Combat():
    MinDammage = 500;
    MaxDammage = 10000;
    CurrentPlayer = "Nobody"; 
    RoundCounter = 1;
    ClearCounter = 0;

  #1.Display names of instantiated class objects engaging in combat using pointers to globals
    print("\nMagic Battle!!!",Player_Opponent.Antagonist_Name,"vs.",Player_Heroine.PonyName,"!");
    Display_Combat_Stats();                  
    time.sleep(2); 

  #2.Determine by random LUCK who gets 1st attack in sequence
    print("Flip a coin for who gets first attack. (HEADS = Heroine. TAILS = Antagonist.)");
    BlindChance = random.randint(1,2);

    if BlindChance == 1:
       CurrentPlayer = "Heroine"; 
       print("Result = Heads! What GOOD LUCK! Heroine gets 1st attack!");
    elif BlindChance == 2:
         CurrentPlayer = "Antagonist";
         print("Result = Tails! Such BAD luck. Opponent gets 1st attack!"); 
    else: print("\nERROR. This should never happen.");  
    
    time.sleep(4);
    system('cls');

  #3.Begin iterating through combat sequence. If either player's health = 0, combat over.
    while Player_Opponent.Antagonist_Health > 0 and Player_Heroine.Health > 0:      
          
          print("\nBeginning combat sequence round #:",RoundCounter); 
          time.sleep(2);

          #If player is HEROINE
          if CurrentPlayer == "Heroine":
             #Don't allow player any post-mortem attacks if lost combat sequence
             if Player_Heroine.Health > 0:
                print("\n------------------------------------------------------------------------------------");
                print(Player_Heroine.PonyName,"attacks",Player_Opponent.Antagonist_Name,"\b!");
                time.sleep(2);
                DAMMAGE = random.randint(MinDammage,MaxDammage);
                print(Player_Heroine.PonyName,"generates",DAMMAGE,"dammage.");
                time.sleep(2);
                ATK_Points = random.randint(10,Player_Heroine.Attack);
                print(Player_Heroine.PonyName,"'s attack skills add",ATK_Points,"to this magic dammage!");
                time.sleep(2);
                DAMMAGE = DAMMAGE + ATK_Points;
                DEF_Points = random.randint(10,Player_Opponent.Antagonist_Defense);
                print("But",Player_Opponent.Antagonist_Name,"defends themselves, blocking",DEF_Points,"dammage.");
                time.sleep(2);
                DAMMAGE = DAMMAGE - DEF_Points;
                print("The total resulting dammage dealt by",Player_Heroine.PonyName,"for this combat round is:",DAMMAGE);
                time.sleep(2);
                #prevent negative values of dammage which would actually ADD health to opponent
                if DAMMAGE < 0: DAMMAGE = 0;
                if (Player_Opponent.Antagonist_Health - DAMMAGE) < 0:
                   Player_Opponent.Antagonist_Health = 0;
                else:
                   Player_Opponent.Antagonist_Health = Player_Opponent.Antagonist_Health - DAMMAGE;
                CurrentPlayer = "Antagonist";
             else: print("\n",Player_Heroine.PonyName,"cannot attack anymore. She has LOST!");

          #If player is ANTAGONIST
          elif CurrentPlayer == "Antagonist":
               #Don't allow player any post-mortem attacks if lost combat sequence
               if Player_Opponent.Antagonist_Health > 0:
                  print("\n------------------------------------------------------------------------------------");
                  print(Player_Opponent.Antagonist_Name,"attacks",Player_Heroine.PonyName,"\b!");
                  time.sleep(2);
                  DAMMAGE = random.randint(MinDammage,MaxDammage);
                  print(Player_Opponent.Antagonist_Name,"generates",DAMMAGE,"dammage.");
                  time.sleep(2);
                  ATK_Points = random.randint(10,Player_Opponent.Antagonist_Attack);
                  print(Player_Opponent.Antagonist_Name,"'s attack skills add",ATK_Points,"to this magic dammage.");
                  time.sleep(2);
                  DAMMAGE = DAMMAGE + ATK_Points;
                  DEF_Points = random.randint(10,Player_Heroine.Defense);
                  print("But",Player_Heroine.PonyName,"defends themselves, blocking",DEF_Points,"dammage.");
                  time.sleep(2);
                  DAMMAGE = DAMMAGE - DEF_Points;
                  print("The total resulting dammage dealt by",Player_Opponent.Antagonist_Name,"for this combat round is:",DAMMAGE);
                  time.sleep(2);
                  #prevent negative values of dammage which would actually ADD health to opponent
                  if DAMMAGE < 0: DAMMAGE = 0;
                  if (Player_Heroine.Health - DAMMAGE) < 0:
                      Player_Heroine.Health = 0;
                  else:
                      Player_Heroine.Health = Player_Heroine.Health - DAMMAGE;
                  CurrentPlayer = "Heroine";
               else: print("\n",Player_Opponent.Antagonist_Name,"cannot attack anymore. They have LOST!");
         
          else: print("\nERROR. This should never happen."); 

          ClearCounter = ClearCounter + 1;
          RoundCounter = RoundCounter + 1;
          Display_Combat_Stats();
          time.sleep(3); 
          if ClearCounter == 2: 
            ClearCounter = 0;
            system('cls');

    print("\nMagic Battle Complete!");

    if Player_Heroine.Health > 0: print("\n",Player_Heroine.PonyName,"is victorious! She defeats",Player_Opponent.Antagonist_Name,"\b!");
    else: print("\n",Player_Opponent.Antagonist_Name,"is victorious! They defeat",Player_Heroine.PonyName,"\b!");

    Display_Combat_Stats();
          
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 


    



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Magic_Battle():
    Create_Characters();
    Pony_Combat();

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-----Invocations------
Magic_Battle();

