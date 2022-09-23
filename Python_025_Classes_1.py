# Title: Classes 1 - Defining, Instantiating, Accessing Data Members
# Author: C. S. Germany 01/15/2022

#Class-------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Monster:
      #Class Attributes
      Monster_Name = "Anonymous Generic Base Class Monster";
      Monster_Health = 1000;
      Monster_Defense = 1000;
      Monster_Attack = 1000;
      Monster_Dexterity = 1000;

      #Member Methods
      def Display_Monster(self):
          print("  ","--------------------Stats--------------------");
          print("  ","Name:",self.Monster_Name);
          print("  ","Health:",self.Monster_Health);
          print("  ","Defense:",self.Monster_Defense);
          print("  ","Attack:",self.Monster_Attack); 
          print("  ","Dexterity:",self.Monster_Dexterity); 
 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 


Generic_Monster = Monster();

Godzilla = Monster();
Godzilla.Monster_Name = "Godzilla";
Godzilla.Monster_Health = 9000;
Godzilla.Monster_Defense = 2000;
Godzilla.Monster_Attack = 4000;
Godzilla.Monster_Dexterity = 950;

Mothra = Monster();
Mothra.Monster_Name = "Mothra";
Mothra.Monster_Health = 7000;
Mothra.Monster_Defense = 1500;
Mothra.Monster_Attack = 2000;
Mothra.Monster_Dexterity = 9000;

print("\nA. Generic Monster");
Generic_Monster.Display_Monster();

print("\nB. Godzilla");
Godzilla.Display_Monster();

print("\nC. Mothra");
Mothra.Display_Monster();

