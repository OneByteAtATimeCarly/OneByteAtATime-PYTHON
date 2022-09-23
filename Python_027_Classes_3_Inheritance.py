# Title: Classes 3 - Inheritance, re-using code and creating class hierarchies
# Author: C. S. Germany 01/15/2022

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
      def __init__(self):
          self.Monster_Name = "Generic Reptilian";
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
      def __init__(self):
          self.Monster_Name = "Generic Winged Insect";
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


Generic_Monster = Monster();
Godzilla = Reptilian();
Mothra = Winged_Insect();

print("\nA. Generic Monster");
Generic_Monster.Display_Monster();

print("\nB. Godzilla");
Godzilla.Monster_Name = "Godzilla";
Godzilla.Display_Monster();
Godzilla.Display_Reptilian_Abilities();

print("\nC. Mothra");
Mothra.Monster_Name = "Mothra";
Mothra.Display_Monster();
Mothra.Display_Winged_Insect_Abilities();

