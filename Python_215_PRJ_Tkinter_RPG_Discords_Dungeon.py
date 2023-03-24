#Title: Discord's Dungeon - A Python tkinter Role Playing Game
#Author: Carly S. Germany
#Created: 09/08/2022
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0

#Note: PlaySound is a very simple module that can play WAV files and MP3s in Python. 
# The FIRST time you want to use Python's PlaySound module, you must install it into your IDE using:
# Example: pip install playsound
# Then RESTART Visual Studio Code or terminal.
# Then just import it with: from playsound import playsound

#Note: To keep game and GUI responsive when you call playsound, you must play each sound in a different thread from mainloop().
      # Also, the new version of playsound is broken and doesn't work right with multi-threading. Old version is better. To remedy this:
      # pip uninstall playsound
      # pip install playsound==1.2.2

#Imports
import tkinter as tk;
import tkinter.messagebox as MB;
from PIL import ImageTk,Image;
import os;
from os import system;
from playsound import playsound;
import threading;
import time;
import random;


#-----GUI Globals------------------------------------------------------------------------------------------------------------------------
window = tk.Tk();
window.title("Python tkinter RPG - Discord\'s Dungeon 1.0 - 2022 - Carly Salali Germany");     
window_Width = 1050;
window_Height = 765;
ScreenWidth = window.winfo_screenwidth();
ScreenHeight = window.winfo_screenheight();
Appear_in_the_Middle = '%dx%d+%d+%d' % (window_Width, window_Height, (ScreenWidth - window_Width) / 2, (ScreenHeight - window_Height) / 2);
window.geometry(Appear_in_the_Middle);
window.resizable(width=False, height=False);
window.configure(bg='white');  
GUI = None;  #pointer that will be used to reference GUI class for functions (instantiated later)



#CLASS: Game_Entity: BEGIN********************************************************************************************************************************************
#Prime Parent (base) Class in Inheritance Hierarchy
class Game_Entity:
      #Class Attributes 
      EntityName = "Anonymous Entity";
      EntityGender = "Female";
      EntityClass = "Undetermined";      
      EntityHealth = 50;
      EntityDefense = 5;
      EntityAttack = 5;
      EntityMagicPower = 10;
      EntityDexterity = 10;
      EntityCharisma = 15;
      EntityLevel = 1;
      EntityCombatExp = 0;
      EntityMoney = 3000;
      WeaponChoice = "None";
      MagicChoice= "None";
      ArmorChoice = "None";
      Invisibility_Active = "FALSE";
      Invisibility_Count = 0;
      FirstTimeShowOpponentInfo = "TRUE";
      
      #Initial Weapon Dammage
      Dammage_Item_Staff = 10;
      Dammage_Item_Pendant = 15;
      Dammage_Item_Sigil = 20;
      Dammage_Item_Orb = 25;
      Dammage_Item_PrincessCloak = 30;
      Dammage_Item_Slingshot = 5;
      Dammage_Skill_IceBlasts = 10;
      Dammage_Skill_FireBalls = 20;
      Dammage_Skill_Lightning = 30;
      Dammage_Skill_Telekinesis = 40;
      Dammage_Skill_Telepathy = 50;
      Dammage_Skill_Teleportation = 60;
      Dammage_Skill_TimeWarp = 70;
      Invisibility_DEF_Amt = 2000;
      DEF_Item_Chain_Mail = 5;
      DEF_Item_Plate_Armor = 10;

      #Inventory Items
      INV_Has_Slingshot = "FALSE";
      Slingshot_Pellets_Amt = 0;
      INV_Has_Staff = "FALSE";
      INV_Has_Pendant = "FALSE";
      INV_Has_Sigil = "FALSE";
      INV_Has_Orb = "FALSE";
      INV_Has_PrincessCloak = "FALSE";
      INV_Has_HealingPotions = 0;
      HealthPotion_Restore_Amt = 100;
      INV_Has_Chain_Mail = "FALSE";
      INV_Has_Plate_Armor = "FALSE"; 

      #Non-combat inventory items
      INV_Has_Grooming_Brush = "FALSE";
      INV_Has_FairyTorch = "FALSE";
      INV_Has_HempRope = "FALSE";
      INV_Has_ClimbingCleats = "FALSE"; 
      INV_Has_NotepadAndPen = "FALSE";     

      #Magic Skills
      SKILL_Has_IceBlasts = "FALSE";
      SKILL_Has_FireBalls = "FALSE";
      SKILL_Has_Lightning = "FALSE";
      SKILL_Has_Telekinesis = "FALSE";
      SKILL_Has_Telepathy = "FALSE";
      SKILL_Has_Teleportation = "FALSE";
      SKILL_Has_TimeWarp = "FALSE";
      SKILL_Has_Invisibility = "FALSE";
      SKILL_Invisibility_Cost = 300;
      SKILL_Has_Healing = "FALSE";
      SKILL_Healing_Restore_Amt = 100;
      SKILL_Has_FriendshipCast = "FALSE";


    #MemberMethod---------------------------------------------------------------------------------------------------------------
      def Cheat_Mode(self): 
          #Give player "god mode" level health and attributes 
          self.EntityHealth = 32000;
          self.EntityDefense = 20000;
          self.EntityAttack = 20000;
          self.EntityMagicPower = 32000;
          self.EntityDexterity = 20000;
          self.EntityCharisma = 30000;
          self.EntityLevel = 9000;
          self.EntityCombatExp = 31000;
          #Greatly increase dmg done by weapons and def by armore
          self.Dammage_Item_Slingshot = 50;
          self.Dammage_Item_Staff = 100;
          self.Dammage_Item_Pendant = 150;
          self.Dammage_Item_Sigil = 200;
          self.Dammage_Item_Orb = 250;
          self.Dammage_Item_PrincessCloak = 300;
          self.DEF_Item_Chain_Mail = 500;
          self.DEF_Item_Plate_Armor = 1000;
          #Greatly increase dmg from magic skills
          self.Dammage_Skill_IceBlasts = 100;
          self.Dammage_Skill_FireBalls = 200;
          self.Dammage_Skill_Lightning = 300;
          self.Dammage_Skill_Telekinesis = 400;
          self.Dammage_Skill_Telepathy = 500;
          self.Dammage_Skill_Teleportation = 600;
          self.Dammage_Skill_TimeWarp = 700;
          self.Invisibility_DEF_Amt = 10000;
          #Increase money
          self.EntityMoney = 32000;
          #Grant player all weapons, armor and magic items
          self.INV_Has_Slingshot = "TRUE";
          self.Slingshot_Pellets_Amt = 20000;
          self.INV_Has_Staff = "TRUE";
          self.INV_Has_Pendant = "TRUE";
          self.INV_Has_Sigil = "TRUE";
          self.INV_Has_Orb = "TRUE";
          self.INV_Has_PrincessCloak = "TRUE";
          self.INV_Has_HealingPotions = 5000;
          self.HealthPotion_Restore_Amt = 300;
          self.INV_Has_Chain_Mail = "TRUE";
          self.INV_Has_Plate_Armor = "TRUE";
          self.INV_Has_FairyTorch = "FALSE";
          self.INV_Has_HempRope = "FALSE";
          self.INV_Has_ClimbingCleats = "FALSE"; 
          self.INV_Has_NotepadAndPen = "FALSE"; 
          self.DEF_Item_Chain_Mail = 1000;
          self.DEF_Item_Plate_Armor = 5000;
          #Grant player all magic skills
          self.SKILL_Has_IceBlasts = "TRUE";
          self.SKILL_Has_FireBalls = "TRUE";
          self.SKILL_Has_Lightning = "TRUE";
          self.SKILL_Has_Telekinesis = "TRUE";
          self.SKILL_Has_Telepathy = "TRUE";
          self.SKILL_Has_Teleportation = "TRUE";
          self.SKILL_Has_TimeWarp = "TRUE";
          self.SKILL_Has_Invisibility = "TRUE";
          self.SKILL_Has_Healing = "TRUE";
          self.SKILL_Healing_Restore_Amt = 1000;
          self.SKILL_Has_FriendshipCast = "TRUE";
          self.WeaponChoice = "Orb";
          self.MagicChoice= "Telekinesis";
          self.ArmorChoice = "PlateArmor";
          self.Invisibility_Active = "TRUE";
          self.Invisibility_Count = 3;
          #Grant all non-combat Inventory Items         
          self.INV_Has_Grooming_Brush = "TRUE";
          self.INV_Has_FairyTorch = "TRUE";
          self.INV_Has_HempRope = "TRUE";
          self.INV_Has_ClimbingCleats = "TRUE"; 
          self.INV_Has_NotepadAndPen = "TRUE";            

    #END-MemberMethod-Cheat_Mode---------------------------------------------------------------------------------------------          


    #MemberMethod---------------------------------------------------------------------------------------------------------------
      def Display_Entity(self):     
          GUI.LAB_Name_Output.configure(text=self.EntityName);
          GUI.LAB_Gender_Output.configure(text=self.EntityGender);
          GUI.LAB_Class_Output.configure(text=self.EntityClass);
          GUI.LAB_Health_Output.configure(text=str(self.EntityHealth));
          GUI.LAB_Mag_Eng_Output.configure(text=str(self.EntityMagicPower));
          GUI.LAB_Attack_Output.configure(text=str(self.EntityAttack));
          GUI.LAB_Defense_Output.configure(text=str(self.EntityDefense));
          GUI.LAB_Armor_Output.configure(text=self.ArmorChoice);
          GUI.LAB_Weapon_Output.configure(text=self.WeaponChoice);
          GUI.LAB_Magic_Output.configure(text=self.MagicChoice);
          GUI.LAB_Money_Output.configure(text=str(self.EntityMoney));
          GUI.LAB_Charisma_Output.configure(text=str(self.EntityCharisma));
          GUI.LAB_Combat_Exp_Output.configure(text=str(self.EntityLevel));
          GUI.LAB_Level_Output.configure(text=str(self.EntityCombatExp));                        
    #END-MemberMethod-Display_Entity---------------------------------------------------------------------------------------------


    #MemberMethod---------------------------------------------------------------------------------------------------------------
      def Display_As_Opponent(self):
          GUI.Text_Append("Name: " + self.EntityName);
          GUI.Text_Append("Class: " + self.EntityClass + "     Gender: " + self.EntityGender);
          GUI.Text_Append("Health: " + str(self.EntityHealth) + "            MP: " + str(self.EntityMagicPower));
          GUI.Text_Append("ATK: " + str(self.EntityAttack) + "                DEF: " + str(self.EntityDefense));
          GUI.Text_Append("DEX: " + str(self.EntityDexterity) + "              CHAR " + str(self.EntityCharisma));
          GUI.Text_Append("Armor Choice: " + self.ArmorChoice);
          GUI.Text_Append("Weapon Choice: " + self.WeaponChoice);
          GUI.Text_Append("Magic Choice: " + self.MagicChoice);
          GUI.Text_Append("LVL: " + str(self.EntityLevel) + "              EXP: " + str(self.EntityCombatExp));

    #END-MemberMethod-Display_Opponent------------------------------------------------------------------------------------------

    #MemberMethod---------------------------------------------------------------------------------------------------------------
      def Display_Character(self):
          self.Display_Entity();
          STATS = "\n--------------------Current Character Stats--------------------";
          STATS += "\nSelected Weapon: ";
          if self.WeaponChoice == "None": 
             STATS = STATS + "Nothing but ";
             if self.EntityGender == "Female": STATS = STATS + "her";
             elif self.EntityGender == "Male": STATS = STATS + "his";
             STATS = STATS + " hooves!";
          elif self.WeaponChoice == "Slingshot": STATS = STATS + "Slingshot" + "   +ATK:" + str(self.Dammage_Item_Slingshot);   
          elif self.WeaponChoice == "Staff": STATS = STATS + "Staff" + "   +ATK:" + str(self.Dammage_Item_Staff);
          elif self.WeaponChoice == "Pendant": STATS = STATS + "Pendant"  + "   +ATK:" + str(self.Dammage_Item_Pendant);
          elif self.WeaponChoice == "Sigil": STATS = STATS + "Sigil"  + "   +ATK:" + str(self.Dammage_Item_Sigil);
          elif self.WeaponChoice == "Orb": STATS = STATS + "Power Orb"  + "   +ATK:" + str(self.Dammage_Item_Orb);
          elif self.WeaponChoice == "PrincessCloak": STATS = STATS + "PrincessCloak"  + "   +ATK:" + str(self.Dammage_Item_PrincessCloak);
          GUI.Text_Append(STATS);

          STATS = "Selected Armor: ";
          if self.ArmorChoice == "None": 
             STATS = STATS + "Nothing but ";
             if self.EntityGender == "Female": STATS = STATS + "her";
             elif self.EntityGender == "Male": STATS = STATS + "his";
             STATS = STATS + " birthday suit.";
          elif self.ArmorChoice == "ChainMail": STATS = STATS + "Link Chain Mail" + "   +DEF:" + str(self.DEF_Item_Chain_Mail);
          elif self.ArmorChoice == "PlateArmor": STATS = STATS + "Plate Armor" + "   +DEF:" + str(self.DEF_Item_Plate_Armor);   
          GUI.Text_Append(STATS);
          
          STATS = "Selected Magic: ";
          if self.MagicChoice == "None": 
             STATS = STATS + "Nothing but ";
             if self.EntityGender == "Female": STATS = STATS + "her";
             elif self.EntityGender == "Male": STATS = STATS + "his";
             STATS = STATS + " wits!";
          elif self.MagicChoice == "IceBlasts": STATS = STATS + "Ice Blasts" + "   +ATK:" + str(self.Dammage_Skill_IceBlasts);
          elif self.MagicChoice == "FireBalls": STATS = STATS + "Fire Balls" + "   +ATK:" + str(self.Dammage_Skill_FireBalls);            
          elif self.MagicChoice == "Lightning": STATS = STATS + "Lightning" + "   +ATK:" + str(self.Dammage_Skill_Lightning);
          elif self.MagicChoice == "Telekinesis": STATS = STATS + "Telekinesis" + "     +ATK:" + str(self.Dammage_Skill_Telekinesis);
          elif self.MagicChoice == "Telepathy": STATS = STATS + "Telepathy" + "   +ATK:" + str(self.Dammage_Skill_Telepathy);
          elif self.MagicChoice == "Teleportation": STATS = STATS + "Teleportation" + "   +ATK:" + str(self.Dammage_Skill_Teleportation);
          elif self.MagicChoice == "TimeWarp": STATS = STATS + "Time Warp" + "   +ATK:" + str(self.Dammage_Skill_TimeWarp);
          elif self.MagicChoice == "Invisibility": STATS = STATS + "Invisibility";
          elif self.MagicChoice == "Healing": STATS = STATS + "Healing"; 
          elif self.MagicChoice == "FriendshipCast": STATS = STATS + "Friendship Cast";
          GUI.Text_Append(STATS);

          MESSAGE = "";
          if(self.Invisibility_Active == "TRUE"):
             MESSAGE += "Invisibility: Active      [Remaining:" + str(self.Invisibility_Count) + "]   [+DEF:" + str(self.Invisibility_DEF_Amt) + "]"; 
          else: MESSAGE += "Invisibility: Inactive";   
          GUI.Text_Append(MESSAGE);
    #END-MemberMethod-Display_Character------------------------------------------------------------------------------------------------    

    #MemberMethod---------------------------------------------------------------------------------------------------------------
      def Inventory_Display(self):
          Inv_Array = ["NOTHING"];
          MESSAGE = "\n-----------------------Current Inventory-----------------------";
          if(self.INV_Has_Staff == "FALSE" and self.INV_Has_Pendant == "FALSE" and self.INV_Has_Sigil == "FALSE" and self.INV_Has_Orb == "FALSE" and 
             (self.INV_Has_HealingPotions <= 0) and self.INV_Has_Chain_Mail == "FALSE" and self.INV_Has_Plate_Armor == "FALSE" and
              self.INV_Has_Slingshot == "FALSE" and self.Slingshot_Pellets_Amt <= 0 and self.INV_Has_Grooming_Brush == "FALSE" and
              self.INV_Has_FairyTorch == "FALSE" and self.INV_Has_HempRope == "FALSE" and self.INV_Has_ClimbingCleats == "FALSE" and
              self.INV_Has_NotepadAndPen == "FALSE"):
              MESSAGE += "\n" + self.EntityName + " has abolutely NOTHING! Not a single thing.\nNothing at all. A big NOPE. Go FIND something!";
              Inv_Array.append("Absolutely NOTHING");
          else:   
                InvCount = 0;
                if(self.INV_Has_Slingshot == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Slingshot [" + str(self.Slingshot_Pellets_Amt) + "]");
                   MESSAGE += "\n " + str(InvCount) + ". Slingshot [pellets:" + str(self.Slingshot_Pellets_Amt) + "]    ATK+"+ str(self.Dammage_Item_Staff);
                if(self.INV_Has_Staff == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Staff");
                   MESSAGE += "\n " + str(InvCount) + ". Staff                            ATK+"+ str(self.Dammage_Item_Staff);
                if(self.INV_Has_Pendant == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Pendant");
                   MESSAGE += "\n" + str(InvCount) + ". Pendant                         ATK+" + str(self.Dammage_Item_Pendant);
                if(self.INV_Has_Sigil == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Magic Sigil");
                   MESSAGE += "\n" + str(InvCount) + ". Magic Sigil                    ATK+" + str(self.Dammage_Item_Sigil);
                if(self.INV_Has_Orb == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Orb of Power");
                   MESSAGE += "\n" + str(InvCount) + ". Orb of Power                ATK+" + str(self.Dammage_Item_Orb);
                if(self.INV_Has_PrincessCloak == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Princess Cloak");
                   MESSAGE += "\n" + str(InvCount) + ". Cloak of Princessness     ATK+" + str(self.Dammage_Item_PrincessCloak);
                if(self.INV_Has_HealingPotions > 0):
                   InvCount = InvCount + 1;
                   Inv_Array.append(("Healing Potions: " + str(self.INV_Has_HealingPotions)));
                   MESSAGE += "\n" + str(InvCount) + ". Healing Potions:             Health+" + str(self.HealthPotion_Restore_Amt) + "   Amt:" + str(self.INV_Has_HealingPotions);
                if(self.INV_Has_Chain_Mail == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Chain Mail");
                   MESSAGE += "\n" + str(InvCount) + ". Chain Mail                    DEF+" + str(self.DEF_Item_Chain_Mail);
                if(self.INV_Has_Plate_Armor == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Plate Armor");
                   MESSAGE += "\n" + str(InvCount) + ". Plate Armor                  DEF+" + str(self.DEF_Item_Plate_Armor);
                #Non-combat Inventory items
                if(self.INV_Has_Grooming_Brush == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Grooming Brush (non-cmbt)");
                   MESSAGE += "\n" + str(InvCount) + ". Grooming Brush (non-combat)";
                if(self.INV_Has_FairyTorch == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Fairy Torch (non-cmbt)");
                   MESSAGE += "\n" + str(InvCount) + ". Fairy Torch (non-combat)";
                if(self.INV_Has_HempRope == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Hemp Rope (non-cmbt)");
                   MESSAGE += "\n" + str(InvCount) + ". Hemp Rope (non-combat)";
                if(self.INV_Has_ClimbingCleats == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Climbing Cleats (non-cmbt)");
                   MESSAGE += "\n" + str(InvCount) + ". Climbing Cleats (non-combat)";
                if(self.INV_Has_NotepadAndPen == "TRUE"):
                   InvCount = InvCount + 1;
                   Inv_Array.append("Notepad & Pen  (non-cmbt)");
                   MESSAGE += "\n" + str(InvCount) + ". Notepad & Pen (non-combat)";                                                                            

          GUI.LB_Inventory_Var.set(Inv_Array);
          GUI.Text_Append(MESSAGE);  
    #END-MemberMethod-Inventory_Display--------------------------------------------------------------------------------------


    #MemberMethod------------------------------------------------------------------------------------------------------------
      def Inventory_Equip(self,Selected_Item):
          #self.Inventory_Display();
          CHOICE = Selected_Item;
          MESSAGE = "-------------------Inventory Change-------------------";

          if(CHOICE == "NOTHING"):
             MESSAGE += "\nYou choose NOTHING.\nDe-equipping inventory.";
             self.WeaponChoice = "None"; 
          elif("Slingshot" in CHOICE):
               if(self.Slingshot_Pellets_Amt > 0): 
                  MESSAGE += "\nYou pull back the elastic band and load it with a\n smooth, flat stone. A simple but effective weapon.";
               else: 
                  MESSAGE +="\nYou pull out your trusty slingshot. But you\nhave no pellets. Won't be very effective.";
               self.WeaponChoice = "Slingshot";               
          elif(CHOICE == "Staff"):
               MESSAGE += "\nYou grasp the magic Staff in your hand.\nA personal weapon!";
               self.WeaponChoice = "Staff";
          elif(CHOICE == "Pendant"):
               MESSAGE += "\nYou stroke the magic Pendant to activate it.\nWhat an accessory!";
               self.WeaponChoice = "Pendant";
          elif(CHOICE == "Magic Sigil"):
               MESSAGE += "\nYou initialize the magic Sigil.\nMetallic vibrations fill the air!";
               self.WeaponChoice = "Sigil";
          elif(CHOICE == "Orb of Power"):
               MESSAGE += "\nYou choose the Orb of Power.\nBlinding light emanates from the Orb.";
               self.WeaponChoice = "Orb";
          elif(CHOICE == "Princess Cloak"):
               if(self.INV_Has_Pendant == "TRUE"):
                  MESSAGE += "\nYou choose the Cloak of Ultimate Princessness!\nYour body tingles with celestial energy as\nyou pull it around yourself.";
                  self.WeaponChoice = "PrincessCloak";
          elif("Healing Potions" in CHOICE):
               MESSAGE += "\nYou open a flask and drink a healing potion.\nIt restores " + str(self.HealthPotion_Restore_Amt) + " health!";
               self.EntityHealth = self.EntityHealth + self.HealthPotion_Restore_Amt ;
               self.INV_Has_HealingPotions -= 1;
          elif(CHOICE == "Chain Mail"):
               if(self.ArmorChoice != "ChainMail"):
                  MESSAGE += "\nYou choose to don upon yourself the Chain Mail armor.\nThis increases your DEFENSE capability by " + str(self.DEF_Item_Chain_Mail) + ".";
                  self.ArmorChoice = "ChainMail";
                  self.EntityDefense += self.DEF_Item_Chain_Mail;
               else: 
                     MESSAGE += "\nYou decide to remove the Chain Mail armor.";
                     self.ArmorChoice = "None"; 
                     self.EntityDefense -= self.DEF_Item_Chain_Mail; 
          elif(CHOICE == "Plate Armor"):
               if(self.ArmorChoice != "PlateArmor"):
                  MESSAGE += "\nYou choose to wear the Plate armor. Excellent!\nThis increases your DEFENSE capability by "+ str(self.DEF_Item_Plate_Armor) + ".";
                  self.ArmorChoice = "PlateArmor";
                  self.EntityDefense += self.DEF_Item_Plate_Armor;
               else: 
                     MESSAGE += "\nYou decide to remove the Plate armor.";
                     self.ArmorChoice = "None"; 
                     self.EntityDefense -= self.DEF_Item_Plate_Armor; 
          #Non-combat Inventory items           
          elif("Grooming Brush" in CHOICE):
               if(self.INV_Has_Grooming_Brush == "TRUE"):
                  MESSAGE += "\nYou select the Grooming Brush. (non-combat item)";
          elif("Fairy Torch " in CHOICE):
               if(self.INV_Has_FairyTorch == "TRUE"):
                  MESSAGE += "\nYou select the Fairy Torch. (non-combat item)"; 
          elif("Hemp Rope" in CHOICE):
               if(self.INV_Has_HempRope == "TRUE"):
                  MESSAGE += "\nYou select the Hemp Rope. (non-combat item)"; 
          elif("Climbing Cleats" in CHOICE):
               if(self.INV_Has_ClimbingCleats == "TRUE"):
                  MESSAGE += "\nYou select the Climbing Cleats. (non-combat item)"; 
          elif("Notepad & Pen" in CHOICE):
               if(self.INV_Has_NotepadAndPen == "TRUE"):
                  MESSAGE += "\nYou select the Notepad & Pen. (non-combat item)"; 
                                  

          #Update Inventory Listbox for items dropped/consumed/found
          Inv_Array = ["NOTHING"];
          if(self.INV_Has_Slingshot == "TRUE"): Inv_Array.append("Slingshot [" + str(self.Slingshot_Pellets_Amt) + "]");
          if(self.INV_Has_Staff == "TRUE"): Inv_Array.append("Staff");
          if(self.INV_Has_Pendant == "TRUE"): Inv_Array.append("Pendant");
          if(self.INV_Has_Sigil == "TRUE"): Inv_Array.append("Magic Sigil");
          if(self.INV_Has_Orb == "TRUE"): Inv_Array.append("Orb of Power");
          if(self.INV_Has_PrincessCloak == "TRUE"): Inv_Array.append("Princess Cloak");
          if(self.INV_Has_HealingPotions > 0): Inv_Array.append("Healing Potions: " + str(self.INV_Has_HealingPotions));
          if(self.INV_Has_Chain_Mail == "TRUE"): Inv_Array.append("Chain Mail");
          if(self.INV_Has_Plate_Armor == "TRUE"): Inv_Array.append("Plate Armor"); 
          #Non-combat Inventory items
          if(self.INV_Has_Grooming_Brush == "TRUE"): Inv_Array.append("Grooming Brush (non-cmbt)");
          if(self.INV_Has_FairyTorch == "TRUE"): Inv_Array.append("Fairy Torch (non-cmbt)");
          if(self.INV_Has_HempRope == "TRUE"): Inv_Array.append("Hemp Rope (non-cmbt)");
          if(self.INV_Has_ClimbingCleats == "TRUE"): Inv_Array.append("Climbing Cleats (non-cmbt)");
          if(self.INV_Has_NotepadAndPen == "TRUE"): Inv_Array.append("Notepad & Pen  (non-cmbt)");
          GUI.LB_Inventory_Var.set(Inv_Array);

          GUI.Text_Write(MESSAGE);
          self.Display_Character();
          #self.Inventory_Display();

    #END-MemberMethod-Inventory_Equip----------------------------------------------------------------------------------------   


    #MemberMethod---------------------------------------------------------------------------------------------------------------
      def SKILL_Display(self):
          Ablty_Array = ["NOTHING"];
          MESSAGE = "\n---------------------Acquired Magic Skills---------------------";
          if(self.SKILL_Has_IceBlasts == "FALSE" and self.SKILL_Has_FireBalls == "FALSE" and self.SKILL_Has_Lightning == "FALSE" and
             self.SKILL_Has_Telekinesis == "FALSE" and self.SKILL_Has_Telepathy == "FALSE" and self.SKILL_Has_Teleportation == "FALSE"
             and self.SKILL_Has_TimeWarp == "FALSE" and self.SKILL_Has_Invisibility == "FALSE" and self.SKILL_Has_Healing == "FALSE"
             and self.SKILL_Has_FriendshipCast  == "FALSE"):
             MESSAGE += "\n" + self.EntityName + " has NO magic skills yet. Absolutely none. Go learn some!";
             Ablty_Array.append("No magic skills");
          else:    
                SkillCount = 0;
                if(self.SKILL_Has_IceBlasts == "TRUE"):
                   SkillCount += 1;
                   Ablty_Array.append("Ice Blasts");
                   MESSAGE += "\n" + str(SkillCount) + ". Ice Blasts                 ATK+" + str(self.Dammage_Skill_IceBlasts);
                if(self.SKILL_Has_FireBalls == "TRUE"):
                   SkillCount += 1;
                   Ablty_Array.append("Fire Balls");
                   MESSAGE += "\n" + str(SkillCount) + ". Fire Balls                 ATK+" + str(self.Dammage_Skill_FireBalls);
                if(self.SKILL_Has_Lightning == "TRUE"):
                   SkillCount += 1;
                   Ablty_Array.append("Lightning");
                   MESSAGE += "\n" + str(SkillCount) + ". Lightning                  ATK+" + str(self.Dammage_Skill_Lightning);
                if(self.SKILL_Has_Telekinesis == "TRUE"):
                   SkillCount += 1;
                   Ablty_Array.append("Telekinesis");
                   MESSAGE += "\n" + str(SkillCount) + ". Telekinesis               ATK+" + str(self.Dammage_Skill_Telekinesis);
                if(self.SKILL_Has_Telepathy == "TRUE"):
                   SkillCount += 1;
                   Ablty_Array.append("Telepathy");
                   MESSAGE += "\n" + str(SkillCount) + ". Telepathy                 ATK+" + str(self.Dammage_Skill_Telepathy);
                if(self.SKILL_Has_Teleportation == "TRUE"):
                   SkillCount += 1;
                   Ablty_Array.append("Teleportation");
                   MESSAGE += "\n" + str(SkillCount) + ". Teleportation           ATK+" + str(self.Dammage_Skill_Teleportation);
                if(self.SKILL_Has_TimeWarp == "TRUE"):
                   SkillCount += 1;
                   Ablty_Array.append("Warp Time");
                   MESSAGE += "\n" + str(SkillCount) + ". Warp Time               ATK+" + str(self.Dammage_Skill_TimeWarp);
                if(self.SKILL_Has_Invisibility == "TRUE"):
                   SkillCount += 1;
                   Ablty_Array.append("Invisibility");
                   MESSAGE += "\n" + str(SkillCount) + ". Invisibility"; 
                if(self.SKILL_Has_Healing == "TRUE"):
                   SkillCount += 1;
                   Ablty_Array.append("Healing");
                   MESSAGE += "\n" + str(SkillCount) + ". Healing";
                if(self.SKILL_Has_FriendshipCast == "TRUE"):
                   SkillCount += 1;
                   Ablty_Array.append("Cast Friendship");
                   MESSAGE += "\n" + str(SkillCount) + ". Cast Friendship";   

          GUI.LB_Abilities_Var.set(Ablty_Array);
          GUI.Text_Append(MESSAGE);                                                                        
    #END-MemberMethod-SKILL_Display----------------------------------------------------------------------------------------  


    #MemberMethod------------------------------------------------------------------------------------------------------------
      def SKILL_Equip(self,Selected_Item):
          #self.SKILL_Display();
          CHOICE = Selected_Item;
          MESSAGE = "-------------------Magic Skill Change-------------------";

          if(CHOICE == "NOTHING"):
             MESSAGE += "\nYou choose NOTHING.\nDe-activating all magic skills.";
             self.MagicChoice = "None";
          elif(CHOICE == "Ice Blasts"):
               MESSAGE += "\nThe ambient temperature around you lowers.\nYou prepare an IceBlast!";
               self.MagicChoice = "IceBlasts";
          elif(CHOICE == "Fire Balls"):
               MESSAGE += "\nThe air begins to ripple with heat and plasma.\nIt coalesces as you prepare FireBalls!";
               self.MagicChoice = "FireBalls";
          elif(CHOICE == "Lightning"):
               MESSAGE += "\nCrack! Pop! You charge the air around you.\nIt fills with electric potential as you prepare Lightning!";
               self.MagicChoice = "Lightning";
          elif(CHOICE == "Telekinesis"):
               MESSAGE += "\nThe reality around you ripples as your mind wraps itself\naround the spacetime near you. You activate Telekinesis!";
               self.MagicChoice = "Telekinesis";
          elif(CHOICE == "Telepathy"):
               MESSAGE += "\nYou hear the voices of others around you as you open\nyour mind to their thoughts. You activate Telepathy!";
               self.MagicChoice = "Telepathy";
          elif(CHOICE == "Teleportation"):
                  MESSAGE += "\nSpacetime forms a bubble around you, separating you from\nthis current reality.You initialize Teleportation!";
                  self.MagicChoice = "Teleportation";
          elif(CHOICE == "Warp Time"):
                  MESSAGE += "\nThe 4th dimension of TIME begins to drag and swirl as\nit slows around you. You trigger a Time Warp!";
                  self.MagicChoice = "TimeWarp";
          elif(CHOICE == "Invisibility"):
               if(self.EntityMagicPower - self.SKILL_Invisibility_Cost > 0):
                  self.MagicChoice = "Invisibility";  
                  MESSAGE += "\nInvisibility Active! " + self.EntityName + " bends light around themselves\nto become invisible, thus enhancing their defense."; 
                  self.Invisibility_Active = "TRUE";
                  self.Invisibility_Count = self.Invisibility_Count +3;
                  self.EntityMagicPower = self.EntityMagicPower - self.SKILL_Invisibility_Cost;
                  MESSAGE += "\nYour visible profile disappears and you fade away.\n\nYou have energized this skill to last " + str(self.Invisibility_Count) + " combat rounds.";
               else: MESSAGE += "Sorry, you do not have enough magic power to activate a Invisibility.";  
          elif(CHOICE == "Healing"):
               self.MagicChoice = "Healing";
               MESSAGE += "\nActivating Healing! " + self.EntityName + " attempts to focus and concentrate\nmagic energy all around themselves ..."; 
               if(self.EntityMagicPower - self.SKILL_Healing_Restore_Amt > 0):
                  self.EntityMagicPower = self.EntityMagicPower - self.SKILL_Healing_Restore_Amt;  
                  self.EntityHealth = self.EntityHealth + self.SKILL_Healing_Restore_Amt;
                  MESSAGE += "\n\nYou lay hands upon yourself and cause healing energy to surge\nthroughout your body, adding " + str(self.SKILL_Healing_Restore_Amt) + " to your health.";
               else: MESSAGE += "\nSorry, although you possess the skill,\nyou do not have enough magic power to implement Healing."; 
          elif(CHOICE == "Cast Friendship"):
               MESSAGE += "\nYou cast Friendship on everyone within proximity.\nYour opponents feel much less agressive towards you now.";
               self.MagicChoice = "FriendshipCast";

          #Update Skill/Ability Listbox for items dropped/consumed/found
          Ablty_Array = ["NOTHING"];
          if(self.SKILL_Has_IceBlasts == "TRUE"): Ablty_Array.append("Ice Blasts");
          if(self.SKILL_Has_FireBalls== "TRUE"): Ablty_Array.append("Fire Balls");
          if(self.SKILL_Has_Lightning == "TRUE"): Ablty_Array.append("Lightning");
          if(self.SKILL_Has_Telekinesis == "TRUE"): Ablty_Array.append("Telekinesis");
          if(self.SKILL_Has_Telepathy == "TRUE"): Ablty_Array.append("Telepathy");
          if(self.SKILL_Has_Teleportation == "TRUE"): Ablty_Array.append("Teleportation");
          if(self.SKILL_Has_TimeWarp == "TRUE"): Ablty_Array.append("Warp Time");   
          if(self.SKILL_Has_Invisibility == "TRUE"): Ablty_Array.append("Invisibility");
          if(self.SKILL_Has_Healing == "TRUE"): Ablty_Array.append("Healing");
          if(self.SKILL_Has_FriendshipCast == "TRUE"): Ablty_Array.append("Cast Friendship");
          GUI.LB_Abilities_Var.set(Ablty_Array);

          GUI.Text_Write(MESSAGE);
          self.Display_Character();                                                                                                                                                             
    #END-MemberMethod-Inventory_Equip----------------------------------------------------------------------------------------  



    #MemberMethod------------------------------------------------------------------------------------------------------------
      def Display_All(self):   
          self.Display_Character();
          self.Inventory_Display();
          self.SKILL_Display();
    #END-MemberMethod-Display_All--------------------------------------------------------------------------------------------



    #MemberMethod------------------------------------------------------------------------------------------------------------
      def Attack(self,Opponent):   
          MinDammage = 500;
          MaxDammage = 10000;
          DAMMAGE_MAGIC_ITEM = 0;
          DAMMAGE_MAGIC_SKILL = 0; 
          print("Inside Attack method sequence.");

          MESSAGE = "\n-------Beginning " + self.EntityName + "'s entity attack sequence-------";
          GUI.Text_Append(MESSAGE);

          if(self.FirstTimeShowOpponentInfo == "TRUE"):
             MESSAGE = "\nThe Opponent being faced:";
             GUI.Dramatic_Pause_Append(2,MESSAGE);
             Opponent.Display_As_Opponent();
             self.FirstTimeShowOpponentInfo = "FALSE";
             
          MESSAGE = "\n" + Opponent.EntityName + "'s health BEFORE\n" + self.EntityName + "'s attack: " + str(Opponent.EntityHealth);
          GUI.Dramatic_Pause_Append(5,MESSAGE);

          #1.Generate base dammage to opponent for this combat round.
          DAMMAGE = random.randint(MinDammage,MaxDammage);
          MESSAGE = "#1 of 11\n\n" + self.EntityName + " generates [" + str(DAMMAGE) + "] of random base damage";
          MESSAGE += "\ndue to their magical prowess and strength.";
          GUI.Dramatic_Pause_Write(4,MESSAGE);

          #2.Add ATK skill and experience of Entitiy to base dammage generated.
          DAMMAGE_ATK = random.randint(1,self.EntityAttack);
          MESSAGE = "\n#2 of 11\n\n" + self.EntityName + " generates [" + str(DAMMAGE_ATK) + "] additional dammage";
          MESSAGE += "\ndue to their attack skill and experience.";
          GUI.Dramatic_Pause_Append(4,MESSAGE);
          DAMMAGE += DAMMAGE_ATK;

          #3.If class of object allowed to use a magic ITEM? Process that Entity's choice and calculate additional dammage.
          if(self.EntityClass == "Princess" or self.EntityClass == "Alicorn" or self.EntityClass =="Supreme Agent of Chaos" or 
             self.EntityClass == "Unicorn" or self.EntityClass == "Pegasus" or self.EntityClass == "Antagonist"):
             #ONLY if selected inventory object is a WEAPON useful for ATTACK and not a BENIGN inventory item
             if(self.WeaponChoice == "None" or self.WeaponChoice == "Slingshot" or self.WeaponChoice == "Staff" or self.WeaponChoice == "Pendant" or  
                self.WeaponChoice == "Sigil" or self.WeaponChoice == "Orb" or self.WeaponChoice == "PrincessCloak"):
                if self.WeaponChoice == "None": 
                   MESSAGE = "#3 of 11\n\nForegoing the use of any magic items, " + self.EntityName + "\nfights with bare hooves of horror!\n";              
                else: 
                   MESSAGE = "#3 of 11\n\n" + self.EntityName + " chooses to use a MAGIC item!\n";  
                   if(self.WeaponChoice == "Slingshot"): 
                      if(self.Slingshot_Pellets_Amt > 0):
                         MESSAGE += "\nThey pull back the elastic band on their slingshot\nStinging stones tumble in the air!\nFwwwwwt! (possible +" + str(self.Dammage_Item_Slingshot) + ")";
                         DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Slingshot - 2),self.Dammage_Item_Slingshot);
                         self.Slingshot_Pellets_Amt -= 1;
                      else: 
                         MESSAGE +="You have no more pellets for your slingshot. Sorry.";   
                   elif(self.WeaponChoice == "Staff"): 
                      MESSAGE += "\nThey raise their Staff to fire\na bolt of lightning!\nZzzzzt! (possible +" + str(self.Dammage_Item_Staff) + ")";
                      DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Staff - 3),self.Dammage_Item_Staff); 
                   elif(self.WeaponChoice == "Pendant"): 
                        MESSAGE += "\nThey touch their Pendant enveloping their\nopponent in flames!\nWoosh! (possible +" + str(self.Dammage_Item_Pendant) + ")";
                        DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Pendant - 5),self.Dammage_Item_Pendant);
                   elif(self.WeaponChoice == "Sigil"): 
                        MESSAGE += "\nThey point their Sigil at their opponent unleashing\nblunt force telekinetic trauma!\nPow! (possible +" + str(self.Dammage_Item_Sigil) + ")";
                        DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Sigil - 10),self.Dammage_Item_Sigil);
                   elif(self.WeaponChoice == "Orb"): 
                        MESSAGE += "\nThey cup the Orb in their hands, covering their\nopponent in damaging darkness!\nVroww! (possible +" + str(self.Dammage_Item_Orb) + ")";
                        DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Orb - 15),self.Dammage_Item_Orb);
                   elif(self.WeaponChoice == "PrincessCloak"):
                        MESSAGE += "\nThey flip their PrincessCloak with sass!\nShowering their opponent with celestial glitter bombs.\nBoom! (possible +" + str(self.Dammage_Item_PrincessCloak) + ")";
                        DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_PrincessCloak - 20),self.Dammage_Item_PrincessCloak);
             else: MESSAGE = "\n That magic item choice was invalid.";            

          GUI.Dramatic_Pause_Write(5,MESSAGE);  

          #4.Add magic ITEM damage to total dammage if applicable.
          MESSAGE = "#4 of 11\n\nCheck for magic item if selected and add its dammage to total.\n";
          if(DAMMAGE_MAGIC_ITEM > 0):
             MESSAGE += "\nHit! " + self.EntityName + " generates [" + str(DAMMAGE_MAGIC_ITEM) + "] additional\ndammage by using a magic ITEM!";
             DAMMAGE = DAMMAGE + DAMMAGE_MAGIC_ITEM;
          else: MESSAGE += "\nMiss! No damage generated with magic weapon this round.";
          GUI.Dramatic_Pause_Write(11,MESSAGE);  

          #5.If class of object allowed to use a magic SKILL? Process that Entity's choice and calculate additional dammage.
          if(self.EntityClass == "Princess" or self.EntityClass == "Alicorn" or self.EntityClass =="Supreme Agent of Chaos"):            
             if(self.MagicChoice == "None" or self.MagicChoice == "IceBlasts" or self.MagicChoice == "FireBalls" or self.MagicChoice == "Lightning" or 
                self.MagicChoice == "Telekinesis" or self.MagicChoice == "Telepathy" or self.MagicChoice == "Teleportation" or  self.MagicChoice == "TimeWarp" or
                self.MagicChoice == "Invisibility" or self.MagicChoice == "Healing" or self.MagicChoice == "FriendshipCast"):
                if self.MagicChoice == "None": 
                   MESSAGE = "#5 of 11\n\n" + self.EntityName + " decides not to use magic, leveraging only ";
                   if self.EntityGender == "Female": MESSAGE +=  "her";
                   elif self.EntityGender == "Male": MESSAGE +=  "his";
                   MESSAGE +=  " wits!";
                else: 
                     MESSAGE = "#5 of 11\n\n" + self.EntityName + " chooses to use a MAGIC skill!\n";   
                     if(self.MagicChoice == "IceBlasts"): 
                        if(self.EntityMagicPower - 5 > 0): 
                           MESSAGE += "Ice Blast! The ambient temperature around\nthe opponent nears absolute zero,\ninflicting severe cold damage\n(possible +" + str(self.Dammage_Skill_IceBlasts) + ")";
                           DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_IceBlasts-5,self.Dammage_Skill_IceBlasts);
                           self.EntityMagicPower = self.EntityMagicPower - 5; 
                        else: MESSAGE += "Sorry, you do not have enough magic\npower to activate a Ice Blast.";    
                     elif(self.MagicChoice == "FireBalls"): 
                          if(self.EntityMagicPower - 8 > 0): 
                             MESSAGE += " Fire Ball! Super-heated balls of plasma coalesce\nout of thin air and rush towards the opponent\n(possible +" + str(self.Dammage_Skill_FireBalls) + ")";
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_FireBalls-8,self.Dammage_Skill_FireBalls); 
                             self.EntityMagicPower = self.EntityMagicPower - 8; 
                          else: MESSAGE += "Sorry, you do not have enough magic\npower to activate a Fire Balls.";   
                     elif(self.MagicChoice == "Lightning"): 
                          if(self.EntityMagicPower - 15 > 0): 
                             MESSAGE += "Lightning! Massive electrical potential builds\nand sparks. An arc of lightning races\ntowards the opponent.\n(possible +" + str(self.Dammage_Skill_Lightning) + ")";
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_Lightning-15,self.Dammage_Skill_Lightning);
                             self.EntityMagicPower = self.EntityMagicPower - 15;  
                          else: MESSAGE += "Sorry, you do not have enough magic\npower to activate a Lightning.";   
                     elif(self.MagicChoice == "Telekinesis"): 
                          if(self.EntityMagicPower - 20 > 0): 
                             MESSAGE += "Telekinesis! Mind over matter deals\nmassive blunt force trauma to the opponent\n(possible +" + str(self.Dammage_Skill_Telekinesis) + ")";
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_Telekinesis-20,self.Dammage_Skill_Telekinesis);
                             self.EntityMagicPower = self.EntityMagicPower - 20;  
                          else: MESSAGE += "Sorry, you do not have enough magic\npower to activate a Telekinesis.";
                     elif(self.MagicChoice == "Telepathy"): 
                          if(self.EntityMagicPower - 35 > 0): 
                             MESSAGE += "Telepathy! Opponent's mind is temporarily taken\nover and they commit self-harm\n(possible +" + str(self.Dammage_Skill_Telepathy) + ")";
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_Telepathy-35,self.Dammage_Skill_Telepathy);                           
                             self.EntityMagicPower = self.EntityMagicPower - 35;
                          else: MESSAGE += "Sorry, you do not have enough magic\npower to activate a Telepathy.";   
                     elif(self.MagicChoice == "Teleportation"): 
                          if(self.EntityMagicPower - 40 > 0): 
                             MESSAGE += "Teleportation! Teleporting into opponent's\nmost vulnerable spot, they are\ndevastated by a focused attack\n(possible +" + str(self.Dammage_Skill_Teleportation) + ")"; 
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_Teleportation-40,self.Dammage_Skill_Teleportation); 
                             self.EntityMagicPower = self.EntityMagicPower - 40; 
                          else: MESSAGE += "Sorry, you do not have enough magic\npower to activate a Teleportation.";  
                     elif(self.MagicChoice == "TimeWarp"): 
                          if(self.EntityMagicPower - 50 > 0): 
                             MESSAGE += "TimeWarp! Time warp initiated around opponent.\nAs times slows, multiple succesive blows\nare sustained\n(possible +" + str(self.Dammage_Skill_TimeWarp) + ")";  
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_TimeWarp-50,self.Dammage_Skill_TimeWarp);
                             self.EntityMagicPower = self.EntityMagicPower - 50; 
                          else: MESSAGE += "Sorry, you do not have enough magic\npower to activate a TimeWarp.";     
                     elif(self.MagicChoice == "FriendshipCast"): 
                          MESSAGE += "FriendshipCast! " + self.EntityName + " casts peace,\nlove and friendship on opponent\nThis decreases their aggression."; 
                          MESSAGE += "\nOpponent no longer wishes to fight due to\npositive feelings of love and friendsip.\nDe-escalating combat...";
                          if(self.EntityMagicPower - 300 > 0):
                             self.EntityMagicPower = self.EntityMagicPower - 300;  
                             globals()['Willing_to_Fight'] = "FALSE";
                             MESSAGE += "\nResetting magic skill choice back to \"None\".";
                             self.MagicChoice == "None";
                          else: MESSAGE += "Sorry, you do not have enough magic\npower to activate a FriendshipCast.";   
             else: MESSAGE = "\nThat magic item skill choice was invalid.";

          GUI.Dramatic_Pause_Write(10,MESSAGE);

          #6.Add magic SKILL damage to total dammage if applicable damage-causing skill was chosen.
          if(DAMMAGE_MAGIC_SKILL > 0):
             MESSAGE = "\n#6 of 11\n\n" + self.EntityName + " generates [" + str(DAMMAGE_MAGIC_SKILL) + "] additional dammage by magic SKILL.";
             DAMMAGE = DAMMAGE + DAMMAGE_MAGIC_SKILL;
          else: MESSAGE = "\n #6 of 11\n\nMiss! No damage generated with skill this round."; 
          GUI.Dramatic_Pause_Write(10,MESSAGE);  
 
          #7.Calculate Opponent's base defense due to skill and experience
          DAMMAGE_DEF = random.randint(1,Opponent.EntityDefense);
          MESSAGE = "\n#7 of 11\n\n" + Opponent.EntityName + " defends!\nReducing dammage absorbed in\nthis attack by [" + str(DAMMAGE_DEF) + "]\ndue to their defensive skills.";
          GUI.Dramatic_Pause_Write(7,MESSAGE);


          #8.If Opponent using INVISBILITY? Add to their base defense amount.
          MESSAGE = "\n#8 of 11\n\nCheck INVISIBILITY status for entity " + Opponent.EntityName + ".";
          if(Opponent.Invisibility_Active == "TRUE"):
             MESSAGE += "\nOpponent is capable of INVISIBILITY and it is currently active for " + Opponent.EntityName + ".";
             MESSAGE += "\nThis temporarily increases opponent's\ndefense by [" + str(self.Invisibility_DEF_Amt) + "].\n Hard to hit what you can't see!";
             DAMMAGE_DEF = DAMMAGE_DEF + self.Invisibility_DEF_Amt;
             Opponent.Invisibility_Count = Opponent.Invisibility_Count - 1;
             if(Opponent.Invisibility_Count < 1): 
                MESSAGE += "\nINVISIBILITY has consumed its alloted energy and\nis now powering down for " + Opponent.EntityName + "!";
                Opponent.Invisibility_Active == "FALSE";
                Opponent.Invisibility_Count = 0;
          else: MESSAGE += "\nINVISIBILITY unavailable and inactive for\n" + Opponent.EntityName + ".";
          GUI.Dramatic_Pause_Write(8,MESSAGE);   

          #9.Subtract Opponent's DEFENSE from dammage.
          MESSAGE = "\n#9 of 11\n\nSubtracting defense capability for entity\n" + Opponent.EntityName + " from total damage.";
          if(DAMMAGE > DAMMAGE_DEF):
             DAMMAGE = DAMMAGE - DAMMAGE_DEF;
          else: DAMMAGE = 0;
          GUI.Dramatic_Pause_Write(8,MESSAGE);

          #10.Display resulting dammage after adding magic item and magic skill and subtracting all Opponent defense.
          MESSAGE = "\n#10 of 11\n\nAfter all attack and defense moves\ncalculated for this combat round:\n";
          MESSAGE += "\n" + Opponent.EntityName + " generated " + str(DAMMAGE_DEF) + "\ntotal for their defense.";
          MESSAGE += "\nAfter subtracting opponent's total defense,\n" + self.EntityName + " inflicted a total of [" + str(DAMMAGE) + "]\ndamage against their opponent this round.";
          
          GUI.Dramatic_Pause_Write(5,MESSAGE);

          #11. Prevent negative values, if Opponent health less than 1 this round, they are effectively defeated
          MESSAGE = "\n#11 of 11\n\n Prevent negative values and display final results:\n"
          if(Opponent.EntityHealth - DAMMAGE > 0):
             Opponent.EntityHealth = Opponent.EntityHealth - DAMMAGE;
          else: Opponent.EntityHealth = 0;

          MESSAGE += "\n------------AFTER Attack Sequence------------\n";
          MESSAGE += "   " + self.EntityName + " Health: " + str(self.EntityHealth);
          MESSAGE += "\n   " + Opponent.EntityName + " Health: " + str(Opponent.EntityHealth);
          GUI.Dramatic_Pause_Write(6,MESSAGE);



    #END-MemberMethod-Attack----------------------------------------------------------------------------------------------------------------------------

#END-Class Game_Entity******************************************************************************************************************************************

#INTERMEDIATE derived CHILD class that inherits from the BASE class----------------------------------------------------------------------------------------------------------------------
class ANTAGONIST(Game_Entity):

   #-Antagonist-Constructor
      def __init__(self,GE_Name="Anonymous Antagonist",GE_Class="Antagonist",GE_Gender="Male",GE_Health=25,GE_MP=25,GE_DEF=3,GE_ATK=3):
          self.EntityName = GE_Name;
          self.EntityClass = GE_Class;
          self.EntityGender = GE_Gender;
          self.EntityHealth = GE_Health;
          self.EntityMagicPower = GE_MP;
          self.EntityDefense = GE_DEF;
          self.EntityAttack = GE_ATK;     


 #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#Derived GRANDCHILD class from an intermediate CHILD class that itself inherits from the BASE class-------------------------------------------------------------------------------------
class Chaos_Agent(ANTAGONIST):
      #Class Attributes
      Antagonist_Ability_1 = "Warp SpaceTime";
      Antagonist_Ability_2 = "Improbability Materilization";
      Antagonist_Ability_3 = "Wish Projection";
      Antagonist_Ability_4 = "Ultimate Chaos";

   #-Chaos_Agent-Constructor
      def __init__(self,ANT_Name="Discord",ANT_Class="Antagonist",ANT_Gender="Male",ANT_Health=100,ANT_MP=100,ANT_DEF=10,ANT_ATK=10):
          self.EntityName = ANT_Name;
          self.EntityClass = ANT_Class;
          self.EntityGender = ANT_Gender;
          self.EntityHealth = ANT_Health;
          self.EntityMagicPower = ANT_MP;
          self.EntityDefense = ANT_DEF;
          self.EntityAttack = ANT_ATK;        

      #Member Methods
      def Display_Chaos_Agent(self):
          self.Display_Character;
          self.Display_Entity();
          print("\n     ",self.EntityClass,"Special Abilities:");
          print("     ","Ability 1:",self.Antagonist_Ability_1);
          print("     ","Ability 2:",self.Antagonist_Ability_2);
          print("     ","Ability 3:",self.Antagonist_Ability_3);  
          print("     ","Ability 4:",self.Antagonist_Ability_4);   

 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 


#Example: PARENT (base) Class with CONSTRUCTOR (init method) and DEFAULT ARGUMENTS (can't overload constructors in Python)
#INTERMEDIATE derived CHILD class that inherits from the BASE class----------------------------------------------------------------------------------------------------------------------
class PONY(Game_Entity):
      #Class Attributes
      EntityName = "Anonymous Pony";
      EntityGender = "Female";
      EntityClass = "Pony";
      EntityHealth = 100;
      EntityDefense = 7;
      EntityAttack = 7;
      EntityMagicPower = 250;      
   
      #Constructor (init method) with DEFAULT arguments-------------------------------------------------------------------------------------------------
      def __init__(self, name=EntityName,pclass=EntityClass,health=EntityHealth,defense=EntityDefense,attack=EntityAttack,magicpower=EntityMagicPower):
          self.EntityName = name;
          self.EntityClass = pclass;
          self.EntityHealth = health;
          self.EntityDefense = defense;
          self.EntityAttack = attack;
          self.EntityMagicPower = magicpower;
    #--------------------------------------------------------------------------------------------------------------------------------------------------      

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------      


#Derived GRANDCHILD class from an intermediate CHILD class that itself inherits from the BASE class-------------------------------------------------------------------------------------
class ALICORN(PONY):
      #Class Attributes
      EntityName = "Twilight Sparkle";
      EntityGender = "Female";
      EntityClass = "Alicorn";
      EntityHealth = 31000;
      EntityDefense = 10000;
      EntityAttack = 10000;
      EntityMagicPower = 32000; 
      Alicorn_Ability_01 = "Alicorn Ability 1";
      Alicorn_Ability_02 = "Alicorn Ability 2";

      def __init__(self, name=EntityName,pclass=EntityClass,health=EntityHealth,defense=EntityDefense,attack=EntityAttack,magicpower=EntityMagicPower):
          self.EntityName = name;
          self.EntityClass = pclass;
          self.EntityHealth = health;
          self.EntityDefense = defense;
          self.EntityAttack = attack;
          self.EntityMagicPower = magicpower;      

      def Display_Alicorn(self):
          self.Display_Chracter();
          print("\n     ","Alicorn Special Abilities:");
          print("     ","Ability 1:",self.Alicorn_Ability_01);
          print("     ","Ability 2:",self.Alicorn_Ability_02);
       
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 


#Derived GRANDCHILD class from an intermediate CHILD class that itself inherits from the BASE class-------------------------------------------------------------------------------------
class UNICORN(PONY):
      #Class Attributes
      EntityName = "Rarity";
      EntityGender = "Female";
      EntityClass = "Unicorn";
      EntityHealth = 10000;
      EntityDefense = 1000;
      EntityAttack = 1000;
      EntityMagicPower = 15000; 
      Unicorn_Ability_01 = "Unicorn Ability 1";
      Unicorn_Ability_02 = "Unicorn Ability 2";

      def __init__(self, name=EntityName,pclass=EntityClass,health=EntityHealth,defense=EntityDefense,attack=EntityAttack,magicpower=EntityMagicPower):
          self.EntityName = name;
          self.EntityClass = pclass;
          self.EntityHealth = health;
          self.EntityDefense = defense;
          self.EntityAttack = attack;
          self.EntityMagicPower = magicpower;      

      def Display_Unicorn(self):
          self.Display_Chracter();
          print("\n     ","Unicorn Special Abilities:");
          print("     ","Ability 1:",self.Unicorn_Ability_01);
          print("     ","Ability 2:",self.Unicorn_Ability_02);
       
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 


#Derived GRANDCHILD class from an intermediate CHILD class that itself inherits from the BASE class-------------------------------------------------------------------------------------
class PEGASUS(PONY):
      #Class Attributes
      EntityName = "Rainbow Dash";
      EntityGender = "Female";
      EntityClass = "Pegasus";
      EntityHealth = 12000;
      EntityDefense = 1200;
      EntityAttack = 1200;
      EntityMagicPower = 1000; 
      Pegasus_Ability_01 = "Pegasus Ability 1";
      Pegasus_Ability_02 = "Pegasus Ability 2";

      def __init__(self, name=EntityName,pclass=EntityClass,health=EntityHealth,defense=EntityDefense,attack=EntityAttack,magicpower=EntityMagicPower):
          self.EntityName = name;
          self.EntityClass = pclass;
          self.EntityHealth = health;
          self.EntityDefense = defense;
          self.EntityAttack = attack;
          self.EntityMagicPower = magicpower;      

      def Display_Alicorn(self):
          self.Display_Chracter();
          print("\n     ","Alicorn Special Abilities:");
          print("     ","Ability 1:",self.Pegasus_Ability_01);
          print("     ","Ability 2:",self.Pegasus_Ability_02);
       
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 


#Derived GRANDCHILD class from an intermediate CHILD class that itself inherits from the BASE class-------------------------------------------------------------------------------------
class PRINCESS(ALICORN):
      #Class Attributes
      EntityName = "Celestia";
      EntityGender = "Female";
      EntityClass = "Princess";
      EntityHealth = 32000;
      EntityDefense = 8000;
      EntityAttack = 8000;
      EntityMagicPower = 32000; 
      Princess_Power = 15000;
      Princess_Charisma = 100;
      Princess_Ability_01 = "Ability 1";
      Princess_Ability_02 = "Ability 2";
      Princess_Ability_03 = "Ability 3";

      #Constructor sets PARENT (base) class values for this derived CHILD class
      def __init__(self):
          self.PonyClass = "Princess";
          self.Health = 32000;
          self.MagicPower = 32000;
          self.Defense = 8000;
          self.Attack = 8000;

      def Display_Princess(self):
          self.Display_Chracter();
          print("\n     ","Princess Special Abilities:");
          print("     ","Ability 1:",self.Princess_Ability_01);
          print("     ","Ability 2:",self.Princess_Ability_02);
          print("     ","Ability 3:",self.Princess_Ability_03); 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Derived CHILD class of Primary BASE class-------------------------------------------------------------------------------------------------------------------------------
class NPC(Game_Entity):
      
      Num_Responses = 0;
      RAND_Responses = [];
      Used_Responses = [];
      FirstTime = "TRUE";

  #-NPC-Constructor
      def __init__(self,GE_Name="Anonymous NPC",GE_Class="Generic NPC",GE_Gender="Female",GE_Health=100,GE_MP=50,GE_DEF=5,GE_ATK=5):
          self.EntityName = GE_Name;
          self.EntityClass = GE_Class;
          self.EntityGender = GE_Gender;
          self.EntityHealth = GE_Health;
          self.EntityMagicPower = GE_MP;
          self.EntityDefense = GE_DEF;
          self.EntityAttack = GE_ATK;
  #-------------------------------------------------------------------------------------------------------------------------------        
  
  #-NPC-Member-Method-------------------------------------------------------------------------------------------------------------
      def Set_Random_Responses(self,R_Responses):   
          self.Num_Responses = len(R_Responses);
          self.RAND_Responses = R_Responses;

          print("  There are",self.Num_Responses,"random responses for this NPC:\n");
          GUI.Text_Append("\nThere are " + str(self.Num_Responses) + " random responses for this NPC.\n");
          R_Counter = 0;

          for x in self.RAND_Responses: 
              R_Counter = R_Counter +1;
              print(" ",R_Counter,"\b.",x);
              GUI.Text_Append(" " + str(R_Counter) + ". " + x);

  #-------------------------------------------------------------------------------------------------------------------------------             

  #-NPC-Member-Method-------------------------------------------------------------------------------------------------------------
      def Speak(self):

          ContainsAMatch = "FALSE";
          ContinueLoop = "TRUE";
          WhatToSay = 0;

          #If 1st time populate array with 1st random value then turn off
          if(self.FirstTime == "TRUE"):
             WhatToSay = random.randint(0,(self.Num_Responses-1));
             self.Used_Responses.append(WhatToSay);
             self.FirstTime = "FALSE";
             print("\n ",self.EntityName,"turns to you and says:\n");
             GUI.Text_Append(self.EntityName + " turns to you and says:\n");
             print("  \"",self.RAND_Responses[WhatToSay],"\"",sep="");
             GUI.Text_Append("\"" + self.RAND_Responses[WhatToSay] + "\"");
             #print(" ",self.Used_Responses);
          else:
                #After 1st only populate array with next value if not a match
                while(ContinueLoop == "TRUE"):
                      ContainsAMatch = "FALSE";
                      WhatToSay = random.randint(0,(self.Num_Responses-1));

                      #Go through every element in array and see if WhatToSay matches
                      for x in self.Used_Responses:
                          if(x == WhatToSay):
                             #print("     Match: x=",x," and WhatToSay=",WhatToSay);
                             ContainsAMatch = "TRUE";

                      #If after comparing rand # to every element in array returns no matches? Then ADD new value to array and exit loop
                      if(ContainsAMatch == "FALSE"):       
                         self.Used_Responses.append(WhatToSay);
                         ContinueLoop = "FALSE";
                         print("\n ",self.EntityName,"turns to you and says:");
                         GUI.Text_Append(self.EntityName + " turns to you and says:");
                         print("  \"",self.RAND_Responses[WhatToSay],"\"",sep="");
                         GUI.Text_Append("\"" + self.RAND_Responses[WhatToSay] + "\"");
                         #print(" ",self.Used_Responses);

          #When all random responses used in conversation reset everything and start again                        
          if(len(self.Used_Responses) >= len(self.RAND_Responses)):
             #print("\n  --------------------------------------------------------------------------------------");  
             #print("  MAX # random responses reached. Resetting ...");
             self.Used_Responses.clear();
             self.FirstTime = "TRUE";
  #-------------------------------------------------------------------------------------------------------------------------------
    
  #-NPC-Member-Method-------------------------------------------------------------------------------------------------------------          
      def Conversate(self,PlayerInput):         
          ResponseToPlayer = random.randint(1,5);
          if(ResponseToPlayer == 1):
             print("Really? What about \"",PlayerInput,"\"?",sep="");
             GUI.Text_Append("Really? What about \"" + PlayerInput + "\" ?");
          if(ResponseToPlayer == 2):
             print("Why are you asking me \"",PlayerInput,"\" at a time like this?",sep="");
             GUI.Text_Append("Why are you asking me \"" + PlayerInput + "\" at a time like this?");   
          if(ResponseToPlayer == 3):
             print("I don't really have an answer for you at the moment concerning that particular topic.");
             GUI.Text_Append("I don't really have an answer for you at the moment.");
             GUI.Text_Append("At least not concerning that particular topic.");
          if(ResponseToPlayer == 4):
             print("If you want to know \"",PlayerInput,"\", you will have to do some digging on your own.",sep="");
             GUI.Text_Append("If you want to know about \"" + PlayerInput + "\",");
             GUI.Text_Append("you will have to do some digging on your own!");
          if(ResponseToPlayer == 5):
             print("I don't really feel much like answering your questions right now.");
             GUI.Text_Append("I don't really feel much like answering");
             GUI.Text_Append("your questions right now.");           

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------         






#----Class--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class RPG_GUI:
      
      #Paths
      IMAGE_Directory = os.getcwd() + "\\Images\\";
      SOUND_Directory = os.getcwd() + "\\Sounds\\";

      #L1 Map Navigation Variable Constants
      QUIT = 0;
      L1_INTRO = 1;
      L1_C1 = 2;
      L1_N1 = 3;
      L1_S1 = 4;
      L1_E1 = 5;
      L1_W1 = 6;
      L1_N2 = 7;
      L1_S2 = 8;
      L1_E2 = 9;
      L1_W2 = 10;
      L1_N3 = 11;
      L1_S3 = 12;
      L1_E3 = 13;
      L1_W3 = 14;
      L1_CELESTIASPALACE = 15;
      L1_UNDERGROUND = 16;
      L1_DISCORDSLAIR = 17;
      L1_FRIENDSHIPFOREST = 18;
      L1_PEGASUSCITADEL = 19;
      L1_MOUNTAINOFMEANNESS = 20;
      L1_SWAMPOFSADNESS = 21;
      L1_UNICORNJUNCTION = 22;
      L1_HILLSOFHAPPINESS = 23;
      Need_To_Create_Character = 24;
      L1_N3_Slime_Mold_Encounter = 25;  
      L1_MountainOfMeanness_Harpy_Encounter = 26; 
      L1_SwampOfSadness_Dolphin_Encounter = 27; 
      L1_DiscordsLair_Discord_Boss_Encounter = 28;
      L1_Multiple_Opponents_Encounter = 29; 
      L1_Market_1 = 30;
      Need_To_Create_NPCs = 31;
      L1_NPC_1_Encounter = 32;
      L1_NPC_2_Encounter = 33;
      L1_NPC_3_Encounter = 34;
      COMBAT_SEQUENCE = 99;
      COMBAT_SEQUENCE_MULTIPLE = 100;
      GAME_OVER = 101;

      CHOICE = "";
      LOCATION = L1_INTRO;      

      #Paging Variables
      Create_Character_Page = 1;
      Create_NPC_Page = 1;
      Combat_Attack_Sequence_Page = 1;
      L1_N3_Slime_Mold_Page_Counter = 1;
      L1_MountainOfMeanness_Harpy_Page_Counter = 1;
      L1_SwampOfSadness_Dolphin_Page_Counter = 1;
      L1_DiscordsLair_Discord_Boss_Page_Counter = 1;
      L1_Multiple_Opponents_Encounter_Page_Counter = 1; 
      Retrieved_Player_Input = False;     
      
      #Environment Combat Variables
      Willing_to_Fight = "TRUE";
      L1_N3_Slime_Mold_Alive = True;
      L1_MountainOfMeanness_Harpy_Alive = True;
      L1_SwampOfSadness_Dolphin_Alive = True;
      L1_DiscordsLair_Discord_Boss_Alive = True;
      L1_Multiple_Opponents_Encounter_Alive = True;
      L1_Multiple_Opponents_Num = 0;
      L1_Multiple_Opponents_LOCK = False;
      L1_Multiple_Opponents_ACTIVE = True;
      COMBAT_LOCATION = 0;
      CombatRoundCounter = 1;

      #Map EVENT Variables
      CENTER_FirstTime = True;
      CelestiasPalace_FirstTime = True;
      DiscordsLair_FirstTime = True;
      FriendshipForest_FirstTime = True;      

      #MAP Inventory EVENT Variables
      Found_Staff = False;
      Found_Pendant = False;
      Found_Sigil = False;
      Found_Orb = False;
      Found_PrincessCloak = False;
      Found_Chain_Mail = False;
      Found_Plate_Armor = False; 

      #MAP L1 Skill Items Globals
      Acquired_IceBlasts = False;
      Acquired_FireBalls = False;
      Acquired_Lightning = False;
      Acquired_Telekinesis = False;
      Acquired_Telepathy = False;
      Acquired_Teleportation = False;
      Acquired_TimeWarp = False;
      Acquired_Invisibility = False;
      Acquired_Healing = False;
      Acquired_FriendshipCast = False;

      #MAP L1 Potions Globals
      Found_HealingPotion_1 = False;
      Found_HealingPotion_2 = False;
      Found_HealingPotion_3 = False;
      Found_HealingPotion_4 = False;
      Found_HealingPotion_CelestiasPalace = False;

      #MAP L1 NPCs Globals
      NPC1_Encountered = False;
      NPC2_Encountered = False;
      NPC3_Encountered = False;

      #MAP L1 Traps Globals
      TRAP1_Encountered = False;
      TRAP2_Encountered = False;
      TRAP3_Encountered = False;
      TRAP4_Encountered = False;           

      CharacterToLoad_GET_Value = False;

      #Text and ListBox variables (must be declared up here to be accessible to code below)
      Input_Data = tk.StringVar();
      LB_Abilities_Var = tk.StringVar(); 
      LB_Inventory_Var = tk.StringVar();

      #Pre-load Images
      IMG_Load = Image.open(IMAGE_Directory + "Discord_1.gif");
      IMG_MAP_L1_Intro = Image.open(IMAGE_Directory + "Wolf.jpg");
      IMG_MAP_L1_C1 = Image.open(IMAGE_Directory + "MAP_L1_C1.jpg");
      IMG_MAP_L1_N1 = Image.open(IMAGE_Directory + "MAP_L1_N1.jpg");
      IMG_MAP_L1_N2 = Image.open(IMAGE_Directory + "MAP_L1_N2.jpg");
      IMG_MAP_L1_N3 = Image.open(IMAGE_Directory + "MAP_L1_N3.jpg");
      IMG_MAP_L1_S1 = Image.open(IMAGE_Directory + "MAP_L1_S1.jpg");
      IMG_MAP_L1_S2 = Image.open(IMAGE_Directory + "MAP_L1_S2.jpg");
      IMG_MAP_L1_S3 = Image.open(IMAGE_Directory + "MAP_L1_S3.jpg"); 
      IMG_MAP_L1_E1 = Image.open(IMAGE_Directory + "MAP_L1_E1.jpg");
      IMG_MAP_L1_E2 = Image.open(IMAGE_Directory + "MAP_L1_E2.jpg");
      IMG_MAP_L1_E3 = Image.open(IMAGE_Directory + "MAP_L1_E3.jpg");
      IMG_MAP_L1_W1 = Image.open(IMAGE_Directory + "MAP_L1_W1.jpg");
      IMG_MAP_L1_W2 = Image.open(IMAGE_Directory + "MAP_L1_W2.jpg");
      IMG_MAP_L1_W3 = Image.open(IMAGE_Directory + "MAP_L1_W3.jpg");
      IMG_MAP_L1_CELESTIASPALACE = Image.open(IMAGE_Directory + "MAP_L1_CELESTIASPALACE.jpg");
      IMG_MAP_L1_UNDERGROUND = Image.open(IMAGE_Directory + "MAP_L1_UNDERGROUND.jpg");
      IMG_MAP_L1_DISCORDSLAIR = Image.open(IMAGE_Directory + "MAP_L1_DISCORDSLAIR.jpg");
      IMG_MAP_L1_FRIENDSHIPFOREST = Image.open(IMAGE_Directory + "MAP_L1_FRIENDSHIPFOREST.jpg");
      IMG_MAP_L1_PEGASUSCITADEL = Image.open(IMAGE_Directory + "MAP_L1_PEGASUSCITADEL.jpg");
      IMG_MAP_L1_MOUNTAINOFMEANNESS = Image.open(IMAGE_Directory + "MAP_L1_MOUNTAINOFMEANNESS.jpg");
      IMG_MAP_L1_SWAMPOFSADNESS = Image.open(IMAGE_Directory + "MAP_L1_SWAMPOFSADNESS.jpg");
      IMG_MAP_L1_UNICORNJUNCTION = Image.open(IMAGE_Directory + "MAP_L1_UNICORNJUNCTION.jpg");
      IMG_MAP_L1_HILLSOFHAPPINESS = Image.open(IMAGE_Directory + "MAP_L1_HILLSOFHAPPINESS.jpg");
      IMG_SCENE_L1_MOUNTAINMARKETCABIN_1 = Image.open(IMAGE_Directory + "MountainShop_Cabin_1.jpg");
      IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1 = Image.open(IMAGE_Directory + "MountainShop_Inside_1.jpg");

      #Global to Hold Player Input from Child Frames
      Player_Input = "";

      #Global pointers for passing instantiated objects and/or their attributes between classes
      Plyr_Heroine = None;
      Plyr_Opponent = None;
      CurrentPlayer = "Nobody";
      Opponent_Group = [];
      NPC_1 = None;
      NPC_2 = None;
      NPC_3 = None;

     #SOUNDS
      #Note: To keep game and GUI responsive when you call playsound, you must play each sound in a different thread from mainloop().
      # Also, the new version of playsound is broken and doesn't work right with multi-threading. Old version is better. To remedy this:
      # pip uninstall playsound
      # pip install playsound==1.2.2

    #01.----------------------------------------------------------------------------------------------------------------
      def Sound_Button_Press_1(self): playsound(self.SOUND_Directory + "ButtonPress_1.mp3", block=True);

      def Sound_Button_Press_1_Thread(self):
          threading.Thread(target=self.Sound_Button_Press_1, name="BG_Button_Press_1").start();   
    #02.----------------------------------------------------------------------------------------------------------------
      def Sound_Button_Press_2(self): playsound(self.SOUND_Directory + "ButtonPress_2.mp3", block=False);

      def Sound_Button_Press_2_Thread(self):
          threading.Thread(target=self.Sound_Button_Press_2, name="BG_Button_Press_2").start();   
    #03.----------------------------------------------------------------------------------------------------------------
      def Sound_Button_Press_3(self): playsound(self.SOUND_Directory + "ButtonPress_3.mp3", block=True);

      def Sound_Button_Press_3_Thread(self):
          threading.Thread(target=self.Sound_Button_Press_3, name="BG_Button_Press_3").start();   
    #04.----------------------------------------------------------------------------------------------------------------
      def Sound_RAIN(self): playsound(self.SOUND_Directory + "Rain_1.mp3", block=True);

      def Sound_RAIN_Thread(self):
          threading.Thread(target=self.Sound_RAIN, name="BG_Sound_RAIN").start();   
    #05.----------------------------------------------------------------------------------------------------------------
      def Sound_THUNDER(self): playsound(self.SOUND_Directory + "Thunder1.mp3", block=True);

      def Sound_THUNDER_Thread(self):
          threading.Thread(target=self.Sound_THUNDER, name="BG_Sound_THUNDER").start();  
    #06.----------------------------------------------------------------------------------------------------------------
      def Sound_Wolf_Howl(self): playsound(self.SOUND_Directory + "Wolf_Howl.mp3", block=True);

      def Sound_Wolf_Howl_Thread(self):
          threading.Thread(target=self.Sound_Wolf_Howl, name="BG_Sound_Wolf_Howl").start();             
    #07.----------------------------------------------------------------------------------------------------------------
      def Sound_Footsteps(self): playsound(self.SOUND_Directory + "Footsteps.mp3", block=True);

      def Sound_Footsteps_Thread(self):
          threading.Thread(target=self.Sound_Footsteps, name="BG_Footsteps").start(); 
    #08.----------------------------------------------------------------------------------------------------------------
      def Sound_MockingJay_Whistle(self): playsound(self.SOUND_Directory + "MockingJay_Whistle.mp3", block=True);

      def Sound_MockingJay_Whistle_Thread(self):
          threading.Thread(target=self.Sound_MockingJay_Whistle, name="BG_MockingJay_Whistle").start(); 
    #09.----------------------------------------------------------------------------------------------------------------
      def Sound_Na_Na_Na(self): playsound(self.SOUND_Directory + "Na_Na_Na.mp3", block=True);

      def Sound_Na_Na_Na_Thread(self):
          threading.Thread(target=self.Sound_Na_Na_Na, name="BG_Na_Na_Na").start(); 
    #10.----------------------------------------------------------------------------------------------------------------
      def Sound_Trumpets(self): playsound(self.SOUND_Directory + "Trumpets.mp3", block=True);

      def Sound_Trumpets_Thread(self):
          threading.Thread(target=self.Sound_Trumpets, name="BG_Trumpets").start();
    #11.----------------------------------------------------------------------------------------------------------------
      def Sound_Fire_Burning_1(self): playsound(self.SOUND_Directory + "Fire_Burning_1.mp3", block=True);

      def Sound_Fire_Burning_1_Thread(self):
          threading.Thread(target=self.Sound_Fire_Burning_1, name="BG_Fire_Burning_1").start();
    #12.----------------------------------------------------------------------------------------------------------------
      def Sound_Forest_1(self): playsound(self.SOUND_Directory + "Forest_1.mp3", block=True);

      def Sound_Forest_1_Thread(self):
          threading.Thread(target=self.Sound_Forest_1, name="BG_Forest_1").start();
    #13.----------------------------------------------------------------------------------------------------------------
      def Sound_Horse_Snort_1(self): playsound(self.SOUND_Directory + "Horse_Snort_1.mp3", block=True);

      def Sound_Horse_Snort_1_Thread(self):
          threading.Thread(target=self.Sound_Horse_Snort_1, name="BG_Horse_Snort_1").start();            
    #14.----------------------------------------------------------------------------------------------------------------
      def Sound_Horse_Trot_1(self): playsound(self.SOUND_Directory + "Horse_Trot_1.mp3", block=True);

      def Sound_Horse_Trot_1_Thread(self):
          threading.Thread(target=self.Sound_Horse_Trot_1, name="BG_Horse_Trot_1").start();
    #15.----------------------------------------------------------------------------------------------------------------
      def Sound_Hawk(self): playsound(self.SOUND_Directory + "Hawk.mp3", block=True);

      def Sound_Hawk_Thread(self):
          threading.Thread(target=self.Sound_Hawk, name="BG_Hawk").start();              
    #16.----------------------------------------------------------------------------------------------------------------
      def Sound_Horse_Gallop_1(self): playsound(self.SOUND_Directory + "Horse_Gallop_1.mp3", block=True);

      def Sound_Horse_Gallop_1_Thread(self):
          threading.Thread(target=self.Sound_Horse_Gallop_1, name="BG_Horse_Gallop_1").start();
    #17.----------------------------------------------------------------------------------------------------------------
      def Sound_Wind_1(self): playsound(self.SOUND_Directory + "Wind_1.mp3", block=True);

      def Sound_Wind_1_Thread(self):
          threading.Thread(target=self.Sound_Wind_1, name="BG_Wind_1").start();              
    #-------------------------------------------------------------------------------------------------------------------





    #DRAMATIC PAUSE----------------------------------------------------------------------------------------------------------------
      def Dramatic_Pause_Append(self,NumSeconds,MESSAGE):
          Pause_Amt = (int(NumSeconds) * 1000);
          window.update();
          self.window.after(Pause_Amt, self.Text_Append(MESSAGE));

      def Dramatic_Pause_Write(self,NumSeconds,MESSAGE):
          Pause_Amt = (int(NumSeconds) * 1000);
          window.update();
          self.window.after(Pause_Amt, self.Text_Write(MESSAGE));          
    #------------------------------------------------------------------------------------------------------------------------------

    #---Function-----------------------------------------------------------------------------------------------------
      def Text_Append(self,MESSAGE):
          Previous_Text = self.TXT_Main_Output.get("0.0",tk.END);
          self.TXT_Main_Output.delete("1.0", "end");
          self.TXT_Main_Output.insert("0.0", Previous_Text + MESSAGE);

    #---Function-----------------------------------------------------------------------------------------------------
      def Text_Write(self,MESSAGE):
          self.TXT_Main_Output.delete("0.0", "end");
          self.TXT_Main_Output.insert("0.0", "\n" + MESSAGE);  


        #------------------------------------------------------------------------------------------------------------------------- 
      def All_Nav_Buttons_DISABLE(self):
          self.BTN_North["state"] = tk.DISABLED;
          self.BTN_South ["state"] = tk.DISABLED;
          self.BTN_East["state"] = tk.DISABLED;
          self.BTN_West["state"] = tk.DISABLED; 

        #------------------------------------------------------------------------------------------------------------------------- 
      def All_Nav_Buttons_ENABLE(self):
          self.BTN_North["state"] = tk.NORMAL;
          self.BTN_South ["state"] = tk.NORMAL;
          self.BTN_East["state"] = tk.NORMAL;
          self.BTN_West["state"] = tk.NORMAL;  

        #------------------------------------------------------------------------------------------------------------------------- 


    #---Function-----------------------------------------------------------------------------------------------------
      def SwitchBoard(self):
          print("SwitchBoard: Value of LOCATION =",self.LOCATION);
          if(self.LOCATION == self.Need_To_Create_Character): self.Create_Character();
          if(self.LOCATION == self.Need_To_Create_NPCs): self.Create_NPCs();
          if(self.LOCATION == self.L1_INTRO): self.Introduction();
          if(self.LOCATION == self.L1_C1): self.CENTER_1();
          if(self.LOCATION == self.L1_N1): self.NORTH_1();
          if(self.LOCATION == self.L1_S1): self.SOUTH_1();
          if(self.LOCATION == self.L1_E1): self.EAST_1();
          if(self.LOCATION == self.L1_W1): self.WEST_1();
          if(self.LOCATION == self.L1_N2): self.NORTH_2();
          if(self.LOCATION == self.L1_S2): self.SOUTH_2();
          if(self.LOCATION == self.L1_E2): self.EAST_2();
          if(self.LOCATION == self.L1_W2): self.WEST_2();
          if(self.LOCATION == self.L1_N3): self.NORTH_3();
          if(self.LOCATION == self.L1_S3): self.SOUTH_3();
          if(self.LOCATION == self.L1_E3): self.EAST_3();
          if(self.LOCATION == self.L1_W3): self.WEST_3();
          if(self.LOCATION == self.L1_CELESTIASPALACE): self.CELESTIASPALACE();
          if(self.LOCATION == self.L1_UNDERGROUND): self.UNDERGROUND();
          if(self.LOCATION == self.L1_DISCORDSLAIR): self.DISCORDSLAIR();
          if(self.LOCATION == self.L1_FRIENDSHIPFOREST): self.FRIENDSHIPFOREST();
          if(self.LOCATION == self.L1_PEGASUSCITADEL): self.PEGASUSCITADEL();
          if(self.LOCATION == self.L1_MOUNTAINOFMEANNESS): self.MOUNTAINOFMEANNESS();
          if(self.LOCATION == self.L1_SWAMPOFSADNESS): self.SWAMPOFSADNESS();
          if(self.LOCATION == self.L1_UNICORNJUNCTION): self.UNICORNJUNCTION();
          if(self.LOCATION == self.L1_HILLSOFHAPPINESS): self.HILLSOFHAPPINESS();
          if(self.LOCATION == self.L1_Market_1): self.Market_1();
          if(self.LOCATION == self.L1_N3_Slime_Mold_Encounter): self.Slime_Mold_Encounter();
          if(self.LOCATION == self.L1_MountainOfMeanness_Harpy_Encounter): self.Harpy_Encounter();
          if(self.LOCATION == self.L1_SwampOfSadness_Dolphin_Encounter): self.Dolphin_Encounter();
          if(self.LOCATION == self.L1_DiscordsLair_Discord_Boss_Encounter): self.Discord_Boss_Encounter();
          if(self.LOCATION == self.L1_Multiple_Opponents_Encounter): self.Multiple_Opponents_Encounter();
          if(self.LOCATION == self.L1_NPC_1_Encounter): self.NPC_1_Encounter();
          if(self.LOCATION == self.L1_NPC_2_Encounter): self.NPC_2_Encounter();
          if(self.LOCATION == self.L1_NPC_3_Encounter): self.NPC_3_Encounter();
          if(self.LOCATION == self.COMBAT_SEQUENCE): self.Pony_Combat();
          if(self.LOCATION == self.COMBAT_SEQUENCE_MULTIPLE): self.Pony_Combat_Multiple();
          if(self.LOCATION == self.GAME_OVER): self.Game_Over_Man();

    #---Function-----------------------------------------------------------------------------------------------------
      def Navigate_Action(self):
          #self.Sound_Button_Press_1_Thread();
          self.Sound_Button_Press_2_Thread();
          #self.Sound_Button_Press_3_Thread();
          self.SwitchBoard();
          self.Input_Data.set("");
          self.CHOICE = "#";
          self.ENT_Main_Input.focus();

    #---Function-----------------------------------------------------------------------------------------------------
      def Introduction(self):

          self.IMG_MAP_L1_Intro = self.IMG_MAP_L1_Intro.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_Intro);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);         
          self.Sound_Wolf_Howl_Thread();

          MESSAGE = "Welcome to Discord's Dungeon LEVEL 1.";
          MESSAGE += "\n\n Here's a map showing all the items on this level.";
          MESSAGE += "\n\n Ready to proceed?";
          MESSAGE += "\n\n If so, enter \"y\".\n\n Then click \"GO\" to continue.";
          self.Text_Write(MESSAGE);

          if(self.CHOICE == "y"):   
             self.LOCATION = self.Need_To_Create_Character;
             self.CHOICE = "#"; 
             self.SwitchBoard();

    #---Function-----------------------------------------------------------------------------------------------------
      def Initialize_Character(self):
          self.LAB_Name_Output.configure(text="Anonymous");
          self.LAB_Gender_Output.configure(text="Non-existant");
          self.LAB_Class_Output.configure(text="Generic Entity");
          self.LAB_Health_Output.configure(text="0");
          self.LAB_Mag_Eng_Output.configure(text="0");
          self.LAB_Attack_Output.configure(text="0");
          self.LAB_Defense_Output.configure(text="0");
          self.LAB_Charisma_Output.configure(text="0");
          self.LAB_Combat_Exp_Output.configure(text="0");
          self.LAB_Level_Output.configure(text="0");
          self.LAB_Armor_Output.configure(text="0");
          self.LAB_Weapon_Output.configure(text="0");
          self.LAB_Magic_Output.configure(text="0");
          self.LAB_Money_Output.configure(text="0");
          self.LB_Inventory_Var.set([]); #clear ListBox
          self.LB_Abilities_Var.set([]); #clear ListBox

    #---Function-----------------------------------------------------------------------------------------------------
      def Initialize_Game(self):
          self.LOCATION = self.L1_INTRO;
          self.CENTER_FirstTime = True;
          self.CelestiasPalace_FirstTime = True;
          self.DiscordsLair_FirstTime = True;
          self.FriendshipForest_FirstTime = True;  
          self.ENT_Main_Input.focus();
          self.All_Nav_Buttons_DISABLE();           

    #---Function-----------------------------------------------------------------------------------------------------
      def Create_Character(self):
          print("Called Create_Character.");
          if(self.Create_Character_Page == 1):
             self.Initialize_Character();
             MESSAGE = "Before you can play the game, you need to choose a";
             MESSAGE += "\n character class. Choose from below:\n";
             MESSAGE += "\n   1. Alicorn";
             MESSAGE += "\n   2. Unicorn";
             MESSAGE += "\n   3. Pegasus";
             MESSAGE += "\n   4. Princess (Royal)";
             MESSAGE += "\n   5. Pony (Basic)";
             MESSAGE += "\n\n Enter selection number.";
             self.Text_Write(MESSAGE);

          if(self.Create_Character_Page == 2):
             CHOICE = self.ENT_Main_Input.get();
             if(CHOICE == "1"): 
                self.Text_Write("\n Instantiating an ALICORN.");
                self.Plyr_Heroine = ALICORN();
             elif(CHOICE == "2"): 
                  self.Text_Write("\n Instantiating a UNICORN.");
                  self.Plyr_Heroine = UNICORN(); 
             elif(CHOICE == "3"): 
                  self.Text_Write("\n Instantiating a PEGASUS.");
                  self.Plyr_Heroine = PEGASUS();
             elif(CHOICE == "4"): 
                  self.Text_Write("\n Instantiating a PRINCESS.");
                  self.Plyr_Heroine = PRINCESS();            
             elif(CHOICE == "5"): 
                  self.Text_Write("\n Instantiating a basic PONY.");
                  self.Plyr_Heroine = PONY();
             else: 
                   self.Text_Write("\nThat was an INVALID option.\nPlease choose a LEGITIMATE character class. (1-5)");
                   self.Create_Character_Page -= 2;

             if(self.Plyr_Heroine != None): self.Plyr_Heroine.Display_Entity();              

          if(self.Create_Character_Page == 3):
             MESSAGE = "Now please decide a GENDER for your character.";
             MESSAGE += "\n Choose from below:\n";
             MESSAGE += "\n   1. Female";
             MESSAGE += "\n   2. Male";
             MESSAGE += "\n   3. Non-binary";
             MESSAGE += "\n\n Enter selection number.";
             self.Text_Write(MESSAGE);

          if(self.Create_Character_Page == 4):
             CHOICE = self.ENT_Main_Input.get();
             if(CHOICE == "1"): 
                self.Text_Write("\n It's a beautiful girl pony!");
                self.Plyr_Heroine.EntityGender = "Female";
             elif(CHOICE == "2"): 
                self.Text_Write("\n It's a handsome boy pony!");
                self.Plyr_Heroine.EntityGender = "Male";
             elif(CHOICE == "3"): 
                self.Text_Write("\n It's a wonderfully unique non-binary pony!");  
                self.Plyr_Heroine.EntityGender = "Non-binary"; 
             else: 
                   self.Text_Write("\nThat was an INVALID option.\nPlease choose a LEGITIMATE gender. (1-3)");
                   self.Create_Character_Page -= 2; 

             self.Plyr_Heroine.Display_Entity();

          if(self.Create_Character_Page == 5):
             MESSAGE = "Now please chose a NAME for your character.";
             MESSAGE += "\nEnter a name in the input field below.";
             self.Text_Write(MESSAGE);

          if(self.Create_Character_Page == 6):
             CHOICE = self.ENT_Main_Input.get();
             if(CHOICE != ""): 
                MESSAGE = CHOICE + " is a lovely name.";
                MESSAGE += "\nHappy birthday, " + CHOICE + "!";
                self.Text_Write(MESSAGE);
                self.Plyr_Heroine.EntityName = CHOICE;
                self.Plyr_Heroine.Display_All();
             else: 
                   self.Text_Write("\nNothing is an INVALID name.\nPlease enter a LEGITIMATE name.");
                   self.Create_Character_Page -= 2; 
          
          if(self.Create_Character_Page == 7):
             self.Text_Write("\nGot your character created.");
             self.Text_Append("Now let's make some NPCs!");  

          if(self.Create_Character_Page == 8):
             self.LOCATION = self.Need_To_Create_NPCs;
             self.CHOICE = "#"; 
             #self.SwitchBoard();

          #Ending actions
          self.Text_Append("\n Click \"GO\" to continue.\n"); 
          self.Create_Character_Page += 1;                   


    #---Function-----------------------------------------------------------------------------------------------------
      def CENTER_1(self):
          print("\nIn L1_CENTER_1 now.");
          self.IMG_MAP_L1_C1 = self.IMG_MAP_L1_C1.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_C1);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);    

          if(self.CHOICE == "n"):   
             self.LOCATION = self.L1_N1;
             self.CHOICE = "#"; 
             self.SwitchBoard();

          elif(self.CHOICE == "s"):   
               self.LOCATION = self.L1_S1;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "e"):   
               self.LOCATION = self.L1_E1;
               self.CHOICE = "#"; 
               self.SwitchBoard();

          elif(self.CHOICE == "w"):   
               self.LOCATION = self.L1_W1;
               self.CHOICE = "#";
               self.SwitchBoard();
               
          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Found_Staff == False):
                if(self.CHOICE == "1"):
                   self.Found_Staff = True;
                   self.Plyr_Heroine.INV_Has_Staff = "TRUE";
                   self.Text_Write("\nYou acquire: The gilded Staff of Power!");
                   self.Text_Append("\nWell done!\n");
                   self.Plyr_Heroine.Inventory_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("\nYou foolishly reject the divine gift and walk away.");

                self.Text_Append("\nClick \"GO\" to continue.\n");     

          else: 
               VIEW = "LOCATION: L1_CENTER_1\n";
               if(self.CENTER_FirstTime == True):
                  print("Value of CENTER_FirstTime = TRUE.");
                  VIEW += "\nYou are in a meadow with tall, green grass and reeds swaying in";
                  VIEW += "\nthe breeze. Something shimmers in the distance. A gentle breeze";
                  VIEW += "\nblows all around you, swirling with the intoxicating scents of";
                  VIEW += "\nspring. Gossamer threads of dew like little diamonds glisten in";
                  VIEW += "\nthe sunlight, casting rainbow colors through a thousand tiny";
                  VIEW += "\nsparkling prisms.";
                  self.CENTER_FirstTime = False;
               elif(self.CENTER_FirstTime == False):
                  print("Value of CENTER_FirstTime = FALSE.");
                  VIEW += "\nYou return to the meadow with the tall, green grass and reeds";
                  VIEW += "\nswaying in a gentle breeze. The place you first found yourself";
                  VIEW += "\nwhen you were transported to this magical, mystical world.\n";  
                  VIEW += "\nIn the distance, something shimmers. A cool gust of wind from";
                  VIEW += "\nthe north fills your nostrils with a refreshing tinge of pine.\n"; 
                  if(self.Found_Staff == False):
                     VIEW += "\nIn the dew-covered grass to the South-East, you notice";
                     VIEW += "\nsomething with a metallic glimmer protruding from the  grasss.";
                     VIEW += "\nDidn't notice before. What could it be? Pick it up?"; 
                     VIEW += "\n\n  0 = NO\n  1 = YES";  
                  elif(self.Found_Staff == True): 
                     VIEW += "\nYou see broken reeds and flattened grass in the shape of";
                     VIEW += "\nthe Power Staff you formerly found at this location.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see a ranch house. And beyond it?";
               VIEW += "\nA purple and blue mountain range.\n";
               VIEW += "\nSOUTH: You see a forest of tall evergreens. Through the";
               VIEW += "\ntrees you see a lake in the distance.\n";
               VIEW += "\nEAST:  You see a village. Beyond that? A sunlit valley";
               VIEW += "\novershadowed by mountains to the north.\n";
               VIEW += "\nWEST:  You see an arid, rocky desert. Beyond that? Caves.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n"; 
            
               self.Text_Write(VIEW);

    #---Function-----------------------------------------------------------------------------------------------------
      def NORTH_1(self):
          print("\nIn L1_NORTH_1 now.");
          self.IMG_MAP_L1_N1 = self.IMG_MAP_L1_N1.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_N1);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);           

          if(self.CHOICE == "n"):   
             self.LOCATION = self.L1_N2;
             self.CHOICE = "#"; 
             self.SwitchBoard();

          elif(self.CHOICE == "s"):   
               self.LOCATION = self.L1_C1;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_NORTH1-East: To the EAST, you see solid walls");
               self.Text_Append("of stone. They are definitely un-climb-able.");
               if(self.Acquired_IceBlasts == False):
                  self.Text_Append("\nIn the wall of stone, you see what appears to be");
                  self.Text_Append("a parcel of parchment stuffed into a crevice. Is");
                  self.Text_Append("it some sort of message? What could it be? Pull");
                  self.Text_Append("it out and try to read it? Could this be a TRAP?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.Acquired_IceBlasts == True):
                    self.Text_Append("\nLaying beside the wall of stone, you see the");
                    self.Text_Append("empty parcel that once held the parchment from");
                    self.Text_Append("which you acquired the skill of Ice Blasts."); 

               self.Text_Append("\nClick \"GO\"to continue.\n");        

          elif(self.CHOICE == "w"):   
               self.Text_Write("L1_NORTH1-West: Westward you see ... trees!");
               self.Text_Append(" Lots and lots of trees.");

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Acquired_IceBlasts == False):
                if(self.CHOICE == "1"):
                   self.Acquired_IceBlasts = True;
                   self.Plyr_Heroine.SKILL_Has_IceBlasts = "TRUE";
                   self.Text_Write("\nYou acquire the magic skill of: Ice Blasts!");
                   self.Text_Append("\nExcellent!\n");
                   self.Plyr_Heroine.SKILL_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("\nIt might be a trap. So you leave the parcel be.");

                self.Text_Append("\nClick \"GO\"to continue.\n");

          else: 
               VIEW = "LOCATION: L1_NORTH_1\n";
               VIEW += "\nYou find yourself standing in the courtyard of an old ranch";
               VIEW += "\nhouse. Beside it sits a bright red barn with white-washed";
               VIEW += "\nwindow frames and two large, hinged wooden doors swinging";
               VIEW += "\nslightly in the wind.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see a purple and blue mountain range.\n";
               VIEW += "\nSOUTH: You see a meadow with tall, green grass and reeds";
               VIEW += "\nswaying in the breeze. Something shimmers in the distance.\n";
               VIEW += "\nEAST: You see an impassible drop-off into a shadowy valley";
               VIEW += "\nbeyond a rocky ledge.\n";
               VIEW += "\nWEST: You see towering walls of solid stone impossible to climb.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n"; 

               self.Text_Write(VIEW);

    #---Function-----------------------------------------------------------------------------------------------------
      def SOUTH_1(self):
          print("\nIn L1_SOUTH_1 now.");
          self.IMG_MAP_L1_S1 = self.IMG_MAP_L1_S1.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_S1);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);          

          if(self.CHOICE == "n"):   
             self.LOCATION = self.L1_C1;
             self.CHOICE = "#"; 
             self.SwitchBoard();

          elif(self.CHOICE == "s"):   
               self.LOCATION = self.L1_S2;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_SOUTH1-East: You trot east towards the apple cart");
               self.Text_Append("and a friendly-looking pony with a yellow, straw hat.");
               self.Text_Append("She holds her hoof up in the air and asks you to stop.");
               self.Text_Append("This precocious pony won't let you pass :-(");
               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "w"):   
               self.Text_Write("\n L1_SOUTH1-West: You gallop up to the pink pony. But");
               self.Text_Append("she refuses to get off her 99 bright red balloons and");
               self.Text_Append("blocks any further progress to the east at this point.");
               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          else: 
               VIEW = "LOCATION: L1_SOUTH_1\n";
               VIEW += "\nYou are standing in a damp, cool forest of tall";
               VIEW += "\nevergreens. The trees have grown very tall in this";
               VIEW += "\narea, and enshadow you with a canopy far above your";
               VIEW += "\nhead. You can hear many birds singing their songs and";
               VIEW += "\nnesting in the branches as they sway in the breeze.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see a meadow with tall, green grass and reeds";
               VIEW += "\nswaying in the breeze. Something shimmers in the distance.\n";
               VIEW += "\nSOUTH: You see a lake surrounded by evergreens and rippling";
               VIEW += "\n with their reflection.\n";
               VIEW += "\nEAST: You see an apple cart full of red, delicious apples.";
               VIEW += "\nBeside the cart stands a pony wearing a straw hat.\n";
               VIEW += "\nWEST: You see a large, pink pony bouncing playfully";
               VIEW += "\n on 99 bright red balloons.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n"; 

               self.Text_Write(VIEW);       
    #---Function-----------------------------------------------------------------------------------------------------
      def EAST_1(self):
          print("\nIn L1_EAST_1 now.");
          self.IMG_MAP_L1_E1 = self.IMG_MAP_L1_E1.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_E1);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);          

          if(self.CHOICE == "n"):   
             self.Text_Write("L1_EAST1-North: You try to move north, but are blocked");
             self.Text_Append("by painful, irritating thistles that stab into your flanks");
             self.Text_Append("from thick, dry hedges as far as your eyes can see.");
             self.Text_Append("If only you had a flame?");
             self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "s"):   
               self.Text_Write("L1_EAST1-South: You approach the old hut and pull on the");
               self.Text_Append("hinged iron door with all your might. But it is locked.");
               self.Text_Append("The rusty hinges and corroded dead-bolt hold the door");
               self.Text_Append("shut remarkably well despite their age. And though you");
               self.Text_Append("try with all your might? It still won't budge.");
               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "e"):   
               self.LOCATION = self.L1_E2;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "w"):   
               self.LOCATION = self.L1_C1;
               self.CHOICE = "#";
               self.SwitchBoard();               

          else: 
               VIEW = "LOCATION: L1_EAST_1\n";
               VIEW += "\nSurrounding you is what appears to be an abandoned";
               VIEW += "\nvillage. There are about a dozen wooden cottages with";
               VIEW += "\nthatched roofs and an old hut made of straw that sits";
               VIEW += "\nin the middle of what appears to be the town square.";
               VIEW += "\nYou can see a fire pit smoldering in the distance, and";
               VIEW += "\nwhat appears to be a kettle with a strange bubbling";
               VIEW += "\nliquid brewing.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see thick, thorny hedges through which you can";
               VIEW += "\nsee no light passing through their branches.\n";
               VIEW += "\nSOUTH: You see a small, delapidated wooden hut. In front";
               VIEW += "\nof this hut is a hinged iron door with a key lock.\n";
               VIEW += "\nEAST: You see a swiftly flowing broad river. There are";
               VIEW += "\nsand bars in the distance.\n";
               VIEW += "\nWEST: You see a meadow with tall, green grass and reeds";
               VIEW += "\nswaying in the breeze. Something shimmers in the distance.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n";                

               self.Text_Write(VIEW);   

      #---Function-----------------------------------------------------------------------------------------------------
      def WEST_1(self):
          print("\nIn L1_WEST_1 now.");
          self.IMG_MAP_L1_W1 = self.IMG_MAP_L1_W1.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_W1);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);          

          if(self.CHOICE == "n"):   
             self.Text_Write("L1_WEST1-North: You walk towards the apple trees. Some");
             self.Text_Append("have fallen to the ground. You see bright red apples");
             self.Text_Append("hanging from each tree that surrounds you. Further");
             self.Text_Append("north and east you see a colorful town and station.");
             self.Text_Append("You can proceed no further in this direction.");
             self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "s"):
               if(self.Acquired_FireBalls == False):   
                  self.Text_Write("L1_WEST1-South: You walk over to the oak table and");
                  self.Text_Append("try to open the iron chest but cannot. It is locked.");
                  self.Text_Append("If only you had a key? On the table you see a 6-sided");
                  self.Text_Append("dice. Beside it a sign says:\n");
                  self.Text_Append("┌──────────────────────────────────┐");
                  self.Text_Append("│  Roll a six? It's in the mix.        ");
                  self.Text_Append("│  Roll any other? Pain's your brother.");
                  self.Text_Append("└──────────────────────────────────┘");
                  self.Text_Append("                   |  |              ");
                  self.Text_Append("                   |  |              ");
                  self.Text_Append("\nWill you roll the dice?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.Acquired_FireBalls == True): 
                    self.Text_Write("\n L1_WEST1-South: You walk over to the oak table and"); 
                    self.Text_Append("burned up sign and dice you had previously rolled");
                    self.Text_Append("to acquire the Fire Balls skill.");

               self.Text_Append("\nClick \"GO\"to continue.\n");   

          elif(self.CHOICE == "e"):   
               self.LOCATION = self.L1_C1;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "w"):   
               self.LOCATION = self.L1_W2;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "u"):   
               self.LOCATION = self.L1_UNICORNJUNCTION;
               self.CHOICE = "#";
               self.SwitchBoard(); 

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Acquired_FireBalls == False):
                if(self.CHOICE == "1"):
                   self.Text_Write("You scoop up the 6-sided dice and blow a kiss to Lady Luck!\n");
                   LadyLuck = random.randint(1,6);
                   self.Text_Append("You roll a " + str(LadyLuck) + "!\n");
                   if(LadyLuck == 6):
                      self.Text_Append("You did it! You rolled a perfect 6!");
                      self.Text_Append("The dice you just rolled shimmers and turns into a KEY!");
                      self.Text_Append("You insert the key into the locked box. Click! It opens!");
                      self.Text_Append("\nYou pull out the parchment inside and unfold it. It");
                      self.Text_Append("contains details for exciting molecules to create intense");
                      self.Text_Append("heat  and spontaneous flame. You acquire the skill:");
                      self.Text_Append("\nFire Balls! Nice.\n");
                      self.Acquired_FireBalls = True;
                      self.Plyr_Heroine.SKILL_Has_FireBalls = "TRUE";
                      self.Plyr_Heroine.SKILL_Display();
                   else:
                        self.Text_Append("Sorry Charly. No dice this time. You did not roll a 6.");
                        self.Text_Append("Because you did not roll a 6? You get ... PAIN!");
                        self.Text_Append("An energy bolt emanates from the box shocking");
                        self.Text_Append("you and doing 5 points of dammage.");
                        self.Text_Append("\nYour health WAS: " + str(self.Plyr_Heroine.EntityHealth));
                        self.Plyr_Heroine.EntityHealth -= 5;
                        self.Text_Append("Your health is NOW: " + str(self.Plyr_Heroine.EntityHealth));
                        self.Plyr_Heroine.Display_Entity();

                elif(self.CHOICE == "0"):
                     self.Text_Write("\nIt might be a trap. You leave the dice on the table.");

                self.Text_Append("\nClick \"GO\"to continue.\n");                             

          else: 
               VIEW = "LOCATION: L1_WEST_1\n";
               VIEW += "\nYou plod into an arid, sandy plane. All around you";
               VIEW += "\nthere is withered grass and sparse, dessicated,";
               VIEW += "\nshriveled up trees. Randomly dotted here and there";
               VIEW += "\nyou see large cactuses spiraling upward towards the ";
               VIEW += "\nscorching sun. In between these random and sporadically";
               VIEW += "\npositioned cacti, you see dull gray boulders of pourous";
               VIEW += "\nsandstone. Some of the cacti are have lovely lavender";
               VIEW += "\nflowers blooming between their thorns. You wonder, how";
               VIEW += "\nheavenly SWEET might one of these blossoms taste?";
               VIEW += "\n\nTo the north-east, you see what seems to be a brightly";
               VIEW += "\ncolored train station in the middle of a busy bustling";
               VIEW += "\ntown square.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see wild apple trees. On them hang various red,";
               VIEW += "\ndelicious looking apples. Beyond that? A VILLAGE!\n";
               VIEW += "\nSOUTH: You see a an old table made of oak with a single,";
               VIEW += "\niron chest with a key hole in the middle.\n";
               VIEW += "\nEAST: You see a meadow with tall, green grass and reeds";
               VIEW += "\nswaying in the breeze. Something shimmers in the distance.\n";
               VIEW += "\nWEST: You see dusty, grey, rocky caves protruding from a";
               VIEW += "\nmarbled granite hillside.\n";
               VIEW += "\nU: North-East is a brightly colored train station and town.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n";                

               self.Text_Write(VIEW);                

    #---Function-----------------------------------------------------------------------------------------------------
      def NORTH_2(self):
          print("\nIn L1_NORTH_2 now.");
          self.IMG_MAP_L1_N2 = self.IMG_MAP_L1_N2.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_N2);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);           

          if(self.CHOICE == "n"):   
             self.LOCATION = self.L1_N3;
             self.CHOICE = "#"; 
             self.SwitchBoard();

          elif(self.CHOICE == "s"):   
               self.LOCATION = self.L1_N1;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "e"):   
               self.Text_Write("\n L1_NORTH2-East: You try to ascend the exposed mountain");
               self.Text_Append("side, but it is far too steep and you keep sliding back.");
               if(self.Found_Pendant == False):
                  self.Text_Append("A bit further EAST, you see a silver glimmer in the");
                  self.Text_Append("limbs of a small evergreen.  Could it be a trick of ");
                  self.Text_Append("the light? Something valuable? A trap? Investigate?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.Found_Pendant == True):
                      self.Text_Append("\nYou see a bare limb on an evergreen. It is the");
                      self.Text_Append("same tree where you formerly found the pendant.");

               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "w"):   
               self.Text_Write("\n L1_NORTH2-West: You walk over to the campsite.");
               self.Text_Append("The tent is empty. On the campfire boils a pot of soup.");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Found_Pendant == False):
                if(self.CHOICE == "1"):
                   self.Found_Pendant = True;
                   self.Plyr_Heroine.INV_Has_Pendant = "TRUE";
                   self.Text_Write("\nYou acquire the magic item: Celestia's Pendant");
                   self.Text_Append("\nExcellent!\n");
                   self.Plyr_Heroine.Inventory_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("Not all things that shine and shimmer are good for");
                     self.Text_Append("your health. You decide to leave it alone.");

                self.Text_Append("\nClick \"GO\"to continue.\n");                           

          else: 
               VIEW = "LOCATION: L1_NORTH_2\n";
               VIEW += "\nYou find yourself at the base of a blue and purple";
               VIEW += "\nmountain range. Further north, you spy a meandering";
               VIEW += "\npath that winds its way up into the mountains. Strewn"; 
               VIEW += "\nalong this path are flat flaked of sandstone speckled";
               VIEW += "\nwith something that glitters and catches your eye. In";
               VIEW += "\nthe distance, you see craggy, white mountain peaks";
               VIEW += "\npoking through puffy rings of clouds.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You spy tall mountain peaks ringed by puffy";
               VIEW += "\nwhite clouds.\n";
               VIEW += "\nSOUTH: You see the courtyard of and old ranch house.";
               VIEW += "\nBeside it stands a bright red barn.\n";
               VIEW += "\nEAST: You see the rocky base of an exposed mountain";
               VIEW += "\nside. It is far too steep to climb.\n";
               VIEW += "\nWEST: You notice a solitary campsite. An old, mildew";
               VIEW += "\nstained canvas tent is pitched against a tree. A small";
               VIEW += "\ncampfire is burning beside the tent.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n"; 

               self.Text_Write(VIEW);

    #---Function-----------------------------------------------------------------------------------------------------
      def SOUTH_2(self):
          print("\nIn L1_SOUTH_2 now.");
          self.IMG_MAP_L1_S2 = self.IMG_MAP_L1_S2.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_S2);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);           

          if(self.CHOICE == "n"):   
             self.LOCATION = self.L1_S1;
             self.CHOICE = "#"; 
             self.SwitchBoard();

          elif(self.CHOICE == "s"):   
               self.LOCATION = self.L1_S3;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.TRAP1_Encountered == False):
                if(self.CHOICE == "1"):
                   self.TRAP1_Encountered = True;
                   self.Text_Write("!!!BOOM!!! It was all a TRAP. The box blows up in your");
                   self.Text_Append("face. Shrapnel pierces your skin with tiny slivers of");
                   self.Text_Append("metallic PAIN! This wasn't such a good idea, after");
                   self.Text_Append("all. As a result, you lose 10 health.");
                   self.Text_Append("\nYour health WAS: " + str(self.Plyr_Heroine.EntityHealth));
                   self.Plyr_Heroine.EntityHealth -= 10;
                   self.Text_Append("Your health is NOW: " + str(self.Plyr_Heroine.EntityHealth));
                   self.Plyr_Heroine.Display_Entity();
                elif(self.CHOICE == "0"):
                     self.Text_Write("You cautiously decide to leave the lever as it is.");
                     self.Text_Append("But you can't help but wonder what WONDERFUL,");
                     self.Text_Append("MAGICAL thing you might find if you gave it a tug?");

                self.Text_Append("\nClick \"GO\"to continue.\n");               

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_SOUTH2-East: You walk east. Adorable, chattering, playful");
               self.Text_Append("otters siddenly surround you. You can go no further east.");
               if(self.TRAP1_Encountered == False):
                  self.Text_Append("\nYou see a metal box with a lever on its side and a");
                  self.Text_Append("shiny, silver bell on top. The lever looks SOOOO ");
                  self.Text_Append("tempting. If you pulled on it, what would it DO?");
                  self.Text_Append("Would it ring that beautiful, bright silver bell?");
                  self.Text_Append("Will you pull the lever?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.TRAP1_Encountered == True):   
                    self.Text_Append("\nYou see the silver bell you formerly pulled");
                    self.Text_Append("on that blew up in yoru face. It's broken now");
                    self.Text_Append("and so can do you no more dammage.");
               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "w"):   
               self.Text_Write("L1_SOUTH2-West: Plodding westward through the shallow water,");
               self.Text_Append("you wade among watercress. Small fish swim by your hooves.");
               self.Text_Append("\nWading out of the shallows, you step onto dry land. The");
               self.Text_Append("shore where you stand is rimmed with tall grass. You glance");               
               self.Text_Append("further to the west, ascending gradually to the top of a hill.");
               self.Text_Append("However, from here you can go no further. You are blocked");
               self.Text_Append("by an impassible wall of volcanic rocks and stones.");
               self.Text_Append("\nClick \"GO\"to continue.\n");   

          elif(self.CHOICE == "h"):   
               self.LOCATION = self.L1_HILLSOFHAPPINESS;
               self.CHOICE = "#";
               self.SwitchBoard();               

          else: 
               VIEW = "LOCATION: L1_SOUTH_2\n";
               VIEW += "\nYou arrive at a beautiful, blue pristine lake. Its";
               VIEW += "\ntranslucent waters are as transparent as glass.";
               VIEW += "\nAs the wind blows, it generates ripples that cascade";
               VIEW += "\nacross the surface, generating small waves with aqua";
               VIEW += "\nblue crests and troughs. ";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see a dark green forest of evergreens. The";
               VIEW += "\ncanopy of trees casts shadows over everything beneath.\n";
               VIEW += "\nSOUTH: You see a causeway of flat, gray stones. They";
               VIEW += "\nprotroud from the water and lead to a small island not.";
               VIEW += "\nfar from shore\n";
               VIEW += "\nEAST: You see a narrow beach covered with soft, white,";
               VIEW += "\nsugary sand. You notice several playful otters darting to";
               VIEW += "\nand fro across this sand.\n";
               VIEW += "\nWEST: You a section of shallow water rippling across several";
               VIEW += "\nexposed sandbars. Beyond that? Green hills of wildflowers.\n";
               VIEW += "\nH: To the south-west in the distance you see roving green";
               VIEW += "\nhills covered with beautiful lavender, fushia, azure and";
               VIEW += "\npink wildflowers swaying in a gentle breeze.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n"; 

               self.Text_Write(VIEW); 

    #---Function-----------------------------------------------------------------------------------------------------
      def EAST_2(self):
          print("\nIn L1_EAST_2 now.");
          self.IMG_MAP_L1_E2 = self.IMG_MAP_L1_E2.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_E2);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);           

          if(self.CHOICE == "n"):   
             self.Text_Write("L1_EAST2-North: Trotting north, you examine the fishing");
             self.Text_Append("pole. It has no hook on it, so it is not likely to be");
             self.Text_Append("useful in its current condition. If only you could find a");
             self.Text_Append("hook? It might become useful to catch something. Hmmm...");
             self.Text_Append("\nBeyond this tree, you walktowards the base of the mountain.");
             self.Text_Append("It's covered with gray, colorles lichens and moss. The entire");
             self.Text_Append("mountain, from the base to the peak, appears completely devoid");
             self.Text_Append("of all color. You feel as though you are Dorothy and now");
             self.Text_Append("leaving OZ to go back to Kansas.\n");
             self.Text_Append("But you aren't in Kansas anymore, Dorothy! For some reason,");
             self.Text_Append("you feel very grumpy and agitated now. You begin to ascend");
             self.Text_Append("\nthe montain but are overcome with dread and trepidation");
             self.Text_Append("\nso you can move no further in this direction.");
             self.Text_Append("\nClick \"GO\"to continue.\n");              

          elif(self.CHOICE == "s"): 
               self.Text_Write("L1_EAST2-South: You walk south towards the cart of green");
               self.Text_Append("apples. Why is it missing a wheel? Unfortunately, it");
               self.Text_Append("seems you can't go further south from here.");
               if(self.Acquired_Lightning == False):
                  self.Text_Append("Further examining the broken apple cart, you notice a");
                  self.Text_Append("small plank protruding from its shattered, front axel");
                  self.Text_Append("with symbols inscribed on its edge. What could these");
                  self.Text_Append("symbols mean?\n");
                  self.Text_Append("DARE you read the strange symbols out loud? What would");
                  self.Text_Append("happen if you did? Will you?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.Acquired_Lightning == True):
                    self.Text_Append("\nYou see a pile of ashes and glowing embers");
                    self.Text_Append("where there once was the plank from which");
                    self.Text_Append("you read the magic runes and acquired the");
                    self.Text_Append("magic skill of LIGHTNING.");
               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "e"):   
               self.LOCATION = self.L1_E3;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "w"):   
               self.LOCATION = self.L1_E1;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "m"):   
               self.LOCATION = self.L1_MOUNTAINOFMEANNESS;
               self.CHOICE = "#";
               self.SwitchBoard(); 

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Acquired_Lightning == False):
                if(self.CHOICE == "1"):
                   self.Acquired_Lightning = True;
                   self.Plyr_Heroine.SKILL_Has_Lightning = "TRUE";
                   self.Text_Write("You decide to read the runes out loud. The air");
                   self.Text_Append("begins to crackle and sizzle around you. The");
                   self.Text_Append("hair on your head and arms stands straight up");
                   self.Text_Append("as electric potential fills the atmosphere with");
                   self.Text_Append("with a pulsating charge ...");
                   self.Text_Append("\nYou acquire the magic skill of: LIGHTNING!!!");
                   self.Text_Append("\nElectrifying!\n");
                   self.Plyr_Heroine.SKILL_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("You wisely decide not to read the words aloud.");
                     self.Text_Append("What if they are the incantation of an ancient");
                     self.Text_Append("and terrible CURSE?");

                self.Text_Append("\nClick \"GO\"to continue.\n");                             

          else: 
               VIEW = "LOCATION: L1_EAST_2\n";
               VIEW += "\nYou stand beside a swiftly flowing river. Clumps of";
               VIEW += "\nbroken ice are flowing in the swiftly bubbling current";
               VIEW += "\nthat passes you by. Among the clumps of broken ice, you";
               VIEW += "\nnotice a school of fish darting to and fro around a";
               VIEW += "\ncluster of smooth rocks in the shallows.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: There is a single, solitary fishing pole abandoned";
               VIEW += "\nby a tree. Beyond that? You see a tall, gray mountain";
               VIEW += "\ncovered by dead trees.\n";
               VIEW += "\nSOUTH: A cart of green apples leans against a large rock.";
               VIEW += "\nIt is missing one wheel.\n";
               VIEW += "\nEAST: A small dirt path winds around clumps of trees towards";
               VIEW += "\na free-standing awning. Under it? A blacksmith forge.\n";
               VIEW += "\nWEST: An empty looking village with a dozen wooden cottages";
               VIEW += "\nstands. You can see smoke smouldering from a small fire in";
               VIEW += "\nthe middle.\n";
               VIEW += "\nM: To the north-west, a ring of evil, MEAN-looking mountains";
               VIEW += "\ncovered with thick, dark clouds and flashing lightning.\n"
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n";                

               self.Text_Write(VIEW);   

    #---Function-----------------------------------------------------------------------------------------------------
      def WEST_2(self):
          print("\nIn L1_WEST_2 now.");
          self.IMG_MAP_L1_W2 = self.IMG_MAP_L1_W2.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_W2);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);          

          if(self.CHOICE == "n"): 
             self.Text_Write("L1_WEST2-North: You walk north and approach the");
             self.Text_Append("elderly, contankerous mare surrounded by bundles");
             self.Text_Append("of flowers she is selling to passersby.\n");  
             if(self.Acquired_Telepathy == False):  
                self.Text_Append("She wants to sell you some flowers, but you have");
                self.Text_Append("nothing to buy them with. Even so, she offers you");
                self.Text_Append("the petals of a bright yellow flower. She takes a few");
                self.Text_Append("and puts them in her mouth, making a chewing motion.");
                self.Text_Append("Is she is asking you to eat them? Why can't she speak");
                self.Text_Append("words like any other pony would? Is she deaf? Dumb?");
                self.Text_Append("What if the petals of the flower she ate are POSONOUS?");
                self.Text_Append("But then, why would she eat them? Is she immune to");
                self.Text_Append("their poison? What will you do? DARE you risk consuming");
                self.Text_Append("potentially poisonous petals?");
                self.Text_Append("\n  0 = NO\n  1 = YES");
             elif(self.Acquired_Telepathy == True):
                      self.Text_Append("The salty old mare send positive, warming thoughts");
                      self.Text_Append("into your mind which you can now receive because");
                      self.Text_Append("this is the spot where she formerly gave you the");
                      self.Text_Append("flower petals that once consumed, gave you the");   
                      self.Text_Append("gift of TELEPATHY.");
             self.Text_Append("\nClick \"GO\"to continue.\n");          

          elif(self.CHOICE == "s"):              
               self.Text_Write("L1_WEST2-South: You trot south and try to strike up a");
               self.Text_Append("conversation with the baby dragon. But he seems more");
               self.Text_Append("interested in munching on his carrot than talking to you.");
               self.Text_Append("\nYou walk past him towards the gleaming citadel to the.");
               self.Text_Append("south-east. As you get closer, you are amazed by the");
               self.Text_Append("golden glow shimmering from its gilded walls. The citadel");
               self.Text_Append("is aligned perfectly between 4 towers corresponding to");
               self.Text_Append("the four cardinal directions: north, south, east and west.\n");
               self.Text_Append("You can see compass markings on each tower, and engraved");
               self.Text_Append("within each of their polished brick walls is a beautiful");
               self.Text_Append("pair of wings.");
               self.Text_Append("\nClick \"GO\"to continue.\n");  

          elif(self.CHOICE == "e"):   
               self.LOCATION = self.L1_W1;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "w"):   
               self.LOCATION = self.L1_W3;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "c"):   
               self.LOCATION = self.L1_PEGASUSCITADEL;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Acquired_Telepathy == False):
                if(self.CHOICE == "1"):
                   self.Acquired_Telepathy = True;
                   self.Plyr_Heroine.SKILL_Has_Telepathy = "TRUE";
                   self.Text_Write("\nYou acquire the magic skill of: TELEPATHY!");
                   self.Text_Append("\nThis is gonna be so AWESOME!\n");
                   self.Plyr_Heroine.SKILL_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("You decide the precosious precious petals might");
                     self.Text_Append("possibly be pestulently poisonous. So you decide");
                     self.Text_Append("to reject the old mare's gift and walk away.");
                self.Text_Append("\nClick \"GO\"to continue.\n");                              

          else: 
               VIEW = "LOCATION: L1_WEST_2\n";
               VIEW += "You are standing in the midst of a series of gray,";
               VIEW += "rocky caves carved into the exposed granite hillside";
               VIEW += "of many large, protruding cracks and crevices.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: Your eyes catch glimpse of an old, salty";
               VIEW += "\nmare who appears to be selling flowers.\n";
               VIEW += "\nSOUTH: You see an adorable, purple, baby dragon";
               VIEW += "\nmunching on a carrot. Beyond him? A gleaming citadel.\n";
               VIEW += "\nEAST: You see an arid, sandy plain with withered grass";
               VIEW += "\nand sparse, dessicated, withered trees.\n";
               VIEW += "\nWEST: A castle looms in the distance. Festive, colored";
               VIEW += "\nflags wave from its towers.\n";
               VIEW += "\nC: To the south-east, a GLORIOUS, SHINING citadel looms";
               VIEW += "\nover brightly colored celebratory flags and totems. You";
               VIEW += "\nsee gorgeous, winged pegasi soaring in the skies above it.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n";                

               self.Text_Write(VIEW);        

    #---Function-----------------------------------------------------------------------------------------------------
      def NORTH_3(self):
          print("\nIn L1_NORTH_3 now.");
          self.IMG_MAP_L1_N3 = self.IMG_MAP_L1_N3.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_N3);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);           

          if(self.CHOICE == "n"):   
             self.Text_Append("\n L1_NORTH3-North:");
             if(self.L1_N3_Slime_Mold_Alive == True):
                self.LOCATION = self.L1_N3_Slime_Mold_Encounter;
                self.CHOICE = "#";
                #self.SwitchBoard();
             else:
                   MESSAGE = "\n You see the oooooooooooooey goooooooooooooey remains ";
                   MESSAGE += "\n of the icky slime mold you formerly defeated.";
                   MESSAGE += "\n\n Eeeeeeeeeeeeeewwwwwwwwwwww!";
                   MESSAGE += "\n\n But you can go no further north from here.";
                   self.Text_Append(MESSAGE);
          elif(self.CHOICE == "s"): 
               self.LOCATION = self.L1_N2;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "e"):   
               self.Text_Write("\n L1_NORTH3-East:  You try to ascend further east, but");
               self.Text_Append("are unable to climb the steep, slippery slopes as they");
               self.Text_Append("are covered with ice.\n");
               self.Text_Append("You gallop east into an artificial plateau hewn into the");     
               self.Text_Append("side of the mountain. What sort of a being could have done");
               self.Text_Append("this? Are there GIANTS here this strong and powerful?\n");
               self.Text_Append("Terrifying creatures who can cut through solid granite");
               self.Text_Append("easily as an axe could chop through soft wood?\n");
               self.Text_Append("A shiver travels up your spine as you contemplate these");
               self.Text_Append("disturbing thoughts.");
               if(self.Acquired_Telekinesis == False):
                  self.Text_Append("\nIn the icy slopes glistening beneath your hooves you");
                  self.Text_Append("see what seems to be a translucent, blue box made of");
                  self.Text_Append("transparent crystal and encrusted with bright, green");
                  self.Text_Append("emeralds. Will you open the crystal box, pull out the");
                  self.Text_Append("scroll and try to read it?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.Acquired_Telekinesis == True):
                      self.Text_Append("\nLaying on the icy, frozen tundra beneath your frigid");
                      self.Text_Append("hooves you see an empty ice box where you formerly");
                      self.Text_Append("found the scroll of Telekinesis.");
               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "w"):   
               self.Text_Write("\n L1_NORTH3-West: !!!Mountain Market!!!");
               self.LOCATION = self.L1_Market_1;
               self.CHOICE = "#";
               #self.SwitchBoard();

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Acquired_Telekinesis == False):
                if(self.CHOICE == "1"):
                   self.Acquired_Telekinesis = True;
                   self.Plyr_Heroine.SKILL_Has_Telekinesis = "TRUE";
                   self.Text_Write("\nYou acquire the magic skill of: Telekinesis!");
                   self.Text_Append("\nMind over matter, baby!\n");
                   self.Plyr_Heroine.SKILL_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("You decide not to open the suspicious crystal box.");
                     self.Text_Append("Looks too good to be true that someone would leave");
                     self.Text_Append("something that valuable just lyign around. Better");
                     self.Text_Append("to excercise caution.");
                self.Text_Append("\nClick \"GO\"to continue.\n");                

          else: 
               VIEW = "LOCATION: L1_NORTH_3\n";
               VIEW += "\nYou ascend the base of a mountain and find yourself several";
               VIEW += "\nthousand feet higher amidst sparse clumps of evergreens and";
               VIEW += "\nsnow-covered boulders. A light blanket of frost covers the"; 
               VIEW += "\nlichens and pebbles crunching beneath your feet as you walk.\n";
               VIEW += "\nLooking down, you are overwhelmed by the breath-taking beauty";
               VIEW += "\nof a ring of clouds encircling the mountain in striated bands";
               VIEW += "\nof fluffy white puffiness that cast undulating shadows over";
               VIEW += "\nthe earth beneath them.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see impenetrable mountain slopes of hardened";
               VIEW += "\ngranite covered with ice far too steep and slippery to climb.\n";
               VIEW += "\nSOUTH: The base of a blue and purple mountain range catches";
               VIEW += "\n your eye. So pretty!\n";
               VIEW += "\nEAST: You see an odd and uneven plateau, hewn into the side of";
               VIEW += "\nthe mountain as if by a giant axe.\n";
               VIEW += "\nWEST: A green valley with lush farmland delights your senses.";
               VIEW += "\nBut the incline is too steep to reach it from here.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n";                

               self.Text_Write(VIEW);

    #---Function-----------------------------------------------------------------------------------------------------
      def SOUTH_3(self):
          print("\nIn L1_SOUTH_3 now.");
          self.IMG_MAP_L1_S3 = self.IMG_MAP_L1_S3.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_S3);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);            

          if(self.CHOICE == "n"):   
             self.LOCATION = self.L1_S2;
             self.CHOICE = "#";
             self.SwitchBoard();

          elif(self.CHOICE == "s"):
               self.Text_Write("L1_SOUTH3-South: You try to advance south, but are");
               self.Text_Append("blocked by impenetrable rows of deciduous trees."); 
               self.Text_Append("Strangely, these trees appear to have been petrified");
               self.Text_Append("and turned to stone ages ago.\n");
               if(self.Acquired_Healing == False):
                  self.Text_Append("At the base of one of the petrified trees, you see");
                  self.Text_Append("a weathered, abandoned, dark green canvas satchel.");
                  self.Text_Append("Will you pick up the satchel and look inside?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.Acquired_Healing == True):
                      self.Text_Append("At the base of a petrified tree you see the empty");
                      self.Text_Append("satchel where you formerly found the scroll for");
                      self.Text_Append("\nthe magic skill of HEALING.");               
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_SOUTH3-East: You go east towards the old mare.");
               self.Text_Append("The burden of her pack load looks so heavy! You ask");
               self.Text_Append("her why she is walking in circles around the cave");
               self.Text_Append("entrance. She gives you no answer and pays you no mind.");
               self.Text_Append("What could get her attention?\n");
               self.Text_Append("You look off towards the north-east and see that a cave");
               self.Text_Append("descends deep UNDERGROUND. What could it lead to? You");
               self.Text_Append("\ndecide to walk past the old mare and go spelunking!");
               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "w"):   
               self.Text_Write("L1_SOUTH3-West: You walk west following the causeway,");
               self.Text_Append("hopping from stone to stone. At the end of this path,");
               self.Text_Append("you find yourself on a small island not far from shore.");
               self.Text_Append("You see other islands further out. If only you had a");
               self.Text_Append("boat? You could reach them.\n");
               self.Text_Append("You see several large ravens perching on the cobbled");
               self.Text_Append("stone ruins of what must have been a wall. One of them");
               self.Text_Append("turns its head to one side and says:\n");
               self.Text_Append("\"Hello! A fine day it is. But what comes at night?\n");
               self.Text_Append("For whatever reason, it does not seem odd to you that");
               self.Text_Append("ravens are conversational in these parts. If only you");
               self.Text_Append("had a boat? You could go out onto the lake and sail");
               self.Text_Append("further west ...");
               self.Text_Append("\nClick \"GO\"to continue.\n");                

          elif(self.CHOICE == "u"):   
               self.LOCATION = self.L1_UNDERGROUND;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Acquired_Healing == False):
                if(self.CHOICE == "1"):
                   self.Acquired_Healing = True;
                   self.Plyr_Heroine.SKILL_Has_Healing = "TRUE";
                   self.Text_Write("\nYou acquire the magic skill of: HEALING!");
                   self.Text_Append("\nThis should be nice.\n");
                   self.Plyr_Heroine.SKILL_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("You decide not to pick up the satchel.");
                     self.Text_Append("Something inside it might harm you.");
                self.Text_Append("\nClick \"GO\"to continue.\n");                              

          else: 
               VIEW = "LOCATION: L1_SOUTH_3\n";
               VIEW += "\nYou trot out onto a causeway of flat, gray stones.";
               VIEW += "\nThese stones have been layed out intelligently in an";
               VIEW += "\norganized sequence that creates a winding path you can"; 
               VIEW += "\nfollow.\n";
               VIEW += "\nIf you were to hop from stone to evenly-spaced stone?";
               VIEW += "\nYou realize you could reach a small island they lead to";
               VIEW += "\nin the distance that is only a small ways from the lake";
               VIEW += "\nshore itself.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You gaze at the totality of the pristine lake whose";
               VIEW += "\nshore you now stand beside. It is stunningly beautiful.\n";
               VIEW += "\nSOUTH: You cannot see beyond the shore of the lake due to";
               VIEW += "\na dense grove of thickets and briars.\n";
               VIEW += "\nEAST: You see an old mare with a backpack. She appears to";
               VIEW += "\nbe trotting back and forth in front of a CAVE.\n";
               VIEW += "\nWEST: You see the causeway of stones protruding through";
               VIEW += "the water's surface and leading to the small island.\n";
               VIEW += "\nU: You see the dark entrance to a cave leading to what";
               VIEW += "\nappears to be a deep cavern UNDERGROUND.";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n";                

               self.Text_Write(VIEW); 

    #---Function-----------------------------------------------------------------------------------------------------
      def EAST_3(self):
          print("\nIn L1_EAST_3 now.");
          self.IMG_MAP_L1_E3 = self.IMG_MAP_L1_E3.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_E3);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);           

          if(self.CHOICE == "n"):   
             self.Text_Write("L1_EAST3-North: You trot north towards the GIANT.");
             self.Text_Append("His arms and legs are sprawled haphazzardly around");
             self.Text_Append("this area. You can see no way to proceed further north");
             self.Text_Append("without waking or moving this GIANT.\n");
             self.Text_Append("No matter how hard you try to push and shove, he is too");
             self.Text_Append("heavy and cumbersome and won't budge. And no matter how");
             self.Text_Append("much noise or racket you mane, you cannot seem to awaken");
             self.Text_Append("this sleeping giant.\n");
             self.Text_Append("You will not be able to proceed any further east from");
             self.Text_Append("here until you can either awaken or move this giant.");
             self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "s"):   
               self.Text_Write("L1_EAST3-South: You go south towards the delapidated old");
               self.Text_Append("stable. As you look around, you see piles of hay and straw");
               self.Text_Append("Under an unraveling bail, you see something protruding but ");
               self.Text_Append("cannot make out by its ambiguous shape what it is.");
               self.Text_Append("You can proceed no further south from here.");
               if(self.TRAP3_Encountered == False):
                  self.Text_Append("\nGlancing at your surroundings, you see a small wooden");
                  self.Text_Append("table against the south wall of the stable. On this table");
                  self.Text_Append("is a plate of delicious-looking butter creme frosted");
                  self.Text_Append("strawberry cupcakes! You can small the rich, creamy");
                  self.Text_Append("strawberry aroma wafting into the atmosphere from each");
                  self.Text_Append("cupcake. It tingles your nostrils and makes your stomach");
                  self.Text_Append("growl. So yummy! They look rresistible. Will you try");
                  self.Text_Append("one of these simply SCRUMPTIOUS strawberry cupcakes?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.TRAP3_Encountered == True):
                      self.Text_Append("\nYou see against a wall a table on which rests the");
                      self.Text_Append("platter of poisoned cupcakes you formerly consumed.");
                      self.Text_Append("You have no wish to poison yourself again with them.");
               self.Text_Append("\nClick \"GO\"to continue.\n");       

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_EAST3-South: You gallop east towards a stone table.");
               self.Text_Append("Looking past the stone table, you see only a brick wall");
               self.Text_Append("and no way to proceed further east.");
               if(self.Found_Sigil == False):
                  self.Text_Append("\nAs you get closer? You see dozens of colorful, delicious");
                  self.Text_Append("BLUEBERRY cupcakes on several platters with glass domes.\n");
                  self.Text_Append("You wonder to yourself: Are they safe to eat? And if so?");
                  self.Text_Append("What would they do to you?\n");
                  self.Text_Append("Will you try one of the BLUEBERRY cupcakes?");
                  self.Text_Append("\n  2 = NO\n  3 = YES");
               elif(self.Found_Sigil == True):   
                    self.Text_Append("\nYou see the same table where you formerly found");
                    self.Text_Append("and consumed BLUEBERRY cupcakes and gained the");
                    self.Text_Append("magical SIGIL as a result. But the cupcakes are");
                    self.Text_Append("all GONE now and the platters are all empty.");
               self.Text_Append("\nClick \"GO\"to continue.\n");


          elif(self.CHOICE == "w"):   
               self.LOCATION = self.L1_E2;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "z"):   
               self.LOCATION = self.L1_SWAMPOFSADNESS;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.TRAP3_Encountered == False):
                if(self.CHOICE == "1"):
                   self.Text_Write("You pick up one and take a bite. Though deliciously sweet");
                   self.Text_Append("in your mouth, it becomes sour in your tummy. You begin");
                   self.Text_Append("to feel naueous and weak in the knees. You quickly vomit");
                   self.Text_Append("up what you recently devoured. As disgusting as this is?");
                   self.Text_Append("It may have saved y our life! The poison from the cupcakes");
                   self.Text_Append("has done its damage to your body and a result,");
                   self.Text_Append("you lose 10 health!");
                   self.TRAP3_Encountered = True;
                   self.Text_Append("\nYour health WAS: " + str(self.Plyr_Heroine.EntityHealth));
                   self.Plyr_Heroine.EntityHealth -= 10;
                   self.Text_Append("Your health is NOW: " + str(self.Plyr_Heroine.EntityHealth));
                   self.Plyr_Heroine.Display_Entity();
                elif(self.CHOICE == "0"):
                     self.Text_Write("These cupcakes might be poisonous or have some other undesired");
                     self.Text_Append("or fatal consequences when eaten.");
                self.Text_Append("\nClick \"GO\"to continue.\n");

          elif((self.CHOICE == "2" or self.CHOICE == "3") and self.Found_Sigil == False):
                if(self.CHOICE == "3"):
                   self.Found_Sigil = True;
                   self.Plyr_Heroine.INV_Has_Sigil = "TRUE";
                   self.Text_Write("\nYou acquire the magic item: Nightmare Moon's SIGIL!");
                   self.Text_Append("This is DEFINITELY gonna come in handy.\n");
                   self.Plyr_Heroine.Inventory_Display();
                elif(self.CHOICE == "2"):
                     self.Text_Write("\nThe cupcakes might be a POISONED!");
                     self.Text_Append("So you decide to leave them be.");
                self.Text_Append("\nClick \"GO\"to continue.\n");                                              

          else: 
               VIEW = "LOCATION: L1_EAST_3\n";
               VIEW += "\nYou find yourself beside a free-standing awning made of";
               VIEW += "\ndirty, brown canvas. It stretches out over a rusty, iron";
               VIEW += "\nfire ring in the middle. From this fire ring, billows of"; 
               VIEW += "\nsmoke rise into the air under the awning making the air";
               VIEW += "\ncaustic to breathe. You try not to choke.\n"; 
               VIEW += "\nYou can see a large, heavy cast-iron blacksmith forge,";
               VIEW += "\nwith an anvil in the middle of a flat, polished chunk";
               VIEW += "\nof granite used as a platform to support it.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see a boggy swamp. Against a mangrove at the";
               VIEW += "\nshore a GIANT is sleeping, his enormous head against a";
               VIEW += "\nlarge rock.\n";
               VIEW += "\nSOUTH: You see an abandoned gray stone stable surrounded";
               VIEW += "\nby pludered piles of straw and hay.\n";
               VIEW += "\nEAST: You see a small granite table with a large stone";
               VIEW += "\nsurface. On it are several plated of cupcakes.\n";
               VIEW += "\nWEST: You see a swiftly flowing river with clumps of";
               VIEW += "\nflowing ice.\n";
               VIEW += "\nZ: Further to the north east, you see a sad-looking";
               VIEW += "\nSWAMP (Z). An air of depression emanates from the wispy";
               VIEW += "\ngray fog floating over its boggy, brackish waters.\n"
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n"; 

               self.Text_Write(VIEW); 

    #---Function-----------------------------------------------------------------------------------------------------
      def WEST_3(self):
          print("\nIn L1_WEST_3 now.");
          self.IMG_MAP_L1_W3 = self.IMG_MAP_L1_W3.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_W3);
          self.LAB_Current_View.configure(image=self.IMG_Current_View); 

          self.Sound_Footsteps_Thread();        

          if(self.CHOICE == "n"):   
             self.Text_Write("L1_WEST3-North: You walk norhtwards towards the gate");
             self.Text_Append("find, hanging from a small totem, a large brass bell.");
             self.Text_Append("Beside the bell hanging on its totem, a big, bright");
             self.Text_Append("chartreuse flag rustles in the wind.");
             if(self.Found_Orb == False):
                self.Text_Append("A long, hemp rope hangs down from the large, brass");
                self.Text_Append("bell. Will you pull on the rope to ring the bell?");
                self.Text_Append("\n  0 = NO\n  1 = YES");
             elif(self.Found_Orb == True):
                  self.Text_Append("\nHere lies the bell you formerly rang. It is");
                  self.Text_Append("now somehow frozen in time and no matter how");
                  self.Text_Append("how hard you try, you cannot ring it again.");
                  self.Text_Append("This is where you formerly found the:");
                  self.Text_Append("Orb of Ultimate Power!!!");                        

          elif(self.CHOICE == "s"):   
               self.Text_Write("L1_WEST3-South: Curiosity gets the best of you.");
               self.Text_Append("So you trot haphazzardly down a winding path.");
               self.Text_Append("Tall evergreens, at first in the distance, grow");
               self.Text_Append("closer and closer as you travel southward.\n");
               self.Text_Append("In the distance you see a lush, green forest");
               self.Text_Append("teaming with feathery and furry life forms.");
               self.Text_Append("But you cannot get to it from this direction");
               self.Text_Append("as thick, over-grown shrubs block your path.");
               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "e"): 
               self.LOCATION = self.L1_W2;
               self.CHOICE = "#";
               self.SwitchBoard();  

          elif(self.CHOICE == "w"):   
               self.Text_Write("L1_WEST3-West: You gallop west until you stand at");
               self.Text_Append("the center of the arch of a wide castle moat. This");
               self.Text_Append("moat completely surrounds the castle, yet has waters");
               self.Text_Append("as clear as the purest crystal. It is so wide, you");
               self.Text_Append("could practically call it a good-sized lake.\n");
               self.Text_Append("Large, colorful coy swim to and fro in these");
               self.Text_Append("pristine and soothing waters. This moat is far");
               self.Text_Append("too wide and long to swim across, so in this");
               self.Text_Append("direction you can go no further. Unless, perhaps");
               self.Text_Append("if you had a BOAT?");            
               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "c"):   
               self.LOCATION = self.L1_CELESTIASPALACE;1
               self.CHOICE = "#";
               self.SwitchBoard();

          elif(self.CHOICE == "f"):   
               self.LOCATION = self.L1_FRIENDSHIPFOREST;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Found_Orb == False):
                if(self.CHOICE == "1"):
                   self.Found_Orb = True;
                   self.Plyr_Heroine.INV_Has_Orb = "TRUE";
                   self.Text_Write("\nYou pull the rope and ring the bell. The draw");
                   self.Text_Append("bridge descends, but only half way. It must be");
                   self.Text_Append("broken and in need of repair. However, you see");
                   self.Text_Append("something glimmering in the differential gears");
                   self.Text_Append("and hinges that move the drawbridge up and down.");
                   self.Text_Append("\nYou found the magic item:");
                   self.Text_Append("Chrystalia's ORB of Ultimate POWER!");
                   self.Text_Append("\nSo beautiful! It feels powerful.\n");
                   self.Plyr_Heroine.Inventory_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("\nYou decide it might be a REALLY bad idea to");
                     self.Text_Append("pull the rope and announce your presence to");
                     self.Text_Append("any potential malicious entities that may be");
                     self.Text_Append("lurking near by. Quick thinking!");
                self.Text_Append("\nClick \"GO\"to continue.\n");                                              

          else: 
               VIEW = "LOCATION: L1_WEST_3\n";
               VIEW += "\nYou arrive at the courtyard of a beautiful stone and";
               VIEW += "\ncrystal castle. The castle is over 80 feet tall in some";
               VIEW += "\nareas, and you realize it must contain many floors.\n"; 
               VIEW += "\nSurrounding the castle on each of its 4 corners?";
               VIEW += "\nYou see colorful, festive flags flapping in the wind";
               VIEW += "\nand curling into random shapes as the wind changes";
               VIEW += "\ndirection. The polished stones and crystal slabs that";
               VIEW += "\nintersect with angle and edge of this amazing castle";
               VIEW += "\nsparkle in the sunlight like a tapestry made of a thousand";
               VIEW += "\nshimmering rainbows. How is it always DAY over this";
               VIEW += "\nmagical place, even when it is NIGHT everywhere else?";
               VIEW += "\nDoes the being who lives here somehow control the";
               VIEW += "\nsun itself? You see a moat of crystl waters an lilies";
               VIEW += "\nbefore you, surrounfing this castle. And beyond this";
               VIEW += "\nmoat? A large drawbridge that, if it were to decend? ";
               VIEW += "\nWould give you welcome access to this spectacular palace.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see a gold entry gate jutting out over the moat";
               VIEW += "\nwhere the drawbridge would meet if extended. Beside it, a";
               VIEW += "\nlarge brass bell.\n";
               VIEW += "\nSOUTH: You see a winding path that meanders aimlessly into";
               VIEW += "\na lush, green forest.\n";
               VIEW += "\nEAST: You see a series of gray, rocky caves carved into the";
               VIEW += "\nexposed hillside.\n";
               VIEW += "\nWEST: You see the arch of a wide castle moat as large as a";
               VIEW += "\nsmall lake. It extends around the palace.\n";
               VIEW += "\nC: To the north-east you see CELESTIA'S PALACE.\n";
               VIEW += "\nF: TO the south-east lies FRIENDSHIP FOREST.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n";                

               self.Text_Write(VIEW);


    #---Function-----------------------------------------------------------------------------------------------------
      def CELESTIASPALACE(self):
          print("\nIn L1_CELESTIASPALACE now.");
          self.IMG_MAP_L1_CELESTIASPALACE = self.IMG_MAP_L1_CELESTIASPALACE.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_CELESTIASPALACE);
          self.LAB_Current_View.configure(image=self.IMG_Current_View); 

          self.Sound_Trumpets_Thread();         

          if(self.CHOICE == "n"):
               self.Text_Write("L1_CELESTIASPALACE-North: You walk towards the north wall");
               self.Text_Append("of the castle Great Room in which you are standing. Above"); 
               self.Text_Append("you is a high cathedral ceiling - it must be at least 20");
               self.Text_Append("from the floor! Against this north wall, you see a varnished");
               self.Text_Append("mahogany table embellished with intricate carvings. On this");
               self.Text_Append("table, you see s small crystal box glistening in the");
               self.Text_Append("magical kincadian light that fills every corner of this room.\n");
               if(self.Found_HealingPotion_CelestiasPalace == False):
                  self.Text_Append("You walk over to the table at the north wall. The");
                  self.Text_Append("ice-blue translucent crystal box shimmers. Will you");
                  self.Text_Append("open it and look inside?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.Found_HealingPotion_CelestiasPalace == True):
                      self.Text_Append("At the base of a petrified tree you see the empty");
                      self.Text_Append("crystal box where you formerly found the healing ");
                      self.Text_Append("potion.\n");               
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "s"):   
               self.Text_Write("L1_CELESTIASPALACE-South: Walking towards the south wall,");
               self.Text_Append("you see a beautiful set of tapestries draped over each");
               self.Text_Append("cobbled, marbles stone. On the tapestries are beautiful");
               self.Text_Append("embroidered images of unicorns, pegasi and ponies. All");
               self.Text_Append("are frolicking in fields of gold woven with exquisite");
               self.Text_Append("gossamer threads of precious silk and platinum.\n");
               self.Text_Append("You feel around behind these taptestries, but touch");
               self.Text_Append("nothing but impenetrable, cold stone behind them.");
               self.Text_Append("You can go no further in this direction.");   
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_CELESTIASPALACE-East: Walking over to the east side of");
               self.Text_Append("the palace Great Room, you see three large oval portals.");
               self.Text_Append("Each of these portals is protected by a large, stone door.");
               self.Text_Append("You try each of the 3 doors, but each one is locked.");
               self.Text_Append("If only you had some sort of KEY? You wonder wheer the ");
               self.Text_Append("portals might lead to ...");
               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "w"):   
               #Note: Insert NPC_1 access here in later versions
               self.LOCATION = self.L1_NPC_1_Encounter;
               self.CHOICE = "#";
               self.SwitchBoard();
               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "x"):   
               self.LOCATION = self.L1_W3;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Found_HealingPotion_CelestiasPalace == False):
                if(self.CHOICE == "1"):
                   self.Found_HealingPotion_CelestiasPalace = True;
                   self.Plyr_Heroine.INV_Has_HealingPotions += 1;
                   self.Text_Write("\nYou found a HEALING potion!");
                   self.Text_Append("\nWhat luck! This could come in handy.\n");
                   self.Plyr_Heroine.Inventory_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("You decide not to open the crystal box.");
                     self.Text_Append("What if it's a BOMB? Better to be cautious.");
                self.Text_Append("\nClick \"GO\"to continue.\n");                                              

          else: 
               VIEW = "LOCATION: L1_CELESTIASPALACE\n";
               VIEW += "\nYou walk across the moat over the extended drawbridge and";
               VIEW += "\nfind yourself standing at the front gates of an enormous";
               VIEW += "\npalace made of large, white marbled stone blocks. How";
               VIEW += "\nexquisitely beautiful! You are surrounded by glittering,";
               VIEW += "\ngleaming walls of olished stone. Jasper, jade, emerald";
               VIEW += "\nand amethist. Embellishing the walls on every side? You";
               VIEW += "\nsee rubies, diamonds, opals and saphires.\n";
               VIEW += "\nIn each cardinal direction of this palace is an arched,";
               VIEW += "\ngolden gateway. Four stone towers protrude from the four";
               VIEW += "\ncorners where each palace wall meets another. Atop each";
               VIEW += "\ntower, a brightly colored pavillion flag flaps in the";
               VIEW += "\nbreeze. To the southwest, you see a winding dirt road.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see beautiful castle walls.\n";
               VIEW += "\nSOUTH: You see the door from which you entered this";
               VIEW += "\n amazing, magical place.\n";
               VIEW += "\nEAST: A winding staircase ascends to the second floor.\n";
               VIEW += "\nWEST: You see an elaborately crafted throne made entirely";
               VIEW += "\nof sparkling, transparent diamonds!\n";
               VIEW += "\nX: EXIT Celestia's Palace back to WEST_3.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n"; 

               self.Text_Write(VIEW); 

    #---Function-----------------------------------------------------------------------------------------------------
      def UNDERGROUND(self):
          print("\nIn L1_UNDERGROUND now.");
          self.IMG_MAP_L1_UNDERGROUND = self.IMG_MAP_L1_UNDERGROUND.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_UNDERGROUND);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);  

          self.Sound_Footsteps_Thread();         

          if(self.CHOICE == "n"):   
             self.Text_Write("L1_UNDERGROUND-North:  You walk north towards the stack");
             self.Text_Append("stack of wooden crates. You examine them, but find nothing");
             self.Text_Append("special about them. They don't look very sturdy or strong.");
             if(self.Found_HealingPotion_3 == False):
                self.Text_Append("\nYou think to yourself, one swift KICK to any of these");
                self.Text_Append("fragile, old wooden crates? And they would just shatter!");
                self.Text_Append("You wonder, could anything useful be stored inside of");
                self.Text_Append("one of these wooden crated? Or might something inside");
                self.Text_Append("them HARM you instead? Could this be some sort of TRAP?");
                self.Text_Append("Will you KICK the crates?");
                self.Text_Append("\n  0 = NO\n  1 = YES");
             elif(self.Found_HealingPotion_3 == True):
                      self.Text_Append("\nYou see a pile of shattered wood and nails in");
                      self.Text_Append("the spot where you formerly kicked the wooden");
                      self.Text_Append("crates and found the HEALING postion. There is");
                      self.Text_Append("nothing else of interest here any longer.");             
             self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "s"):   
               self.Text_Write("L1_UNDERGROUND-South:  Walking towards the southern wall");
               self.Text_Append("of the cave your currently in, yu decide to explore the");
               self.Text_Append("mysterious-looking tunnel entrance against this wall.\n");
               self.Text_Append("However, after walking through it for only a few moments,");
               self.Text_Append("you find the passage blocked by a giant boulder. If only");
               self.Text_Append("you had something to blow it up into smaller pieces? Or");
               self.Text_Append("a long rod with a fulcrum might budge it, perhaps?\n");
               self.Text_Append("You reach out with a shaky hoof to tough it ... POOF!");
               self.Text_Append("It crumbles into dust! It was just an illusion.\n");
               self.Text_Append("You trot further into the tunnel and it begins to grow");
               self.Text_Append("brighter ...");
               if(self.Acquired_Invisibility == False):
                  self.Text_Append("As you proceed through the tunnel, you notice an");
                  self.Text_Append("unusual trapazoidal stone. It is translucent, of");
                  self.Text_Append("the consistency of amethist. Could it be valuable?");
                  self.Text_Append("Will you pick up the purple trapazoidal stone to");
                  self.Text_Append("further examine it? Or might this stone be something");
                  self.Text_Append("DANGEROUS? Pick it up?");
                  self.Text_Append("\n  2 = NO\n  3 = YES");
               elif(self.Acquired_Invisibility == True):
                      self.Text_Append("Inside the tunnel, you see the trapazoidal fragment");
                      self.Text_Append("of amethist where you exposed ancient runes that");
                      self.Text_Append("formerly gave you the gift of INVISIBILITY.");
                      self.Text_Append("This tunnel is just a dead-end now. You can go");
                      self.Text_Append("no further south in this direction.");
                      

               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_UNDERGROUND-East:  You proceed further east, but");
               self.Text_Append("are blocked by an impenetrable cave wall made of");
               self.Text_Append("what looks like volcanic obsidian. Scribbled all");
               self.Text_Append("along this dark, black obsidian wall are stick");
               self.Text_Append("figures of ponies, dragons, trees and forest animals");
               self.Text_Append("inscribed with white and red chalk.\n");
               self.Text_Append("You wonder to yourself - who could have left all these");
               self.Text_Append("chalk drawings on this dark, obsidian cave wall?");
               self.Text_Append("You can go no further east in this direction,");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "w"):   
               self.Text_Write("L1_UNDERGROUND-West:  You walk westward inside the");
               self.Text_Append("cavern. As you approach the dark, dusty wall of");
               self.Text_Append("this area of the cave, you find a single wooden");
               self.Text_Append("torch mounted to the cave wall with a brass and");
               self.Text_Append("iron ring.\n");
               self.Text_Append("The light of this torch is what has been creating");
               self.Text_Append("the flickering light with which you can barely see");
               self.Text_Append("all the features of this cavern. The flames of the");
               self.Text_Append("torch cast flickering shadows against the western");
               self.Text_Append("cavern wall. You can go no further in this direction.");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "d"):   
               self.LOCATION = self.L1_DISCORDSLAIR;
               self.CHOICE = "#";
               self.SwitchBoard();               

          elif(self.CHOICE == "x"):   
               self.LOCATION = self.L1_S3;
               self.CHOICE = "#";
               self.SwitchBoard();
               
          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Found_HealingPotion_3 == False):
                if(self.CHOICE == "1"):
                   self.Found_HealingPotion_3 = True;
                   self.Plyr_Heroine.INV_Has_HealingPotions += 1;
                   self.Text_Write("You found a HEALING potion!");
                   self.Text_Append("\nAwesome!\n");
                   self.Plyr_Heroine.Inventory_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("You decide not to KICK the fragile, wodden crates.");
                     self.Text_Append("What if isomething inside them is DANGEROUS?");
                self.Text_Append("\nClick \"GO\"to continue.\n");

          elif((self.CHOICE == "2" or self.CHOICE == "3") and self.Acquired_Invisibility == False):
                if(self.CHOICE == "3"):
                   self.Acquired_Invisibility = True;
                   self.Plyr_Heroine.SKILL_Has_Invisibility = "TRUE";
                   self.Text_Write("You touch the stone and magic runes materialize");
                   self.Text_Append("all along its surface! What in the world?");
                   self.Text_Append("\nYou acquire the magic skill of: INVISIBILITY!");
                   self.Text_Append("\nThis is gonna make combat SO much more interesting.\n");
                   self.Plyr_Heroine.SKILL_Display();
                elif(self.CHOICE == "2"):
                     self.Text_Write("\nThis attactive fragment of amethist looks a bit TOO");
                     self.Text_Append("attractive and tempting. As if by design? Very suspicious.");
                     self.Text_Append("It might do someone HARM if touched. You decide to");
                     self.Text_Append("leave it alone.");                    
                self.Text_Append("\nClick \"GO\"to continue.\n");                                                             

          else: 
               VIEW = "LOCATION: L1_UNDERGROUND\n";
               VIEW += "\nYou descend into a large cavern. As you go deeper into the";
               VIEW += "\ndarkness? Strange shadows begin to dance and flicker across";
               VIEW +="\nthe bleak rocky walls. You glance above into the upper";
               VIEW += "\nexpanse of the cavern and are in awe. Hundreds of long,";
               VIEW += "\npointy stalactites hang from the cave ceiling like gigantic";
               VIEW += "\ncrystal chandeliers.\n";
               VIEW += "\nAs you look down at the cavern floor, you see stalagmites";
               VIEW += "\ngrowing upwards. Several are entombed in piles of sand and";
               VIEW += "\nsharp, crumbled fragments. You tread carefully, lest one";
               VIEW += "\nshould fall from that height upon you and shatter into";
               VIEW += "\nthousands of sharp fragments that would cute you to pieces.\n";
               VIEW += "\nIn the distance further down into the cave? You heear a low,";
               VIEW += "\nrumbling drone that resonates within your rib cage. It is";
               VIEW += "\nmixed with the unmistakable sound of crumbling stone and";
               VIEW += "\nfalling stalactites.\n";
               VIEW += "\nDescending further down and to the south-east you see a deep,";
               VIEW += "\neven darker cavern with a dusty, delapidated wooden sign";
               VIEW += "\naffixed above it that says \"Discord's Lair\". You see";
               VIEW += "\nwhat appear to be the flickering light of candle flames and";
               VIEW += "\nthe shadows those flames cast dancing playfully against the";
               VIEW += "\ncavern walls.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see wooden crates stacked against a cave wall.\n";
               VIEW += "\nSOUTH: You spy a tunnel leading off into the darkness.\n";
               VIEW += "\nEAST: You see only darkness and impenetrable cave walls.\n";
               VIEW += "\nWEST: You see the faint glow of light dimly streaming in";
               VIEW += "\nfrom the cave entrance you came from.\n";
               VIEW += "\nD: Journey into the dark cavern designated \"Discord's Lair\"\n";
               VIEW += "\nX: EXIT L1_UNDERGROUND back to SOUTH_3.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n"; 

               self.Text_Write(VIEW); 

    #---Function-----------------------------------------------------------------------------------------------------
      def DISCORDSLAIR(self):
          print("\nIn L1_DISCORDSLAIR now.");
          self.IMG_MAP_L1_DISCORDSLAIR = self.IMG_MAP_L1_DISCORDSLAIR.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_DISCORDSLAIR);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);  

          self.Sound_Fire_Burning_1_Thread();

          if(self.CHOICE == "n"):   
               self.Text_Write("L1_DISCORDSLAIR-North: Discord looks at you! Nooo!");
               if(self.L1_DiscordsLair_Discord_Boss_Alive == True):
                  self.LOCATION = self.L1_DiscordsLair_Discord_Boss_Encounter;
                  self.CHOICE = "#";
                  #self.SwitchBoard(); #disable for combat sequences
               else:
                     MESSAGE = "Here lies the scaly disfigured remains of";
                     MESSAGE += "\n the old dungeon master of chaos himself.";
                     MESSAGE += "\n Of course, you know he's not REALLY dead.";
                     MESSAGE += "\n This is Discord we're talking about here!";
                     MESSAGE += "\n\n But you can go no further north from here.";
                     self.Text_Write(MESSAGE);
                     self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "s"):   
               self.Text_Write("L1_DISCORDSLAIR-South: You advance south. Examining the");
               self.Text_Append("giant book shelf, you are completely amazed. There must");
               self.Text_Append("be THOUSANDS of books, scrolls, tomes and stone tablets");
               self.Text_Append("on this enormous shelf!\n");
               self.Text_Append("You see a track that spans the length of the shelf.");
               self.Text_Append("Attached to it is a ladder on wheels. You surmise that");
               self.Text_Append("this ladder must be used to reach the three upper levels");
               self.Text_Append("of this giant library.\n");
               self.Text_Append("Your curioisty is driving you mad! You want to look at");
               self.Text_Append("some of the books so bad.");
               if(self.Found_Plate_Armor == False):
                  self.Text_Append("You see an old, dusty book in the center of one shelf.");
                  self.Text_Append("It is pulled half-way out. You wonder why?");
                  self.Text_Append("Perhaps this book was one that was recently read?");
                  self.Text_Append("\nYou wonder - if you pulled on the book, would it");
                  self.Text_Append("activate some sort of secret passage or a TRAP?");
                  self.Text_Append("Will you pull this book towards you?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.Found_Plate_Armor == True):
                      self.Text_Append("\nYou see an open panel in the book shelf leading");
                      self.Text_Append("to a small room where you formerly found the");
                      self.Text_Append("Princess Plate Armor of Perfection.");
               self.Text_Append("\nClick \"GO\"to continue.\n");                          

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_DISCORDSLAIR-East:  You trot east over to the wooden");
               self.Text_Append("table. You look into the large clay bowl and find a");
               self.Text_Append("rainbow-colored assortment of fruit rings of various");
               self.Text_Append("flavors. Yummy! They are swimming in milk and have a");
               self.Text_Append("pleasant citrus aroma. You wonder what would happen if");
               self.Text_Append("you ate some?\n");
               self.Text_Append("But you dare not! The strange being in the center of");
               self.Text_Append("this odd-looking lair could get quite upset if you ate");
               self.Text_Append("his his breakfast.");
               if(self.Acquired_FriendshipCast == False):
                  self.Text_Append("Looking at the bowl of fruit rings on the wooden table,");
                  self.Text_Append("you are overcome with a ravenous hunger. They look so");
                  self.Text_Append("DELICIOUS, and at this point you can't imagine ANYTHING");
                  self.Text_Append("that would be more satisfying than to fill your drooling");
                  self.Text_Append("mouth with all those sparkling fruity flavors!\n");
                  self.Text_Append("Dare you consume this DANGEROUSLY tantalizing bowl of");
                  self.Text_Append("scrumptious fruit rings?");
                  self.Text_Append("\n  2 = NO\n  3 = YES");
               elif(self.Acquired_FriendshipCast == True):
                      self.Text_Append("\nYou see an empty bowl on a wooden table. This empty");
                      self.Text_Append("bowl is the same one where you formerly ate those");
                      self.Text_Append("DELICIOUS fruit rings and acquired Friendship Cast.");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "w"):   
               self.Text_Write("L1_DISCORDSLAIR-West:  You walk west of to the rusty iron");
               self.Text_Append("cages. As you get closer, you can see the sad, lonely faces");
               self.Text_Append("of a menagerie of forest creatures trapped inside each cage.");
               self.Text_Append("Their eyes are hollow and full of despair, as if they have");
               self.Text_Append("lost all hope. You try to open the cages and set them free,");
               self.Text_Append("but you cannot. They are locked!\n");
               self.Text_Append(" If only you could find the key to these locks? You could");
               self.Text_Append("set them free and they might return to their forest homes");
               self.Text_Append("and be happy again.");
               if(self.TRAP2_Encountered == False):
                  self.Text_Append("Further westward, you spy a small, rusty cage. In it you");
                  self.Text_Append("see a poor, grumpy, fluffy Pallas cat (Manul). It's so");
                  self.Text_Append("completely FLUFFY! Never in your life have you seen so");
                  self.Text_Append("much fur and teeth. The Pallas cat looks so miserable");
                  self.Text_Append("and sad. There is a key in the door of its cage.\n");
                  self.Text_Append("Will you turn the KEY and set the sad Manul free?");
                  self.Text_Append("\n  4 = NO\n  5 = YES");
               elif(self.TRAP2_Encountered == True):   
                  self.Text_Append("You see an empty cage where formerly you freed a very");
                  self.Text_Append("angry and grumpy Pallas cat. You can still feel the pain");
                  self.Text_Append("of its nasty scratches on your flanks.");
               self.Text_Append("\nClick \"GO\"to continue.\n");                

               self.Text_Append("\nClick \"GO\"to continue.\n");             

          elif(self.CHOICE == "x"):   
               self.LOCATION = self.L1_UNDERGROUND;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Found_Plate_Armor == False):
                if(self.CHOICE == "1"):
                   self.Found_Plate_Armor = True;
                   self.Plyr_Heroine.INV_Has_Plate_Armor = "TRUE";
                   self.Text_Write("\nYou acquire the magic item:");
                   self.Text_Append("Princess Plate Armor of Perfection!\n");
                   self.Text_Append("\nSo shiny!\n");
                   self.Plyr_Heroine.Inventory_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("\nIt might be a TRAP. You decide it would be");
                     self.Text_Append("safer to leave the book alone.");
                self.Text_Append("\nClick \"GO\"to continue.\n");

          elif((self.CHOICE == "2" or self.CHOICE == "3") and self.Acquired_FriendshipCast == False):
                if(self.CHOICE == "3"):
                   self.Acquired_FriendshipCast = True;
                   self.Plyr_Heroine.SKILL_Has_FriendshipCast = "TRUE";
                   self.Text_Write("\nYou bury your hungry face in the fruit rings. So");
                   self.Text_Append("delicious! So tangy and sweet and citrisy! When you");
                   self.Text_Append("do, you strangely begin to feel at peace with the");
                   self.Text_Append("entire universe and become completely calm. It is as");
                   self.Text_Append("if every being in the entire universe has suddenly");
                   self.Text_Append("desired to become your BFF! What on earth?");
                   self.Text_Append("\nYou acquire the magic skill: FRIENDSHIP Cast!");
                   self.Text_Append("\nAnd those fruit rings were SO yummy!\n");
                   self.Plyr_Heroine.SKILL_Display();
                elif(self.CHOICE == "2"):
                     self.Text_Write("\nAs delicious as they look, you choose not to eat");
                     self.Text_Append("the spectacularly colred fruit rings. What if it");
                     self.Text_Append("angered the strange-looking dragon? What if they");
                     self.Text_Append("are POISON?!?");
                self.Text_Append("\nClick \"GO\"to continue.\n");

          elif((self.CHOICE == "4" or self.CHOICE == "5") and self.TRAP2_Encountered == False):
                if(self.CHOICE == "5"):
                   self.TRAP2_Encountered = True;
                   self.Text_Write("You turn the key and open the crusty cage door. As");
                   self.Text_Append("soon as you do, the Pallas cat jumps out of the cage");
                   self.Text_Append("bearing a serious grudge and full of fury and claws");
                   self.Text_Append("and fangs!");
                   self.Text_Append("It bites and scrathces you for 10 points of dammage.");
                   self.Text_Append("\nYour health WAS: " + str(self.Plyr_Heroine.EntityHealth));
                   self.Plyr_Heroine.EntityHealth -= 10;
                   self.Text_Append("Your health is NOW: " + str(self.Plyr_Heroine.EntityHealth));
                   self.Plyr_Heroine.Display_Entity();
                elif(self.CHOICE == "4"):
                     self.Text_Write("Maybe setting this grumpy Guss free would be a mistake?");
                     self.Text_Append("You decide to leave the Manul right where it sits.");
                self.Text_Append("\nClick \"GO\"to continue.\n");                                                                             

          else: 
               VIEW = "LOCATION: L1_DISCORDSLAIR\n";
               VIEW += "\nYou walk into an enormous cavern, blinking as your";
               VIEW += "\npupils dilate and try to adjust to the intense green";
               VIEW += "\nbrightness reflecting from a large crystal stalactite";
               VIEW += "\ndescending from the cave ceiling far above you. It";
               VIEW += "\nseems as bright and hot as a sun would be, and you";
               VIEW += "\navert your eyes as they cannot withstand the heat and";
               VIEW += "\nbrightness for long. You look around and realize you";
               VIEW += "\nare surrounded by dark, flat black obsidian walls that";
               VIEW += "\n somehow swallow the intense green light being emitted";
               VIEW += "\nfrom above.\n";
               VIEW += "\nTo your great astonishment, you see what looks like a";
               VIEW += "\npatchwork quilt of a dragon, made up of what looks like a";
               VIEW += "\nrandom assortment of mis-matched and asymmetrical spare";
               VIEW += "\nbody parts. This being is enveloped in a cloud of rainbow";
               VIEW += "\ncolors and sparkles randomly exploding all around it like";
               VIEW += "\nbrilliant fireworks! It is preoccupied with reading";
               VIEW += "\nsomething from a strange tablet with unintelligible"
               VIEW += "\nsymbols. It doesn't notice you at the moment.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see Discord! He's reading something from";
               VIEW += "\na tablet. What's he up to?";
               VIEW += "\nSOUTH: You see dark obsidian walls. A large shelf 100 feet";
               VIEW += "\nlong and 20 feet high holds books and stone tablets.\n";
               VIEW += "\nEAST: You see a wooden table with a large clay bowl and a";
               VIEW += "\nwodden spoon. A box of fruity cereal and a pitcher of milk";
               VIEW += "\n sit beside it.\n";
               VIEW += "\nWEST: You see several rusty iron cages with small forest";
               VIEW += "\ncreatures trapped behind their bars.\n";
               VIEW += "\nX: You see the EXIT from Discord's Lair to the underground";
               VIEW += "\ncavern from which you came.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n";                

               self.Text_Write(VIEW); 

    #---Function-----------------------------------------------------------------------------------------------------
      def FRIENDSHIPFOREST(self):
          print("\nIn L1_FRIENDSHIPFOREST now.");
          self.IMG_MAP_L1_FRIENDSHIPFOREST = self.IMG_MAP_L1_FRIENDSHIPFOREST.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_FRIENDSHIPFOREST);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);

          self.Sound_Forest_1_Thread();

          if(self.CHOICE == "n"):   
             self.Text_Write("L1_FRIENDSHIPFOREST-North: You walk towards the north end");
             self.Text_Append("of this lush forest, weaving your way through low-hanging");
             self.Text_Append("branches of dew-covered evergreens. You look down at your");
             self.Text_Append("hoves and make slow progress as the ground is covered");
             self.Text_Append("with thick, gnarly roots criss-crossing the base of each");
             self.Text_Append("tree in the forest. You hear the pleasing chirp of crickets");
             self.Text_Append("and you wonder why they are chirping at this odd hour?\n");
             self.Text_Append("You hear a cacphony of songbirds and the calls of grackles,");
             self.Text_Append("starlings, bluejays, finches and robins. Overhead, you see");
             self.Text_Append("a pair of hawks circling. Perhaps they are mates? You can");
             self.Text_Append("go no further in this direction.");
             self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "s"):   
               self.Text_Write("L1_FRIENDSHIPFOREST-South: Traveling south through the");
               self.Text_Append("evergreens, you are delighted by the fresh invigorating");
               self.Text_Append("scent carried on the wind that fills your nostrils.");
               if(self.Found_HealingPotion_4 == False):
                  self.Text_Append("You notice a hollow stump in the distance. Something");
                  self.Text_Append("glimmers in the stump. In the patchy light drifting down");
                  self.Text_Append("through the forest canopy above, the object in the stump");
                  self.Text_Append("sparkles radiantly when rays of sunlight refract on it at");
                  self.Text_Append("just the right angle.\n");
                  self.Text_Append("Standing right beside the stump now, you can't quite make");
                  self.Text_Append("out what is in side the dark hollow space of this tree");
                  self.Text_Append("stump. Will you reach into and see what treasures it may");
                  self.Text_Append("contain? Or will you refrain from being so bold, just in");
                  self.Text_Append("case this is a TRAP?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.Found_HealingPotion_4 == True):
                      self.Text_Append("\nOff in the distance you see the hollow tree stump");
                      self.Text_Append("where you formerly found the healing potion hidden");
                      self.Text_Append("inside it. You can go no further south from here.");
               self.Text_Append("\nClick \"GO\"to continue.\n");       

          elif(self.CHOICE == "e"):   
               #Note: Insert NPC_3 access here in later versions
               self.LOCATION = self.L1_NPC_3_Encounter;
               self.CHOICE = "#";
               self.SwitchBoard();
               self.Text_Append("\nClick \"GO\"to continue.\n");               

          elif(self.CHOICE == "w"):   
               self.Text_Write("L1_FRIENDSHIPFOREST-West: Trotting WEST, you step into");
               self.Text_Append("the middle of a circle of cute, fluffy bunnies. You feel");
               self.Text_Append("a bit awkward, as they all stare at you now and you are");
               self.Text_Append("at the center of their attention. You introduce yourself,");
               self.Text_Append("but they do not repond. If only you had something to break");
               self.Text_Append("the ice with? Something that would earn their favor?\n");
               self.Text_Append("You decide to go no further west until you find a way to");
               self.Text_Append("bountifully befriend these beautiful bunnies!");
               if(self.Acquired_Teleportation == False):
                  self.Text_Append("Among all the cute fluffy bunnies, you see one holding");
                  self.Text_Append("a bag of mushy pink marshmallows. It holds up a sign in");
                  self.Text_Append("its furry little paws that is barley legible. Squinting,");
                  self.Text_Append("you eventually realize the sign says:\n");
                  self.Text_Append("Put this ENTIRE bag of marshmallows in your mouth and");
                  self.Text_Append("then say the words: \"CUTE FLUFFY BUNNIES!\" Do this");
                  self.Text_Append("10 times before you swallow.\n");
                  self.Text_Append("Will you try to eat an entire bag of pink, mushy");
                  self.Text_Append("marshmallows at once? And will you say the words");
                  self.Text_Append("\"CUTE FLUFFY BUNNIES\" 10 times before you swallow?\n");
                  self.Text_Append("Is this binge worth the effort? What if you CHOKE to");
                  self.Text_Append("death on pink mushy marshmallows?!? not an honorable");
                  self.Text_Append("way to go, for sure. What will you do?");
                  self.Text_Append("\n  2 = NO\n  3 = YES");
               elif(self.Acquired_Teleportation == True):
                      self.Text_Append("Coming back to this area fills your mind with fond");
                      self.Text_Append("memories of the savory taste of a mouth stuffed with");
                      self.Text_Append("gluttonous quantitites of pink mushy marshmallows.");
                      self.Text_Append("Victory can be so SWEET! For here is the place where");
                      self.Text_Append("you acquired the mnagic skill of TELEPORTATION.");
               self.Text_Append("\nClick \"GO\"to continue.\n");       

          elif(self.CHOICE == "x"):   
               self.LOCATION = self.L1_W3;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Found_HealingPotion_4 == False):
                if(self.CHOICE == "1"):
                   self.Found_HealingPotion_4 = True;
                   self.Plyr_Heroine.INV_Has_HealingPotions += 1;
                   self.Text_Write("\nYou found a HEALING potion!");
                   self.Text_Append("\nThese rare items are true blessings.\n");
                   self.Plyr_Heroine.Inventory_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("You decide not to reach into the hollow tree");
                     self.Text_Append("stump. What if something malignant is inside");
                     self.Text_Append("it and BITES you?!?");
                self.Text_Append("\nClick \"GO\"to continue.\n");

          elif((self.CHOICE == "2" or self.CHOICE == "3") and self.Acquired_Teleportation == False):
                if(self.CHOICE == "3"):
                   self.Acquired_Teleportation = True;
                   self.Plyr_Heroine.SKILL_Has_Teleportation = "TRUE";
                   self.Text_Write("\nYou acquire the magic skill of: TELEPORTATION!");
                   self.Text_Append("\nMoving around just got a lot cooler.\n");
                   self.Plyr_Heroine.SKILL_Display();
                elif(self.CHOICE == "2"):
                     self.Text_Write("\nIt might be a TRAP! You could choke on all those");
                     self.Text_Append("pink mushy marshmallows and DIE! You decide now to");
                     self.Text_Append("listen to the bantering bunny.");

                self.Text_Append("\nClick \"GO\"to continue.\n");                                                              

          else: 
               VIEW = "LOCATION: L1_FRIENDSHIPFOREST\n";
               VIEW += "\nYou find yourself at the edge of a lush, everfreen forest.";
               VIEW += "\nAll around you are tall evergreen trees that spiral into";
               VIEW += "\nthe sky. The trees are so tall and clos together, the";
               VIEW += "\ncreate a large canopy above that shades the earth beneath.";
               VIEW += "\nFurry and feathery forest creatures fill the branches of";
               VIEW += "\nthese trees as far as you can see.\n";
               VIEW += "\nFluffy, squirrels and cute, cuddly bunnies dart to and";
               VIEW += "\nfrom among the massive roots of the evergreens that";
               VIEW += "\nspread out across the forest floor.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: you see a castle courtyard in the distance. Beyond";
               VIEW += "\nit a tall castle spirals into the sky.\n";
               VIEW += "\nSOUTH: you see a small wooden sign planted next to a";
               VIEW += "\ngrassy path lined with evergreens on both sides.\n";
               VIEW += "\nEAST: You see endless woodlands full of happy hopping,";
               VIEW += "\nscampering, flying and prancing forest creatures.\n";
               VIEW += "\nWEST: You see a small circle of cute, chubby, fluffy";
               VIEW += "\nbunnies has gathered together for a meeting.\n";
               VIEW += "X: EXIT FriendshipForest back to WEST_3.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n"; 

               self.Text_Write(VIEW); 

    #---Function-----------------------------------------------------------------------------------------------------
      def PEGASUSCITADEL(self):
          print("\nIn L1_PEGASUSCITADEL now.");
          self.IMG_MAP_L1_PEGASUSCITADEL = self.IMG_MAP_L1_PEGASUSCITADEL.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_PEGASUSCITADEL);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);

          self.Sound_Horse_Snort_1_Thread();
          self.Sound_Horse_Trot_1_Thread();

          if(self.CHOICE == "n"):   
             self.Text_Write("L1_PEGASUSCITADEL-North: Walking north within the citadel,");
             self.Text_Append("you approcah a group pf pegasi that appear to be celebrating");
             self.Text_Append("a joyous and raucous festival. Everypony is frolicking and");
             self.Text_Append("chasing each other to and fro. There are contests and games");
             self.Text_Append("and long tables filled with festive treats and a huge variety");
             self.Text_Append("of foods. You try to strike up a conversation with come of the");
             self.Text_Append("celebrants, but it seems like no one even notices you exist.");
             self.Text_Append("You wonder: what would you have to do to get their attention?");
             self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "s"):   
               self.Text_Write("\L1_PEGASUSCITADEL-South: Walking over to the SOUTH end of");
               self.Text_Append("the citadel, you see several restaurants and inns with");
               self.Text_Append("brightly colored windows and doors. On one corner of a");
               self.Text_Append("festively decorated street between two old, 18th Century");
               self.Text_Append("style Victorian lamp posts sits a quaint, french styled");
               self.Text_Append("open-air café.\n");
               self.Text_Append("Several peagasi are seated at heart-shaped tables in");
               self.Text_Append("wrought iron chairs at this café, many sipping what");
               self.Text_Append("smells like coffee and hot chocolate from GIANT cups");
               self.Text_Append("the size of saucers. A sign above the café advertises:\n");
               self.Text_Append("\"Coffee: 3 Pony Pence per Cup");
               self.Text_Append(" Hot chocolate: 2.5 Pony Pence per Cup\"");
               self.Text_Append("You think about sitting down to have some coffee");
               self.Text_Append("or a nice cup of hot chocolate. But you realize that you");
               self.Text_Append("can go no further soutward from this location.");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_PEGASUSCITADEL-East: You push along eastward inside the");
               self.Text_Append("Pegasus Citadel. You pass several pegasi trotting along");
               self.Text_Append("bright white sidewalks embedded with pyrite, amethist,");
               self.Text_Append("gypsum, agate, jasper, opals, moonstone, rosy quartz and");
               self.Text_Append("selenite. You marvel at the sparkling beauty of such");
               self.Text_Append("walkways. Why would pegasi who have wings and fly spend");
               self.Text_Append("so much effort creating spectacular sidewalks? Hmmm...\n");
               self.Text_Append("Movine further east in the citadel, you spy a fountain.");
               self.Text_Append("Inside the fountain is a large 40-foot talk clock - as");
               self.Text_Append("large as a building that could hold 50 ponies! Water");
               self.Text_Append("from the fountain swirls around the giant clock like");
               self.Text_Append("a moat surrounding a castle.");
               if(self.Acquired_TimeWarp == False):
                  self.Text_Append("\nGazing at the clock a bit longer, you notice that");
                  self.Text_Append("the hour, minute and second hands of the clock have");
                  self.Text_Append("all stopped at 4:44. Why would pegasi who worked so");
                  self.Text_Append("hard creating spectacular sidewalks tolerate a giant");
                  self.Text_Append("broken clock in the middle of their citadel?\n");
                  self.Text_Append("You wonder: is there a way to FIX this gaping eye sore?");
                  self.Text_Append("You walk up to the edge of the fountain and notice");
                  self.Text_Append("a sealed door on one side of the enormous clock. Next");
                  self.Text_Append("to the door is a lever, slanted upwards towards one of");
                  self.Text_Append("the walls of the clock. You wonder, what would happen");
                  self.Text_Append("if you pulled the level?\n");
                  self.Text_Append("Unable to resist your curiosity, you jump into the ");
                  self.Text_Append("fountain's, walk across to the door and pull the lever");
                  self.Text_Append("down beside it. The door opens and you walk inside.");
                  self.Text_Append("Inside, you notice a spring has popped out of place,");
                  self.Text_Append("hindering the clock from its normal operation.\n");
                  self.Text_Append("DARE you push the clock spring back into place? Would");
                  self.Text_Append("it restart the clock? And if it did, would it be a");
                  self.Text_Append("good thing, or a bad thing? Will you do it?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.Acquired_TimeWarp == True):
                      self.Text_Append("\nGazing across the crystal-clear fountain waters,");
                      self.Text_Append("you see the same giant clock where you previously");
                      self.Text_Append("acquired the magic skill TIMEWARP. You take pride");
                      self.Text_Append("in know that YOU personally fixed the clock and");
                      self.Text_Append("started all its mechanisms running again. Beyond");
                      self.Text_Append("the fountain and clock, you see the east citadel");
                      self.Text_Append("wall. You realize you can go no further east from");
                      self.Text_Append("here. The only option is to turn around.");
               self.Text_Append("\nClick \"GO\"to continue.\n");  

          elif(self.CHOICE == "w"):   
               self.Text_Write("L1_PEGASUSCITADEL-West: Walking WEST, you run into a gang");
               self.Text_Append("of 3 adolescent, unruly teenage dragons.");
               if(self.L1_Multiple_Opponents_Encounter_Alive  == True):
                  self.LOCATION = self.L1_Multiple_Opponents_Encounter;
                  self.CHOICE = "#";
                  #self.SwitchBoard(); #disable for combat sequences
               else:
                     MESSAGE = "Here lies a pile of garrish, punk 80's clothing";
                     MESSAGE += "\nthat once belonged to the rebellious group";
                     MESSAGE += "\nof 3 EMO teenage dragons you formerly";
                     MESSAGE += "\nvanquished. You feel a deep sense of";
                     MESSAGE += "\naccomplishmentand satisfaction at this feat.";
                     MESSAGE += "\n\nBut you can go no further WEST from here.";
                     self.Text_Write(MESSAGE);
                     self.Text_Append("\nClick \"GO\"to continue.\n"); 
               self.Text_Append("\nClick \"GO\"to continue.\n");  

          elif(self.CHOICE == "x"):   
               self.LOCATION = self.L1_W2;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Acquired_TimeWarp == False):
                if(self.CHOICE == "1"):
                   self.Acquired_TimeWarp = True;
                   self.Plyr_Heroine.SKILL_Has_TimeWarp = "TRUE";
                   self.Text_Write("You try with all your strength to push the protruding");
                   self.Text_Append("clock spring back into its proper place. After much");
                   self.Text_Append("effort, it slides back into the clock differnential");
                   self.Text_Append("mechanism. CLICK! The clock begins ticking, the hour,");
                   self.Text_Append("minute and second hands moving once again. You fixed");
                   self.Text_Append("it! You feel a tingling sensation and everything around");
                   self.Text_Append("beings slowing down until everything has come to a");
                   self.Text_Append("complete stop and you are the only one still moving.");
                   self.Text_Append("\nYou acquire the magic skill of: TIME WARP!");
                   self.Text_Append("\nFinally! More of something you are always");
                   self.Text_Append("running out of :-)");
                   self.Plyr_Heroine.SKILL_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("\nYou decide not to push the spring back int place.");
                     self.Text_Append("What if the clock was stopped for a reason? What if");
                     self.Text_Append("by fixing the clock it caused something HORRIBLE to");
                     self.Text_Append("happen? A catastrophe perhaps the clock was broken");
                     self.Text_Append("purposefully for just to prevent? You DARE not risk");
                     self.Text_Append("restarting it. So you turn and trot away.");
                self.Text_Append("\nClick \"GO\"to continue.\n");                                             

          else: 
               VIEW = "LOCATION: L1_PEGASUSCITADEL\n";
               VIEW += "\nYou find yourself in the midst of a fabulous equestrian";
               VIEW += "\ncitadel! Everywhere you look? You see small stone houses,";
               VIEW += "\nshops, stables and buildings. Streets line this citadel, ";
               VIEW += "\nand at its center is a market where various vendors have ";
               VIEW += "\nsetup their carts and tables to sell produce, fruit,";
               VIEW += "\ntackle and clothing. All around you are colorful pegasi,";
               VIEW += "\nleaping to and fro and bounding into the air on feathered,"; 
               VIEW += "\ncolorful wings.\n";
               VIEW += "\nIn the middle of the marketplace you see a tablet with a";
               VIEW += "\nlarge, bronze plaque. Inscribed upon it are the words:"; 
               VIEW += "\n\"Honoring Rainbow Dash - inventor of the Sonic RainBoom.\"";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see gray, rocky caves and a salty old mare";
               VIEW += "\nselling flowers.n";
               VIEW += "\nSOUTH: You see cobbled stone huts and houses.\n";
               VIEW += "\nEAST: You spy an enormous apple orchard. The trees are";
               VIEW += "\nfull of ripe, red delicious apples.\n";
               VIEW += "\nWEST: You see a large stone building with dozens of";
               VIEW += "\nweather veins and observation stations.\n";
               VIEW += "\nX: EXIT the Pegasus Citadel back to WEST_2.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n"; 

               self.Text_Write(VIEW); 

    #---Function-----------------------------------------------------------------------------------------------------
      def MOUNTAINOFMEANNESS(self):
          print("\nIn L1_MOUNTAINOFMEANNESS now.");
          self.IMG_MAP_L1_MOUNTAINOFMEANNESS = self.IMG_MAP_L1_MOUNTAINOFMEANNESS.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_MOUNTAINOFMEANNESS);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);

          self.Sound_THUNDER_Thread();          

          if(self.CHOICE == "n"):   
             self.Text_Write("L1_MOUNTAINOFMEANNESS-North:  Unscalable cliffs!");
             if(self.L1_MountainOfMeanness_Harpy_Alive == True):
                self.LOCATION = self.L1_MountainOfMeanness_Harpy_Encounter;
                self.CHOICE = "#";
                #self.SwitchBoard(); #disable for combat sequences
             else:
                   MESSAGE = "You see blood, talons and feathers.";
                   MESSAGE += "\n Here lies the remains of the horrible";
                   MESSAGE += "\n horse eating harpy you bravely defeated.";
                   MESSAGE += "\n\n You can go no further north from here.";
                   self.Text_Write(MESSAGE);
                   self.Text_Append("\nClick \"GO\"to continue.\n");             

          elif(self.CHOICE == "s"):   
               self.Text_Write("L1_MOUNTAINOFMEANNESS-South: Moving south you follow a");
               self.Text_Append("a rocky path down a steep ridge. All along the path");
               self.Text_Append("are loose stones and pebbles that appear to have been");
               self.Text_Append("dislodged from the towering cliffs above. You have to");
               self.Text_Append("step carefully over them, you wouldn't want to trip");
               self.Text_Append("and fall in an area like this. Thinking how precarious");
               self.Text_Append("this path is becoming, you notice that it drops off");
               self.Text_Append("down an immensely steep cliff and you can go no further");
               self.Text_Append("in this direction down the mountain, if you value your");
               self.Text_Append("life ...");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_MOUNTAINOFMEANNESS-East: You walk EAST over");
               self.Text_Append("to the exposed, hollow trunk of a long-since-deceased tree.");
               self.Text_Append("Inside the tree, you find a clump of straw and realize");
               self.Text_Append("it's an abandonded woodpecker's nest!\n");
               self.Text_Append("Peering beyond the trees dead branches and shriveled");
               self.Text_Append("roots, you see only the steep side of the mountain");
               self.Text_Append("descending into the fathomless depths below.");
               if(self.Found_HealingPotion_2 == False):
                  self.Text_Append("In the clump of straw, you see something glimmer");
                  self.Text_Append("and shimmer. What could it be? Will you reach into");
                  self.Text_Append("the pile of straw and twigs to see what it could be?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.Found_HealingPotion_2 == True):
                      self.Text_Append("\nInside the tree branches and woodpecker nest");
                      self.Text_Append("you see an empty pile of twigs and straw where");
                      self.Text_Append("you previously found the healing potion.");                 
               self.Text_Append("\nYou can go no further east from here ...");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "w"):   
               self.Text_Write("L1_MOUNTAINOFMEANNESS-West: Going WEST, you stop");
               self.Text_Append("abruptly at a steep ledge. You can go no further.");
               self.Text_Append("You shudder to think what would happen if you");
               self.Text_Append("slipped and fell on the sharp rocks below.\n");
               if(self.TRAP4_Encountered == False):
                  self.Text_Append("A bit more towards theledge you see a hollow");
                  self.Text_Append("log. In this hollowed out log you see a satchel");
                  self.Text_Append("with a leather handle protruding from the bough.");
                  self.Text_Append("Pull out and examine the satchel?");
                  self.Text_Append("\n  2 = NO\n  3 = YES");
               elif(self.TRAP4_Encountered == True):   
                  self.Text_Append("You see a small crater and a pile of ashes where");
                  self.Text_Append("the booby-trapped satchel and the hollow tree had");
                  self.Text_Append("formerly exploded on you.");
               self.Text_Append("\nClick \"GO\"to continue.\n");                

          elif(self.CHOICE == "x"):   
               self.LOCATION = self.L1_E2;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Found_HealingPotion_2 == False):
                if(self.CHOICE == "1"):
                   self.Found_HealingPotion_2 = True;
                   self.Plyr_Heroine.INV_Has_HealingPotions += 1;
                   self.Text_Write("\nYou found a HEALING potion!");
                   self.Text_Append("\nSuper!\n");
                   self.Plyr_Heroine.Inventory_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("You decide not to reach into the woodpecker nest.");
                     self.Text_Append("What if it's a TRAP? Better to err on the side");
                     self.Text_Append("of caution.");
                self.Text_Append("\nClick \"GO\"to continue.\n");  

          elif((self.CHOICE == "2" or self.CHOICE == "3") and self.TRAP4_Encountered == False):
                if(self.CHOICE == "3"):
                   self.TRAP4_Encountered = True;
                   self.Text_Write("!!!BOOM!!! It was all a TRAP. When you tug on the");
                   self.Text_Append("satchel's handle it explodes. Burning hot gun");
                   self.Text_Append("gun powder burns your nostrils. Ouch!");
                   self.Text_Append("As a result, you lose 10 health.");
                   self.Text_Append("\nYour health WAS: " + str(self.Plyr_Heroine.EntityHealth));
                   self.Plyr_Heroine.EntityHealth -= 10;
                   self.Text_Append("Your health is NOW: " + str(self.Plyr_Heroine.EntityHealth));
                   self.Plyr_Heroine.Display_Entity();
                elif(self.CHOICE == "2"):
                     self.Text_Write("You cautiously decide to leave the satchel");
                     self.Text_Append("right where it is. What if it's a TRAP?");
                     self.Text_Append("Better to be SAFE than SORRY.");
                self.Text_Append("\nClick \"GO\"to continue.\n");                                                            

          else: 
               VIEW = "LOCATION: L1_MOUNTAINOFMEANNESS\n";
               VIEW += "\nYou arrive at the top of a colorless, gray mountain.";
               VIEW += "\nYou don't know why, but as you pause to catch your";
               VIEW += "\nbreath? You feel absolutely ANGRY. But why? You can't";
               VIEW += "\nseem to stop the flood of negative emotions that are";
               VIEW += "\nnow filling your mind.\n"; 
               VIEW += "\nYou are enshrouded by a cold mist that makes you";
               VIEW += "\nshiver. All around you everything is covered with fog.";
               VIEW += "\nYou can only see a few feet in front of you."; 

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You spy a ring of large boulders, each with";
               VIEW += "\npatches of short, gray lichens growing in the middle.\n";
               VIEW += "\nSOUTH: Southward down the mountain, you see a swiftly";
               VIEW += "\nflowing river with floating clumps of ice.\n";
               VIEW += "\nEAST: You see a large, dead, hollow tree. You wonder -";
               VIEW += "\nHow is this long-deceased tree still standing?\n";
               VIEW += "\nWEST: A sharp ledge juts out over an incline. Below this";
               VIEW += "\nincline the side of the mountain decends into obscurity.\n";
               VIEW += "\nX: EXIT the MountainOfMeanness back to East_2.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n";                

               self.Text_Write(VIEW);  

    #---Function-----------------------------------------------------------------------------------------------------
      def SWAMPOFSADNESS(self):
          print("\nIn L1_SWAMPOFSADNESS now.");
          self.IMG_MAP_L1_SWAMPOFSADNESS = self.IMG_MAP_L1_SWAMPOFSADNESS.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_SWAMPOFSADNESS);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);   
          self.Sound_RAIN_Thread();

          self.Sound_MockingJay_Whistle_Thread();
          self.Sound_Wind_1_Thread();

          if(self.CHOICE == "n"):   
             self.Text_Write("L1_SWAMPOFSADNESS-North: You wade northwards through the");
             self.Text_Append("murky waters of the bog. Soon you approach a cluster of");
             self.Text_Append("decaying, rotting mangroves. Perhaps the poison waters");
             self.Text_Append("of the swamp was more than they could handle. Not poison");
             self.Text_Append("that kills the body, but poison that kills the soul.\n");
             if(self.Found_Chain_Mail == False):
                self.Text_Append("In the brackish water lapping at the roots of the");
                self.Text_Append("dead and rotting mangroves, you see something glimmer");
                self.Text_Append("in the cloudy waters beneath. It doesn't look like");
                self.Text_Append("the source of thsi metallic shininess is too deep");
                self.Text_Append("beneath the water to touch. It looks like the depth");
                self.Text_Append("of the water only approaches your flanks in this");
                self.Text_Append("area. Will you wade out to retrieve whatever this");
                self.Text_Append("shiny object may be?");
                self.Text_Append("\n  0 = NO\n  1 = YES");
             elif(self.Found_Chain_Mail == True):
                  self.Text_Append("You see a dead clump of rotten mangroves. Beneath");
                  self.Text_Append("them lies the roots and murky water where you");
                  self.Text_Append("formerly found the enchanted CHAIN MAIL. Because");
                  self.Text_Append("the mangroves and their roots are so thick in");
                  self.Text_Append("this area, you can proceed no further in this");
                  self.Text_Append("direction.");
             self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "s"):   
               self.Text_Write("L1_SWAMPOFSADNESS-South: You plod southward through");
               self.Text_Append("the dank, dark, depressing dismal, dreary, diabolically");
               self.Text_Append("destructive atmosphere. The thick fog surrounding and");
               self.Text_Append("enshrouding everything aroudd you seems to weigh like");
               self.Text_Append("a heavy, crushing weight on your shoulders and it fills");
               self.Text_Append("you with despair. As you walk, the mud beneath your");
               self.Text_Append("hooves gets softer and softer and you begin to sink");
               self.Text_Append("lower and lower the further south you move at this");
               self.Text_Append("location.\n");
               self.Text_Append("When the mud comes up to your belly, you stop,");
               self.Text_Append("realizing you can go no firther south without the");
               self.Text_Append("risk of being swallowed alive in the muck you are");
               self.Text_Append("now standing in. The weight of despair continues");
               self.Text_Append("to crush your shoulders and pull you down into the");
               self.Text_Append("muck. The depression surrounding you and filling");
               self.Text_Append("your mind is so thick you could cut it with a knife.");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_SWAMPOFSADNESS-East:  ");
               if(self.L1_SwampOfSadness_Dolphin_Alive == True):
                self.LOCATION = self.L1_SwampOfSadness_Dolphin_Encounter;
                self.CHOICE = "#";
                #self.SwitchBoard(); #disable for combat sequences
               else:
                   #Note: Insert NPC_1 access here in later versions
                   self.LOCATION = self.L1_NPC_2_Encounter;
                   self.CHOICE = "#";
                   self.SwitchBoard();
                   self.Text_Append("\nClick \"GO\"to continue.\n");               

          elif(self.CHOICE == "w"):   
               self.Text_Write("L1_SWAMPOFSADNESS-West: Here you encounter NPC2.");
               self.Text_Append("You will be able to have conversations with this");
               self.Text_Append("character and she will drop some game clues. But");
               self.Text_Append("navigation-wise you can go no further in this");
               self.Text_Append("direction.");
               self.Text_Append("\nClick \"GO\"to continue.\n"); 

          elif(self.CHOICE == "x"):   
               self.LOCATION = self.L1_E3;
               self.CHOICE = "#";
               self.SwitchBoard(); 

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Found_Chain_Mail == False):
                if(self.CHOICE == "1"):
                   self.Found_Chain_Mail = True;
                   self.Plyr_Heroine.INV_Has_Chain_Mail = "TRUE";
                   self.Text_Write("\nYou acquire the magic item:");
                   self.Text_Append("Enchanted CHAIN MAIL!\n");
                   self.Text_Append("You feel a bit more protected now.");
                   self.Plyr_Heroine.Inventory_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("\nIt might be a TRAP. Or what if the water");
                     self.Text_Append("is actually much deeper than it appears and");
                     self.Text_Append("you were to drown trying to retrieve what");
                     self.Text_Append("might be somethign completely useless? You");
                     self.Text_Append("decide to leave the shimmering object where");
                     self.Text_Append("it rests submerged beneath the murky depths.");
                self.Text_Append("\nClick \"GO\"to continue.\n");                                            

          else: 
               VIEW = "LOCATION: L1_SWAMPOFSADNESS\n";
               VIEW += "\nYou feel heavy, sorrowful and depressed as you trot";
               VIEW += "\nreluctantly into the Swamp of Sadness. You find";
               VIEW += "\nyourself standing in shallow, murky, brackish waters.";
               VIEW += "\n Your hooves sink into the mud, and you feel like the";
               VIEW += "\nweight of the entire world on your shoulders.";
               VIEW += "\nAll around you are the remains of once-living trees.";
               VIEW += "\nThe smell of death and decay permeate the air.";
               VIEW += "\nTo the southwest, you see a winding dirt road.\n";
               VIEW += "\nSouth-eastward you see a sleeping giant. A winding";
               VIEW += "\npath meanders of into the distance behind this sleeping";
               VIEW += "\ncolossus. But you cannot explore in this direction as";
               VIEW += "\nlong as this sleeping giant obstructs the path.\n";
               VIEW += "\nThe terrible titan snoozing next to you is snoring."; 
               VIEW += "\nThe rumble of his bellowing breath rumbles like a";
               VIEW += "\nhurricane. The stench of rotten eggs and sulfur fills";
               VIEW += "\nyour burning nostrils. You feel so sad here.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see only the endless expanse of this dark";
               VIEW += "\nand dreary swamp. It fills you with hopelessness.\n";
               VIEW += "\nSOUTH: In the distance, you see an old canvas awning";
               VIEW += "\nand beneath it a blacksmith's forge. You see smoke ";
               VIEW += "\nfrom a small fire billowing beneath.\n";
               VIEW += "\nEAST: You spy a clump of mangroves. Nested in the";
               VIEW += "\nbranches of those mangroves, you see many pairs of";
               VIEW += "\nred eyes glaring back at you.\n";
               VIEW += "\nWEST: You see only murky swamp water and bubbling bogg.";
               VIEW += "\nHere and there dead, fallen tree trunks protrude from";
               VIEW += "\nbeneath the cloudy water.\n";
               VIEW += "\nX: EXIT the Swamp of Sadness back to East_3.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n"; 

               self.Text_Write(VIEW); 

    #---Function-----------------------------------------------------------------------------------------------------
      def UNICORNJUNCTION(self):
          print("\nIn L1_UNICORNJUNCTION now.");
          self.IMG_MAP_L1_UNICORNJUNCTION = self.IMG_MAP_L1_UNICORNJUNCTION.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_UNICORNJUNCTION);
          self.LAB_Current_View.configure(image=self.IMG_Current_View); 

          self.Sound_Hawk_Thread();
          self.Sound_Horse_Gallop_1_Thread();

          if(self.CHOICE == "n"):   
             self.Text_Write("L1_UNICORNJUNCTION-North: You walk NORTH towards the");
             self.Text_Append("gazebo and find yourself surrounded by tables of");
             self.Text_Append("scrumptious-looking cupcakes. Some of them, OH YES,");
             self.Text_Append("they have SPRINKLES!!! You wonder if they are for sale?");
             self.Text_Append("Or perhaps prepared for someone special on their birthday?\n");
             if(self.Found_HealingPotion_1 == False):
                self.Text_Append("Looking around, you notice a small, translucent tube at");
                self.Text_Append("the base of a platter of cupcakes on one of the tables.");
                self.Text_Append("The tube has been stuffed into the strawberry frosting");
                self.Text_Append("of a large, delicious cupcake! Examining the glassy tube");
                self.Text_Append("futher, you make out some strange characters inscribed");
                self.Text_Append("on the edge of the glass tube. The characters suddenly");
                self.Text_Append("rearrange themselves as you view them and for the word\n");
                self.Text_Append(" \"GALADRIEL\"\n");
                self.Text_Append("You wonder - should you touch it? Could it be something");
                self.Text_Append("poisonous or harmful? Or could it be some kind of TEST");
                self.Text_Append("or maybe even a TRAP? It sparkles like starlight! What");
                self.Text_Append("will you do? Will you touch it?");
                self.Text_Append("\n  0 = NO\n  1 = YES");
             elif(self.Found_HealingPotion_1 == True):
                  self.Text_Append("You seen an incredibly large and delicious looking");
                  self.Text_Append("strawberry cupcake with strawberry frosting. In the");
                  self.Text_Append("middle of the cake is a large cavity where there is");
                  self.Text_Append("no longer any icing. The cavity in this cupcake is");
                  self.Text_Append("all that remains after you took the healing potion");
                  self.Text_Append("from it.");               
             self.Text_Append("\nClick \"GO\"to continue.\n");                

          elif(self.CHOICE == "s"):   
               self.Text_Write("L1_UNICORNJUNCTION-South: You walk southward and come");
               self.Text_Append("to a flea market filled with tables of various goods");
               self.Text_Append("and venders selling their wares. You see many useful");
               self.Text_Append("items at this flea market. If only you had some");
               self.Text_Append("CURRENCY? Perhaps you could buy something useful");
               self.Text_Append("from these venders. But without MONEY, you see no");
               self.Text_Append("reason to explore this area any further.");
               self.Text_Append("\nClick \"GO\"to continue.\n");  

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_UNICORNJUNCTION-East: You trot EAST over to a shop");
               self.Text_Append("with a sign that reads \"Relationship Counseling\".");
               self.Text_Append("You try to turn the door knob and open the door, but");
               self.Text_Append("you cannot. It is LOCKED. If only you had a KEY?");
               self.Text_Append("Until you find one, you can proceed no further east");
               self.Text_Append("from this location.");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "w"):   
               self.Text_Write("L1_UNICORNJUNCTION-West: You gallop WEST over towards");
               self.Text_Append("a building with a sign that says \"Magic Shop\". You");
               self.Text_Append("ee a sign hanging in the window. It says:\n");
               self.Text_Append("\"Out to lunch. Be back soon. Come back later.\"\n");
               self.Text_Append("Perhaps if you came back at a better time? There");
               self.Text_Append("might be some really useful items for sale in this");
               self.Text_Append("shop if you had money ro something to trade with.");
               self.Text_Append("But until the shop keeper returns, this area");
               self.Text_Append("is inaccessible to you. You can go no further west");
               self.Text_Append("in this direction.");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "x"):   
               self.LOCATION = self.L1_W1;
               self.CHOICE = "#";
               self.SwitchBoard();    

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Found_HealingPotion_1 == False):
                if(self.CHOICE == "1"):
                   self.Found_HealingPotion_1 = True;
                   self.Plyr_Heroine.INV_Has_HealingPotions += 1;
                   self.Text_Write("\nYou found a HEALING potion!");
                   self.Text_Append("\nThese come in really handy.\n");
                   self.Plyr_Heroine.Inventory_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("You decide not to touch the translucent glass");
                     self.Text_Append("tube. What if it's a TEST? A TRAP?");
                self.Text_Append("\nClick \"GO\"to continue.\n");                                          

          else: 
               VIEW = "LOCATION: L1_UNICORNJUNCTION\n";
               VIEW += "\nYou trot into a lively equestrian village. All around";
               VIEW += "\nyou, unicorns are ahoof carrying packages and parcels";
               VIEW += "\ntelikinetically - by magic! The wood and straw houses in";
               VIEW += "\nthis village are all painted purple, pink and lavender.\n";
               VIEW += "\nArriving at the center of this colorful, quaint village";
               VIEW += "\nyou find yourself standing on an old wooden platform in a";
               VIEW += "\nbrightly colored train station. All around you are";
               VIEW += "\nbeautiful unicorns of different sizes. They are chatting";
               VIEW += "\nwith one another and galloping and prancing in random";
               VIEW += "\ndirections. To the southeast, you see a winding dirt road.\n";
               VIEW += "\nYou see a large banner draped across the center of the"; 
               VIEW += "\nvillage. It says:\n";
               VIEW += "\n\"Twilight's Twinkly Friendshp Fair\".\n"; 
               VIEW += "\nIn the center of the village is a large gazebo. Dozens";
               VIEW += "\nof tables and chairs have been setup around and within"; 
               VIEW += "\nthis gazebo, Each table is filled with cupcakes! Yum!";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see many tables surrounding a gazebo with";
               VIEW += "\ncolorful CUPCAKES. They have SPRINKLES!!!\n";
               VIEW += "\nSOUTH: You see a friendly looking mare. She has a";
               VIEW += "\nstraw hat and overalls and appears to be serving";
               VIEW += "\na stallion a tall, refreshing glass of lemonaid.";
               VIEW += "\nEAST: You see a shop with a sign that says:";
               VIEW += "\n\"Relationship Counseling\". Outside the shop are";
               VIEW += "\nseveral wooden barrels.\n";
               VIEW += "\nWEST: You see a cobbled stone building with a large,";
               VIEW += "\nwhite sign on top that says \"Magic Shop\".\n";
               VIEW += "\nX: EXIT Unicorn Junction and return to West_1.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n";                

               self.Text_Write(VIEW); 

    #---Function-----------------------------------------------------------------------------------------------------
      def HILLSOFHAPPINESS(self):
          print("\nIn L1_HILLSOFHAPPINESS now.");
          self.IMG_MAP_L1_HILLSOFHAPPINESS = self.IMG_MAP_L1_HILLSOFHAPPINESS.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_HILLSOFHAPPINESS);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);    

          self.Sound_Na_Na_Na_Thread();      

          if(self.CHOICE == "n"):   
             self.Text_Write("L1_HILLSOFHAPPINESS-North: You trot over to the ring of");
             self.Text_Append("hills covered in tall, green grass. It looks so tasty!");
             self.Text_Append("You bend down to nibble some, and it does not disappoint.");
             self.Text_Append("Your mouth fills with a savory sweetness as you munch on");
             self.Text_Append("these tall blades of juicy greenness.\n");
             self.Text_Append("Looking beyond these mouth-watering stalks, you realize");
             self.Text_Append("you can't go any further northward. The path is blocked");
             self.Text_Append("by thick, thorny briars and thorny vines that are by any");
             self.Text_Append("reasonable means of locomotion, impassible.");
             self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "s"):   
               self.Text_Write("L1_HILLSOFHAPPINESS-South: You walk into a fragrant meadow");
               self.Text_Append("filled with colorful wildflowers dancing in the wind.");
               self.Text_Append("Fluttering capriciously around these flowers is the");
               self.Text_Append("laughter of nature itself - the flapping wings of");
               self.Text_Append("butterflies. It's poestry in motion. Beyond the meadow is");
               self.Text_Append("the sandy shore of a river, too broad to swim across and ");
               self.Text_Append("go any further south.");
               if(self.Found_PrincessCloak == False):
                  self.Text_Append("On the sandy shore, a small mangrove climbs toward the");
                  self.Text_Append("sky, about 3 feet tall. On one of its branches is a");
                  self.Text_Append("purple garment covered with pearls and shiny stones. It");
                  self.Text_Append("looks like a cloak! Will you try and take this gorgeous");
                  self.Text_Append("cloak? Or will you leave it where it is? Is this just");
                  self.Text_Append("a fantastic streak of LUCK? Or is it a TRAP? Will you");
                  self.Text_Append("take the cloak?");
                  self.Text_Append("\n  0 = NO\n  1 = YES");
               elif(self.Found_PrincessCloak == True):
                      self.Text_Append("\nYou see a small mangrove about 3 feet high. Its");
                      self.Text_Append("branches are empty. On one of them, the bark is");
                      self.Text_Append("a bit discolored. This discoloration is at exactly");               
                      self.Text_Append("the spot where you formerly found the magical");
                      self.Text_Append("mystical Cloak of Perfect Princessness.");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "e"):   
               self.Text_Write("L1_HILLSOFHAPPINESS-East: Proceeding eastward, you roam");
               self.Text_Append("capriciously across the rolling green hills. Butterflies");
               self.Text_Append("flutter around you like a cloud and humming birds hover");
               self.Text_Append("over sun flowers and daisies sipping nectar. You are");
               self.Text_Append("lost in a cloud of bliss and contentment. The freash");
               self.Text_Append("fragrance of flowering grass fills your nsotrils.");
               self.Text_Append("You can go no further east from this location, as an");
               self.Text_Append("impassible granite mountainside towers thousands of");
               self.Text_Append("feet above you.");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "w"):   
               self.Text_Write("L1_HILLSOFHAPPINESS-West: You walk WEST and into a ring");
               self.Text_Append("of small, smooth river stones. In the middle of this");
               self.Text_Append("ring you see tall grass and cattails. Among them? Hides");
               self.Text_Append("a strange and unusual creature with rabbit ears and");
               self.Text_Append("cat's eyes and a face like a racoon. You are delighted");
               self.Text_Append("by this unusual ball of fur - if only you had some food");
               self.Text_Append("to offer it you might tame it and keep it for a pet?");
               self.Text_Append("But what sort of food does it eat? Where would you find");
               self.Text_Append("this food? If only ...\n");
               self.Text_Append("You can go no further west in this direction, as a 30");
               self.Text_Append("foot tall cobblestone wall is blocking your path.");
               self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "x"):   
               self.LOCATION = self.L1_S2;
               self.CHOICE = "#";
               self.SwitchBoard();

          elif((self.CHOICE == "0" or self.CHOICE == "1") and self.Found_PrincessCloak == False):
                if(self.CHOICE == "1"):
                   self.Found_PrincessCloak = True;
                   self.Plyr_Heroine.INV_Has_PrincessCloak = "TRUE";
                   self.Text_Write("\nYou acquire the mystical magic item:");
                   self.Text_Append("Cloak of Perfect Princessness");
                   self.Text_Append("\nWoohoo!\n");
                   self.Plyr_Heroine.Inventory_Display();
                elif(self.CHOICE == "0"):
                     self.Text_Write("\nIt might be a TRAP. You leave the cloak behind.");
                self.Text_Append("\nClick \"GO\"to continue.\n");                                             

          else: 
               VIEW = "LOCATION: L1_HILLSOFHAPPINESS\n";
               VIEW += "\nClimbing to the top of the incline, you find yourself";
               VIEW += "\nsurrounded by rolling green hills. You are standing the middle";
               VIEW += "\nof a pristine, blossoming, flowering meadow. The rolling hills";
               VIEW += "\nof this expanse are thickly covered with tall, lush blades of";
               VIEW += "\ndew-covered grass that sway in the gentle breeze.\n";
               VIEW += "\nThe flowers and grass captivate you with their sweet fragrance";
               VIEW += "\nas the wind blows through your mane.Back eastward, you see a";
               VIEW += "\nwinding dirt road.\n";
               VIEW += "\nYou are strangely filled with a calm, glowing happiness as you"; 
               VIEW += "\nstand in this location. Positive feelings begin to well up";
               VIEW += "\nwithin you, creating an intense feeling of contentment and a";
               VIEW += "\ndeep sensation of inner peace.";

               VIEW += "\n\nNavigation options:\n";
               VIEW += "\nNORTH: You see a ring of hills covered in tall, dark green";
               VIEW += "\ngrass. You imagine it would taste delightful.\n";
               VIEW += "\nSOUTH: You spy a meadow full of colorful wildflowers. Amidst";
               VIEW += "\nthe spread, butterflies flutter freely.\n";
               VIEW += "\nEAST: You see a placid, blue, beautiful and pristine lake.\n";
               VIEW += "\nWEST: A ring lf small river rocks encircles a group of tall ";
               VIEW += "\nreeds and cattails.\n";
               VIEW += "\nX: EXIT the Hills of Happiness and return to South_2.\n";
               VIEW += "\nUse the Navigation buttons to travel in your chosen direction.\n";                

               self.Text_Write(VIEW);    


    #Function-------------------------------------------------------------------------------------------------------------------
      def Slime_Mold_Encounter(self):
          print("In Slime_Mold_Encounter.");
          if(self.L1_N3_Slime_Mold_Page_Counter == 1):
             self.All_Nav_Buttons_DISABLE();
             MESSAGE = "\n You try to proceed further north but cannot.";
             MESSAGE += "\n A ravenous, agressive slimemold blocks your path.";
             MESSAGE += "\n It moves menancingly towards you.";
             MESSAGE += "\n\n Teach this unruly slimemold a lesson through combat?";
             MESSAGE += "\n Or will you walk away? (Y/N)";
             MESSAGE += "\n\n Enter your decision below.";
             self.Text_Write(MESSAGE);

          if(self.L1_N3_Slime_Mold_Page_Counter == 2):
             CHOICE = ((self.ENT_Main_Input.get()).lower())[0];
             if(CHOICE == "y"):
                self.Plyr_Opponent = ANTAGONIST();
                self.Plyr_Opponent.EntityClass = "Antagonist";
                self.Plyr_Opponent.EntityName = "Reincarnated Slime";
                self.Plyr_Opponent.EntityHealth  = 10000;
                self.Plyr_Opponent.EntityDefense  = 5000;
                self.Plyr_Opponent.EntityAttack  = 8000;
                self.Plyr_Opponent.EntityCombatExp = 8500;
                self.Plyr_Opponent.EntityLevel = 10;
                self.COMBAT_LOCATION = self.LOCATION;
                self.LOCATION = self.COMBAT_SEQUENCE;
                #self.SwitchBoard(); #Note: Don't call SwitchBoard() for combat sequences!
                self.L1_N3_Slime_Mold_Page_Counter = 3;

             elif(CHOICE == "n"):
                  self.L1_N3_Slime_Mold_Page_Counter = 3;
                  self.All_Nav_Buttons_ENABLE();
             elif(CHOICE != "#" and CHOICE != "y" and CHOICE != "n"): 
                   self.Text_Write("\n Your CHOICE is invalid!");
                   self.L1_N3_Slime_Mold_Page_Counter -= 2;

          if(self.L1_N3_Slime_Mold_Page_Counter == 3):
             self.Text_Append("\n Exiting combat sequence event.\n Returning to N3.");

          if(self.L1_N3_Slime_Mold_Page_Counter == 4): 
             self.L1_N3_Slime_Mold_Page_Counter = 0;   
             self.LOCATION = self.L1_N3;
             self.CHOICE = "#";
             self.SwitchBoard();           

          #Advance to next page
          self.Text_Append("\n Click \"GO\" to continue."); 
          self.L1_N3_Slime_Mold_Page_Counter += 1;
    #-------------------------------------------------------------------------------------------------------------------------       


    #Function-------------------------------------------------------------------------------------------------------------------
      def Harpy_Encounter(self):
          print("In Harpy_Encounter.");
          if(self.L1_MountainOfMeanness_Harpy_Page_Counter == 1):
             self.All_Nav_Buttons_DISABLE();
             MESSAGE = "\n Your attempt to trek further north is impeded.";
             MESSAGE += "\n A horrible horse eating harpy descends from";
             MESSAGE += "\n the dismal gray clouds above you and hovers";
             MESSAGE += "\n screeching with menace in front of you.";
             MESSAGE += "\n\n Do you choose to tussle with this opponent?";
             MESSAGE += "\n Or will you run away? (Y/N)";
             MESSAGE += "\n\n Enter your decision below.";
             self.Text_Write(MESSAGE);

          if(self.L1_MountainOfMeanness_Harpy_Page_Counter == 2):
             CHOICE = ((self.ENT_Main_Input.get()).lower())[0];
             if(CHOICE == "y"):
                self.Plyr_Opponent = ANTAGONIST();
                self.Plyr_Opponent.EntityClass = "Antagonist";
                self.Plyr_Opponent.EntityName = "Horrible Harpy";
                self.Plyr_Opponent.EntityHealth  = 2000;
                self.Plyr_Opponent.EntityDefense  = 1000;
                self.Plyr_Opponent.EntityAttack  = 1000;
                self.Plyr_Opponent.EntityCombatExp = 2500;
                self.Plyr_Opponent.EntityLevel = 9;
                self.COMBAT_LOCATION = self.LOCATION;
                self.LOCATION = self.COMBAT_SEQUENCE;
                #self.SwitchBoard(); #Note: Don't call SwitchBoard() for combat sequences!
                self.L1_MountainOfMeanness_Harpy_Page_Counter = 3;

             elif(CHOICE == "n"):
                  self.L1_MountainOfMeanness_Harpy_Page_Counter = 3;
                  self.All_Nav_Buttons_ENABLE();
             elif(CHOICE != "#" and CHOICE != "y" and CHOICE != "n"): 
                   self.Text_Write("\n Your CHOICE is invalid!");
                   self.L1_MountainOfMeanness_Harpy_Page_Counter -= 2;

          if(self.L1_MountainOfMeanness_Harpy_Page_Counter == 3):
             self.Text_Append("\n Exiting combat sequence event.\n Returning to Mountain of Meanness.");

          if(self.L1_MountainOfMeanness_Harpy_Page_Counter == 4): 
             self.L1_MountainOfMeanness_Harpy_Page_Counter = 0;   
             self.LOCATION = self.L1_MOUNTAINOFMEANNESS;
             self.CHOICE = "#";
             self.SwitchBoard();           

          #Advance to next page
          self.Text_Append("\n Click \"GO\" to continue."); 
          self.L1_MountainOfMeanness_Harpy_Page_Counter += 1;


    #Function-------------------------------------------------------------------------------------------------------------------
      def Dolphin_Encounter(self):
          print("In Dolphin_Encounter.");
          if(self.L1_SwampOfSadness_Dolphin_Page_Counter == 1):
             self.All_Nav_Buttons_DISABLE();
             MESSAGE = "\n Splashing around in the brackish, sludgy swamp";
             MESSAGE += "\n water, you see a drearily depressed dolphin.";
             MESSAGE += "\n She swims up to you, crying out in pain.";
             MESSAGE += "\n What is wrong with this dolphin?";
             MESSAGE += "\n\n Will you tangle with this terror?";
             MESSAGE += "\n Or will you run away? (Y/N)";
             MESSAGE += "\n\n Enter your decision below.";
             self.Text_Write(MESSAGE);

          if(self.L1_SwampOfSadness_Dolphin_Page_Counter == 2):
             CHOICE = ((self.ENT_Main_Input.get()).lower())[0];
             if(CHOICE == "y"):
                self.Plyr_Opponent = ANTAGONIST();
                self.Plyr_Opponent.EntityClass = "Antagonist";
                self.Plyr_Opponent.EntityName = "Depressed Dolphin";
                self.Plyr_Opponent.EntityHealth  = 1500;
                self.Plyr_Opponent.EntityDefense  = 2000;
                self.Plyr_Opponent.EntityAttack  = 1800;
                self.Plyr_Opponent.EntityCombatExp = 3800;
                self.Plyr_Opponent.EntityLevel = 7;
                self.COMBAT_LOCATION = self.LOCATION;
                self.LOCATION = self.COMBAT_SEQUENCE;
                #self.SwitchBoard(); #Note: Don't call SwitchBoard() for combat sequences!
                self.L1_SwampOfSadness_Dolphin_Page_Counter = 3;

             elif(CHOICE == "n"):
                  self.L1_SwampOfSadness_Dolphin_Page_Counter = 3;
                  self.All_Nav_Buttons_ENABLE();
             elif(CHOICE != "#" and CHOICE != "y" and CHOICE != "n"): 
                   self.Text_Write("\n Your CHOICE is invalid!");
                   self.L1_SwampOfSadness_Dolphin_Page_Counter -= 2;

          if(self.L1_SwampOfSadness_Dolphin_Page_Counter == 3):
             self.Text_Append("\n Exiting combat sequence event.\n Returning to Swamps of Sadness.");

          if(self.L1_SwampOfSadness_Dolphin_Page_Counter == 4): 
             self.L1_SwampOfSadness_Dolphin_Page_Counter = 0;   
             self.LOCATION = self.L1_SWAMPOFSADNESS;
             self.CHOICE = "#";
             self.SwitchBoard();           

          #Advance to next page
          self.Text_Append("\n Click \"GO\" to continue."); 
          self.L1_SwampOfSadness_Dolphin_Page_Counter += 1;          


    #Function-------------------------------------------------------------------------------------------------------------------
      def Discord_Boss_Encounter(self):
          print("In Discord_Boss_Encounter(.");                    
          if(self.L1_DiscordsLair_Discord_Boss_Page_Counter == 1):
             self.All_Nav_Buttons_DISABLE();
             MESSAGE = "\n In this dark and musty cave, you see ";
             MESSAGE += "\n an old, familiar malice. A serpentine";
             MESSAGE += "\n apparition levitates before you, laughing";
             MESSAGE += "\n maniacally and uncontrollably.";
             MESSAGE += "\n\n Do you DARE to dance with DISCORD?";
             MESSAGE += "\n Or will you run, fast as you can? (Y/N)";
             MESSAGE += "\n\n Enter your decision below.";
             self.Text_Write(MESSAGE);

          if(self.L1_DiscordsLair_Discord_Boss_Page_Counter == 2):
             CHOICE = ((self.ENT_Main_Input.get()).lower())[0];
             if(CHOICE == "y"):
                self.Plyr_Opponent = ANTAGONIST();
                self.Plyr_Opponent.EntityClass = "Antagonist";
                self.Plyr_Opponent.EntityName = "Discord: Chaos Agent";
                self.Plyr_Opponent.EntityHealth  = 15000;
                self.Plyr_Opponent.EntityDefense  = 5000;
                self.Plyr_Opponent.EntityAttack  = 5000;
                self.Plyr_Opponent.EntityCombatExp = 7000;
                self.Plyr_Opponent.EntityLevel = 25;
                self.COMBAT_LOCATION = self.LOCATION;
                self.LOCATION = self.COMBAT_SEQUENCE;
                #self.SwitchBoard(); #Note: Don't call SwitchBoard() for combat sequences!
                self.L1_DiscordsLair_Discord_Boss_Page_Counter = 3;

             elif(CHOICE == "n"):
                  self.L1_DiscordsLair_Discord_Boss_Page_Counter = 3;
                  self.All_Nav_Buttons_ENABLE();
             elif(CHOICE != "#" and CHOICE != "y" and CHOICE != "n"): 
                   self.Text_Write("\n Your CHOICE is invalid!");
                   self.L1_DiscordsLair_Discord_Boss_Page_Counter -= 2;

          if(self.L1_DiscordsLair_Discord_Boss_Page_Counter == 3):
             self.Text_Append("\n Exiting combat sequence event.\n Returning to Discord's Lair.");

          if(self.L1_DiscordsLair_Discord_Boss_Page_Counter == 4): 
             self.L1_DiscordsLair_Discord_Boss_Page_Counter = 0;   
             self.LOCATION = self.L1_DISCORDSLAIR;
             self.CHOICE = "#";
             self.SwitchBoard();           

          #Advance to next page
          self.Text_Append("\n Click \"GO\" to continue."); 
          self.L1_DiscordsLair_Discord_Boss_Page_Counter += 1; 


    #Function-------------------------------------------------------------------------------------------------------------------
      def Multiple_Opponents_Encounter(self):
          print("In L1_Multiple_Opponents_Encounter.");                    
          if(self.L1_Multiple_Opponents_Encounter_Page_Counter == 1):
             self.All_Nav_Buttons_DISABLE();
             MESSAGE = "You see a group of 3 rebellious, punky looking";
             MESSAGE += "\nteenage dragons. They don't look very strong";
             MESSAGE += "\nor committed to any kind of goal. They are";
             MESSAGE += "\nstanding beneath a lamp-post in a semi-circle.";
             MESSAGE += "\n\nTwo are giving you the side-eye. The 3rd";
             MESSAGE += "\nrolls their eyes at you. All three tell you";
             MESSAGE += "\nto go away.";
             MESSAGE += "\n\n Do you DARE tangle with THREE punky teen";
             MESSAGE += "\ndragons dressed in 80's clothing all at once?";
             MESSAGE += "\n\n(Y/N) Enter your decision below.";
             self.Text_Write(MESSAGE);

          if(self.L1_Multiple_Opponents_Encounter_Page_Counter == 2):
             CHOICE = ((self.ENT_Main_Input.get()).lower())[0];
             if(CHOICE == "y"):
                #1. Build 3 Dragons
                DRAGON1 = ANTAGONIST();
                DRAGON1.EntityClass = "Dragon";
                DRAGON1.EntityName = "Curly";
                DRAGON1.EntityHealth  = 100;
                DRAGON1.EntityDefense  = 20;
                DRAGON1.EntityAttack  = 20;
                DRAGON1.EntityCombatExp = 5;
                DRAGON1.EntityLevel = 1; 

                DRAGON2 = ANTAGONIST();
                DRAGON2.EntityClass = "Dragon";
                DRAGON2.EntityName = "Larry";
                DRAGON2.EntityHealth  = 100;
                DRAGON2.EntityDefense  = 20;
                DRAGON2.EntityAttack  = 20;
                DRAGON2.EntityCombatExp = 5;
                DRAGON2.EntityLevel = 1; 

                DRAGON3 = ANTAGONIST();
                DRAGON3.EntityClass = "Dragon";
                DRAGON3.EntityName = "Moe";
                DRAGON3.EntityHealth  = 100;
                DRAGON3.EntityDefense  = 20;
                DRAGON3.EntityAttack  = 20;
                DRAGON3.EntityCombatExp = 5;
                DRAGON3.EntityLevel = 1;              

                #2. Add the Dragons to an array
                self.Opponent_Group.append(DRAGON1);
                self.Opponent_Group.append(DRAGON2);
                self.Opponent_Group.append(DRAGON3);

                self.COMBAT_LOCATION = self.LOCATION;         
                self.L1_Multiple_Opponents_LOCK = True;
                self.LOCATION = self.COMBAT_SEQUENCE_MULTIPLE;
                #self.SwitchBoard(); #Note: Don't call SwitchBoard() for combat sequences!
                self.L1_Multiple_Opponents_Encounter_Page_Counter = 3;

             elif(CHOICE == "n"):
                  self.L1_Multiple_Opponents_Encounter_Page_Counter = 3;
                  self.All_Nav_Buttons_ENABLE();
             elif(CHOICE != "#" and CHOICE != "y" and CHOICE != "n"): 
                   self.Text_Write("\n Your CHOICE is invalid!");
                   self.L1_Multiple_Opponents_Encounter_Page_Counter -= 2;

          if(self.L1_Multiple_Opponents_Encounter_Page_Counter == 3):
             self.Text_Append("\n Exiting combat sequence event.\n Returning to Pegasus Citadel.");

          if(self.L1_Multiple_Opponents_Encounter_Page_Counter == 4): 
             self.L1_Multiple_Opponents_Encounter_Page_Counter = 0;   
             self.LOCATION = self.L1_PEGASUSCITADEL;
             self.CHOICE = "#";
             self.SwitchBoard();           

          #Advance to next page
          self.Text_Append("\n Click \"GO\" to continue."); 
          self.L1_Multiple_Opponents_Encounter_Page_Counter += 1; 


    #---Function-----------------------------------------------------------------------------------------------------
      def Get_Player_Input(self):
          Player_Input_Win = tk.Toplevel(window);
          Player_Input_Win.configure(bg='black'); 
          Player_Input_Win.title("Player Input Window");
          Name_Window_Width = 395;
          Name_Window_Height = 100;
          ScreenWidth = Player_Input_Win.winfo_screenwidth();
          ScreenHeight = Player_Input_Win.winfo_screenheight();
          Appear_in_the_Middle = '%dx%d+%d+%d' % (Name_Window_Width, Name_Window_Height, (ScreenWidth - Name_Window_Width) / 2,(ScreenHeight - Name_Window_Height) / 2);
          Player_Input_Win.geometry(Appear_in_the_Middle);
          Player_Input_Win.resizable(width=False, height=False);

          def SUBMIT_Button_Handler():
              self.Player_Input = Input_Entry.get();
              Player_Input_Win.destroy();        

          MESSAGE = "Input what you'd like to say in the box below.";
          LAB_NAM = tk.Label(master=Player_Input_Win, text=MESSAGE, font=('Helvetica 10'), bg='black', fg='white', justify="center");
          LAB_NAM.place(width=375,height=15,x=10,y=8);

          Input_Entry = tk.Entry(master=Player_Input_Win, text="Input text here", font=("Comic Sans MS", 11), justify="center", fg="white", bg="black");
          Input_Entry.place(width=375,height=25,x=10,y=30);
          Input_Entry.focus();

          BTN_SUBMIT = tk.Button(Player_Input_Win, width=15, height=5, font=('Helvetica 11'), text="SUBMIT", bg='blue', fg="white", command=SUBMIT_Button_Handler);
          BTN_SUBMIT.place(anchor="nw", height=25, width=90, x=155, y=65);  
          
          self.Retrieved_Player_Input = True;
          self.CHOICE = "c";
          self.Text_Append("\nEnter \"C\" and click \"GO\"to continue.\n");

          


    #---Function-----------------------------------------------------------------------------------------------------
      def NPC_1_Encounter(self):
          print("\nIn L1_NPC_1_Encounter now.");
          #self.IMG_MAP_L1_HILLSOFHAPPINESS = self.IMG_MAP_L1_HILLSOFHAPPINESS.resize((485,378), Image.ANTIALIAS);                       
          #self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_HILLSOFHAPPINESS);
          #self.LAB_Current_View.configure(image=self.IMG_Current_View);    

          #self.Sound_Na_Na_Na_Thread();      

          if(self.CHOICE == "s"):  
             self.Text_Write("NPC1 speaking.\n"); 
             self.NPC_1.Speak();
             self.Text_Append("\nClick \"GO\"to continue.\n");

          #Note: Have to Completely finish processing from input child window and destroy() call BEFORE using value. Hence paging.
          elif(self.CHOICE == "c"):  
               if(self.Retrieved_Player_Input == False): 
                  self.Text_Write("NPC1 conversating.\n"); 
                  self.Get_Player_Input();
               elif(self.Retrieved_Player_Input == True):
                    #self.Text_Append("Value of Player_Input: " + self.Player_Input);
                    self.NPC_1.Conversate(self.Player_Input);
                    self.Retrieved_Player_Input = False;
                    self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "x"):   
               self.LOCATION = self.L1_CELESTIASPALACE;
               self.CHOICE = "#";
               self.SwitchBoard();                                           

          else: 
               VIEW = "LOCATION: L1_NPC_1_Encounter\n";
               VIEW += "\nWalking towards the west end of";
               VIEW += "\nthe palace Great Room, you see a large, rainbow-colored";
               VIEW += "\nmechanical owl perched on polished, golden pedestal.";
               VIEW += "\nThe owl slowly turns its head 180 degrees and opens its";
               VIEW += "\nover-sized eyes. Staring at you and blinking with";
               VIEW += "\nartificially precise timeing. It whirs and clicks.";

               VIEW += "\n\nOptions:\n";
               VIEW += "\nS: SPEAK with " + self.NPC_1.EntityName + ".";
               VIEW += "\nC: CONVERSATE with " + self.NPC_1.EntityName + ".";
               VIEW += "\nX: EXIT back to Celestia's Palace throne room.\n";
               VIEW += "\nChoose an option above and click \"GO\".\n";                

               self.Text_Write(VIEW);    



    #---Function-----------------------------------------------------------------------------------------------------
      def NPC_2_Encounter(self):
          print("\nIn L1_NPC_2_Encounter now.");
          #self.IMG_MAP_L1_HILLSOFHAPPINESS = self.IMG_MAP_L1_HILLSOFHAPPINESS.resize((485,378), Image.ANTIALIAS);                       
          #self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_HILLSOFHAPPINESS);
          #self.LAB_Current_View.configure(image=self.IMG_Current_View);    

          #self.Sound_Na_Na_Na_Thread();      

          if(self.CHOICE == "s"):  
             self.Text_Write("NPC2 speaking.\n"); 
             self.NPC_1.Speak();
             self.Text_Append("\nClick \"GO\"to continue.\n");

          #Note: Have to Completely finish processing from input child window and destroy() call BEFORE using value. Hence paging.
          elif(self.CHOICE == "c"):  
               if(self.Retrieved_Player_Input == False): 
                  self.Text_Write("NPC2 conversating.\n"); 
                  self.Get_Player_Input();
               elif(self.Retrieved_Player_Input == True):
                    #self.Text_Append("Value of Player_Input: " + self.Player_Input);
                    self.NPC_2.Conversate(self.Player_Input);
                    self.Retrieved_Player_Input = False;
                    self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "x"):   
               self.LOCATION = self.L1_CELESTIASPALACE;
               self.CHOICE = "#";
               self.SwitchBoard();                                           

          else: 
               VIEW = "LOCATION: L1_NPC_2_Encounter\n";
               VIEW += "\nYou see the dolphin you freed from chains of";
               VIEW += "\ndepressing darkness. Liberated from her heavy";
               VIEW += "\nburdens, she swims and frolicks happily in the";
               VIEW += "\nbrackish waters. In spite of the joy of her";
               VIEW += "\nliberation, you can wade no further east from";
               VIEW += "\nin this direction. The waters are too deep.";
               VIEW += "\nPerhaps - if you had a boat? She swims near to";
               VIEW += "\nwhere you are standing singing a dolphin song.";

               VIEW += "\n\nOptions:\n";
               VIEW += "\nS: SPEAK with " + self.NPC_2.EntityName + ".";
               VIEW += "\nC: CONVERSATE with " + self.NPC_2.EntityName + ".";
               VIEW += "\nX: EXIT back to Celestia's Palace throne room.\n";
               VIEW += "\nChoose an option above and click \"GO\".\n";                

               self.Text_Write(VIEW);   
      

          #---Function-----------------------------------------------------------------------------------------------------
      def NPC_3_Encounter(self):
          print("\nIn L1_NPC_3_Encounter now.");
          #self.IMG_MAP_L1_HILLSOFHAPPINESS = self.IMG_MAP_L1_HILLSOFHAPPINESS.resize((485,378), Image.ANTIALIAS);                       
          #self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_MAP_L1_HILLSOFHAPPINESS);
          #self.LAB_Current_View.configure(image=self.IMG_Current_View);    

          #self.Sound_Na_Na_Na_Thread();      

          if(self.CHOICE == "s"):  
             self.Text_Write("NPC3 speaking.\n"); 
             self.NPC_1.Speak();
             self.Text_Append("\nClick \"GO\"to continue.\n");

          #Note: Have to Completely finish processing from input child window and destroy() call BEFORE using value. Hence paging.
          elif(self.CHOICE == "c"):  
               if(self.Retrieved_Player_Input == False): 
                  self.Text_Write("NPC3 conversating.\n"); 
                  self.Get_Player_Input();
               elif(self.Retrieved_Player_Input == True):
                    #self.Text_Append("Value of Player_Input: " + self.Player_Input);
                    self.NPC_3.Conversate(self.Player_Input);
                    self.Retrieved_Player_Input = False;
                    self.Text_Append("\nClick \"GO\"to continue.\n");

          elif(self.CHOICE == "x"):   
               self.LOCATION = self.L1_CELESTIASPALACE;
               self.CHOICE = "#";
               self.SwitchBoard();                                           

          else: 
               VIEW = "LOCATION: L1_NPC_3_Encounter\n";
               VIEW += "\nL1_FRIENDSHIPFOREST-East: You walk into the midst of dozens";
               VIEW += "\nof happy, hopping, scurrying, twittering squirrels, birds,";
               VIEW += "\nbunnies, foxes, feral kitties, does with their fawns,";
               VIEW += "\nracoons, possums, skunks and field mice. You ask them";
               VIEW += "\nwhat do they call this place in which you now find";
               VIEW += "\nyourself. Hoping for an answer, you wait for their reply.";
               VIEW += "\nBut they don't give you one. Why are they so silent?\n";
               VIEW += "\nWhy can't these animals talk like other animals you have";
               VIEW += "\nmet before?\n";
               VIEW += "\nAfraid of getting lost, you decide not to travel any";
               VIEW += "\nfurther east. However, turning around, you notice a";
               VIEW += "\nstrange a tall, middle-aged mare standing in a clump";
               VIEW += "\nof trees beside the path from which you originally came.";

               VIEW += "\n\nOptions:\n";
               VIEW += "\nS: SPEAK with " + self.NPC_3.EntityName + ".";
               VIEW += "\nC: CONVERSATE with " + self.NPC_3.EntityName + ".";
               VIEW += "\nX: EXIT back to Celestia's Palace throne room.\n";
               VIEW += "\nChoose an option above and click \"GO\".\n";                

               self.Text_Write(VIEW);   
      


    #Function-------------------------------------------------------------------------------------------------------------------
      def Display_Combat_Stats(self,Player_Heroine,Player_Opponent):
          MESSAGE = "--------------Heroine Combat Stats--------------";
          MESSAGE += "\nName: " + Player_Heroine.EntityName;
          MESSAGE += "\nHealth: " + str(Player_Heroine.EntityHealth);
          MESSAGE += "\nAttack: " + str(Player_Heroine.EntityAttack);
          MESSAGE += "\nDefense: " + str(Player_Heroine.EntityDefense);
          MESSAGE += "\nMagicPower: " + str(Player_Heroine.EntityMagicPower);
          MESSAGE += "\nClass: " + Player_Heroine.EntityClass;
          MESSAGE += "\n\n--------------Opponent Combat Stats--------------";
          MESSAGE += "\nName: " + Player_Opponent.EntityName;
          MESSAGE += "\nHealth: " + str(Player_Opponent.EntityHealth);
          MESSAGE += "\nAttack: " + str(Player_Opponent.EntityAttack);
          MESSAGE += "\nDefense: " + str(Player_Opponent.EntityDefense);
          MESSAGE += "\nMagicPower: " + str(Player_Opponent.EntityMagicPower);
          MESSAGE += "\nClass: " + Player_Opponent.EntityClass;
          self.Text_Write(MESSAGE);
    #-------------------------------------------------------------------------------------------------------------------------       


    #---Function-----------------------------------------------------------------------------------------------------
      def Pony_Combat(self):
          print("\nInside Pony_Combat.");

          if(self.Combat_Attack_Sequence_Page == 1):
             #1.Display names of instantiated class objects engaging in combat using pointers to globals
             MESSAGE = "\nMagic Battle!!!\n" + self.Plyr_Opponent.EntityName + " vs. " + self.Plyr_Heroine.EntityName + " !";
             GUI.Text_Write(MESSAGE);

             #2.Determine by random LUCK who gets 1st attack in sequence
             MESSAGE = "\nFlipping a coin for who gets first attack.\n(HEADS = Heroine. TAILS = Antagonist.)";
             BlindChance = random.randint(1,2);

             if(BlindChance == 1):
                self.CurrentPlayer = "Heroine"; 
                MESSAGE += "\n\nResult = Heads!\n\nWhat GOOD LUCK!\nHeroine gets 1st attack!";
             elif(BlindChance == 2):
                  self.CurrentPlayer = "Antagonist";
                  MESSAGE += "\n\nResult = Tails!\n\nSuch BAD luck.\nOpponent gets 1st attack!"; 
             else: MESSAGE += "\nERROR. This should never happen.";  
             
             #GUI.Dramatic_Pause_Append(2,MESSAGE);
             self.Text_Append(MESSAGE);

          if(self.Combat_Attack_Sequence_Page == 2):             
             #3.Begin iterating through combat sequence. If either player's health = 0, combat is over.          
             GUI.Text_Write(""); 
             self.Display_Combat_Stats(self.Plyr_Heroine,self.Plyr_Opponent); 

          if(self.Combat_Attack_Sequence_Page == 3):
             #Hold Player and Opponent here until we have a winner
             self.Combat_Attack_Sequence_Page -= 1;
             #Prevent combat sequence from occuring if either Heroine or Antagonist is dead
             if(self.Plyr_Opponent.EntityHealth > 0 and self.Plyr_Heroine.EntityHealth > 0 and GUI.Willing_to_Fight == "TRUE"):    
                GUI.Text_Write("\nCombat sequence. Round # " + str(self.CombatRoundCounter) + "."); 
                self.CombatRoundCounter += 1;
                if(self.CurrentPlayer == "Heroine"):
                   GUI.Text_Append(self.Plyr_Heroine.EntityName + " attacks " + self.Plyr_Opponent.EntityName + "!");
                   self.Plyr_Heroine.Attack(self.Plyr_Opponent);
                   self.CurrentPlayer = "Antagonist";
                elif(self.CurrentPlayer == "Antagonist"):
                   GUI.Text_Append(self.Plyr_Opponent.EntityName + " attacks " + self.Plyr_Heroine.EntityName + "!");
                   self.Plyr_Opponent.Attack(self.Plyr_Heroine);
                   self.Plyr_Heroine.Display_Entity();
                   self.CurrentPlayer = "Heroine"; 

             #We have a winner and a loser
             if(self.Plyr_Opponent.EntityHealth <= 0 or self.Plyr_Heroine.EntityHealth <= 0): 
                #Advance to next page in dialog
                self.Combat_Attack_Sequence_Page += 1;
                #Heroine wins and Opponent loses combat
                if(self.Plyr_Opponent.EntityHealth <= 0 and self.Plyr_Heroine.EntityHealth > 0):
                   GUI.Text_Append("\n" + self.Plyr_Heroine.EntityName + " defeats " + self.Plyr_Opponent.EntityName + "!");

                #Opponent wins and Heroine loses combat - GAME OVER!
                elif(self.Plyr_Heroine.EntityHealth <= 0 and self.Plyr_Opponent.EntityHealth > 0): 
                     GUI.Text_Append("\n" + self.Plyr_Opponent.EntityName + " defeats " + self.Plyr_Heroine.EntityName + "!\n\nGAME OVER.");

                #Heroine and Opponent both annihilate each other = GAME also OVER!
                elif(self.Plyr_Heroine.EntityHealth <= 0 and self.Plyr_Opponent.EntityHealth <= 0):
                     GUI.Text_Append("\nEveryone dies! Player and Opponent annihilate each other. Game Over.");     

          if(self.Combat_Attack_Sequence_Page == 4):
             GUI.Text_Append("\nExiting combat this sequence.");  
             #We have a winner and a loser
             if(self.Plyr_Opponent.EntityHealth <= 0 or self.Plyr_Heroine.EntityHealth <= 0):                
                #Heroine wins and Opponent loses combat - Reset values for next round of combat and put player back at last map location 
                if(self.Plyr_Opponent.EntityHealth <= 0 and self.Plyr_Heroine.EntityHealth > 0):
                   #Reset values for next round of combat and put player back at last map location 
                   self.CurrentPlayer = "Nobody"; 
                   self.LOCATION = self.COMBAT_LOCATION;
                   self.CombatRoundCounter = 1;  
                   self.Combat_Attack_Sequence_Page = 0;
                   self.All_Nav_Buttons_ENABLE();

                   if(self.COMBAT_LOCATION == self.L1_N3_Slime_Mold_Encounter): 
                      self.L1_N3_Slime_Mold_Alive = False;
                   if(self.COMBAT_LOCATION == self.L1_MountainOfMeanness_Harpy_Encounter): 
                      self.L1_MountainOfMeanness_Harpy_Alive = False;
                   if(self.COMBAT_LOCATION == self.L1_SwampOfSadness_Dolphin_Encounter): 
                      self.L1_SwampOfSadness_Dolphin_Alive = False;
                   if(self.COMBAT_LOCATION == self.L1_DiscordsLair_Discord_Boss_Alive): 
                      self.L1_DiscordsLair_Discord_Boss_Alive = False;          

                #Opponent wins and Heroine loses combat - GAME OVER!
                elif(self.Plyr_Heroine.EntityHealth <= 0 and self.Plyr_Opponent.EntityHealth > 0): 
                     self.LOCATION = self.GAME_OVER;

                #Heroine and Opponent both annihilate each other = GAME also OVER!
                elif(self.Plyr_Heroine.EntityHealth <= 0 and self.Plyr_Opponent.EntityHealth <= 0):
                     self.LOCATION = self.GAME_OVER;
             
             #Toggle Multiple Combat back on if Player fighting multiple opponents
             if(self.L1_Multiple_Opponents_LOCK == True and self.L1_Multiple_Opponents_ACTIVE == False):
                self.L1_Multiple_Opponents_ACTIVE = True;
                self.LOCATION = self.COMBAT_SEQUENCE_MULTIPLE;

          self.Text_Append("\nClick \"GO\" to continue.");
          self.Combat_Attack_Sequence_Page += 1;


    #---Function-----------------------------------------------------------------------------------------------------
      def Pony_Combat_Multiple(self):
          print("\nInside Pony_Combat_Multiple.");
          
          #EXAMPLE of Console CODE: Could Iterate through Array of Antagonists so Player can combat multiple opponents
          #for X in range(len(self.Opponent_Group)):
          #    print("Engaging in group combat with opponent ",(X+1)," of ",len(self.Opponent_Group)," opponents.",sep='');
          #    self.Text_Write("Engaging in group combat with opponent " + str((X+1)) + " of " + str(len(self.Opponent_Group)) + " opponents.");

          #EVENT-based logic with a GUI is DIFFERENT from CONSOLE logic
          Total_Num_Opponents = len(self.Opponent_Group); 

          #ONLY if a multiple combat sequence is currently active.
          if(self.L1_Multiple_Opponents_ACTIVE == True):
             #Make sure you don't index past the last element in the array. A NULL value will crash the game.
             if(self.L1_Multiple_Opponents_Num < Total_Num_Opponents):         
                print("Engaging in group combat with opponent ",(self.L1_Multiple_Opponents_Num+1)," of ",Total_Num_Opponents," opponents.",sep='');
                self.Text_Write("Engaging in group combat with opponent " + str((self.L1_Multiple_Opponents_Num+1)) + " of " + str(Total_Num_Opponents) + " opponents.");
                print("Current Opponent name:",self.Opponent_Group[self.L1_Multiple_Opponents_Num].EntityName,sep='');
                self.Text_Append("Current Opponent name: " + self.Opponent_Group[self.L1_Multiple_Opponents_Num].EntityName);
                self.Plyr_Opponent = self.Opponent_Group[self.L1_Multiple_Opponents_Num];
                self.LOCATION = self.COMBAT_SEQUENCE;
                self.L1_Multiple_Opponents_ACTIVE = False;
                self.L1_Multiple_Opponents_Num += 1;
                self.Text_Append("\nClick \"GO\" to continue.");
             
             else:
                #Make sure all opponents in array have been defeated
                Total_Enemy_Health = 0;   
                 
                for X in range(len(self.Opponent_Group)):
                    self.Text_Append("Opnt Name: " + self.Opponent_Group[X].EntityName + "  Hlth: " + str(self.Opponent_Group[X].EntityHealth));
                    Total_Enemy_Health += self.Opponent_Group[X].EntityHealth;

                if(Total_Enemy_Health <= 0):
                   #Mark map combat event data completed at end of sequence if PLAYER still alive
                   if(self.Plyr_Heroine.EntityHealth > 0):
                      self.L1_Multiple_Opponents_LOCK = False;
                      self.L1_Multiple_Opponents_ACTIVE = True;
                      self.L1_Multiple_Opponents_Num = 0; #reset counter
                      #Empty array so it can be re-populated with new antagonists next time PLAYER fights multiple opponents 
                      self.Opponent_Group.clear();
                      self.Text_Append("\nLooks like after facing multiple opponents?\nPLAYER is still alive! Woohoo!");     
                      #Allow for future multiple combat locations
                      if(self.COMBAT_LOCATION == self.L1_Multiple_Opponents_Encounter): 
                         self.L1_Multiple_Opponents_Encounter_Alive = False;
                         self.LOCATION = self.COMBAT_LOCATION;
                           

    #---Function-----------------------------------------------------------------------------------------------------
      def Game_Over_Man(self):
          self.Text_Write("Game Over. Player has died.");



    #---Function-----------------------------------------------------------------------------------------------------
      def Market_1(self):
          print("\nIn Market_1 (Mountain Market) now.");
          self.IMG_SCENE_L1_MOUNTAINMARKETCABIN_1 = self.IMG_SCENE_L1_MOUNTAINMARKETCABIN_1.resize((485,378), Image.ANTIALIAS);                       
          self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_SCENE_L1_MOUNTAINMARKETCABIN_1);
          self.LAB_Current_View.configure(image=self.IMG_Current_View);

          Cost_GroomingBrush = 10;
          Cost_Slingshot = 20;
          Cost_Slingshot_Pellets = 10;
          Cost_HealingPotion = 50;
          Cost_MagicElixir = 100;
          Cost_MagicMushroom = 120;
          Cost_FairyTorch  = 30;
          Cost_HempRope = 25;
          Cost_ClimbingCleats = 40;
          Cost_NotepadAndPen = 15;        

          if(self.CHOICE == "n"):
               self.IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1 = self.IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1.resize((485,378), Image.ANTIALIAS);                       
               self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1);
               self.LAB_Current_View.configure(image=self.IMG_Current_View);   
               self.Text_Write("MountainMarket-North: You see a shelf against the");
               self.Text_Append("north wall lined with items for sale.");
               self.Text_Append("\nClick \"GO\"to continue.\n");
          elif(self.CHOICE == "s"):
               self.IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1 = self.IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1.resize((485,378), Image.ANTIALIAS);                       
               self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1);
               self.LAB_Current_View.configure(image=self.IMG_Current_View); 
               self.Text_Write("MountainMarket-South: You see racks of clothing");
               self.Text_Append("and boxes with blankest for sale.");
               self.Text_Append("\nClick \"GO\"to continue.\n");
          elif(self.CHOICE == "e"): 
               self.IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1 = self.IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1.resize((485,378), Image.ANTIALIAS);                       
               self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1);
               self.LAB_Current_View.configure(image=self.IMG_Current_View);  
               self.Text_Write("MountainMarket-East: You see the hinged, heavy");
               self.Text_Append("wooden door from which you entered the market.");
               self.Text_Append("\nClick \"GO\"to continue.\n");
          elif(self.CHOICE == "w"):
               self.IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1 = self.IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1.resize((485,378), Image.ANTIALIAS);                       
               self.IMG_Current_View = ImageTk.PhotoImage(self.IMG_SCENE_L1_MOUNTAINMARKETINSIDE_1);
               self.LAB_Current_View.configure(image=self.IMG_Current_View);   
               self.Text_Write("MountainMarket-West: You see a long counter that");
               self.Text_Append("runs all along the shop's western wall.");
               self.Text_Append("\nClick \"GO\"to continue.\n");
          elif(self.CHOICE == "x"):   
               self.Text_Write("Leaving Mountain Market");
               self.LOCATION = self.L1_N3;
               self.CHOICE = "#";
               self.SwitchBoard();              

          #0. Grooming Brush
          elif(self.CHOICE == "0"):
                #Make sure player has enough to buy item 
                if(self.Plyr_Heroine.EntityMoney > Cost_GroomingBrush):
                   #Make sure player doesn't already have item
                   if(self.Plyr_Heroine.INV_Has_Grooming_Brush == "TRUE"):
                      self.Text_Write("You already have a Grooming Brush!");
                      self.Text_Append("Sorry. No room for another."); 
                   else:
                      self.Text_Write("The Grooming Brush costs: $" + str(Cost_GroomingBrush) + ".");
                      self.Text_Append("You have: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                      self.Text_Append("It is enough! You purchase it.");
                      self.Plyr_Heroine.EntityMoney -= Cost_GroomingBrush;
                      self.Text_Append("Your remaining money is now: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                      self.Plyr_Heroine.INV_Has_Grooming_Brush = "TRUE";
                      self.Plyr_Heroine.Display_Entity(); #money
                      self.Plyr_Heroine.Inventory_Display(); #item
                else:   
                   self.Text_Write("Sorry. You do not have enough money.");
                   self.Text_Append("You have only: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Write("But the Grooming Brush costs: $" + str(Cost_GroomingBrush) + ".");

          #1. Slingshot
          elif(self.CHOICE == "1"):
                #Make sure player has enough to buy item 
                if(self.Plyr_Heroine.EntityMoney > Cost_Slingshot):
                   #Make sure player doesn't already have item
                   if(self.Plyr_Heroine.INV_Has_Slingshot == "TRUE"):
                      self.Text_Write("You already have a Slingshot!");
                      self.Text_Append("Sorry. No room for another."); 
                   else:
                      self.Text_Write("The Slingshot costs: $" + str(Cost_Slingshot) + ".");
                      self.Text_Append("You have: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                      self.Text_Append("It is enough! You purchase it.");
                      self.Plyr_Heroine.EntityMoney -= Cost_GroomingBrush;
                      self.Text_Append("Your remaining money is now: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                      self.Plyr_Heroine.INV_Has_Slingshot = "TRUE";
                      self.Plyr_Heroine.Display_Entity(); #money
                      self.Plyr_Heroine.Inventory_Display(); #item
                else:   
                   self.Text_Write("Sorry. You do not have enough money.");
                   self.Text_Append("You have only: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Write("But the Slingshot costs: $" + str(Cost_Slingshot) + ".");

          #2. Slingshot Pellets
          elif(self.CHOICE == "2"):
                #Make sure player has enough to buy item 
                if(self.Plyr_Heroine.EntityMoney > Cost_Slingshot_Pellets):
                   #Player can hold more. Add to current # Slingshot Pellets
                   self.Text_Write("Slingshot Pellets cost: $" + str(Cost_Slingshot_Pellets) + ".");
                   self.Text_Append("You have: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Append("It is enough! You purchase them.");
                   self.Plyr_Heroine.EntityMoney -= Cost_Slingshot_Pellets;
                   self.Text_Append("Your remaining money is now: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Plyr_Heroine.Slingshot_Pellets_Amt += 10;
                   self.Plyr_Heroine.Display_Entity(); #money
                   self.Plyr_Heroine.Inventory_Display(); #item
                else:   
                   self.Text_Write("Sorry. You do not have enough money.");
                   self.Text_Append("You have only: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Write("But Slingshot Pellets cost: $" + str(Cost_Slingshot_Pellets) + ".");

          #3. Healing Potion
          elif(self.CHOICE == "3"):
                #Make sure player has enough to buy item 
                if(self.Plyr_Heroine.EntityMoney > Cost_HealingPotion):
                   #Player can hold more. Add to current # Slingshot Pellets
                   self.Text_Write("A Healing Potion costs: $" + str(Cost_HealingPotion) + ".");
                   self.Text_Append("You have: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Append("It is enough! You purchase it.");
                   self.Plyr_Heroine.EntityMoney -= Cost_HealingPotion;
                   self.Text_Append("Your remaining money is now: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Plyr_Heroine.INV_Has_HealingPotions += 1;
                   self.Plyr_Heroine.Display_Entity(); #money
                   self.Plyr_Heroine.Inventory_Display(); #item
                else:   
                   self.Text_Write("Sorry. You do not have enough money.");
                   self.Text_Append("You have only: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Write("But a Healing Potion costs: $" + str(Cost_HealingPotion) + ".");                  

          #4. Magic Elixir
          elif(self.CHOICE == "4"):
                #Make sure player has enough to buy item 
                if(self.Plyr_Heroine.EntityMoney > Cost_MagicElixir):
                   #Player can hold more. Add to current # Slingshot Pellets
                   self.Text_Write("A Magic Elixir costs: $" + str(Cost_MagicElixir) + ".");
                   self.Text_Append("You have: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Append("It is enough! You purchase it.");
                   self.Text_Append("You drink it down right then and there!");
                   self.Text_Append("The elixir increases your magic power by 30.");
                   self.Plyr_Heroine.EntityMoney -= Cost_MagicElixir;
                   self.Text_Append("Your remaining money is now: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Plyr_Heroine.EntityMagicPower += 30;
                   self.Plyr_Heroine.Display_Entity(); #money
                   self.Plyr_Heroine.Inventory_Display(); #item
                else:   
                   self.Text_Write("Sorry. You do not have enough money.");
                   self.Text_Append("You have only: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Write("But a Magic Elixir costs: $" + str(Cost_MagicElixir) + ".");     

          #5. Magic Mushroom
          elif(self.CHOICE == "5"):
                #Make sure player has enough to buy item 
                if(self.Plyr_Heroine.EntityMoney > Cost_MagicMushroom):
                   #Player can hold more. Add to current # Slingshot Pellets
                   self.Text_Write("A Magic Mushroom costs: $" + str(Cost_MagicMushroom) + ".");
                   self.Text_Append("You have: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Append("It is enough! You purchase it.");
                   self.Text_Append("You devour the delicious fungus on the spot.");
                   self.Text_Append("The mushroom increases your health by 50.");
                   self.Plyr_Heroine.EntityMoney -= Cost_MagicMushroom;
                   self.Text_Append("Your remaining money is now: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Plyr_Heroine.EntityHealth += 50;
                   self.Plyr_Heroine.Display_Entity(); #money
                   self.Plyr_Heroine.Inventory_Display(); #item
                else:   
                   self.Text_Write("Sorry. You do not have enough money.");
                   self.Text_Append("You have only: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Write("But a Magic Mushroom costs: $" + str(Cost_MagicMushroom) + "."); 

          #6. Fairy Torch
          elif(self.CHOICE == "6"):
                #Make sure player has enough to buy item 
                if(self.Plyr_Heroine.EntityMoney > Cost_FairyTorch):
                   #Make sure player doesn't already have item
                   if(self.Plyr_Heroine.INV_Has_FairyTorch == "TRUE"):
                      self.Text_Write("You already have a Fairy Torch!");
                      self.Text_Append("Sorry. No room for another."); 
                   else:
                      self.Text_Write("The Fairy Torch costs: $" + str(Cost_FairyTorch) + ".");
                      self.Text_Append("You have: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                      self.Text_Append("It is enough! You purchase it.");
                      self.Plyr_Heroine.EntityMoney -= Cost_FairyTorch;
                      self.Text_Append("Your remaining money is now: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                      self.Plyr_Heroine.INV_Has_FairyTorch = "TRUE";
                      self.Plyr_Heroine.Display_Entity(); #money
                      self.Plyr_Heroine.Inventory_Display(); #item
                else:   
                   self.Text_Write("Sorry. You do not have enough money.");
                   self.Text_Append("You have only: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Write("But the Fairy Torch costs: $" + str(Cost_FairyTorch) + ".");

          #7. Hemp Rope
          elif(self.CHOICE == "7"):
                #Make sure player has enough to buy item 
                if(self.Plyr_Heroine.EntityMoney > Cost_HempRope):
                   #Make sure player doesn't already have item
                   if(self.Plyr_Heroine.INV_Has_HempRope == "TRUE"):
                      self.Text_Write("You already have a Hemp Rope!");
                      self.Text_Append("Sorry. No room for another."); 
                   else:
                      self.Text_Write("The Hemp Rope costs: $" + str(Cost_HempRope) + ".");
                      self.Text_Append("You have: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                      self.Text_Append("It is enough! You purchase it.");
                      self.Plyr_Heroine.EntityMoney -= Cost_HempRope;
                      self.Text_Append("Your remaining money is now: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                      self.Plyr_Heroine.INV_Has_HempRope = "TRUE";
                      self.Plyr_Heroine.Display_Entity(); #money
                      self.Plyr_Heroine.Inventory_Display(); #item
                else:   
                   self.Text_Write("Sorry. You do not have enough money.");
                   self.Text_Append("You have only: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Write("But the Hemp Rope costs: $" + str(Cost_HempRope) + ".");

          #8. Climbing Cleats
          elif(self.CHOICE == "8"):
                #Make sure player has enough to buy item 
                if(self.Plyr_Heroine.EntityMoney > Cost_ClimbingCleats):
                   #Make sure player doesn't already have item
                   if(self.Plyr_Heroine.INV_Has_ClimbingCleats == "TRUE"):
                      self.Text_Write("You already have Climbing Cleats!");
                      self.Text_Append("Sorry. No room for more."); 
                   else:
                      self.Text_Write("Climbing Cleats costs: $" + str(Cost_ClimbingCleats) + ".");
                      self.Text_Append("You have: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                      self.Text_Append("It is enough! You purchase it.");
                      self.Plyr_Heroine.EntityMoney -= Cost_ClimbingCleats;
                      self.Text_Append("Your remaining money is now: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                      self.Plyr_Heroine.INV_Has_ClimbingCleats = "TRUE";
                      self.Plyr_Heroine.Display_Entity(); #money
                      self.Plyr_Heroine.Inventory_Display(); #item
                else:   
                   self.Text_Write("Sorry. You do not have enough money.");
                   self.Text_Append("You have only: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Write("But Climbing Cleats cost: $" + str(Cost_ClimbingCleats) + ".");

          #9. Notepad & Pen
          elif(self.CHOICE == "9"):
                #Make sure player has enough to buy item 
                if(self.Plyr_Heroine.EntityMoney > Cost_NotepadAndPen):
                   #Make sure player doesn't already have item
                   if(self.Plyr_Heroine.INV_Has_NotepadAndPen == "TRUE"):
                      self.Text_Write("You already have a Notepad & Pen!");
                      self.Text_Append("Sorry. No room for more."); 
                   else:
                      self.Text_Write("A Notepad & Pen costs: $" + str(Cost_NotepadAndPen) + ".");
                      self.Text_Append("You have: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                      self.Text_Append("It is enough! You purchase it.");
                      self.Plyr_Heroine.EntityMoney -= Cost_NotepadAndPen;
                      self.Text_Append("Your remaining money is now: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                      self.Plyr_Heroine.INV_Has_NotepadAndPen = "TRUE";
                      self.Plyr_Heroine.Display_Entity(); #money
                      self.Plyr_Heroine.Inventory_Display(); #item
                else:   
                   self.Text_Write("Sorry. You do not have enough money.");
                   self.Text_Append("You have only: $" + str(self.Plyr_Heroine.EntityMoney) + ".");
                   self.Text_Write("But a Notepad & Pen costs: $" + str(Cost_NotepadAndPen) + ".");
              
          else: 
               VIEW = "LOCATION: MountainMarket\n";
               VIEW += "\nYou find yourself in the magnificently marvelous";
               VIEW += "\nmodern Mountain Market! A handsome looking stallion";
               VIEW += "\nwearing denim overalls looks at you and says:\n";
               VIEW += "\n\"Welcome to Mountain Market! We have lots of";
               VIEW += "\nitems for sale. What would you like to buy?\"\n";

               VIEW += "\nItems for sale:\n";
               VIEW += "\n  0 = Grooming Brush  [$10]";
               VIEW += "\n  1 = Slingshot  [$20]";
               VIEW += "\n  2 = Slingshot Pellets (10)  [$10]";
               VIEW += "\n  3 = Healing Potion (health + 20)  [$50]";
               VIEW += "\n  4 = Magic Elixir (magic power + 30)  [$100]";
               VIEW += "\n  5 = Magic Mushroom (health + 50)  [$120]";
               VIEW += "\n  6 = Fairy Torch  [$30]";
               VIEW += "\n  7 = Hemp Rope  [$25]";
               VIEW += "\n  8 = Climbing Cleats  [$40]";
               VIEW += "\n  9 = Notepad and Pen  [$15]";
               VIEW += "\n\nX: EXIT Mountain Market back to North_3.\n";
               VIEW += "\nEnter # of what you want to buy. Or enter";
               VIEW += "\n\"X\" and click \"GO\" to EXIT the market.";                

               self.Text_Write(VIEW);


    #---Function-----------------------------------------------------------------------------------------------------
      def Reset_Game_State(self):
          #The Basics - Initial State
          self.Plyr_Heroine = None;
          self.Plyr_Opponent = None;
          self.CurrentPlayer = "Nobody";
          self.Opponent_Group.clear();
          self.NPC_1 = None;
          self.NPC_2 = None;
          self.NPC_3 = None;
          self.CHOICE = "";
          self.LOCATION = self.L1_INTRO;      

          #Paging Variables
          self.Create_Character_Page = 1;
          self.Create_NPC_Page = 1;
          self.Combat_Attack_Sequence_Page = 1;
          self.L1_N3_Slime_Mold_Page_Counter = 1;
          self.L1_MountainOfMeanness_Harpy_Page_Counter = 1;
          self.L1_SwampOfSadness_Dolphin_Page_Counter = 1;
          self.L1_DiscordsLair_Discord_Boss_Page_Counter = 1;
          self.L1_Multiple_Opponents_Encounter_Page_Counter = 1;      
      
          #Environment Combat Variables
          self.Willing_to_Fight = "TRUE";
          self.L1_N3_Slime_Mold_Alive = True;
          self.L1_MountainOfMeanness_Harpy_Alive = True;
          self.L1_SwampOfSadness_Dolphin_Alive = True;
          self.L1_DiscordsLair_Discord_Boss_Alive = True;
          self.L1_Multiple_Opponents_Encounter_Alive = True;
          self.L1_Multiple_Opponents_Num = 0;
          self.L1_Multiple_Opponents_LOCK = False;
          self.L1_Multiple_Opponents_ACTIVE = True;
          self.COMBAT_LOCATION = 0;
          self.CombatRoundCounter = 1;

          #Map EVENT Variables
          self.CENTER_FirstTime = True;
          self.CelestiasPalace_FirstTime = True;
          self.DiscordsLair_FirstTime = True;
          self.FriendshipForest_FirstTime = True;      

          #MAP Inventory EVENT Variables
          self.Found_Staff = False;
          self.Found_Pendant = False;
          self.Found_Sigil = False;
          self.Found_Orb = False;
          self.Found_PrincessCloak = False;
          self.Found_Chain_Mail = False;
          self.Found_Plate_Armor = False; 

          #MAP L1 Skill Items Globals
          self.Acquired_IceBlasts = False;
          self.Acquired_FireBalls = False;
          self.Acquired_Lightning = False;
          self.Acquired_Telekinesis = False;
          self.Acquired_Telepathy = False;
          self.Acquired_Teleportation = False;
          self.Acquired_TimeWarp = False;
          self.Acquired_Invisibility = False;
          self.Acquired_Healing = False;
          self.Acquired_FriendshipCast = False;

          #MAP L1 Potions Globals
          self.Found_HealingPotion_1 = False;
          self.Found_HealingPotion_2 = False;
          self.Found_HealingPotion_3 = False;
          self.Found_HealingPotion_4 = False;
          self.Found_HealingPotion_CelestiasPalace = False;

          #MAP L1 NPCs Globals
          self.NPC1_Encountered = False;
          self.NPC2_Encountered = False;
          self.NPC3_Encountered = False;

          #MAP L1 Traps Globals
          self.TRAP1_Encountered = False;
          self.TRAP2_Encountered = False;
          self.TRAP3_Encountered = False;
          self.TRAP4_Encountered = False;

          self.Text_Write("Game has been RESET.\n");
          self.Text_Append("Please click \"GO\" to begin a NEW game.");    


    #---Function-----------------------------------------------------------------------------------------------------
      def Save_Game(self):
          print("\nSaving Game");
          self.Text_Write("Saving Game");

          #1. Get current script directory (needs "import os").
          CurrentDir = os.getcwd();  
          print("\n1. Creating Char and GameState save files in: \"",CurrentDir,"\"",sep='');
          self.Text_Append("\n1. Creating Char and GameState save files in:");
          self.Text_Append(CurrentDir);

          #2. Create game character file based on character's name
          print("\n2. Saving Character Data ...");
          self.Text_Append("\n2. Saving Character Data ...");

          Char_Name = CurrentDir + "\\" + "DD_Character_" + self.Plyr_Heroine.EntityName + ".DDchar";
          print("Complete file name and path is:",Char_Name);
          self.Text_Append("Complete file name and path is:");
          self.Text_Append(Char_Name);
    
          #3. Overwrite existing character file if already exists.
          print("\n3. Overwrite existing char file if exists ...");
          self.Text_Append("\n3. Overwrite existing char file if exists ...");
          CharSaveFile = open(Char_Name, "w");

          #4. Create and populate Array to serialize derived and base class data members
          print("\n4. Serialize all derived and base class data members");
          print("   Create + populate array with each class's data");
          print("   and then write entire array as object to file.");
          self.Text_Append("\n4. Create + populate array with class data members.");
          self.Text_Append("Create + populate array with each class's data");
          self.Text_Append("and then write entire array as object to file.");
          Char_Data = [];
          Char_Data.append( (self.Plyr_Heroine.EntityName + "\n") );
          Char_Data.append( (self.Plyr_Heroine.EntityGender + "\n") ); 
          Char_Data.append( (self.Plyr_Heroine.EntityClass + "\n") ); 
          Char_Data.append( (str(self.Plyr_Heroine.EntityHealth) + "\n") ); 
          Char_Data.append( (str(self.Plyr_Heroine.EntityDefense) + "\n") ); 
          Char_Data.append( (str(self.Plyr_Heroine.EntityAttack) + "\n") ); 
          Char_Data.append( (str(self.Plyr_Heroine.EntityMagicPower) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.EntityDexterity) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.EntityCharisma) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.EntityLevel) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.EntityCombatExp) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.EntityMoney) + "\n") );
          Char_Data.append( (self.Plyr_Heroine.WeaponChoice + "\n") ); 
          Char_Data.append( (self.Plyr_Heroine.MagicChoice + "\n") ); 
          Char_Data.append( (self.Plyr_Heroine.ArmorChoice + "\n") ); 
          Char_Data.append( (self.Plyr_Heroine.Invisibility_Active + "\n") ); 
          Char_Data.append( (str(self.Plyr_Heroine.Invisibility_Count) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Item_Slingshot) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Item_Staff) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Item_Pendant) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Item_Sigil) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Item_Orb) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Item_PrincessCloak) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Skill_IceBlasts) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Skill_FireBalls) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Skill_Lightning) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Skill_Telekinesis) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Skill_Telepathy) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Skill_Teleportation) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Dammage_Skill_TimeWarp) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Invisibility_DEF_Amt) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.DEF_Item_Chain_Mail) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.DEF_Item_Plate_Armor) + "\n") );
          Char_Data.append( (self.Plyr_Heroine.INV_Has_Slingshot + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.Slingshot_Pellets_Amt) + "\n") );
          Char_Data.append( (self.Plyr_Heroine.INV_Has_Staff + "\n") );
          Char_Data.append( (self.Plyr_Heroine.INV_Has_Pendant + "\n") );
          Char_Data.append( (self.Plyr_Heroine.INV_Has_Sigil + "\n") );
          Char_Data.append( (self.Plyr_Heroine.INV_Has_Orb + "\n") );
          Char_Data.append( (self.Plyr_Heroine.INV_Has_PrincessCloak + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.INV_Has_HealingPotions) + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.HealthPotion_Restore_Amt) + "\n") );
          Char_Data.append( (self.Plyr_Heroine.INV_Has_Chain_Mail + "\n") );
          Char_Data.append( (self.Plyr_Heroine.INV_Has_Plate_Armor + "\n") );
          Char_Data.append( (self.Plyr_Heroine.SKILL_Has_IceBlasts + "\n") );
          Char_Data.append( (self.Plyr_Heroine.SKILL_Has_FireBalls + "\n") );
          Char_Data.append( (self.Plyr_Heroine.SKILL_Has_Lightning + "\n") );
          Char_Data.append( (self.Plyr_Heroine.SKILL_Has_Telekinesis + "\n") );
          Char_Data.append( (self.Plyr_Heroine.SKILL_Has_Telepathy + "\n") );
          Char_Data.append( (self.Plyr_Heroine.SKILL_Has_Teleportation + "\n") );
          Char_Data.append( (self.Plyr_Heroine.SKILL_Has_TimeWarp + "\n") );
          Char_Data.append( (self.Plyr_Heroine.SKILL_Has_Invisibility + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.SKILL_Invisibility_Cost) + "\n") );
          Char_Data.append( (self.Plyr_Heroine.SKILL_Has_Healing + "\n") );
          Char_Data.append( (str(self.Plyr_Heroine.SKILL_Healing_Restore_Amt) + "\n") );
          Char_Data.append( (self.Plyr_Heroine.SKILL_Has_FriendshipCast + "\n") );

          #5. Write character data to file using line as a delimiter and close file.
          print("\n5. Write character data to file using line as a delimiter and close file.");
          self.Text_Append("\n5. Write character data to file using line as a");
          self.Text_Append("delimiter. Then close file.");
          CharSaveFile.writelines(Char_Data);
          CharSaveFile.close();

          #6.  Create Game State file. 
          print("\n6. Saving Game State and MAP location Data ...");
          print("\n   Create Game State file.");
          self.Text_Append("\n6. Saving Game State and MAP location Data ...");
          self.Text_Append("Create Game State file.");
          GameState_Name = CurrentDir + "\\" + "DD_GameState_" + self.Plyr_Heroine.EntityName + ".DDgame";
          print("Complete file name and path is:",GameState_Name);
          self.Text_Append("Complete file name and path is:");
          self.Text_Append(GameState_Name);

          #7. Overwrite existing Game State file if already exists.
          print("\n7. Overwrite existing GameState file if exists ...");
          self.Text_Append("\n7. Overwrite existing GameState file if exists ...");
          GameStateSaveFile = open(GameState_Name, "w");

          # 8. Create and populate Array to serialize Game State data
          print("\n8. Serialize all RPG GUI wrapper class data members");
          print("   Create + populate array with class's data");
          print("   and then write entire array as object to file.");
          self.Text_Append("\n8. Serialize all RPG GUI wrapper class data members");
          self.Text_Append("Create + populate array with class's data");
          self.Text_Append("and then write entire array as object to file.");          
          GameState_Data = [];
          GameState_Data.append( (str(self.LOCATION) + "\n") );          
          GameState_Data.append( (str(self.L1_N3_Slime_Mold_Alive) + "\n") );
          GameState_Data.append( (str(self.L1_MountainOfMeanness_Harpy_Alive) + "\n") );
          GameState_Data.append( (str(self.L1_SwampOfSadness_Dolphin_Alive) + "\n") );
          GameState_Data.append( (str(self.L1_DiscordsLair_Discord_Boss_Alive) + "\n") );
          GameState_Data.append( (str(self.L1_Multiple_Opponents_Encounter_Alive) + "\n") );
          GameState_Data.append( (str(self.CENTER_FirstTime) + "\n") );
          GameState_Data.append( (str(self.CelestiasPalace_FirstTime) + "\n") );
          GameState_Data.append( (str(self.DiscordsLair_FirstTime) + "\n") );
          GameState_Data.append( (str(self.FriendshipForest_FirstTime) + "\n") );
          GameState_Data.append( (str(self.Found_Staff) + "\n") );
          GameState_Data.append( (str(self.Found_Pendant) + "\n") );
          GameState_Data.append( (str(self.Found_Sigil) + "\n") );
          GameState_Data.append( (str(self.Found_Orb) + "\n") );
          GameState_Data.append( (str(self.Found_PrincessCloak) + "\n") );
          GameState_Data.append( (str(self.Found_Chain_Mail) + "\n") );
          GameState_Data.append( (str(self.Found_Plate_Armor) + "\n") );
          GameState_Data.append( (str(self.Acquired_IceBlasts) + "\n") );
          GameState_Data.append( (str(self.Acquired_FireBalls) + "\n") );
          GameState_Data.append( (str(self.Acquired_Lightning)  + "\n") );
          GameState_Data.append( (str(self.Acquired_Telekinesis) + "\n") );
          GameState_Data.append( (str(self.Acquired_Telepathy) + "\n") );
          GameState_Data.append( (str(self.Acquired_Teleportation) + "\n") );
          GameState_Data.append( (str(self.Acquired_TimeWarp) + "\n") );
          GameState_Data.append( (str(self.Acquired_Invisibility) + "\n") );    
          GameState_Data.append( (str(self.Acquired_Healing) + "\n") );   
          GameState_Data.append( (str(self.Acquired_FriendshipCast) + "\n") );
          GameState_Data.append( (str(self.Found_HealingPotion_1) + "\n") );
          GameState_Data.append( (str(self.Found_HealingPotion_2) + "\n") );
          GameState_Data.append( (str(self.Found_HealingPotion_3) + "\n") );
          GameState_Data.append( (str(self.Found_HealingPotion_4) + "\n") );
          GameState_Data.append( (str(self.Found_HealingPotion_CelestiasPalace) + "\n") );
          GameState_Data.append( (str(self.NPC1_Encountered) + "\n") );
          GameState_Data.append( (str(self.NPC2_Encountered) + "\n") );
          GameState_Data.append( (str(self.NPC3_Encountered) + "\n") );
          GameState_Data.append( (str(self.TRAP1_Encountered) + "\n") );
          GameState_Data.append( (str(self.TRAP2_Encountered) + "\n") );
          GameState_Data.append( (str(self.TRAP3_Encountered) + "\n") );
          GameState_Data.append( (str(self.TRAP4_Encountered) + "\n") );

          #9. Write Game State data to file using line as a delimiter and close file. 
          print("\n9. Write GameState data to file using line as a delimiter and close file.");
          self.Text_Append("\n9. Write GameState data to file using line as a");
          self.Text_Append("delimiter. Then close file.");
          GameStateSaveFile.writelines(GameState_Data);
          GameStateSaveFile.close();   

          self.Text_Append("\nYour game has been successfully saved."); 
          self.Text_Append("Your may EXIT the game now and continue later.");  
          self.Text_Append("Or click \"GO\" to continue playing.\n");  


    #---Function-----------------------------------------------------------------------------------------------------
      def Load_Game(self):
          print("\nLoading Game");
          self.Text_Write("Loading Game");
          
          if(self.CharacterToLoad_GET_Value == False):
             #1. Get current script directory (needs "import os").
             print("\n1. Getting current script directory and searching");
             print("for Character and GameState files.\n");
             self.Text_Append("\n1. Getting current script directory and searching");
             self.Text_Append("for Character and GameState files.\n");

             CurrentDir = os.getcwd(); 

             print("Searching for files in directory: \"",CurrentDir,"\"",sep='');
             self.Text_Append("Searching for files in directory:");
             self.Text_Append(CurrentDir);

             #2. List files in that directory
             print("\nA. Listing CHARACTER files in this directory.");
             print("----------------------------------------------------------------");
             self.Text_Append("\nA. Listing CHARACTER files in this directory.");
             self.Text_Append("---------------------------------------------------");

             FileCounter = 0;
             Array_of_Files_In_Dir = os.listdir();
    
             for x in Array_of_Files_In_Dir:
                 if(x.endswith(".DDchar")):
                    FileCounter = FileCounter + 1;
                    print(" ",FileCounter,"\b.",x);
                    self.Text_Append("  " + str(FileCounter) + ". " + x);

             print("----------------------------------------------------------------\n");
             self.Text_Append("---------------------------------------------------");                 

             print("\nB. Listing GameState files in this directory.");
             print("----------------------------------------------------------------");
             self.Text_Append("\nB. Listing GameState files in this directory.");
             self.Text_Append("---------------------------------------------------");

             FileCounter = 0;

             for x in Array_of_Files_In_Dir:
                 if(x.endswith(".DDgame")):
                    FileCounter = FileCounter + 1;
                    print(" ",FileCounter,"\b.",x);
                    self.Text_Append("  " + str(FileCounter) + ". " + x);                 

             print("----------------------------------------------------------------\n");
             self.Text_Append("---------------------------------------------------");  

             print("\nEnter the Char & GameState name you want after the prefix_ and");
             print("before the .ext. Then click \"LOAD\" again to load them.");
             self.Text_Append("\nEnter the Char & GameState name you want"); 
             self.Text_Append("after the prefix_ and before the .ext."); 
             self.Text_Append("\nThen click \"LOAD\" again to load them.\n");

             self.CharacterToLoad_GET_Value = True;

          elif(self.CharacterToLoad_GET_Value == True):
               #3. Ask player to choose game to load and open file
               CHOICE = self.ENT_Main_Input.get();
               if(CHOICE == ""):
                  self.Text_Append("NULL values not allowed.");
                  self.Text_Append("Click \"GO\" to continue.");
                  self.CharacterToLoad_GET_Value = False;
               else:
                  CurrentDir = os.getcwd();
                  Char_File_Name = CurrentDir + "\\" + "DD_Character_" + CHOICE + ".DDchar";
                  print("\n3. Opening Character file: " + Char_File_Name);
                  self.Text_Append("\n3. Opening Character file:");
                  self.Text_Append(Char_File_Name);
                  CharSave_File = open(Char_File_Name, "r");

                  #4. Read data from file into an array, line by line into each element. Close file to be SAFE.
                  print("\n4. Read data from file into array, line by line into each element. Close file to be SAFE.");
                  self.Text_Append("\n4. Read data from file into array, line by");
                  self.Text_Append("line into each element. Close file to be SAFE.");
                  Char_Data = CharSave_File.read().splitlines();
                  CharSave_File.close(); #No longer need file open now that data has been extracted to array

                  #5. Instantiate Character object for game based on CLASS data type saved to file
                  print("\n5. Instantiate Character object for game based on CLASS data type saved to file.");
                  self.Text_Append("\n5. Instantiate Character object for game");
                  self.Text_Append("based on CLASS data type saved to file.");
                  if(Char_Data[2] == "Alicorn"): 
                     print("\nInstantiating an ALICORN.");
                     self.Text_Append("\nInstantiating an ALICORN.");
                     self.Plyr_Heroine = ALICORN();
                  elif(Char_Data[2] == "Unicorn"): 
                       print("\nInstantiating a UNICORN.");
                       self.Text_Append("\nInstantiating an UNICORN.");
                       self.Plyr_Heroine = UNICORN();   
                  elif(Char_Data[2] == "Pegasus"): 
                       print("\nInstantiating a PEGASUS.");
                       self.Text_Append("\nInstantiating an PEGASUS.");
                       self.Plyr_Heroine = PEGASUS();
                  elif(Char_Data[2] == "Princess"): 
                       print("\nInstantiating a PRINCESS.");
                       self.Text_Append("\nInstantiating an PRINCESS.");
                       self.Plyr_Heroine = PRINCESS();               
                  elif(Char_Data[2] == "Pony"): 
                       print("\nInstantiating a basic PONY.");
                       self.Text_Append("\nInstantiating an PONY.");
                       self.Plyr_Heroine = PONY();               
                  
                  #6. Load and assign values to newly instantiated Character object
                  print("\n6. Loading and assigning values to newly instantiated Character object.");
                  self.Text_Append("\n6. Loading and assigning values to newly");
                  self.Text_Append("instantiated Character object.\n");
                  print("Name: ",Char_Data[0]);
                  self.Text_Append("Name: " + Char_Data[0]);
                  self.Plyr_Heroine.EntityName = Char_Data[0];
                  print("Gender: ",Char_Data[1]);
                  self.Text_Append("Gender: " + Char_Data[1]);
                  self.Plyr_Heroine.EntityGender = Char_Data[1];
                  print("Class: ",Char_Data[2]);
                  self.Text_Append("Class: " + Char_Data[2]);
                  self.Plyr_Heroine.EntityClass = Char_Data[2];
                  print("Health: ",Char_Data[3]);
                  self.Text_Append("Health: " + Char_Data[3]);
                  self.Plyr_Heroine.EntityHealth = int(Char_Data[3]);
                  print("Defense: ",Char_Data[4]);
                  self.Text_Append("Defense: " + Char_Data[4]);
                  self.Plyr_Heroine.EntityDefense = int(Char_Data[4]);
                  print("Attack: ",Char_Data[5]);
                  self.Text_Append("Attack: " + Char_Data[5]);
                  self.Plyr_Heroine.EntityAttack = int(Char_Data[5]);
                  print("Magic Power: ",Char_Data[6]);
                  self.Text_Append("Magic Power: " + Char_Data[6]);
                  self.Plyr_Heroine.EntityMagicPower = int(Char_Data[6]);
                  print("Dexterity: ",Char_Data[7]);
                  self.Text_Append("Dexterity: " + Char_Data[7]);
                  self.Plyr_Heroine.EntityDexterity = int(Char_Data[7]);
                  print("Charisma: ",Char_Data[8]);
                  self.Text_Append("Charisma: " + Char_Data[8]);
                  self.Plyr_Heroine.EntityCharisma = int(Char_Data[8]);
                  print("Level: ",Char_Data[9]);
                  self.Text_Append("Level: " + Char_Data[9]);
                  self.Plyr_Heroine.EntityLevel = int(Char_Data[9]);
                  print("Combat Exp: ",Char_Data[10]);
                  self.Text_Append("Combat Exp: " + Char_Data[10]);
                  self.Plyr_Heroine.EntityCombatExp = int(Char_Data[10]);
                  print("Money: ",Char_Data[11]);
                  self.Text_Append("Money: " + Char_Data[11]);
                  self.Plyr_Heroine.EntityMoney = int(Char_Data[11]);
                  print("Weapon Choice: ",Char_Data[12]);
                  self.Text_Append("Weapon Choice: " + Char_Data[12]);
                  self.Plyr_Heroine.WeaponChoice = Char_Data[12];                  
                  print("Magic Choice: ",Char_Data[13]);
                  self.Text_Append("Magic Choice: " + Char_Data[13]);
                  self.Plyr_Heroine.MagicChoice = Char_Data[13];
                  print("Armor Choice: ",Char_Data[14]);
                  self.Text_Append("Armor Choice: " + Char_Data[14]);
                  self.Plyr_Heroine.ArmorChoice = Char_Data[14];
                  print("Invisibility Active: ",Char_Data[15]);
                  self.Text_Append("Invisibility Active: " + Char_Data[15]);
                  self.Plyr_Heroine.Invisibility_Active = Char_Data[15];
                  print("Invisibility Count: ",Char_Data[16]);
                  self.Text_Append("Invisibility Count: " + Char_Data[16]);
                  self.Plyr_Heroine.Invisibility_Count = int(Char_Data[16]);
                  print("Dammage_Item_Slingshot: ",Char_Data[17]);
                  self.Text_Append("Dammage_Item_Slingshot: " + Char_Data[17]);
                  self.Plyr_Heroine.Dammage_Item_Slingshot = int(Char_Data[17]);
                  print("Dammage_Item_Staff: ",Char_Data[18]);
                  self.Text_Append("Dammage_Item_Staff: " + Char_Data[18]);
                  self.Plyr_Heroine.Dammage_Item_Staff = int(Char_Data[18]);
                  print("Dammage_Item_Pendant: ",Char_Data[19]);
                  self.Text_Append("Dammage_Item_Pendant: " + Char_Data[19]);
                  self.Plyr_Heroine.Dammage_Item_Pendant = int(Char_Data[19]);
                  print("Dammage_Item_Sigil: ",Char_Data[20]);
                  self.Text_Append("Dammage_Item_Sigil: " + Char_Data[20]);
                  self.Plyr_Heroine.Dammage_Item_Sigil = int(Char_Data[20]);
                  print("Dammage_Item_Orb: ",Char_Data[21]);
                  self.Text_Append("Dammage_Item_Orb: " + Char_Data[21]);
                  self.Plyr_Heroine.Dammage_Item_Orb = int(Char_Data[21]);
                  print("Dammage_Item_PrincessCloak: ",Char_Data[21]);
                  self.Text_Append("Dammage_Item_PrincessCloak: " + Char_Data[22]);
                  self.Plyr_Heroine.Dammage_Item_PrincessCloak = int(Char_Data[22]);
                  print("Dammage_Skill_IceBlasts: ",Char_Data[22]);
                  self.Text_Append("Dammage_Skill_IceBlasts: " + Char_Data[23]);
                  self.Plyr_Heroine.Dammage_Skill_IceBlasts = int(Char_Data[23]);
                  print("Dammage_Skill_FireBalls: ",Char_Data[23]);
                  self.Text_Append("Dammage_Skill_FireBalls: " + Char_Data[24]);
                  self.Plyr_Heroine.Dammage_Skill_FireBalls = int(Char_Data[24]);
                  print("Dammage_Skill_Lightning: ",Char_Data[24]);
                  self.Text_Append("Dammage_Skill_Lightning: " + Char_Data[25]);
                  self.Plyr_Heroine.Dammage_Skill_Lightning = int(Char_Data[25]);
                  print("Dammage_Skill_Telekinesis: ",Char_Data[26]);
                  self.Text_Append("Dammage_Skill_Telekinesis: " + Char_Data[26]);
                  self.Plyr_Heroine.Dammage_Skill_Telekinesis = int(Char_Data[26]);
                  print("Dammage_Skill_Telepathy: ",Char_Data[27]);
                  self.Text_Append("Dammage_Skill_Telepathy: " + Char_Data[27]);
                  self.Plyr_Heroine.Dammage_Skill_Telepathy = int(Char_Data[27]);
                  print("Dammage_Skill_Teleportation: ",Char_Data[28]);
                  self.Text_Append("Dammage_Skill_Teleportation: " + Char_Data[28]);
                  self.Plyr_Heroine.Dammage_Skill_Teleportation = int(Char_Data[28]);
                  print("Dammage_Skill_TimeWarp: ",Char_Data[29]);
                  self.Text_Append("Dammage_Skill_TimeWarp: " + Char_Data[29]);
                  self.Plyr_Heroine.Dammage_Skill_TimeWarp = int(Char_Data[29]); 
                  print("Invisibility_DEF_Amt: ",Char_Data[30]);
                  self.Text_Append("Invisibility_DEF_Amt: " + Char_Data[30]);
                  self.Plyr_Heroine.Invisibility_DEF_Amt = int(Char_Data[30]);
                  print("DEF_Item_Chain_Mail: ",Char_Data[31]);
                  self.Text_Append("DEF_Item_Chain_Mail: " + Char_Data[31]);
                  self.Plyr_Heroine.DEF_Item_Chain_Mail = int(Char_Data[31]);
                  print("DEF_Item_Plate_Armor: ",Char_Data[32]);
                  self.Text_Append("DEF_Item_Plate_Armor: " + Char_Data[32]);
                  self.Plyr_Heroine.DEF_Item_Plate_Armor = int(Char_Data[32]);
                  print("INV_Has_Slingshot: ",Char_Data[33]);
                  self.Text_Append("INV_Has_Slingshot: " + Char_Data[33]);
                  self.Plyr_Heroine.INV_Has_Slingshot = Char_Data[33];
                  print("Slingshot_Pellets_Amt: ",Char_Data[34]);
                  self.Text_Append("Slingshot_Pellets_Amt: " + Char_Data[34]);
                  self.Plyr_Heroine.Slingshot_Pellets_Amt = int(Char_Data[34]);
                  print("INV_Has_Staff: ",Char_Data[35]);
                  self.Text_Append("INV_Has_Staff: " + Char_Data[35]);
                  self.Plyr_Heroine.INV_Has_Staff = Char_Data[35];
                  print("INV_Has_Pendant: ",Char_Data[36]);
                  self.Text_Append("INV_Has_Pendant: " + Char_Data[36]);
                  self.Plyr_Heroine.INV_Has_Pendant = Char_Data[36];
                  print("INV_Has_Sigil: ",Char_Data[37]);
                  self.Text_Append("INV_Has_Sigil: " + Char_Data[37]);
                  self.Plyr_Heroine.INV_Has_Sigil = Char_Data[37];
                  print("INV_Has_Orb: ",Char_Data[38]);
                  self.Text_Append("INV_Has_Orb: " + Char_Data[38]);
                  self.Plyr_Heroine.INV_Has_Orb = Char_Data[38];
                  print("INV_Has_PrincessCloak: ",Char_Data[39]);
                  self.Text_Append("INV_Has_PrincessCloak: " + Char_Data[39]);
                  self.Plyr_Heroine.INV_Has_PrincessCloak = Char_Data[39];
                  print("INV_Has_HealingPotions: ",Char_Data[40]);
                  self.Text_Append("INV_Has_HealingPotions: " + Char_Data[40]);
                  self.Plyr_Heroine.INV_Has_HealingPotions = int(Char_Data[40]);
                  print("HealthPotion_Restore_Amt: ",Char_Data[41]);
                  self.Text_Append("HealthPotion_Restore_Amt: " + Char_Data[41]);
                  self.Plyr_Heroine.HealthPotion_Restore_Amt = int(Char_Data[41]);
                  print("INV_Has_Chain_Mail: ",Char_Data[42]);
                  self.Text_Append("INV_Has_Chain_Mail: " + Char_Data[42]);
                  self.Plyr_Heroine.INV_Has_Chain_Mail = Char_Data[42];
                  print("INV_Has_Plate_Armor: ",Char_Data[43]);
                  self.Text_Append("INV_Has_Plate_Armor: " + Char_Data[43]);
                  self.Plyr_Heroine.INV_Has_Plate_Armor = Char_Data[43];
                  print("SKILL_Has_IceBlasts: ",Char_Data[44]);
                  self.Text_Append("SKILL_Has_IceBlasts: " + Char_Data[44]);
                  self.Plyr_Heroine.SKILL_Has_IceBlasts = Char_Data[44];
                  print("SKILL_Has_FireBalls: ",Char_Data[45]);
                  self.Text_Append("SKILL_Has_FireBalls: " + Char_Data[45]);
                  self.Plyr_Heroine.SKILL_Has_FireBalls = Char_Data[45];
                  print("SKILL_Has_Lightning: ",Char_Data[46]);
                  self.Text_Append("SKILL_Has_Lightning: " + Char_Data[46]);
                  self.Plyr_Heroine.SKILL_Has_Lightning = Char_Data[46];
                  print("SKILL_Has_Telekinesis: ",Char_Data[47]);
                  self.Text_Append("SKILL_Has_Telekinesis: " + Char_Data[47]);
                  self.Plyr_Heroine.SKILL_Has_Telekinesis = Char_Data[47];
                  print("SKILL_Has_Telepathy: ",Char_Data[48]);
                  self.Text_Append("SKILL_Has_Telepathy: " + Char_Data[48]);
                  self.Plyr_Heroine.SKILL_Has_Telepathy = Char_Data[48];
                  print("SKILL_Has_Teleportation: ",Char_Data[49]);
                  self.Text_Append("SKILL_Has_Teleportation: " + Char_Data[49]);
                  self.Plyr_Heroine.SKILL_Has_Teleportation = Char_Data[49];
                  print("SKILL_Has_TimeWarp: ",Char_Data[50]);
                  self.Text_Append("SKILL_Has_TimeWarp: " + Char_Data[50]);
                  self.Plyr_Heroine.SKILL_Has_TimeWarp = Char_Data[50];
                  print("SKILL_Has_Invisibility: ",Char_Data[51]);
                  self.Text_Append("SKILL_Has_Invisibility: " + Char_Data[51]);
                  self.Plyr_Heroine.SKILL_Has_Invisibility = Char_Data[51];
                  print("SKILL_Invisibility_Cost: ",Char_Data[52]);
                  self.Text_Append("SKILL_Invisibility_Cost: " + Char_Data[52]);
                  self.Plyr_Heroine.SKILL_Invisibility_Cost = int(Char_Data[52]);
                  print("SKILL_Has_Healing: ",Char_Data[53]);
                  self.Text_Append("SKILL_Has_Healing: " + Char_Data[53]);
                  self.Plyr_Heroine.SKILL_Has_Healing = Char_Data[53];
                  print("SKILL_Healing_Restore_Amt: ",Char_Data[54]);
                  self.Text_Append("SKILL_Healing_Restore_Amt: " + Char_Data[54]);
                  self.Plyr_Heroine.SKILL_Healing_Restore_Amt = int(Char_Data[54]);
                  print("SKILL_Has_FriendshipCast: ",Char_Data[55]);
                  self.Text_Append("SKILL_Has_FriendshipCast: " + Char_Data[55]);
                  self.Plyr_Heroine.SKILL_Has_FriendshipCast = Char_Data[55];

                  #7. Open Game State file
                  print("\n7. Open Game State file");
                  self.Text_Append("\n7. Open Game State file");
                  GameState_File_Name = CurrentDir + "\\" + "DD_GameState_" + CHOICE + ".DDgame";
                  GameState_File = open(GameState_File_Name, "r");

                  #8. Read data from file into array, line by line into each element. Close file.
                  print("\n8. Read data from file into array, line by line into each element. Then close file.");
                  self.Text_Append("\n8. Read data from file into array, line by");
                  self.Text_Append("line into each element. Then close file.");
                  GameState_Data = GameState_File.read().splitlines();
                  GameState_File.close(); #No longer need file open now that data has been extracted to array

                  #9. Load and assign values from array to GameState
                  print("\n9. Load & assign values from array to GameState");
                  self.Text_Append("\n9. Load & assign values from array to GameState");
                  print("LOCATION: ",GameState_Data[0]);
                  self.Text_Append("LOCATION: " + GameState_Data[0]);
                  self.LOCATION = int(GameState_Data[0]);
                  print("L1_N3_Slime_Mold_Alive: ",GameState_Data[1]);
                  self.Text_Append("L1_N3_Slime_Mold_Alive: " + GameState_Data[1]);
                  self.L1_N3_Slime_Mold_Alive = bool(GameState_Data[1]);
                  print("L1_MountainOfMeanness_Harpy_Alive: ",GameState_Data[2]);
                  self.Text_Append("L1_MountainOfMeanness_Harpy_Alive: " + GameState_Data[2]);
                  self.L1_MountainOfMeanness_Harpy_Alive = bool(GameState_Data[2]);
                  print("L1_SwampOfSadness_Dolphin_Alive: ",GameState_Data[3]);
                  self.Text_Append("L1_SwampOfSadness_Dolphin_Alive: " + GameState_Data[3]);
                  self.L1_SwampOfSadness_Dolphin_Alive = bool(GameState_Data[3]);
                  print("L1_DiscordsLair_Discord_Boss_Alive: ",GameState_Data[4]);
                  self.Text_Append("L1_DiscordsLair_Discord_Boss_Alive: " + GameState_Data[4]);
                  self.L1_DiscordsLair_Discord_Boss_Alive = bool(GameState_Data[4]);
                  print("L1_Multiple_Opponents_Encounter_Alive: ",GameState_Data[5]);
                  self.Text_Append("L1_Multiple_Opponents_Encounter_Alive: " + GameState_Data[5]);
                  self.L1_Multiple_Opponents_Encounter_Alive = bool(GameState_Data[5]);
                  print("CENTER_FirstTime: ",GameState_Data[6]);
                  self.Text_Append("CENTER_FirstTime: " + GameState_Data[6]);
                  self.CENTER_FirstTime = bool(GameState_Data[6]);
                  print("CelestiasPalace_FirstTime: ",GameState_Data[7]);
                  self.Text_Append("CelestiasPalace_FirstTime: " + GameState_Data[7]);
                  self.CelestiasPalace_FirstTime = bool(GameState_Data[7]);
                  print("DiscordsLair_FirstTime: ",GameState_Data[8]);
                  self.Text_Append("DiscordsLair_FirstTime: " + GameState_Data[8]);
                  self.DiscordsLair_FirstTime = bool(GameState_Data[8]);
                  print("FriendshipForest_FirstTime: ",GameState_Data[9]);
                  self.Text_Append("FriendshipForest_FirstTime: " + GameState_Data[9]);
                  self.FriendshipForest_FirstTime = bool(GameState_Data[9]);
                  print("Found_Staff: ",GameState_Data[10]);
                  self.Text_Append("Found_Staff: " + GameState_Data[10]);
                  self.Found_Staff = bool(GameState_Data[10]);
                  print("Found_Pendant: ",GameState_Data[11]);
                  self.Text_Append("Found_Pendant: " + GameState_Data[11]);
                  self.Found_Pendant = bool(GameState_Data[11]);
                  print("Found_Sigil: ",GameState_Data[12]);
                  self.Text_Append("Found_Sigil: " + GameState_Data[12]);
                  self.Found_Sigil = bool(GameState_Data[12]);
                  print("Found_Orb: ",GameState_Data[13]);
                  self.Text_Append("Found_Orb: " + GameState_Data[13]);
                  self.Found_Orb = bool(GameState_Data[13]);
                  print("Found_PrincessCloak: ",GameState_Data[14]);
                  self.Text_Append("Found_PrincessCloak: " + GameState_Data[14]);
                  self.Found_PrincessCloak = bool(GameState_Data[14]);
                  print("Found_Chain_Mail: ",GameState_Data[15]);
                  self.Text_Append("Found_Chain_Mail: " + GameState_Data[15]);
                  self.Found_Chain_Mail = bool(GameState_Data[15]);
                  print("Found_Plate_Armor: ",GameState_Data[16]);
                  self.Text_Append("Found_Plate_Armor: " + GameState_Data[16]);
                  self.Found_Plate_Armor = bool(GameState_Data[16]);
                  print("Acquired_IceBlasts: ",GameState_Data[17]);
                  self.Text_Append("Acquired_IceBlasts: " + GameState_Data[17]);
                  self.Acquired_IceBlasts = bool(GameState_Data[17]);
                  print("Acquired_FireBalls: ",GameState_Data[18]);
                  self.Text_Append("Acquired_FireBalls: " + GameState_Data[18]);
                  self.Acquired_FireBalls = bool(GameState_Data[18]);
                  print("Acquired_Lightning: ",GameState_Data[19]);
                  self.Text_Append("Acquired_Lightning: " + GameState_Data[19]);
                  self.Acquired_Lightning = bool(GameState_Data[19]);
                  print("Acquired_Telekinesis: ",GameState_Data[20]);
                  self.Text_Append("Acquired_Telekinesis: " + GameState_Data[20]);
                  self.Acquired_Telekinesis = bool(GameState_Data[20]);
                  print("Acquired_Telepathy: ",GameState_Data[21]);
                  self.Text_Append("Acquired_Telepathy: " + GameState_Data[21]);
                  self.Acquired_Telepathy = bool(GameState_Data[21]);
                  print("Acquired_Teleportation: ",GameState_Data[22]);
                  self.Text_Append("Acquired_Teleportation: " + GameState_Data[22]);
                  self.Acquired_Teleportation = bool(GameState_Data[22]);
                  print("Acquired_TimeWarp: ",GameState_Data[23]);
                  self.Text_Append("Acquired_TimeWarp: " + GameState_Data[23]);
                  self.Acquired_TimeWarp = bool(GameState_Data[23]);
                  print("Acquired_Invisibility: ",GameState_Data[24]);
                  self.Text_Append("Acquired_Invisibility: " + GameState_Data[24]);
                  self.Acquired_Invisibility = bool(GameState_Data[24]);
                  print("Acquired_Healing: ",GameState_Data[25]);
                  self.Text_Append("Acquired_Healing: " + GameState_Data[25]);
                  self.Acquired_Healing = bool(GameState_Data[25]);
                  print("Acquired_FriendshipCast: ",GameState_Data[26]);
                  self.Text_Append("Acquired_FriendshipCast: " + GameState_Data[26]);
                  self.Acquired_FriendshipCast = bool(GameState_Data[26]);
                  print("Found_HealingPotion_1: ",GameState_Data[27]);
                  self.Text_Append("Found_HealingPotion_1: " + GameState_Data[27]);
                  self.Found_HealingPotion_1 = bool(GameState_Data[27])
                  print("Found_HealingPotion_2: ",GameState_Data[28]);
                  self.Text_Append("Found_HealingPotion_2: " + GameState_Data[28]);
                  self.Found_HealingPotion_2 = bool(GameState_Data[28]);
                  print("Found_HealingPotion_3: ",GameState_Data[29]);
                  self.Text_Append("Found_HealingPotion_3: " + GameState_Data[29]);
                  self.Found_HealingPotion_3 = bool(GameState_Data[29]);
                  print("Found_HealingPotion_4: ",GameState_Data[30]);
                  self.Text_Append("Found_HealingPotion_4: " + GameState_Data[30]);
                  self.Found_HealingPotion_4 = bool(GameState_Data[30]);
                  print("Found_HealingPotion_CelestiasPalace: ",GameState_Data[31]);
                  self.Text_Append("Found_HealingPotion_CelestiasPalace: " + GameState_Data[31]);
                  self.Found_HealingPotion_CelestiasPalace = bool(GameState_Data[31]);
                  print("NPC1_Encountered: ",GameState_Data[32]);
                  self.Text_Append("NPC1_Encountered: " + GameState_Data[32]);
                  self.NPC1_Encountered = bool(GameState_Data[32]);
                  print("NPC2_Encountered: ",GameState_Data[33]);
                  self.Text_Append("NPC2_Encountered: " + GameState_Data[33]);
                  self.NPC2_Encountered = bool(GameState_Data[33]);
                  print("NPC3_Encountered: ",GameState_Data[34]);
                  self.Text_Append("NPC3_Encountered: " + GameState_Data[34]);
                  self.NPC3_Encountered = bool(GameState_Data[34]);
                  print("TRAP1_Encountered: ",GameState_Data[35]);
                  self.Text_Append("TRAP1_Encountered: " + GameState_Data[35]);
                  self.TRAP1_Encountered = bool(GameState_Data[35]);
                  print("TRAP2_Encountered: ",GameState_Data[36]);
                  self.Text_Append("TRAP2_Encountered: " + GameState_Data[36]);
                  self.TRAP2_Encountered = bool(GameState_Data[36]);
                  print("TRAP3_Encountered: ",GameState_Data[37]);
                  self.Text_Append("TRAP3_Encountered: " + GameState_Data[37]);
                  self.TRAP3_Encountered = bool(GameState_Data[37]);
                  print("TRAP4_Encountered: ",GameState_Data[38]);
                  self.Text_Append("TRAP4_Encountered: " + GameState_Data[38]);
                  self.TRAP4_Encountered = bool(GameState_Data[38]);

                  #Need to unlock NAV buttons if game successfully loads
                  self.All_Nav_Buttons_ENABLE();

                  #Update Interface
                  self.Plyr_Heroine.Display_All();

                  self.Text_Append("\nYour game has been successfully loaded. You"); 
                  self.Text_Append("may continue playing from your last save point.");  
                  self.Text_Append("Click \"GO\" to resume your game.\n");  


    #---Function-------------------------------------------------------------------------------------------
      #Just a small, quick example of how to code your own casting functions to convert between data types
      def BOOLISH(self,TheString):
          if(TheString == "False"): 
             return False;
          elif(TheString == "True"):
             return True;    


      #Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
      def Create_NPCs(self): 
          print("Instantiating the NPCs ...");
          self.Text_Write("Instantiating the NPCs ..."); 

          if(self.Create_NPC_Page == 1):
             #NPC 1
             print("\n Instantiating NPC 1.");
             self.Text_Append("\nInstantiating NPC 1."); 
             self.NPC_1 = NPC("Madrigastafula","NPC Pony"); 
             self.NPC_1.Display_All();  

             RAND_Responses = ["Odd weather we seem to be having today, eh?",
                               "And then she turned to me and said \"WHATEVER!\".\nThe nerve of that pony!",
                               "Seems like everypony has a sad story these days.",
                               "Why do today what you can put off until tomorrow?",
                               "A stitch in time saves nine.",
                               "I have a headache.",
                               "Fancy meeting you here!",
                               "What are the odds that you and I are thinking\nthe very same thing?",
                               "Is anything ever what it seems in this place?",
                               "All we are is dust in the wind. Dude."];              

             self.NPC_1.Set_Random_Responses(RAND_Responses);
             #NPC_1.Speak();     

             #NPC 2
             print("\n Instantiating NPC 2.");
             self.Text_Append("\nInstantiating NPC 2."); 
             self.NPC_2 = NPC("Chrystalia","Alicorn"); 
             self.NPC_2.Display_All();  

             RAND_Responses = ["Fore score and seven yarns ago ...",
                               "There's no time like the present.",
                               "What is? Once was. What was? Will be again.",
                               "But in the end? It doesn't even matter.",
                               "The answer my friend is blowing in the wind.",
                               "Don't go out tonight. You're bound to lose your\nlife. I see a bad moon on the rise.",
                               "I hear hurricanes a-blowing.\nI know the end is coming soon.\nI fear rivers over flowing.\nI hear the voice of rage and ruin.",
                               "And you tell me over and over and over again,\nmy friend.\nHow you don't believe\nwe're on the eve\nof destruction.",
                               "If I could find a souvenir?\nJust to prove the world was here.",
                               "It's all over and I'm standing pretty.\nIn this dust that was a city."];              

             self.NPC_2.Set_Random_Responses(RAND_Responses);
             #NPC_2.Speak(); 

             #NPC 3
             print("\n Instantiating NPC 3.");
             self.Text_Append("\nInstantiating NPC 3."); 
             self.NPC_3 = NPC("Raya","Pegasus"); 
             self.NPC_3.Display_All();  

             RAND_Responses = ["When the last eagle flies\nover the last crumbling mountain?",
                               "And the last lion roars\nat the last dusty fountain?",
                               "In the shadow of the forest\nthough she may be old and worn.",
                               "They will stare unbelieving\nat the Last Unicorn.",
                               "When the first breath of winter\nthrough the flowers is icing?",
                               "And you look to the north\nand a pale moon is rising?",
                               "And it seems like all is dying \nand would leave the world to mourn.",
                               "In the distance hear the laughter\nof the Last Unicorn.",
                               "When the last moon is cast\nover the last star of morning.",
                               "And the future has passed\nwithout even a last desparate warning?"];              

             self.NPC_3.Set_Random_Responses(RAND_Responses);
             #NPC_3.Speak(); 

             self.Text_Append("\nLet's see. YOU exist. NPCs exist.");
             self.Text_Append("Looks like we're ready to go now. No?");
      
          if(self.Create_NPC_Page == 2):       
             self.All_Nav_Buttons_ENABLE();
             self.LOCATION = self.L1_C1;
             self.CHOICE = "#"; 
             #self.SwitchBoard(); 

          #Ending actions
          self.Text_Append("\n Click \"GO\" to continue.\n"); 
          self.Create_NPC_Page += 1;      


    #---GUI Class Constructor----------------------------------------------------------------------------
      def __init__(self, master=None):
          self.window = master;

          #MENU event handlers
          #Event handlers for File menu items
          def File_Menu_NEW_Handler(): Handle_Button_New();
          def File_Menu_SAVE_Handler(): Handle_Button_Save(); 
          def File_Menu_LOAD_Handler(): Handle_Button_Load(); 
          def File_Menu_Future1_Handler(): MB.showinfo(title='Menu Event Future1 Triggered: ', message="For Future 1 use."); 
          def File_Menu_Future2_Handler(): MB.showinfo(title='Menu Event Future2 Triggered: ', message="For Future 2 use."); 

          #Event handlers for Edit menu items
          def Edit_Menu_CHEAT_Handler(): Handle_Button_Cheat();
          def Edit_Menu_CHEAT_Master_Map_Handler(): Handle_Button_Cheat_Map();
          def Edit_Menu_UNDO_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked UNDO");
          def Edit_Menu_REDO_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked REDO"); 
          def Edit_Menu_CUT_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked CUT"); 
          def Edit_Menu_COPY_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked COPY"); 
          def Edit_Menu_PASTE_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked PASTE");
          def Edit_Menu_DELETE_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked DELETE"); 
          def Edit_Menu_SELECTALL_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked SELECT ALL");

          #Event handlers for View menu items
          def View_Menu_ZOOMIN_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From VIEW menu clicked ZOOM IN");
          def View_Menu_ZOOMOUT_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From VIEW menu clicked ZOOM OUT"); 
          def View_Menu_STATUSBAR_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From VIEW menu clicked STATUS BAR");

          #Event handlers for Help menu items
          def Help_Menu_HELP_Handler(): 
              TITLE = "HELP:   Discord's Dungeon    ©2022 Carly Salali Germany";
              MESSAGE = "You find yourself transported by an unknown power to the magical land of Equestria. You must:";
              MESSAGE += "\n\n1. Create a character. You may choose from several types like Pony, Alicorn, Pegasus, Unicorn,";
              MESSAGE += "\n   Princess, etc. Once you have chosen a character class, assign your character gender and name.";
              MESSAGE += "\n\n2. Once you have created your character, you will begin the game by materializing at the Level 1";
              MESSAGE += "\n   starting location on the game map. Once you begin, you may navigate freely back and forth using";
              MESSAGE += "\n   cardinal directions to navigate between grids on the game map. As you proceed through each";
              MESSAGE += "\n   map, you will face puzzles, traps and encounters with adversaries that you must vanquish in";
              MESSAGE += "\n   order to complete each level. Along the way, you will be rewarded for solving puzzles and";
              MESSAGE += "\n   defeating antagonists by acquiring magic items, potions, weapons and armor that will be added";
              MESSAGE += "\n   to your inventory. Additionally, you will learn magic skills after completing different puzzles";
              MESSAGE += "\n   and defeating opponents in challenging combat. Good luck!";
              MESSAGE += "\n\n3. Once you have created your character and started a level, you will be able to SAVE the game";
              MESSAGE += "\n   state: including your character's attributes, inventory, skill set, completed quests and map";
              MESSAGE += "\n   details to a file. You will then be able to LOAD this and continue playing the game from where";
              MESSAGE += "\n   you left off on your last save. SAVE and LOAD are both accessed through the OPTIONS menu.";

              Help_Win = tk.Toplevel(window);
              Help_Win.configure(bg='black'); 
              Help_Win.title(TITLE);
              Name_Window_Width = 750;
              Name_Window_Height = 510;
              ScreenWidth = Help_Win.winfo_screenwidth();
              ScreenHeight = Help_Win.winfo_screenheight();
              Appear_in_the_Middle = '%dx%d+%d+%d' % (Name_Window_Width, Name_Window_Height, (ScreenWidth - Name_Window_Width) / 2, (ScreenHeight - Name_Window_Height) / 2);
              Help_Win.geometry(Appear_in_the_Middle);
              Help_Win.resizable(width=False, height=False);

              def CLOSE_Button_Handler():
                  Help_Win.destroy();        

              LAB_NAM = tk.Label(Help_Win, text=TITLE, font=('Helvetica 10'), bg='black', fg='white');
              LAB_NAM.place(anchor="nw", height=20, width=550, x=90, y=8); 

              TXT_Help = tk.Text(Help_Win);
              TXT_Help.configure(width=50, height=10, background="#e3d3f8", borderwidth=3, font="{Comic Sans MS} 12 {}");
              TXT_Help.configure(relief="flat", selectborderwidth=2, setgrid="false", state="normal", takefocus=False);
              TXT_Help.place(anchor="nw", height=425, width=730, x=10, y=35);    
              TXT_Help.insert("0.0",MESSAGE);

              BTN_CLOSE = tk.Button(Help_Win, width=15, height=5, font=('Helvetica 11'), text="CLOSE", bg='red', command=CLOSE_Button_Handler);
              BTN_CLOSE.place(anchor="nw", height=25, width=100, x=330, y=470);                 
              
          def Help_Menu_ABOUT_Handler(): 
              MESSAGE = "     ABOUT:\n\n  Discord's Dungeon\n©2022 Carly Salali Germany\n     Version 1.0";

              About_Win = tk.Toplevel(window);
              About_Win.configure(bg='black'); 
              About_Win.title("ABOUT: DD ©2022 C.S.G.");
              Name_Window_Width = 310;
              Name_Window_Height = 135;
              ScreenWidth = About_Win.winfo_screenwidth();
              ScreenHeight = About_Win.winfo_screenheight();
              Appear_in_the_Middle = '%dx%d+%d+%d' % (Name_Window_Width, Name_Window_Height, (ScreenWidth - Name_Window_Width) / 2, (ScreenHeight - Name_Window_Height) / 2);
              About_Win.geometry(Appear_in_the_Middle);
              About_Win.resizable(width=False, height=False);

              def CLOSE_Button_Handler():
                  About_Win.destroy();        

              LAB_NAM = tk.Label(About_Win, text=MESSAGE, font=('Helvetica 10'), bg='black', fg='white');
              LAB_NAM.place(anchor="nw", height=80, width=280, x=10, y=8); 

              BTN_CLOSE = tk.Button(About_Win, width=15, height=5, font=('Helvetica 11'), text="CLOSE", bg='red', command=CLOSE_Button_Handler);
              BTN_CLOSE.place(anchor="nw", height=25, width=100, x=100, y=100);   

          #Event Handlers for Buttons
        #-------------------------------------------------------------------------------------------------------------------------      
          def Handle_Button_Use():
              self.Sound_Button_Press_1_Thread();
              MB.showinfo(title='USE Button Event Triggered: ', message="Clicked USE button");  
        #-------------------------------------------------------------------------------------------------------------------------    
          def Handle_Button_Attack():
              self.Sound_Button_Press_1_Thread();
              MB.showinfo(title='ATTACK Button Event Triggered: ', message="Clicked ATTACK button");
        #-------------------------------------------------------------------------------------------------------------------------          
          def Handle_Button_Defend():
              MB.showinfo(title='DEFEND Button Event Triggered: ', message="Clicked DEFEND button");
        #-------------------------------------------------------------------------------------------------------------------------    
          def Handle_Button_Look():
              self.Sound_Button_Press_1_Thread();
              MB.showinfo(title='LOOK Button Event Triggered: ', message="Clicked LOOK button");
        #-------------------------------------------------------------------------------------------------------------------------    
          def Handle_Button_Hint():
              self.Sound_Button_Press_1_Thread();
              MB.showinfo(title='HINT Button Event Triggered: ', message="Clicked HINT button"); 
        #-------------------------------------------------------------------------------------------------------------------------    
          def Handle_Button_Go():
              self.Sound_Button_Press_1_Thread();
              self.CHOICE = self.Input_Data.get();
              if(self.CHOICE == ""):
                 self.CHOICE = "#";

              self.SwitchBoard();

              self.Input_Data.set("");
              self.CHOICE = "#";
              self.ENT_Main_Input.focus();
        #-------------------------------------------------------------------------------------------------------------------------    
          def Handle_Button_North():
              self.CHOICE = "n";
              self.Navigate_Action();    
        #-------------------------------------------------------------------------------------------------------------------------    
          def Handle_Button_South():
              self.CHOICE = "s";
              self.Navigate_Action(); 
        #-------------------------------------------------------------------------------------------------------------------------    
          def Handle_Button_East():
              self.CHOICE = "e";
              self.Navigate_Action(); 
        #-------------------------------------------------------------------------------------------------------------------------    
          def Handle_Button_West():
              self.CHOICE = "w";
              self.Navigate_Action(); 
        #-------------------------------------------------------------------------------------------------------------------------    
          def Handle_Button_Save():
              self.Save_Game();
        #-------------------------------------------------------------------------------------------------------------------------    
          def Handle_Button_Load(): 
              self.Load_Game(); 
        #-------------------------------------------------------------------------------------------------------------------------    
          def Handle_Button_New():
              self.Reset_Game_State();           
        #-------------------------------------------------------------------------------------------------------------------------  
          def Handle_Button_Cheat():
              self.Plyr_Heroine.Cheat_Mode();
              self.Plyr_Heroine.Display_All();
        #-------------------------------------------------------------------------------------------------------------------------        
          def Handle_Button_Cheat_Map():
              Cheat_Map_Win = tk.Toplevel(window);
              Cheat_Map_Win.configure(bg='black'); 
              Cheat_Map_Win.title("You dirty CHEATER! This is the L1 Master Map");
              Name_Window_Width = 550;
              Name_Window_Height = 550;
              ScreenWidth = Cheat_Map_Win.winfo_screenwidth();
              ScreenHeight = Cheat_Map_Win.winfo_screenheight();
              Appear_in_the_Middle = '%dx%d+%d+%d' % (Name_Window_Width, Name_Window_Height, (ScreenWidth - Name_Window_Width) / 2, (ScreenHeight - Name_Window_Height) / 2);
              Cheat_Map_Win.geometry(Appear_in_the_Middle);
              Cheat_Map_Win.resizable(width=False, height=False);

              def CLOSE_Button_Handler():
                  Cheat_Map_Win.destroy();        

              MESSAGE = "Here's the Level 1 Master Map you DIRTY CHEATER!";
              LAB_NAM = tk.Label(master=Cheat_Map_Win, text=MESSAGE, font=('Helvetica 10'), bg='black', fg='white', justify="center");
              LAB_NAM.place(width=320,height=15,x=120,y=8);

              IMG_CHEATER_MAP = Image.open(self.IMAGE_Directory + "MAP_L1_All_Items.jpg");
              IMG_CHEATER_MAP = IMG_CHEATER_MAP.resize((465,450), Image.ANTIALIAS);
              IMG_CHEATER_MAP = ImageTk.PhotoImage(IMG_CHEATER_MAP);
              Label_Cheat_Map = tk.Label(master=Cheat_Map_Win,image=IMG_CHEATER_MAP,background="black",width=465,height=450);                               
              Label_Cheat_Map.place(anchor="nw",width=465,height=450,x=45,y=45);

              BTN_CLOSE = tk.Button(Cheat_Map_Win, width=15, height=5, font=('Helvetica 11'), text="CLOSE", bg='red', command=CLOSE_Button_Handler);
              BTN_CLOSE.place(anchor="nw", height=25, width=100, x=225, y=510);  

              Cheat_Map_Win.mainloop();  

        #-------------------------------------------------------------------------------------------------------------------------  


          #Event Handlers for ListBoxes  
        #-------------------------------------------------------------------------------------------------------------------------   
          #Event Handler for Inventory ListBox
          def Inventory_Changed_Handler(Inventory_Event):
              Inventory_Items = self.LB_Inventory.curselection();
              Inventory_Selection = ",".join([self.LB_Inventory.get(i) for i in Inventory_Items]);
              self.Plyr_Heroine.Inventory_Equip(Inventory_Selection);
              #The_Message = "You selected: " + Inventory_Selection; 
              #MB.showinfo(title='Inventory Selected Items', message=The_Message); 
        #-------------------------------------------------------------------------------------------------------------------------
          #Event Handler for Abilities ListBox
          def Abilities_Changed_Handler(Abilities_Event):
              Abilities_Items = self.LB_Abilities.curselection();
              Abilities_Selection = ",".join([self.LB_Abilities.get(i) for i in Abilities_Items]);
              self.Plyr_Heroine.SKILL_Equip(Abilities_Selection);
              #The_Message = "You selected: " + Abilities_Selection;
              #MB.showinfo(title='Abilities Selected Items', message=The_Message);
        #-------------------------------------------------------------------------------------------------------------------------  


        #---A. Frame: Main Window -------------------------------------------------------------
          self.FRM_Main = tk.Frame(master);
          self.FRM_Main.configure(height=755, width=1050, borderwidth=3, relief="flat", background="#000000");
          self.FRM_Main.place(anchor="nw", height=755, width=1050, x=3, y=3);

          self.LAB_Title = tk.Label(self.FRM_Main);
          self.LAB_Title.configure(text="Discord's Dungeon - 2022 C.S.G.",background="#000000", foreground="#ffffff");
          self.LAB_Title.place(anchor="nw", height=20, width=300, x=140, y=0);

        #---B. Frame: Main Input and Output ---------------------------------------------------
          self.LFRM_Main_Output_Input = tk.LabelFrame(self.FRM_Main);
          self.LFRM_Main_Output_Input.configure(background="#000000",borderwidth=3,foreground="#ffffff",width=530,height=530,relief="sunken",text="Main Input Output");
          self.LFRM_Main_Output_Input.place(anchor="nw", height=515, width=530, x=0, y=20);

          self.FRM_Main_Output = tk.Frame(self.LFRM_Main_Output_Input);
          self.FRM_Main_Output.configure(background="#000000",borderwidth=3,width=530,height=530,relief="sunken");
          self.FRM_Main_Output.place(anchor="nw", height=410, width=530, x=0, y=0);          

          self.SB_Vert_TXT_Main_Output = tk.Scrollbar(self.FRM_Main_Output, orient = tk.VERTICAL);
          self.SB_Vert_TXT_Main_Output.pack(side=tk.RIGHT, fill=tk.Y);          

          self.TXT_Main_Output = tk.Text(self.FRM_Main_Output, yscrollcommand=self.SB_Vert_TXT_Main_Output.set);
          self.TXT_Main_Output.configure(background="#e3d3f8", borderwidth=3, font="{Comic Sans MS} 12 {}", height=10);
          self.TXT_Main_Output.configure(relief="flat", selectborderwidth=2, setgrid="false", state="normal");
          self.TXT_Main_Output.configure(tabstyle="tabular", takefocus=False, width=50);
          self.TXT_Main_Output.insert("0.0", " Welcome to Discord's Dungeon!\n\n Click \"GO\" to begin.");
          self.TXT_Main_Output.place(anchor="nw", height=410, width=510, x=0, y=0);          

          self.SB_Vert_TXT_Main_Output.config(command=self.TXT_Main_Output.yview); #set scrollbar behavior

          MESSAGE = "\n\n A long, long time ago\n in a galaxy far, far away\n it was a dark and stormy night\n and we have a story to tell.";
          MESSAGE +=  "\n It was the best of times.\n It was the worst of times.\n It was all of them together at once.";
          self.TXT_Main_Output.insert(tk.END, MESSAGE);

          self.ENT_Main_Input = tk.Entry(self.LFRM_Main_Output_Input, textvariable=self.Input_Data);
          self.ENT_Main_Input.configure(takefocus=True,background="#ff00ff", foreground="#ffffff",font="{Comic Sans MS} 14 {}");
          self.ENT_Main_Input.delete("0", "end");
          #self.ENT_Main_Input.insert("0", " Main Input");
          self.ENT_Main_Input.place(anchor="nw", height=30, width=510, x=7, y=420);
        
          self.BTN_Use = tk.Button(self.LFRM_Main_Output_Input, command=Handle_Button_Use);
          self.BTN_Use.configure(background="#8000ff", foreground="#ffffff", justify="center");
          self.BTN_Use.configure(state="normal", text="USE"); #to disable buttons on startup or in game set state="disabled"
          self.BTN_Use.place(anchor="nw", height=30, width=70, x=7, y=460);

          self.BTN_Attack = tk.Button(self.LFRM_Main_Output_Input, command=Handle_Button_Attack);
          self.BTN_Attack.configure(background="#8000ff", foreground="#ffffff", justify="center");
          self.BTN_Attack.configure(state="normal", text="ATTACK");
          self.BTN_Attack.place(anchor="nw", height=30, width=70, x=84, y=460);

          self.BTN_Defend = tk.Button(self.LFRM_Main_Output_Input, command=Handle_Button_Defend);
          self.BTN_Defend.configure(background="#8000ff", foreground="#ffffff", justify="center");
          self.BTN_Defend.configure(state="normal", text="DEFEND");
          self.BTN_Defend.place(anchor="nw", height=30, width=70, x=160, y=460);

          self.BTN_Look = tk.Button(self.LFRM_Main_Output_Input, command=Handle_Button_Look);
          self.BTN_Look.configure(background="#8000ff", foreground="#ffffff", justify="center");
          self.BTN_Look.configure(state="normal", text="LOOK");
          self.BTN_Look.place(anchor="nw", height=30, width=70, x=238, y=460);

          self.BTN_Hint = tk.Button(self.LFRM_Main_Output_Input, command=Handle_Button_Hint);
          self.BTN_Hint.configure(background="#8000ff", foreground="#ffffff", justify="center");
          self.BTN_Hint.configure(state="normal", text="HINT");
          self.BTN_Hint.place(anchor="nw", height=30, width=70, x=317, y=460);

          self.BTN_Go = tk.Button(self.LFRM_Main_Output_Input, command=Handle_Button_Go);
          self.BTN_Go.configure(background="#8000ff", foreground="#ffffff", justify="center");
          self.BTN_Go.configure(state="normal", text="GO");
          self.BTN_Go.place(anchor="nw", height=30, width=120, x=396, y=460);

        #---C. Frame: Inventory -----------------------------------------------------------  
          self.LFRM_Inventory = tk.LabelFrame(self.FRM_Main);
          self.LFRM_Inventory.configure(background="#000000", foreground="#ffffff", height=190, width=260);
          self.LFRM_Inventory.configure(borderwidth=3, relief="sunken", text="Inventory");
          self.LFRM_Inventory.place(anchor="nw", height=205, width=260, x=1, y=545)

          self.LB_Inventory_Var.set([' Power Staff',' Pendant',' Sigil',' Infinity Orb',' Pri Cloak',' Chain Mail',' Plate Armor',' Healing Potions']);
          self.LB_Inventory = tk.Listbox(self.LFRM_Inventory, listvariable=self.LB_Inventory_Var, background="#e3d3f8",exportselection=0);
          self.LB_Inventory.place(anchor="nw", height=180, width=247, x=3, y=0);
          self.LB_Inventory.bind('<<ListboxSelect>>', Inventory_Changed_Handler);

        #---D. Frame: Abilities -----------------------------------------------------------
          self.LFRM_Abilities = tk.LabelFrame(self.FRM_Main);
          self.LFRM_Abilities.configure(background="#000000", foreground="#ffffff", height=190, width=260);
          self.LFRM_Abilities.configure(borderwidth=3,relief="sunken", text="Abilities");
          self.LFRM_Abilities.place(anchor="nw", height=205, width=260, x=270, y=545);

          self.LB_Abilities_Var.set([' Ice Blasts',' Fireballs',' Lightning ',' Telekinesis',' Telepathy',' Teleportation',' TimeWarp',' Invisibility',' Healing',' Friendship Cast']);
          self.LB_Abilities = tk.Listbox(self.LFRM_Abilities, listvariable=self.LB_Abilities_Var, background="#e3d3f8", exportselection=0);
          self.LB_Abilities.place(anchor="nw", height=180, width=247, x=3, y=0);
          self.LB_Abilities.bind('<<ListboxSelect>>', Abilities_Changed_Handler);

        #---E. Frame: Current View -----------------------------------------------------------        
          self.LFRM_Current_Map_View = tk.LabelFrame(self.FRM_Main);
          self.LFRM_Current_Map_View.configure(background="#000000", foreground="#ffffff", height=190, width=260);
          self.LFRM_Current_Map_View.configure(borderwidth=3, relief="sunken", text="Current Map View");
          self.LFRM_Current_Map_View.place(anchor="nw", height=400, width=495, x=540, y=20);

          self.IMG_Load = self.IMG_Load.resize((200,200), Image.ANTIALIAS);                       
          self.img_Wolf = ImageTk.PhotoImage(self.IMG_Load);       
          
          self.LAB_Current_View = tk.Label(self.LFRM_Current_Map_View);
          self.LAB_Current_View.configure(image=self.img_Wolf, justify="center", text="Current View");
          self.LAB_Current_View.place(anchor="nw", height=380, width=490, x=0, y=0);

        #---F. Frame: Navigation-----------------------------------------------------------
          self.LFRM_Navigation = tk.LabelFrame(self.FRM_Main);
          self.LFRM_Navigation.configure(background="#000000", foreground="#ffffff", height=125, width=250);
          self.LFRM_Navigation.configure(borderwidth=3, relief="sunken", text="Navigation");
          self.LFRM_Navigation.place(anchor="nw", height=125, width=250, x=539, y=425);

          self.BTN_North = tk.Button(self.LFRM_Navigation, command=Handle_Button_North);
          self.BTN_North.configure(background="#8000ff", foreground="#ffffff", justify="center", text="NORTH");
          self.BTN_North.place(anchor="nw", height=40, width=75, x=85, y=5);

          self.BTN_South = tk.Button(self.LFRM_Navigation, command=Handle_Button_South);
          self.BTN_South.configure(background="#8000ff", foreground="#ffffff", justify="center", text="SOUTH");
          self.BTN_South.place(anchor="nw", height=40, width=75, x=85, y=50);

          self.BTN_East = tk.Button(self.LFRM_Navigation, command=Handle_Button_East);
          self.BTN_East.configure(background="#8000ff", foreground="#ffffff", justify="center", text="EAST");
          self.BTN_East.place(anchor="nw", height=40, width=75, x=165, y=30);

          self.BTN_West = tk.Button(self.LFRM_Navigation, command=Handle_Button_West);
          self.BTN_West.configure(background="#8000ff", foreground="#ffffff", justify="center", text="WEST");
          self.BTN_West.place(anchor="nw", height=40, width=75, x=5, y=30);

        #---G. Frame: Save and Load -----------------------------------------------------------
          self.LFRM_Save_and_Load = tk.LabelFrame(self.FRM_Main);
          self.LFRM_Save_and_Load.configure(background="#000000", foreground="#ffffff", height=125, width=235);
          self.LFRM_Save_and_Load.configure(borderwidth=3, relief="sunken", text="Save and Load");
          self.LFRM_Save_and_Load.place(anchor="nw", height=125, width=235, x=800, y=425);

          self.BTN_Save = tk.Button(self.LFRM_Save_and_Load, command=Handle_Button_Save);
          self.BTN_Save.configure(background="#ff00ff", foreground="#ffffff", text="SAVE");
          self.BTN_Save.place(anchor="nw", height=40, width=65, x=10, y=15);

          self.BTN_Load = tk.Button(self.LFRM_Save_and_Load, command=Handle_Button_Load);
          self.BTN_Load.configure(background="#ff00ff", foreground="#ffffff", text="LOAD");
          self.BTN_Load.place(anchor="nw", height=40, width=65, x=83, y=15);

          self.BTN_NEW = tk.Button(self.LFRM_Save_and_Load, command=Handle_Button_New);
          self.BTN_NEW.configure(background="#ff00ff", foreground="#ffffff", text="NEW");
          self.BTN_NEW.place(anchor="nw", height=40, width=65, x=155, y=15);          

          self.BTN_Cheat = tk.Button(self.LFRM_Save_and_Load, command=Handle_Button_Cheat);
          self.BTN_Cheat.configure(background="#FF0000", foreground="#ffffff", text="CHEAT: G Mode");
          self.BTN_Cheat.place(anchor="nw", height=30, width=100, x=120, y=70);

          self.BTN_Cheat_Map = tk.Button(self.LFRM_Save_and_Load, command=Handle_Button_Cheat_Map);
          self.BTN_Cheat_Map.configure(background="#FF0000", foreground="#ffffff", text="CHEAT: Map");
          self.BTN_Cheat_Map.place(anchor="nw", height=30, width=100, x=10, y=70);

        #---H. Frame: Character Stats -----------------------------------------------------------
          self.LFRM_Character_Stats = tk.LabelFrame(self.FRM_Main);
          self.LFRM_Character_Stats.configure(background="#e3d3f8", foreground="#000000", height=190, width=495);
          self.LFRM_Character_Stats.configure(borderwidth=3, relief="sunken", text="Character Stats");
          self.LFRM_Character_Stats.place(anchor="nw", height=190, width=495, x=539, y=560);        

          self.LAB_Name = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Name.configure(background="#e3d3f8", text="Name:");
          self.LAB_Name.place(anchor="nw", height=20, width=50, x=4, y=6);

          self.LAB_Name_Output = tk.Label(self.LFRM_Character_Stats)
          self.LAB_Name_Output.configure(background="#e3d3f8", foreground="#ff0000", justify="center");
          self.LAB_Name_Output.configure(borderwidth=3, relief="sunken", text=" Carly Salali Germany");      
          self.LAB_Name_Output.place(anchor="nw", height=20, width=150, x=65, y=6);        

          self.LAB_Gender = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Gender.configure(background="#e3d3f8", text="Gender:");
          self.LAB_Gender.place(anchor="nw", height=20, width=50, x=4, y=28);

          self.LAB_Gender_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Gender_Output.configure(background="#e3d3f8", foreground="#ff0000", justify="center");
          self.LAB_Gender_Output.configure(borderwidth=3, relief="sunken", text=" Female");
          self.LAB_Gender_Output.place(anchor="nw", height=20, width=150, x=65, y=28);   

          self.LAB_Class = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Class.configure(background="#e3d3f8", text="Class:");
          self.LAB_Class.place(anchor="nw", height=20, width=50, x=4, y=51);

          self.LAB_Class_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Class_Output.configure(background="#e3d3f8", foreground="#ff0000", justify="center");
          self.LAB_Class_Output.configure(borderwidth=3, relief="sunken", text=" Alicorn");
          self.LAB_Class_Output.place(anchor="nw", height=20, width=150, x=65, y=51);

          self.LAB_Health = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Health.configure(background="#e3d3f8", text="Health:");
          self.LAB_Health.place(anchor="nw", height=20, width=50, x=4, y=72);

          self.LAB_Health_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Health_Output.configure(background="#e3d3f8", foreground="#ff0000", justify="center");
          self.LAB_Health_Output.configure(borderwidth=3, relief="sunken", text=" 20000");
          self.LAB_Health_Output.place(anchor="nw", height=20, width=150, x=65, y=72);

          self.LAB_Mag_Eng = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Mag_Eng.configure(background="#e3d3f8", text="Mag Eng:");
          self.LAB_Mag_Eng.place(anchor="nw", height=20, width=50, x=4, y=93);

          self.LAB_Mag_Eng_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Mag_Eng_Output.configure(background="#e3d3f8",  foreground="#ff0000", justify="center");
          self.LAB_Mag_Eng_Output.configure(borderwidth=3, relief="sunken", text=" 5000");
          self.LAB_Mag_Eng_Output.place(anchor="nw", height=20, width=150, x=65, y=93);

          self.LAB_Attack = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Attack.configure(background="#e3d3f8", text="Attack:");
          self.LAB_Attack.place(anchor="nw", height=20, width=50, x=4, y=115);

          self.LAB_Attack_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Attack_Output.configure(background="#e3d3f8",  foreground="#ff0000", justify="center");
          self.LAB_Attack_Output.configure(borderwidth=3, relief="sunken", text=" 2000");
          self.LAB_Attack_Output.place(anchor="nw", height=20, width=150, x=65, y=115);

          self.LAB_Defense = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Defense.configure(background="#e3d3f8", text="Defense:");
          self.LAB_Defense.place(anchor="nw", height=20, width=50, x=4, y=136);

          self.LAB_Defense_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Defense_Output.configure(background="#e3d3f8",  foreground="#ff0000", justify="center");
          self.LAB_Defense_Output.configure(borderwidth=3, relief="sunken", text=" 8000");
          self.LAB_Defense_Output.place(anchor="nw", height=20, width=150, x=65, y=136);

          self.LAB_Charisma = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Charisma.configure(background="#e3d3f8", text="Charisma:");
          self.LAB_Charisma.place(anchor="nw", height=20, width=60, x=275, y=6);

          self.LAB_Charisma_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Charisma_Output.configure(background="#e3d3f8",  foreground="#ff0000", justify="center");
          self.LAB_Charisma_Output.configure(borderwidth=3, relief="sunken", text=" 7777");
          self.LAB_Charisma_Output.place(anchor="nw", height=20, width=120, x=360, y=6);       

          self.LAB_Combat_Exp = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Combat_Exp.configure(background="#e3d3f8", text="Combat Exp:");
          self.LAB_Combat_Exp.place(anchor="nw", height=20, width=70, x=275, y=28);

          self.LAB_Combat_Exp_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Combat_Exp_Output.configure(background="#e3d3f8",  foreground="#ff0000", justify="center");
          self.LAB_Combat_Exp_Output.configure(borderwidth=3, relief="sunken", text=" 1000");
          self.LAB_Combat_Exp_Output.place(anchor="nw", height=20, width=120, x=360, y=28);

          self.LAB_Level = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Level.configure(background="#e3d3f8", text="Level:");
          self.LAB_Level.place(anchor="nw", height=20, width=50, x=275, y=51);

          self.LAB_Level_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Level_Output.configure(background="#e3d3f8",  foreground="#ff0000", justify="center");
          self.LAB_Level_Output.configure(borderwidth=3, relief="sunken", text=" 9000");
          self.LAB_Level_Output.place(anchor="nw", height=20, width=120, x=360, y=51);

          self.LAB_Armor = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Armor.configure(background="#e3d3f8", text="Armor:");
          self.LAB_Armor.place(anchor="nw", height=20, width=50, x=275, y=72);

          self.LAB_Armor_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Armor_Output.configure(background="#e3d3f8",  foreground="#ff0000", justify="center");
          self.LAB_Armor_Output.configure(borderwidth=3, relief="sunken", text=" Plate Mail");
          self.LAB_Armor_Output.place(anchor="nw", height=20, width=120, x=360, y=72);

          self.LAB_Weapon = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Weapon.configure(background="#e3d3f8", text="Weapon:");
          self.LAB_Weapon.place(anchor="nw", height=20, width=50, x=275, y=93);

          self.LAB_Weapon_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Weapon_Output.configure(background="#e3d3f8",  foreground="#ff0000", justify="center");
          self.LAB_Weapon_Output.configure(borderwidth=3, relief="sunken", text=" Power Staff");
          self.LAB_Weapon_Output.place(anchor="nw", height=20, width=120, x=360, y=93);

          self.LAB_Magic = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Magic.configure(background="#e3d3f8", text="Magic:");
          self.LAB_Magic.place(anchor="nw", height=20, width=50, x=275, y=115);

          self.LAB_Magic_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Magic_Output.configure(background="#e3d3f8",  foreground="#ff0000", justify="center");
          self.LAB_Magic_Output.configure(borderwidth=3, relief="sunken", text=" Telekinesis");
          self.LAB_Magic_Output.place(anchor="nw", height=20, width=120, x=360, y=115);

          self.LAB_Money = tk.Label(self.LFRM_Character_Stats, anchor="w");
          self.LAB_Money.configure(background="#e3d3f8", text="Money:");
          self.LAB_Money.place(anchor="nw", height=20, width=50, x=275, y=136);

          self.LAB_Money_Output = tk.Label(self.LFRM_Character_Stats);
          self.LAB_Money_Output.configure(background="#e3d3f8",  foreground="#ff0000", justify="center");
          self.LAB_Money_Output.configure(borderwidth=3, relief="sunken", text=" 100");
          self.LAB_Money_Output.place(anchor="nw", height=20, width=120, x=360, y=136);

        #---Create main Menu Bar-------------------------------------------------------   
          self.master = master;
          self.Main_Menu_Bar = tk.Menu(self.master);
          self.master.config(menu = self.Main_Menu_Bar);

          #File Menu
          self.File_Menu = tk.Menu(self.Main_Menu_Bar, tearoff=0);
          self.File_Menu.add_command(label="NEW Game", command=File_Menu_NEW_Handler);
          self.File_Menu.add_command(label="SAVE Game", command=File_Menu_SAVE_Handler);
          self.File_Menu.add_command(label="LOAD Game", command=File_Menu_LOAD_Handler);
          self.File_Menu.add_command(label="EXIT Game", command=window.destroy); #use this one if using child frames and windows
          #self.File_Menu.add_command(label="Exit", command=window.quit); #built-in method closes window 
          self.File_Menu.add_separator(); # Add separator line to menu
          self.File_Menu.add_command(label="Future 1", command=File_Menu_Future1_Handler);
          self.File_Menu.add_command(label="Future 2", command=File_Menu_Future2_Handler);
          self.Main_Menu_Bar.add_cascade(label="File", menu=self.File_Menu); #adds menu File_Menu to Main_Menu_Bar             

          #Edit Menu
          self.Edit_Menu = tk.Menu(self.Main_Menu_Bar, tearoff=0);
          self.Edit_Menu.add_command(label="CHEAT: G Mode", command=Edit_Menu_CHEAT_Handler);
          self.Edit_Menu.add_command(label="CHEAT: Master Map", command=Edit_Menu_CHEAT_Master_Map_Handler);
          self.Edit_Menu.add_command(label="Undo", command=Edit_Menu_UNDO_Handler);
          self.Edit_Menu.add_command(label="Redo", command=Edit_Menu_REDO_Handler);
          self.Edit_Menu.add_command(label="Cut", command=Edit_Menu_CUT_Handler);
          self.Edit_Menu.add_command(label="Copy", command=Edit_Menu_COPY_Handler);
          self.Edit_Menu.add_command(label="Paste", command=Edit_Menu_PASTE_Handler);
          self.Edit_Menu.add_command(label="Delete", command=Edit_Menu_DELETE_Handler);
          self.Edit_Menu.add_command(label="Select All", command=Edit_Menu_SELECTALL_Handler);    
          self.Main_Menu_Bar.add_cascade(label="Edit", menu=self.Edit_Menu); #adds menu File_Menu to Main_Menu_Bar      

          #View Menu
          self.View_Menu = tk.Menu(self.Main_Menu_Bar, tearoff=0);
          self.View_Menu.add_command(label="Zoom In +", command=View_Menu_ZOOMIN_Handler);
          self.View_Menu.add_command(label="Zoom Out -", command=View_Menu_ZOOMOUT_Handler);
          self.View_Menu.add_command(label="Status Bar", command=View_Menu_STATUSBAR_Handler);
          self.Main_Menu_Bar.add_cascade(label="View", menu=self.View_Menu); #adds menu File_Menu to Main_Menu_Bar    

          #Help Menu
          self.Help_Menu = tk.Menu(self.Main_Menu_Bar, tearoff=0);
          self.Help_Menu.add_command(label="Help", command=Help_Menu_HELP_Handler);
          self.Help_Menu.add_command(label="About", command=Help_Menu_ABOUT_Handler);
          self.Main_Menu_Bar.add_cascade(label="Help", menu=self.Help_Menu); #adds menu File_Menu to Main_Menu_Bar       

          #Initial Values After Loading Main Window Frame
          self.Initialize_Game();
        
#---End Class-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-----Invocations-----
GUI = RPG_GUI(window); #instantiate GUI class

#---Launch Main Window---
window.mainloop();







     