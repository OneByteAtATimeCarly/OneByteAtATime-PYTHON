#Title: Discord's Dungeon 01 - Coding a Class Hierarchy, Building Custom Objects and Re-Using Code by Employing Inheritance
#Project: Discord's Dungeon - A Python Text-Based RPG
#Author: Carly Salali Germany
#Date: 01/19/2022
#Description: A project-based approach to teach the basic structures of Python by incorporating each new concept into a text-based RPG.


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

      #Member Methods
      def Display_Antagonist(self):
          print("\n     ","Antagonist Stats:");
          print("     ","Antagonist Name:",self.Antagonist_Name);
          print("     ","Antagonist Class:",self.Antagonist_Class);
          print("     ","Antagonist Health:",self.Antagonist_Health);
          print("     ","Antagonist Defense:",self.Antagonist_Defense);
          print("     ","Antagonist Attack:",self.Antagonist_Attack); 
          print("     ","Antagonist MP:",self.Antagonist_MP);

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
      def DisplayPony(self):
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

      #Constructor sets PARENT (base) class values for this derived CHILD class
      def __init__(self):
          self.PonyClass = "Princess";
          self.MagicPower = 25000;
          self.Defense = 30000;
          self.Attack = 15000;

      def Display_Abilities(self):
          print("\n     ","Special Abilities:");
          print("     ","Ability 1:",self.Princess_Ability_1);
          print("     ","Ability 2:",self.Princess_Ability_2);    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Create_Characters():
    
    print("\n#1. Instantiating a BASIC class in Python");
    Agent_Smith = NPC();
    Agent_Smith.Display_NPC();

    print("\n#2. Instantiating a BASIC class in Python and setting data members");
    Discord = Antagonist();
    Discord.Antagonist_Name = "Discord";
    Discord.Antagonist_Class = "Supreme Agent of Chaos";
    Discord.Antagonist_Health = 32000;
    Discord.Antagonist_Defense = 32000;
    Discord.Antagonist_Attack = 32000;
    Discord.Antagonist_MP = 32000;
    Discord.Display_Antagonist();   

    print("\n#3. Instantiating a PARENT (base) class with a CONSTRUCTOR that uses DEFAULT ARGUMENTS when NO values are passed in");
    Fluttershy = PONY();
    Fluttershy.DisplayPony();

    print("\n#4. Instantiating a PARENT (base) class with a CONSTRUCTOR that uses DEFAULT ARGUMENTS WITH values passed in");
    Fluttershy = PONY("Fluttershy","Pegasus",1000,100,100,9000);
    Fluttershy.DisplayPony();

    print("\n#5. Setting attributes on an instantiated class object");
    RB_Dash = PONY();
    RB_Dash.PonyName = "Rainbow Dash";
    RB_Dash.PonyClass = "SuperPegasus";
    RB_Dash.Health = 9000;
    RB_Dash.Attack = 9000;
    RB_Dash.Defense = 9000;
    RB_Dash.DisplayPony();

    print("\n#6. Instantiating a CHILD (derived) class with a CONSTRUCTOR that uses DEFAULT ARGUMENTS WITH values passed in");
    Princess_Celeestia = PRINCESS_PONY();
    Princess_Celeestia.PonyName = "Celestia";
    Princess_Celeestia.DisplayPony();
    Princess_Celeestia.Display_Abilities();

    print("\n");
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#-----Invocations------
Create_Characters();
