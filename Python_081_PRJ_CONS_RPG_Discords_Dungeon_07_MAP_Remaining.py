
#Title: Discord's Dungeon 07 - Coding Remaining MAP and Navigation. Completing and Polishing Level 1 Template.
#Project: Discord's Dungeon - A Python Text-Based RPG
#Author: Carly Salali Germany
#Date: 01/19/2022
#Description: A project-based approach to teach the basic structures of Python by incorporating each new concept into a text-based RPG.


#Imports
from os import system,name;
import random,math;
import time;
import os;
from os import listdir;
from os.path import isfile, join;

#Globals
Player_Opponent = None;
Player_Heroine = None;

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Game MAP Globals
CurrentLocation = "NOWHERE";

#MAP Location Globals
CENTER_FirstTime = "TRUE";
CelestiasPalace_FirstTime = "TRUE";
DiscordsLair_FirstTime = "TRUE";
FriendshipForest_FirstTime = "TRUE";

#MAP L1 Combat Globals
S1_Abominable_Alive = "TRUE";
W2_Giant_Alive = "TRUE";
SwampOfSadness_BloodBat_Alive = "TRUE";
E3_DragonFish_Alive = "TRUE";
N3_FireRat_Alive = "TRUE";
S3_CarnivorousPlant_Alive = "TRUE";
DiscordsLair_Alive = "TRUE";
S2_MotleyCrewAlive = "TRUE";
UNDERGROUND_DragonPairAlive = "TRUE";
Willing_to_Fight = "TRUE";

#MAP L1 Inventory Items Globals
Found_Staff = "FALSE";
Found_Pendant = "FALSE";
Found_Sigil = "FALSE";
Found_Orb = "FALSE";
Found_PrincessCloak = "FALSE";
Found_Chain_Mail = "FALSE";
Found_Plate_Armor = "FALSE";

#MAP L1 Skill Items Globals
Acquired_IceBlasts = "FALSE";
Acquired_FireBalls = "FALSE";
Acquired_Lightning = "FALSE";
Acquired_Telekinesis = "FALSE";
Acquired_Telepathy = "FALSE";
Acquired_Teleportation = "FALSE";
Acquired_TimeWarp = "FALSE";
Acquired_Invisibility = "FALSE";
Acquired_Healing = "FALSE";
Acquired_FriendshipCast = "FALSE";

#MAP L1 Potions Globals
Found_HealingPotion_1 = "FALSE";
Found_HealingPotion_2 = "FALSE";
Found_HealingPotion_3 = "FALSE";
Found_HealingPotion_4 = "FALSE";
Found_HealingPotion_CelestiasPalace = "FALSE";

#MAP L1 NPCs Globals
NPC1_Encountered = "FALSE";
NPC2_Encountered = "FALSE";
NPC3_Encountered = "FALSE";

#MAP L1 Traps Globals
TRAP1_Encountered = "FALSE";
TRAP2_Encountered = "FALSE";
TRAP3_Encountered = "FALSE";
TRAP4_Encountered = "FALSE";

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Prime Parent (base) Class--------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Game_Entity:
      #Class Attributes 
      EntityName = "Anonymous Entity";
      EntityGender = "Female";
      EntityClass = "Undetermined";      
      EntityHealth = 50;
      EntityDefense = 5;
      EntityAttack = 5;
      EntityMagicPower = 10;
      WeaponChoice = "None";
      MagicChoice= "None";
      ArmorChoice = "None";
      Invisibility_Active = "FALSE";
      Invisibility_Count = 0;
      FirstTimeShowOpponentInfo = "TRUE";
      
      Dammage_Item_Staff = 10;
      Dammage_Item_Pendant = 15;
      Dammage_Item_Sigil = 20;
      Dammage_Item_Orb = 25;
      Dammage_Item_PrincessCloak = 30;

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

      INV_Has_Staff = "FALSE";
      INV_Has_Pendant = "FALSE";
      INV_Has_Sigil = "FALSE";
      INV_Has_Orb = "FALSE";
      INV_Has_PrincessCloak = "FALSE";
      INV_Has_HealingPotions = 0;
      HealthPotion_Restore_Amt = 100;

      INV_Has_Chain_Mail = "FALSE";
      INV_Has_Plate_Armor = "FALSE";      

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
          self.EntityHealth = 32000;
          self.EntityDefense = 20000;
          self.EntityAttack = 20000;
          self.EntityMagicPower = 32000;   
          self.Dammage_Item_Staff = 100;
          self.Dammage_Item_Pendant = 150;
          self.Dammage_Item_Sigil = 200;
          self.Dammage_Item_Orb = 250;
          self.Dammage_Item_PrincessCloak = 300;
          self.DEF_Item_Chain_Mail = 500;
          self.DEF_Item_Plate_Armor = 1000;
          self.Dammage_Skill_IceBlasts = 100;
          self.Dammage_Skill_FireBalls = 200;
          self.Dammage_Skill_Lightning = 300;
          self.Dammage_Skill_Telekinesis = 400;
          self.Dammage_Skill_Telepathy = 500;
          self.Dammage_Skill_Teleportation = 600;
          self.Dammage_Skill_TimeWarp = 700;
          self.Invisibility_DEF_Amt = 10000;
          self.INV_Has_Staff = "TRUE";
          self.INV_Has_Pendant = "TRUE";
          self.INV_Has_Sigil = "TRUE";
          self.INV_Has_Orb = "TRUE";
          self.INV_Has_PrincessCloak = "TRUE";
          self.INV_Has_HealingPotions = 5000;
          self.HealthPotion_Restore_Amt = 300;
          self.INV_Has_Chain_Mail = "TRUE";
          self.INV_Has_Plate_Armor = "TRUE";
          self.DEF_Item_Chain_Mail = 1000;
          self.DEF_Item_Plate_Armor = 5000;
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

    #END-MemberMethod-Cheat_Mode---------------------------------------------------------------------------------------------          


    #MemberMethod---------------------------------------------------------------------------------------------------------------
      def Display_Entity(self):
          print("\n     ",self.EntityClass,"Stats:");
          print("     ","Name:",self.EntityName);
          print("     ","Gender:",self.EntityGender);
          print("     ","Class:",self.EntityClass);
          print("     ","Health:",self.EntityHealth);
          print("     ","Defense:",self.EntityDefense);
          print("     ","Attack:",self.EntityAttack);
          print("     ","MagicPower:",self.EntityMagicPower);           
    #END-MemberMethod-Display_Entity---------------------------------------------------------------------------------------------


    #MemberMethod---------------------------------------------------------------------------------------------------------------
      def Display_Character(self):
          self.Display_Entity();
          STATS = "";
          if self.WeaponChoice == "None": 
             STATS = STATS + "Nothing but ";
             if self.EntityGender == "Female": STATS = STATS + "her";
             elif self.EntityGender == "Male": STATS = STATS + "his";
             STATS = STATS + " hooves!";
          elif self.WeaponChoice == "Staff": STATS = STATS + "Staff" + "   +ATK: " + str(self.Dammage_Item_Staff);
          elif self.WeaponChoice == "Pendant": STATS = STATS + "Pendant"  + "   +ATK: " + str(self.Dammage_Item_Pendant);
          elif self.WeaponChoice == "Sigil": STATS = STATS + "Sigil"  + "   +ATK: " + str(self.Dammage_Item_Sigil);
          elif self.WeaponChoice == "Orb": STATS = STATS + "Orb"  + "   +ATK: " + str(self.Dammage_Item_Orb);
          elif self.WeaponChoice == "PrincessCloak": STATS = STATS + "PrincessCloak"  + "   +ATK: " + str(self.Dammage_Item_PrincessCloak);
          print("     ","Selected Weapon:",STATS);
      
          STATS = "";
          if self.ArmorChoice == "None": 
             STATS = STATS + "Nothing but ";
             if self.EntityGender == "Female": STATS = STATS + "her";
             elif self.EntityGender == "Male": STATS = STATS + "his";
             STATS = STATS + " birthday suit.";
          elif self.ArmorChoice == "ChainMail": STATS = STATS + "Link Chain Mail" + "   +DEF: " + str(self.DEF_Item_Chain_Mail);
          elif self.ArmorChoice == "PlateArmor": STATS = STATS + "Plate Armor" + "   +DEF: " + str(self.DEF_Item_Plate_Armor);   
          print("     ","Selected Armor:",STATS);
          
          STATS = "";
          if self.MagicChoice == "None": 
             STATS = STATS + "Nothing but ";
             if self.EntityGender == "Female": STATS = STATS + "her";
             elif self.EntityGender == "Male": STATS = STATS + "his";
             STATS = STATS + " wits!";
          elif self.MagicChoice == "IceBlasts": STATS = STATS + "Ice Blasts" + "   +ATK: " + str(self.Dammage_Skill_IceBlasts);
          elif self.MagicChoice == "FireBalls": STATS = STATS + "Fire Balls" + "   +ATK: " + str(self.Dammage_Skill_FireBalls);            
          elif self.MagicChoice == "Lightning": STATS = STATS + "Lightning" + "   +ATK: " + str(self.Dammage_Skill_Lightning);
          elif self.MagicChoice == "Telekinesis": STATS = STATS + "Telekinesis" + "   +ATK: " + str(self.Dammage_Skill_Telekinesis);
          elif self.MagicChoice == "Telepathy": STATS = STATS + "Telepathy" + "   +ATK: " + str(self.Dammage_Skill_Telepathy);
          elif self.MagicChoice == "Teleportation": STATS = STATS + "Teleportation" + "   +ATK: " + str(self.Dammage_Skill_Teleportation);
          elif self.MagicChoice == "TimeWarp": STATS = STATS + "Time Warp" + "   +ATK: " + str(self.Dammage_Skill_TimeWarp);
          elif self.MagicChoice == "Invisibility": STATS = STATS + "Invisibility";
          elif self.MagicChoice == "Healing": STATS = STATS + "Healing"; 
          elif self.MagicChoice == "FriendshipCast": STATS = STATS + "Friendship Cast";
          print("     ","Selected Magic:",STATS); 

          if(self.Invisibility_Active == "TRUE"):
             print("      Invisibility: Active!   [Remaining:",self.Invisibility_Count,"\b]   [+DEF:",self.Invisibility_DEF_Amt,"\b]"); 
    #END-MemberMethod-Display_Character------------------------------------------------------------------------------------------------    

    #MemberMethod---------------------------------------------------------------------------------------------------------------
      def Inventory_Display(self):
          print("\n----------------------------Current Inventory----------------------------");
          if(self.INV_Has_Staff == "FALSE" and self.INV_Has_Pendant == "FALSE" and self.INV_Has_Sigil == "FALSE" and self.INV_Has_Orb == "FALSE" and 
             (self.INV_Has_HealingPotions <= 0) and self.INV_Has_Chain_Mail == "FALSE" and self.INV_Has_Plate_Armor == "FALSE"):
              print("\n     ",self.EntityName,"has abolutely NOTHING! Not a single thing. Nothing at all. A big NOPE. Go FIND something!");
          else:   
                InvCount = 0;
                if(self.INV_Has_Staff == "TRUE"):
                   InvCount = InvCount + 1;
                   print("      ",InvCount,"\b. (S)taff                    (ATK +",self.Dammage_Item_Staff,"\b)");
                if(self.INV_Has_Pendant == "TRUE"):
                   InvCount = InvCount + 1;
                   print("      ",InvCount,"\b. (P)endant                  (ATK +",self.Dammage_Item_Pendant,"\b)");
                if(self.INV_Has_Sigil == "TRUE"):
                   InvCount = InvCount + 1;
                   print("      ",InvCount,"\b. (M)agic Sigil              (ATK +",self.Dammage_Item_Sigil,"\b)");
                if(self.INV_Has_Orb == "TRUE"):
                   InvCount = InvCount + 1;
                   print("      ",InvCount,"\b. (O)rb of Power             (ATK +",self.Dammage_Item_Orb,"\b)");
                if(self.INV_Has_PrincessCloak == "TRUE"):
                   InvCount = InvCount + 1;
                   print("      ",InvCount,"\b. (C)loak of Princessness    (ATK +",self.Dammage_Item_PrincessCloak,"\b)");
                if(self.INV_Has_HealingPotions > 0):
                   InvCount = InvCount + 1;
                   print("      ",InvCount,"\b. (H)ealingPotions:          (Health +",self.HealthPotion_Restore_Amt,"\b)    Amt:",self.INV_Has_HealingPotions);
                if(self.INV_Has_Chain_Mail == "TRUE"):
                   InvCount = InvCount + 1;
                   print("      ",InvCount,"\b. (L)inked Chain Mail        (DEF +",self.DEF_Item_Chain_Mail,"\b)");
                if(self.INV_Has_Plate_Armor == "TRUE"):
                   InvCount = InvCount + 1;
                   print("      ",InvCount,"\b. (A)rmor Plating            (DEF +",self.DEF_Item_Plate_Armor,"\b)");
          print("-------------------------------------------------------------------------");   
    #END-MemberMethod-Inventory_Display--------------------------------------------------------------------------------------


    #MemberMethod------------------------------------------------------------------------------------------------------------
      def Inventory_Equip(self):
          self.Inventory_Display();
          CHOICE = input("\n       Select item to equip (n = NOTHING): ");
          CHOICE = CHOICE.lower();

          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "p" and CHOICE != "m" and CHOICE != "o" and CHOICE != "c" and CHOICE != "h" and CHOICE != "l" and CHOICE != "a"):
             print("\nThat was an invalid choice.");
          else:
               if(CHOICE == "n"):
                  print("\n      You choose NOTHING. De-equipping inventory.");
                  self.WeaponChoice = "None";             
               elif(CHOICE == "s"):
                    if(self.INV_Has_Staff == "TRUE"):
                       print("\n      You grasp the magic Staff in your hand. A personal weapon!");
                       self.WeaponChoice = "Staff";
                    else: print("\n      Sorry, you don't have a Staff."); 
               elif(CHOICE == "p"):
                    if(self.INV_Has_Pendant == "TRUE"):
                       print("\n      You stroke the magic Pendant to activate it. What an accessory!");
                       self.WeaponChoice = "Pendant";
                    else: print("\n      Sorry, you don't have a Pendant.");  
               elif(CHOICE == "m"):
                    if(self.INV_Has_Sigil == "TRUE"):
                       print("\n      You initialize the magic Sigil. Metallic vibrations fill the air!");
                       self.WeaponChoice = "Sigil";
                    else: print("\n      Sorry, you don't have a Sigil.");  
               elif(CHOICE == "o"):
                    if(self.INV_Has_Pendant == "TRUE"):
                       print("\n      You choose the Orb of Power. Blinding light emanates from the Orb.");
                       self.WeaponChoice = "Orb";
                    else: print("\n      Sorry, you don't have a Pendant.");  
               elif(CHOICE == "c"):
                    if(self.INV_Has_Pendant == "TRUE"):
                       print("\n      You choose the Cloak of Princessness. Your body tingles with celestial energy as you pull it around yourself.");
                       self.WeaponChoice = "PrincessCloak";
                    else: print("\n      Sorry, you don't have a PrincessCloak.");
               elif(CHOICE == "h"):
                    if(self.INV_Has_HealingPotions > 0):
                       print("\n      You open a flask and drink a healing potion, restoring",self.HealthPotion_Restore_Amt,"health!");
                       self.EntityHealth = self.EntityHealth + self.HealthPotion_Restore_Amt ;
                       self.INV_Has_HealingPotions = self.INV_Has_HealingPotions - 1;
                    else: print("\n      Sorry, you don't have any Healing potions at the moment.");
               elif(CHOICE == "l"):
                    if(self.INV_Has_Chain_Mail == "TRUE"):
                       print("\n      You choose to don upon yourself the Link Chain Mail armor. This increases your DEFENSE capability by",self.DEF_Item_Chain_Mail,".");
                       self.ArmorChoice = "ChainMail";
                    else: print("\n      Sorry, you don't have any Link Chain Mail armor.");
               elif(CHOICE == "a"):
                    if(self.INV_Has_Plate_Armor == "TRUE"):
                       print("\n      You choose to wear the Plate Armor. Excellent! This increases your DEFENSE capability by",self.DEF_Item_Plate_Armor,".");
                       self.ArmorChoice = "PlateArmor";
                    else: print("\n      Sorry, you don't have any Plate Armor.");                                            

               self.Display_Character();

    #END-MemberMethod-Inventory_Equip----------------------------------------------------------------------------------------   


    #MemberMethod---------------------------------------------------------------------------------------------------------------
      def SKILL_Display(self):
          print("\n------------------Acquired Magic Skills------------------");
          if(self.SKILL_Has_IceBlasts == "FALSE" and self.SKILL_Has_FireBalls == "FALSE" and self.SKILL_Has_Lightning == "FALSE" and
             self.SKILL_Has_Telekinesis == "FALSE" and self.SKILL_Has_Telepathy == "FALSE" and self.SKILL_Has_Teleportation == "FALSE"
             and self.SKILL_Has_TimeWarp == "FALSE" and self.SKILL_Has_Invisibility == "FALSE" and self.SKILL_Has_Healing == "FALSE"
             and self.SKILL_Has_FriendshipCast  == "FALSE"):
             print("\n     ",self.EntityName,"has NO magic skills yet. Absolutely none. Go learn some!");
          else:    
                SkillCount = 0;
                if(self.SKILL_Has_IceBlasts == "TRUE"):
                   SkillCount = SkillCount + 1;
                   print("      ",SkillCount,"\b. (I)ce Blasts              (ATK +",self.Dammage_Skill_IceBlasts,"\b)");
                if(self.SKILL_Has_FireBalls == "TRUE"):
                   SkillCount = SkillCount + 1;
                   print("      ",SkillCount,"\b. (F)ire Balls              (ATK +",self.Dammage_Skill_FireBalls,"\b)");
                if(self.SKILL_Has_Lightning == "TRUE"):
                   SkillCount = SkillCount + 1;
                   print("      ",SkillCount,"\b. (L)ightning               (ATK +",self.Dammage_Skill_Lightning,"\b)");
                if(self.SKILL_Has_Telekinesis == "TRUE"):
                   SkillCount = SkillCount + 1;
                   print("      ",SkillCount,"\b. (T)elekinesis             (ATK +",self.Dammage_Skill_Telekinesis,"\b)");
                if(self.SKILL_Has_Telepathy == "TRUE"):
                   SkillCount = SkillCount + 1;
                   print("      ",SkillCount,"\b. (M)ental Telepathy        (ATK +",self.Dammage_Skill_Telepathy,"\b)");
                if(self.SKILL_Has_Teleportation == "TRUE"):
                   SkillCount = SkillCount + 1;
                   print("      ",SkillCount,"\b. (S)pace Teleportation     (ATK +",self.Dammage_Skill_Teleportation,"\b)");
                if(self.SKILL_Has_TimeWarp == "TRUE"):
                   SkillCount = SkillCount + 1;
                   print("      ",SkillCount,"\b. (W)arp Time               (ATK +",self.Dammage_Skill_TimeWarp,"\b)");
                if(self.SKILL_Has_Invisibility == "TRUE"):
                   SkillCount = SkillCount + 1;
                   print("      ",SkillCount,"\b. (A)ctivate Invisibility"); 
                if(self.SKILL_Has_Healing == "TRUE"):
                   SkillCount = SkillCount + 1;
                   print("      ",SkillCount,"\b. (H)ealing");
                if(self.SKILL_Has_FriendshipCast == "TRUE"):
                   SkillCount = SkillCount + 1;
                   print("      ",SkillCount,"\b. (C)ast Friendship");   
          print("---------------------------------------------------------");                                                                        
    #END-MemberMethod-SKILL_Display----------------------------------------------------------------------------------------  


    #MemberMethod------------------------------------------------------------------------------------------------------------
      def SKILL_Equip(self):
          self.SKILL_Display();
          CHOICE = input("\n      Select magic skill to equip (n = NOTHING): ");
          CHOICE = CHOICE.lower();

          if(CHOICE != "n" and CHOICE != "i" and CHOICE != "f" and CHOICE != "l" and CHOICE != "t" and CHOICE != "m" and CHOICE != "s" and CHOICE != "w" and CHOICE != "a" and CHOICE != "h" and CHOICE != "c"):
             print("\nThat was an inalid choice.");
          else:
               if(CHOICE == "n"):
                  print("\nYou choose NOTHING. De-equipping all magic skills.");
                  self.MagicChoice = "None";             
               elif(CHOICE == "i"):
                    if(self.SKILL_Has_IceBlasts == "TRUE"):
                       print("\nThe ambient temperature around you lowers. You prepare an IceBlast!");
                       self.MagicChoice = "IceBlasts";
                    else: print("\nSorry, you haven't acquired the IceBlast skill yet."); 
               elif(CHOICE == "f"):
                    if(self.SKILL_Has_FireBalls == "TRUE"):
                       print("\nThe air begins to ripple with heat and plasma coalesces as you prepare FireBalls!");
                       self.MagicChoice = "FireBalls";
                    else: print("\nSorry, you haven't acquired the FireBall skill yet.");  
               elif(CHOICE == "l"):
                    if(self.SKILL_Has_Lightning == "TRUE"):
                       print("\nCrack! Pop! You charge the air around you with electric potential and prepare Lightning!");
                       self.MagicChoice = "Lightning";
                    else: print("\nSorry, you haven't acquired the Lightning skill yet."); 
               elif(CHOICE == "t"):
                    if(self.SKILL_Has_Telekinesis == "TRUE"):
                       print("\nThe matter around you ripples as your mind wraps itself around the spacetime near you. You activate Telekinesis!");
                       self.MagicChoice = "Telekinesis";
                    else: print("\nSorry, you haven't acquired the Telekinesis skill yet.");
               elif(CHOICE == "m"):
                    if(self.SKILL_Has_Telepathy == "TRUE"):
                       print("\nYou hear the voices of others around you as you open your mind. You activate Mental Telepathy!");
                       self.MagicChoice = "Telepathy";
                    else: print("\nSorry, you haven't acquired the Mental Telepathy skill yet."); 
               elif(CHOICE == "s"):
                    if(self.SKILL_Has_Teleportation == "TRUE"):
                       print("\nSpacetime forms a bublle around you, separating you from reality. You initialize Space Teleportation!");
                       self.MagicChoice = "Teleportation";
                    else: print("\nSorry, you haven't acquired the SpaceTime Teleportation skill yet.");    
               elif(CHOICE == "w"):
                    if(self.SKILL_Has_TimeWarp == "TRUE"):
                       print("\nTime begins to slow and swirl around you in every direction. You trigger a Time Warp!");
                       self.MagicChoice = "TimeWarp";
                    else: print("\nSorry, you haven't acquired the Warp Time skill yet."); 
               elif(CHOICE == "a"):
                    if(self.SKILL_Has_Invisibility == "TRUE"):
                       if(self.EntityMagicPower - self.SKILL_Invisibility_Cost > 0):
                          MESSAGE = MESSAGE + "Invisibility Active! " + self.EntityName + " bends light around themselves to become invisible, enhancing their defense."; 
                          self.Invisibility_Active = "TRUE";
                          self.Invisibility_Count = self.Invisibility_Count +3;
                          self.EntityMagicPower = self.EntityMagicPower - self.SKILL_Invisibility_Cost;
                          print("\nYour visible profile disappears and you fade away. You have energized this skill to last",self.Invisibility_Count,"combat rounds.");
                       else: MESSAGE = MESSAGE + "Sorry, you do not have enough magic power to activate a Invisibility.";  
                    else: print("\nSorry, you haven't acquired the Invisbility skill yet.");     
               elif(CHOICE == "h"):
                    if(self.SKILL_Has_Healing == "TRUE"):
                       MESSAGE = MESSAGE + "Healing! " + self.EntityName + " attempts to focus and concentrate magic energy around themselves ..."; 
                       if(self.EntityMagicPower - self.SKILL_Healing_Restore_Amt > 0):
                             self.EntityMagicPower = self.EntityMagicPower - self.SKILL_Healing_Restore_Amt;  
                             self.EntityHealth = self.EntityHealth + self.SKILL_Healing_Restore_Amt;
                             print("\nYou lay hands upon yourself and cause healing energy to surge throughout your body, adding",self.SKILL_Healing_Restore_Amt,"to your health.");
                       else: MESSAGE = MESSAGE + "Sorry, although you possess the skill, you do not have enough magic power to implement Healing."; 
                    else: print("\nSorry, you haven't acquired the Healing skill yet."); 
               elif(CHOICE == "c"):
                    if(self.SKILL_Has_FriendshipCast == "TRUE"):
                       print("\nYou cast Friendship on everyone within proximity. Your opponents feel much less agressive.");
                       self.MagicChoice = "FriendshipCast";
                    else: print("\nSorry, you haven't acquired the FriendshipCast skill yet.");  

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
          MESSAGE = "";

          system("cls");
          print("\n----------------------Beginning " + self.EntityName + "'s entity attack sequence----------------------");
          time.sleep(2);

          if(self.FirstTimeShowOpponentInfo == "TRUE"):
             print("\nThe Opponent being faced:");
             Opponent.Display_Character();
             self.FirstTimeShowOpponentInfo = "FALSE"
             time.sleep(6);
             system("cls");
             
          print("\n",Opponent.EntityName,"\b's health BEFORE",self.EntityName,"\b's attack:",Opponent.EntityHealth);
          
          #1.Generate base dammage to opponent for this combat round.
          DAMMAGE = random.randint(MinDammage,MaxDammage);
          print("\n ",self.EntityName," generates [",DAMMAGE,"] of random base dammage due to their magical prowess and strength.",sep='');
          time.sleep(4);

          #2.Add ATK skill and experience of Entitiy to base dammage generated.
          DAMMAGE_ATK = random.randint(1,self.EntityAttack);
          print("\n ",self.EntityName," generates [",DAMMAGE_ATK,"] additional dammage due to their attack skill and experience.",sep='');
          DAMMAGE = DAMMAGE + DAMMAGE_ATK;
          time.sleep(4);          

          #3.If class of object allowed to use a magic ITEM? Process that Entity's choice and calculate additional dammage.
          if(self.EntityClass == "Princess" or self.EntityClass == "Alicorn" or self.EntityClass =="Supreme Agent of Chaos"):
             if(self.WeaponChoice == "None" or self.WeaponChoice == "Staff" or self.WeaponChoice == "Pendant" or self.WeaponChoice == "Sigil" or 
                self.WeaponChoice == "Orb" or self.WeaponChoice == "PrincessCloak"):
                if self.WeaponChoice == "None": 
                   MESSAGE = "\n Foregoing the use of any magic items, " + self.EntityName + " fights with bare hooves of horror!\n";              
                else: 
                   MESSAGE = "\n " + self.EntityName + " chooses to use a MAGIC item!\n";  
                   if self.WeaponChoice == "Staff": 
                      MESSAGE = MESSAGE + " They raise their Staff to fire a bolt of lightning! Zzzzzt! (possible +" + str(self.Dammage_Item_Staff) + ")";
                      DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Staff - 3),self.Dammage_Item_Staff); 
                   elif self.WeaponChoice == "Pendant": 
                        MESSAGE = MESSAGE + " They touch their Pendant enveloping thier opponent in flames! Woosh! (possible +" + str(self.Dammage_Item_Pendant) + ")";
                        DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Pendant - 5),self.Dammage_Item_Pendant);
                   elif self.WeaponChoice == "Sigil": 
                        MESSAGE = MESSAGE + " They point their Sigil at their opponent unleashing blunt force telekinetic trauma! Pow! (possible +" + str(self.Dammage_Item_Sigil) + ")";
                        DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Sigil - 10),self.Dammage_Item_Sigil);
                   elif self.WeaponChoice == "Orb": 
                        MESSAGE = MESSAGE + " They cup the Orb in their hands, covering their opponent in damaging darkness! Vroww! (possible +" + str(self.Dammage_Item_Orb) + ")";
                        DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Orb - 15),self.Dammage_Item_Orb);
                   elif self.WeaponChoice == "PrincessCloak":
                        MESSAGE = MESSAGE + " They flip their PrincessCloak with sass! Showering their opoonent with clestial projectiles. Boom! (possible +" + str(self.Dammage_Item_PrincessCloak) + ")";
                        DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_PrincessCloak - 20),self.Dammage_Item_PrincessCloak);
             else: MESSAGE = "\n That magic item choice was invalid.";            

          print(MESSAGE);   
          time.sleep(4);   
          
          #4.Add magic ITEM damage to total dammage if applicable.
          if(DAMMAGE_MAGIC_ITEM > 0):
             print(" ",self.EntityName," generates [",DAMMAGE_MAGIC_ITEM,"] additional dammage by magic ITEM.",sep='');
             DAMMAGE = DAMMAGE + DAMMAGE_MAGIC_ITEM;
          else: print("Miss! No damage generated with weapon this round.");
          time.sleep(2);

          #5.If class of object allowed to use a magic SKILL? Process that Entity's choice and calculate additional dammage.
          if(self.EntityClass == "Princess" or self.EntityClass == "Alicorn" or self.EntityClass =="Supreme Agent of Chaos"):            
             if(self.MagicChoice == "None" or self.MagicChoice == "IceBlasts" or self.MagicChoice == "FireBalls" or self.MagicChoice == "Lightning" or 
                self.MagicChoice == "Telekinesis" or self.MagicChoice == "Telepathy" or self.MagicChoice == "Teleportation" or  self.MagicChoice == "TimeWarp" or
                self.MagicChoice == "Invisibility" or self.MagicChoice == "Healing" or self.MagicChoice == "FriendshipCast"):
                if self.MagicChoice == "None": 
                   MESSAGE = self.EntityName + "decides not to use magic, leveraging only ";
                   if self.EntityGender == "Female": MESSAGE = MESSAGE +  "her";
                   elif self.EntityGender == "Male": MESSAGE = MESSAGE +  "his";
                   MESSAGE = MESSAGE +  " wits!";
                else: 
                     MESSAGE = "\n " + self.EntityName + " chooses to use a MAGIC skill!\n";   
                     if(self.MagicChoice == "IceBlasts"): 
                        if(self.EntityMagicPower - 5 > 0): 
                           MESSAGE = MESSAGE + " Ice Blast! The ambient temperature around the opponent nears absolute zero, inflicting severe cold damage (possible +" + str(self.Dammage_Skill_IceBlasts) + ")";
                           DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_IceBlasts-5,self.Dammage_Skill_IceBlasts);
                           self.EntityMagicPower = self.EntityMagicPower - 5; 
                        else: MESSAGE = MESSAGE + " Sorry, you do not have enough magic power to activate a Ice Blast.";    
                     elif(self.MagicChoice == "FireBalls"): 
                          if(self.EntityMagicPower - 8 > 0): 
                             MESSAGE = MESSAGE + " Fire Ball! Super-heated balls of plasma coalesce out of thin air and rush towards the opponent (possible +" + str(self.Dammage_Skill_FireBalls) + ")";
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_FireBalls-8,self.Dammage_Skill_FireBalls); 
                             self.EntityMagicPower = self.EntityMagicPower - 8; 
                          else: MESSAGE = MESSAGE + " Sorry, you do not have enough magic power to activate a Fire Balls.";   
                     elif(self.MagicChoice == "Lightning"): 
                          if(self.EntityMagicPower - 15 > 0): 
                             MESSAGE = MESSAGE + " Lightning! Massive electrical potential builds and sparks and an arc of lightning races towards the opponent. (possible +" + str(self.Dammage_Skill_Lightning) + ")";
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_Lightning-15,self.Dammage_Skill_Lightning);
                             self.EntityMagicPower = self.EntityMagicPower - 15;  
                          else: MESSAGE = MESSAGE + " Sorry, you do not have enough magic power to activate a Lightning.";   
                     elif(self.MagicChoice == "Telekinesis"): 
                          if(self.EntityMagicPower - 20 > 0): 
                             MESSAGE = MESSAGE + " Telekinesis! Mind over matter deals massive blunt force trauma to the opponent (possible +" + str(self.Dammage_Skill_Telekinesis) + ")";
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_Telekinesis-20,self.Dammage_Skill_Telekinesis);
                             self.EntityMagicPower = self.EntityMagicPower - 20;  
                          else: MESSAGE = MESSAGE + " Sorry, you do not have enough magic power to activate a Telekinesis.";
                     elif(self.MagicChoice == "Telepathy"): 
                          if(self.EntityMagicPower - 35 > 0): 
                             MESSAGE = MESSAGE + " Telepathy! Opponent's mind is temporarily taken over and they commit self-harm (possible +" + str(self.Dammage_Skill_Telepathy) + ")";
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_Telepathy-35,self.Dammage_Skill_Telepathy);                           
                             self.EntityMagicPower = self.EntityMagicPower - 35;
                          else: MESSAGE = MESSAGE + " Sorry, you do not have enough magic power to activate a Telepathy.";   
                     elif(self.MagicChoice == "Teleportation"): 
                          if(self.EntityMagicPower - 40 > 0): 
                             MESSAGE = MESSAGE + " Teleportation! Teleporting into opponent's most vulnerable spot, they are devastated by a focused attack (possible +" + str(self.Dammage_Skill_Teleportation) + ")"; 
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_Teleportation-40,self.Dammage_Skill_Teleportation); 
                             self.EntityMagicPower = self.EntityMagicPower - 40; 
                          else: MESSAGE = MESSAGE + " Sorry, you do not have enough magic power to activate a Teleportation.";  
                     elif(self.MagicChoice == "TimeWarp"): 
                          if(self.EntityMagicPower - 50 > 0): 
                             MESSAGE = MESSAGE + " TimeWarp! Time warp initiated around opponent. As times slows, multiple succesive blows are sustained (possible +" + str(self.Dammage_Skill_TimeWarp) + ")";  
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_TimeWarp-50,self.Dammage_Skill_TimeWarp);
                             self.EntityMagicPower = self.EntityMagicPower - 50; 
                          else: MESSAGE = MESSAGE + " Sorry, you do not have enough magic power to activate a TimeWarp.";     
                     elif(self.MagicChoice == "FriendshipCast"): 
                          MESSAGE = MESSAGE + " FriendshipCast! " + self.EntityName + " casts peace, love and friendship on opponent decreasing aggression."; 
                          MESSAGE = MESSAGE + "\n Opponent no longer wishes to fight due to positive feelings of love and friendsip. De-escalating combat...";
                          if(self.EntityMagicPower - 300 > 0):
                             self.EntityMagicPower = self.EntityMagicPower - 300;  
                             globals()['Willing_to_Fight'] = "FALSE";
                             MESSAGE = MESSAGE + "\n Resetting magic skill choice back to \"None\".";
                             self.MagicChoice == "None";
                          else: MESSAGE = MESSAGE + " Sorry, you do not have enough magic power to activate a FriendshipCast.";   
             else: MESSAGE = "\nThat magic item skill choice was invalid.";

          print(MESSAGE); 
          time.sleep(3);

          #6.Add magic SKILL damage to total dammage if applicable damage-causing skill was chosen.
          if(DAMMAGE_MAGIC_SKILL > 0):
             print(" ",self.EntityName," generates [",DAMMAGE_MAGIC_SKILL,"] additional dammage by magic SKILL.",sep='');
             DAMMAGE = DAMMAGE + DAMMAGE_MAGIC_SKILL;
          else: print("Miss! No damage generated with skill this round.");   
          time.sleep(2);   

          #7.Calculate Opponent's base defense due to skill and experience
          DAMMAGE_DEF = random.randint(1,Opponent.EntityDefense);
          print("\n ",Opponent.EntityName," defends! Reducing dammage absorbed in this attack by [",DAMMAGE_DEF,"] due to their defensive skills.",sep='');
          time.sleep(2);

          #8.If Opponent using INVISBILITY? Add to their base defense amount.
          if(Opponent.Invisibility_Active == "TRUE"):
             print("\n INVISIBILITY is currently active for entity",Opponent.EntityName,"!");
             print(" This temporarily increases opponent's defense by [",self.Invisibility_DEF_Amt,"].\n Hard to hit what you can't see!",sep='');
             DAMMAGE_DEF = DAMMAGE_DEF + self.Invisibility_DEF_Amt;
             time.sleep(2);
             Opponent.Invisibility_Count = Opponent.Invisibility_Count - 1;
             if(Opponent.Invisibility_Count < 1): 
                Opponent.Invisibility_Active == "FALSE";
                Opponent.Invisibility_Count = 0;

          #9.Subtract Opponent's DEFENSE from dammage.
          if(DAMMAGE > DAMMAGE_DEF):
             DAMMAGE = DAMMAGE - DAMMAGE_DEF;
          else: DAMMAGE = 0;
          
          #10.Display resulting dammage after adding magic item and magic skill and subtracting all Opponent defense.
          print("\n After all attack and defense moves calculated for this combat round:");
          print(" ",self.EntityName," generated [",DAMMAGE,"] total dammage against their opponent.",sep='');
          time.sleep(2);

          #Prevent negative values, if Opponent health less than 1 this round, they are effectively defeated
          if(Opponent.EntityHealth - DAMMAGE > 0):
             Opponent.EntityHealth = Opponent.EntityHealth - DAMMAGE;
          else: Opponent.EntityHealth = 0;

          print("\n------------AFTER Attack Sequence------------");
          print("   ",self.EntityName,"Health:",self.EntityHealth);
          print("   ",Opponent.EntityName,"Health:",Opponent.EntityHealth);
          time.sleep(2);
    #END-MemberMethod-Attack----------------------------------------------------------------------------------------------------------------------------

#END-ClassSpecification-Game_Entity------------------------------------------------------------------------------------------------------------------------------------------------------



#INTERMEDIATE derived CHILD class that inherits from the BASE class----------------------------------------------------------------------------------------------------------------------
class ANTAGONIST(Game_Entity):
      #Class Attributes
      EntityName = "Anonymous Antagonist";
      EntityGender = "Male";
      EntityClass = "Antagonist";
      EntityHealth = 100;
      EntityDefense = 5;
      EntityAttack = 5;
      EntityMagicPower = 200;
 #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#Derived GRANDCHILD class from an intermediate CHILD class that itself inherits from the BASE class-------------------------------------------------------------------------------------
class Chaos_Agent(ANTAGONIST):
      #Class Attributes
      EntityName = "Discord";
      EntityGender = "Male";
      EntityClass = "Supreme Agent of Chaos";
      EntityHealth = 32000;
      EntityDefense = 5000;
      EntityAttack = 5000;
      EntityMagicPower = 32000;
      Antagonist_Ability_1 = "Warp SpaceTime";
      Antagonist_Ability_2 = "Improbability Materilization";
      Antagonist_Ability_3 = "Wish Projection";
      Antagonist_Ability_4 = "Ultimate Chaos";

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
      EntityHealth = 32000;
      EntityDefense = 5000;
      EntityAttack = 5000;
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



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Create_Character(): 
    CHOICE = "";  
    system('cls');
    print("\n You must create a Game_Entity object before you can play.");
    print("\n First, we must Instantiate your created character as the player object.");
    print("\n 1. Choose a CLASS for your character:\n");

    while(CHOICE != "a" and CHOICE != "u" and CHOICE != "p" and CHOICE != "r" and CHOICE != "b"):
          print("           Character Classes");
          print("       ┌─────────────────────────┐");
          print("       |     (A)licorn           |");
          print("       |     (U)nicorn           |");
          print("       |     (P)egasus           |");
          print("       |     (R)oyal Princess    |");
          print("       |     (B)asic Pony        |");
          print("       └─────────────────────────┘");    
          CHOICE = input("\nChoose: ");
          CHOICE = CHOICE.lower();
          if(CHOICE == "a"): 
             print("\n Instantiating an ALICORN.");
             Heroine = ALICORN();
          elif(CHOICE == "u"): 
               print("\n Instantiating a UNICORN.");
               Heroine = UNICORN();   
          elif(CHOICE == "p"): 
               print("\n Instantiating a PEGASUS.");
               Heroine = PEGASUS();
          elif(CHOICE == "r"): 
               print("\n Instantiating a PRINCESS.");
               Heroine = PRINCESS();               
          elif(CHOICE == "b"): 
               print("\n Instantiating a basic PONY.");
               Heroine = PONY();
          else: print("That was an INVALID option. Please choose a character class.");

    print("\n 2. Choose a GENDER for your character (m/f):\n");
    while(CHOICE != "m" and CHOICE != "f"):
          print("           Choose Gender");
          print("       ┌───────────────────┐");
          print("       │      (F)emale     │");
          print("       │      (M)ale       │");
          print("       └───────────────────┘");    
          CHOICE = input("\nChoose: ");
          CHOICE = CHOICE.lower();
          if(CHOICE == "f"): 
             print("\n It's a girl pony!");
             Heroine.EntityGender = "Female";
          elif(CHOICE == "m"): 
               print("\n It's a boy pony!");
               Heroine.EntityGender = "Male";
          else: print("That was an INVALID option. Please choose a gender.");

    print("\n 3. Please choose a NAME for your character:");
    CHOICE = input("\nChoose: ");   
    Heroine.EntityName = CHOICE;

    globals()['Player_Heroine'] = Heroine; 
    Heroine.Display_All();
    ContinueIT = input("\nPress ENTER to proceed.");      
    Create_Antagonists();
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Create_Antagonists(): 
    system("cls");
    print(" Second, we must build the opponent object(s).");

    #Antagonist 1
    print("\n Instantiating a Chaos_Agent.");
    Opponent = Chaos_Agent();
    globals()['Player_Opponent'] = Opponent;
    Opponent.Cheat_Mode();
    Opponent.Display_All();   
    ContinueIT = input("\nPress ENTER to proceed.");
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Display_Combat_Stats():
    print("\n");
    print ("{:<20} {:<7} {:<7} {:<8} {:<11} {:<20}".format("Name","Health","Attack","Defense","MagicPower","Class"));
    print("---------------------------------------------------------------------------");
    print ("{:<20} {:<7} {:<7} {:<8} {:<11} {:<20}".format(Player_Opponent.EntityName,Player_Opponent.EntityHealth,Player_Opponent.EntityAttack,Player_Opponent.EntityDefense,Player_Opponent.EntityMagicPower,Player_Opponent.EntityClass));
    print ("{:<20} {:<7} {:<7} {:<8} {:<11} {:<20}".format(Player_Heroine.EntityName,Player_Heroine.EntityHealth,Player_Heroine.EntityAttack,Player_Heroine.EntityDefense,Player_Heroine.EntityMagicPower,Player_Heroine.EntityClass));
    print("\n");
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Pony_Combat():
    MinDammage = 500;
    MaxDammage = 10000;
    CurrentPlayer = "Nobody"; 
    RoundCounter = 0;
    CHOICE = "NULL";
    CombatMode = "NULL";

  #1.Display names of instantiated class objects engaging in combat using pointers to globals
    system('cls');
    print("\nMagic Battle!!!",Player_Opponent.EntityName,"vs.",Player_Heroine.EntityName,"\b!");
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

    ContinueIT = input("\nENTER anything to continue:");
    
    system('cls');
    print("\nWhat combat mode do you desire to use for this battle?");
    print("INTERACTIVE mode will allow you to choose and change weapons and skills with each passing melee round.");
    print("AUTOMATED mode will use your currently selected weapon and skill for all melee rounds.\n");

    while(CHOICE != "i" and CHOICE != "a"):
          print("                  Combat Modes");
          print("       ┌────────────────────────────────┐");
          print("       |      (I)nteractive Combat      |");
          print("       |      (A)utomated Combat        |");
          print("       └────────────────────────────────┘");    
          CHOICE = input("\n       Your choice: ");
          CHOICE = CHOICE.lower();
          if(CHOICE == "i"): CombatMode = "INTERACTIVE";
          elif(CHOICE == "a"): CombatMode = "AUTOMATED";
          else: print("That was an INVALID option. Please choose a combat mode.");

    print("Combat Mode set to:",CombatMode);
    if(CombatMode == "AUTOMATED"):
       print("\nSince you chose AUTOMATED, choose an initial weapon, armor and skill before initiating battle.");
       ContinueIT = input("\nPress ENTER to proceed.");
       Options();
    else: 
         ContinueIT = input("\nPress ENTER to proceed.");
    system('cls');

  #3.Begin iterating through combat sequence. If either player's health = 0, combat over.
    while(Player_Opponent.EntityHealth > 0 and Player_Heroine.EntityHealth > 0 and (globals()['Willing_to_Fight'] == "TRUE")):               
          RoundCounter = RoundCounter + 1;
          system("cls");
          print("\nBeginning combat sequence round #:",RoundCounter); 
          print("Combat Mode:",CombatMode);
          Display_Combat_Stats();
          time.sleep(3);

          #If player is HEROINE
          if CurrentPlayer == "Heroine":
             print("\n------------------------------------------------------------------------------------");
             print(Player_Heroine.EntityName,"attacks",Player_Opponent.EntityName,"\b!");
             time.sleep(2);
             if(CombatMode == "INTERACTIVE"): 
                ContinueIT = input("\nINTERACTIVE MODE: Press ENTER to choose combat options.");
                Options();
                system("cls");

             #Don't allow player any post-mortem attacks if lost combat sequence
             if Player_Heroine.EntityHealth > 0:
                Player_Heroine.Attack(Player_Opponent);
                CurrentPlayer = "Antagonist";
             else: print("\n",Player_Heroine.EntityName,"cannot attack anymore. She has LOST!");

          #If player is ANTAGONIST
          elif CurrentPlayer == "Antagonist":
               print("\n------------------------------------------------------------------------------------");
               print(Player_Opponent.EntityName,"attacks",Player_Heroine.EntityName,"\b!");
               time.sleep(2);
               #Don't allow player any post-mortem attacks if lost combat sequence
               if Player_Opponent.EntityHealth > 0:
                  Player_Opponent.Attack(Player_Heroine);
                  CurrentPlayer = "Heroine";
               else: print("\n",Player_Opponent.EntityName,"cannot attack anymore. They have LOST!");
         
          else: print("\nERROR. This should never happen."); 

          #Clear console of text after every combat round
          ContinueIT = input("\nPress ENTER to proceed.");  
          system('cls');

    print("\nMagic Battle Complete!");
    Display_Combat_Stats();

    if Player_Heroine.EntityHealth > 0: print("\n",Player_Heroine.EntityName,"is victorious! She defeats",Player_Opponent.EntityName,"\b!");
    else: print("\n",Player_Opponent.EntityName,"is victorious! They defeat",Player_Heroine.EntityName,"\b!");

    globals()['Willing_to_Fight'] = "TRUE";
    ContinueIT = input("\nPress ENTER to proceed.");  
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Options():
    Present_Options_Menu = "TRUE";

    while Present_Options_Menu != "FALSE":
          system('cls');
          print("\n                    Options Menu");
          print("       ┌───────────────────────────────────────┐");
          print("       |        0. Exit                        |");
          print("       |        1. Display Stats               |");
          print("       |        2. Display Inventory           |");
          print("       |        3. Display Magic Skills        |");
          print("       |        4. Display Everything          |");
          print("       |        5. Equip Inventory Item        |");
          print("       |        6. Equip Magic Skill           |");
          print("       |        7. Save Game                   |");
          print("       |        8. Load Game                   |");
          print("       |        9. Activate Cheat Mode         |");
          print("       |        10. Help                       |");
          print("       |        11. Game Map                   |");
          print("       |        12. Quit Current Game          |");
          print("       └───────────────────────────────────────┘");


          CHOICE = input("\n       Your choice: ");
          CHOICE = CHOICE.lower();

          if(CHOICE != "0" and CHOICE != "1" and CHOICE != "2" and CHOICE != "3" and CHOICE != "4" and CHOICE != "5" and 
             CHOICE != "6" and CHOICE != "7" and CHOICE != "8" and CHOICE != "9" and CHOICE != "10" and CHOICE != "11" and CHOICE != "12"):
             print("\nThat was an invalid choice.");
          else:   
                if(CHOICE == "0"):
                     print("\nExiting Options menu ..."); 
                     Present_Options_Menu = "FALSE";
                elif(CHOICE == "1"): 
                   Player_Heroine.Display_Character(); 
                elif(CHOICE == "2"): 
                     Player_Heroine.Inventory_Display();  
                elif(CHOICE == "3"): 
                     Player_Heroine.SKILL_Display(); 
                elif(CHOICE == "4"): 
                     Player_Heroine.Display_All();
                elif(CHOICE == "5"): 
                     Player_Heroine.Inventory_Equip();
                elif(CHOICE == "6"): 
                     Player_Heroine.SKILL_Equip();
                elif(CHOICE == "7"): 
                     Save_Game();
                elif(CHOICE == "8"): 
                     Load_Game();
                elif(CHOICE == "9"):
                     print("\nActivating CHEAT Mode!");
                     Player_Heroine.Cheat_Mode();                     
                elif(CHOICE == "10"):
                     Game_Help();
                elif(CHOICE == "11"):
                     Game_MAP();     
                elif(CHOICE == "12"):
                     globals()['CurrentLocation'] = "QUIT_GAME";
                     Present_Options_Menu = "FALSE";          

          if(CHOICE != "12"):
             ContinueIT = input("\nPress ENTER to proceed.");                                                                                                          
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Main_Menu():
    Present_Main_Menu = "TRUE";

    while Present_Main_Menu != "FALSE":
          system('cls');
          print("\nWelcome to Discord's Dungeon!");
          print("©2022 Carly Salali Germany\n\n");
          print("\n                   Main Menu");
          print("      ┌──────────────────────────────────┐");
          print("      │        0. Exit                   │");
          print("      │        1. Create Character       │");
          print("      │        2. Options                │");
          print("      │        3. Magic Combat           │");
          print("      │        4. Play RPG               │");
          print("      └──────────────────────────────────┘");

          CHOICE = input("\n      Your choice: ");
          CHOICE = CHOICE.lower();

          if(CHOICE != "0" and CHOICE != "1" and CHOICE != "2" and CHOICE != "3" and CHOICE != "4"):
             print("\nThat was an invalid choice.");
          else:   
                if(CHOICE == "0"): 
                   Present_Main_Menu = "FALSE";
                   print("\nNow exiting Discord's Dungeon ... Goodbye!");   
                elif(CHOICE == "1"): 
                   Create_Character();
                   #Auto_Create_Characters_for_Testing();
                elif(CHOICE == "2"): 
                     Options(); 
                elif(CHOICE == "3"): 
                     Pony_Combat();  
                elif(CHOICE == "4"): 
                     Play_RPG();                                                                                                                         
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Auto_Create_Characters_for_Testing():   

    system('cls');
    print("\nCreating Game_Entity objects for level 1.");
    print("\n1. Instantiating a Heroine");
    Heroine = ALICORN();
    Heroine.Cheat_Mode();
    Heroine.Display_All();
    globals()['Player_Heroine'] = Heroine;

    print("\n2. Instantiating an Opponent");
    Opponent = Chaos_Agent();
    Opponent.Cheat_Mode();
    Opponent.Display_All();   
    globals()['Player_Opponent'] = Opponent;

    ContinueIT = input("\nPress ENTER to proceed.");
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Play_RPG():
    CHOICE = "";
    print("\nPlay RPG \"Discord's Dungeon\"");
    print("What would you like to do?");
    
    while(CHOICE != "n" and CHOICE != "l" and CHOICE != "s" and CHOICE != "q"):
          system("cls");
          print("\n               RPG Menu");
          print("       ┌──────────────────────┐");
          print("       │      (N)ew Game      │");
          print("       │      (L)oad Game     │");
          print("       │      (S)ave Game     │");
          print("       │      (Q)uit          │");
          print("       └──────────────────────┘");    
          CHOICE = input("\n       Choose: ");
          CHOICE = CHOICE.lower();
          if(CHOICE == "n"): 
             Create_Character();
             Initialize_Globals();
             SwitchBoard();
          elif(CHOICE == "l"): 
               print("Call Load Game function here");
          elif(CHOICE == "s"): 
               print("Call Save Game function here");
          elif(CHOICE == "q"): 
               print("\nExiting ...");
               ContinueIT = input("\nPress ENTER to proceed.");
          else: print("That was an INVALID option. Please choose a combat mode.");    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Game_Help():
    system("cls");
    print("\n\n    Discord's Dungeon                            HELP                           ©2022 Carly Salali Germany");
    print("   ┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐");
    print("   │  You find yourself transported by an unknown power to the magical land of Equestria. You must:       │");
    print("   │                                                                                                      │");
    print("   │  1. Create a character. You may choose from several types like Pony, Alicorn, Pegasus, Unicorn,      │");
    print("   │     Princess, etc. Once you have chosen a character class, assign your character gender and name.    │");
    print("   │                                                                                                      │");
    print("   │  2. Once you have created your character, you will begin the game by materializing at the Level 1    │");
    print("   │     starting location on the game map. Once you begin, you may navigate freely back and forth using  │");
    print("   │     cardinal directions to navigate between grids on the game map. As you proceed through each       │");
    print("   │     map, you will face puzzles, traps and encounters with adversaries that you must vanquish in      │");
    print("   │     order to complete each level. Along the way, you will be rewarded for solving puzzles and        │");
    print("   │     defeating antagonists by acquiring magic items, potions, weapons and armor that will be added    │");
    print("   │     to your inventory. Additionally, you will learn magic skills after completing different puzzles  │");
    print("   │     and defeating opponents in challenging combat. Good luck!                                        │");
    print("   │                                                                                                      │");
    print("   │  3. Once you have created your character and started a level, you will be able to SAVE the game      │");
    print("   │     state: including your character's attributes, inventory, skill set, completed quests and map     │");
    print("   │     details to a file. You will then be able to LOAD this and continue playing the game from where   │");
    print("   │     you left off on your last save. SAVE and LOAD are both accessed through the OPTIONS menu.        │");
    print("   └──────────────────────────────────────────────────────────────────────────────────────────────────────┘");
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Initialize_Globals():
    globals()['CurrentLocation'] = "L1_START";
    globals()['CENTER_FirstTime'] = "TRUE";
    globals()['CelestiasPalace_FirstTime'] = "TRUE";
    globals()['DiscordsLair_FirstTime'] = "TRUE";
    globals()['FriendshipForest_FirstTime'] = "TRUE";
    globals()['S1_Abominable_Alive'] = "TRUE";
    globals()['W2_Giant_Alive'] = "TRUE";
    globals()['SwampOfSadness_BloodBat_Alive'] = "TRUE";
    globals()['E3_DragonFish_Alive'] = "TRUE";
    globals()['N3_FireRat_Alive'] = "TRUE";
    globals()['S3_CarnivorousPlant_Alive'] = "TRUE";
    globals()['DiscordsLair_Alive'] = "TRUE";
    globals()['S2_MotleyCrewAlive'] = "TRUE";
    globals()['UNDERGROUND_DragonPairAlive'] = "TRUE";
    globals()['Willing_to_Fight'] = "TRUE";
    globals()['Found_Staff'] = "FALSE";
    globals()['Found_Pendant'] = "FALSE";
    globals()['Found_Sigil'] = "FALSE";
    globals()['Found_Orb'] = "FALSE";
    globals()['Found_PrincessCloak'] = "FALSE";
    globals()['Found_Chain_Mail'] = "FALSE";
    globals()['Found_Plate_Armor'] = "FALSE";
    globals()['Acquired_IceBlasts'] = "FALSE";
    globals()['Acquired_FireBalls'] = "FALSE";
    globals()['Acquired_Lightning'] = "FALSE";
    globals()['Acquired_Telekinesis'] = "FALSE";
    globals()['Acquired_Telepathy'] = "FALSE";
    globals()['Acquired_Teleportation'] = "FALSE";
    globals()['Acquired_TimeWarp'] = "FALSE";
    globals()['Acquired_Invisibility'] = "FALSE";
    globals()['Acquired_Healing'] = "FALSE";
    globals()['Acquired_FriendshipCast'] = "FALSE";
    globals()['Found_HealingPotion_1'] = "FALSE";
    globals()['Found_HealingPotion_2'] = "FALSE";
    globals()['Found_HealingPotion_3'] = "FALSE";
    globals()['Found_HealingPotion_4'] = "FALSE";
    globals()['Found_HealingPotion_CelestiasPalace'] = "FALSE";
    globals()['NPC1_Encountered'] = "FALSE";
    globals()['NPC2_Encountered'] = "FALSE";
    globals()['NPC3_Encountered'] = "FALSE";
    globals()['TRAP1_Encountered'] = "FALSE";
    globals()['TRAP2_Encountered'] = "FALSE";
    globals()['TRAP3_Encountered'] = "FALSE";
    globals()['TRAP4_Encountered'] = "FALSE";




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def SwitchBoard():
    while(globals()['CurrentLocation'] != "QUIT_GAME"):
          if(globals()['CurrentLocation'] == "L1_START"):
             L1_START();
          elif(globals()['CurrentLocation'] == "L1_CENTER"):
               L1_CENTER();
          elif(globals()['CurrentLocation'] == "L1_NORTH_1"):
               L1_NORTH_1();
          elif(globals()['CurrentLocation'] == "L1_SOUTH_1"):
               L1_SOUTH_1();
          elif(globals()['CurrentLocation'] == "L1_EAST_1"):
              L1_EAST_1();
          elif(globals()['CurrentLocation'] == "L1_WEST_1"):
               L1_WEST_1();
          elif(globals()['CurrentLocation'] == "L1_NORTH_2"):
               L1_NORTH_2();
          elif(globals()['CurrentLocation'] == "L1_SOUTH_2"):
               L1_SOUTH_2();
          elif(globals()['CurrentLocation'] == "L1_EAST_2"):
               L1_EAST_2();
          elif(globals()['CurrentLocation'] == "L1_WEST_2"):
               L1_WEST_2(); 
          elif(globals()['CurrentLocation'] == "L1_NORTH_3"):
               L1_NORTH_3();
          elif(globals()['CurrentLocation'] == "L1_SOUTH_3"):
               L1_SOUTH_3();
          elif(globals()['CurrentLocation'] == "L1_EAST_3"):
               L1_EAST_3();
          elif(globals()['CurrentLocation'] == "L1_WEST_3"):
               L1_WEST_3(); 
          elif(globals()['CurrentLocation'] == "L1_CELESTIASPALACE"):
               L1_CELESTIASPALACE();
          elif(globals()['CurrentLocation'] == "L1_UNDERGROUND"):
               L1_UNDERGROUND();
          elif(globals()['CurrentLocation'] == "L1_DISCORDSLAIR"):
               L1_DISCORDSLAIR();  
          elif(globals()['CurrentLocation'] == "L1_FRIENDSHIPFOREST"):
               L1_FRIENDSHIPFOREST();  
          elif(globals()['CurrentLocation'] == "L1_PEGASUSCITADEL"):
               L1_PEGASUSCITADEL();   
          elif(globals()['CurrentLocation'] == "L1_MOUNTAINOFMEANNESS"):
               L1_MOUNTAINOFMEANNESS();  
          elif(globals()['CurrentLocation'] == "L1_SWAMPOFSADNESS"):
               L1_SWAMPOFSADNESS();   
          elif(globals()['CurrentLocation'] == "L1_UNICORNJUNCTION"):
               L1_UNICORNJUNCTION();  
          elif(globals()['CurrentLocation'] == "L1_HILLSOFHAPPINESS"):
               L1_HILLSOFHAPPINESS();                                                                                          

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Game_MAP():
    system("cls");
    print("\n\n");
    print("MAP: Level 1\n");
    print("                                ┌────┐                                         ");
    print("     ┌────────────┐             │ N3 │          ┌──────────────┐               ");
    print("     | Celestia's |             └────┘          |  Mountain of |               ");
    print("     | Palace     |                |            |  Meanness    |               ");
    print("     └────────────┘             ┌────┐          └──────────────┘               ");
    print("          /                     │ N2 │                |                        ");
    print("         /                      └────┘                |        ┌──────────┐    ");
    print("        /       ┌──────────┐       |                  |        | Swamp of |    ");
    print("       /        | Unicorn  |    ┌────┐                |        | Sadness  |    ");
    print("      /         | Junction |    │ N1 │                |        └──────────┘    ");
    print("     /          └──────────┘    └────┘                |          |             ");
    print("    /                    |         |                  |          |             ");
    print("  ┌────┐    ┌────┐    ┌────┐    ┌────┐    ┌────┐    ┌────┐    ┌────┐           ");
    print("  | W3 |────| W2 |────│ W1 │────| C1 |────| E1 |────| E2 |────| E3 |           ");
    print("  └────┘    └────┘    └────┘    └────┘    └────┘    └────┘    └────┘           ");
    print("    |          |                   |                                           ");
    print("    |    ┌─────────┐            ┌────┐                                         ");
    print("    |    | Pegasus |            │ S1 │      ┌─────────────┐                    ");
    print("    |    | Citadel |            └────┘      | Underground |                    ");
    print("    |    └─────────┘               |        └─────────────┘\                   ");
    print("    |        ┌────────────┐     ┌────┐      /               \                  ");
    print("    |        |  Hills of  |_____│ S2 │     /                 \                 ");
    print("    |        |  Happiness |     └────┘    /                ┌────────────────┐  ");
    print("    |        └────────────┘        |     /                 | Discord's Lair |  ");
    print("  ┌───────────────────┐         ┌────┐  /                  └────────────────┘  ");
    print("  | Friendship Forest |         │ S3 │ /                                       ");
    print("  └───────────────────┘         └────┘                                         ");
    print("");

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_START():
    system("cls");
    print("\n Location: [Level 1] START\n");

    print(" You awake feeling somewhat dizzy. You can't believe your eyes as you look over your");
    print(" brand new body parts. You have been ponified! You have hooves. Pointy, soft, fuzzy ears.");
    print(" A mane. A tail. You are covered in fur. You stagger a bit as you get used to 4 legs. What?!?");
    print("\n You take in your surroundings. You are in the middle of a plush, green, grassy field with.");
    print(" flowing reeds and cattails that sway in the gentle breeze. The delicious, sweet aroma of");
    print(" the meadow in which you now prance fills your nostrils with refreshing delight.");
    print("\n In the distance you see something shimmering and reflecting the sunlight brightly amidst");
    print(" the tall, swaying grass rustling in the wind. You trot over to this shiny object and discover");
    print(" it is a strange, shimmering mirror. You stop and gaze at your reflection. To your surprise?\n");

    if(Player_Heroine.EntityGender == "Female"):
       print(" You are a beautiful girl",Player_Heroine.EntityClass,"with sparkling eyes and a gorgeous, flowing mane!");
    elif(Player_Heroine.EntityGender == "Male"):
       print("You are a handsome boy",Player_Heroine.EntityClass,"with strong muscles and broad shoulders!");
    
    globals()['CurrentLocation'] = "L1_CENTER";

    ContinueIT = input("\nPress ENTER to proceed.");
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_CENTER():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] CENTER");

    if(globals()['CENTER_FirstTime']  == "TRUE"):
       VIEW =        "\n View:  You are in a meadow with tall, green grass and reeds swaying in the breeze.";
       VIEW = VIEW + "\n Something shimmers in the distance. A gentle breeze blows all around you, swirling";
       VIEW = VIEW + "\n with the intoxicating scents of spring. Gossamer threads of dew like little diamonds";
       VIEW = VIEW + "\n glisten in the sunlight, casting rainbow colors through a thousand tiny prisms.";
       print(VIEW);
       globals()['CENTER_FirstTime']  = "FALSE";
    else:
          VIEW =        "\n View:  You return to the meadow with tall, green grass and reeds swaying in the breeze.";  
          VIEW = VIEW + "\n The place from which you came. In the distance, something shimmers. A gentle breeze blows.";
          print(VIEW);
          
          if(globals()['Found_Staff'] == "FALSE"):
             VIEW = "\n In the dew-covered grass to the South-East you notice something protruding from grasss ";
             VIEW = VIEW + "\n didn't notice before. What could it be?";
             print(VIEW);
          
             while(CHOICE != "y" and CHOICE != "#"):
                   CHOICE = input("\n Investigate? (Y)es or (N)o : ");
                   CHOICE = CHOICE.lower();          
                   if(CHOICE == "y"):
                      print("\n You decide to investigate. As you feel around inside the grass?");
                      print(" You find the Staff of Power! It is glowing with a strange, white aurora.");
                      Player_Heroine.INV_Has_Staff = "TRUE";
                      globals()['Found_Staff']  = "TRUE";
                      Player_Heroine.Inventory_Display(); 
                   elif(CHOICE == "n"):
                        print(" You decide it's not worth your time.");
                        CHOICE = "#"; #Must invalidate CHOICE since "n" = north in while loop below also
                   else:
                        print(" That choice was invalid. Ignoring it.");
          else : print("\n You see a withered patch of grass where you formerly found the staff of power.");                  

    print("\n Navigation options:");
    print(" (N)orth, you see a ranch house. And beyond it? A purple and blue mountain range.");
    print(" (S)outh, you see a forest of tall evergreens. Through the trees you see a lake in the distance.");
    print(" (E)ast, you see a village. Beyond that? A sunlit valley overshadowed by mountains to the north.");
    print(" (W)est, you see an arid, rocky desert. Beyond that? Caves.");

    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_CENTER";       
                elif(CHOICE == "n"):
                     globals()['CurrentLocation'] = "L1_NORTH_1";
                elif(CHOICE == "s"):
                     globals()['CurrentLocation'] = "L1_SOUTH_1"; 
                elif(CHOICE == "e"):
                     globals()['CurrentLocation'] = "L1_EAST_1"; 
                elif(CHOICE == "w"):
                     globals()['CurrentLocation'] = "L1_WEST_1";
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_NORTH_1():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] NORTH 1");

    VIEW =        "\n View:  You find yourself standing in the courtyard of an old ranch house.";
    VIEW = VIEW + "\n Beside it sits a bright red barn";
    print(VIEW);

    print("\n Navigation options:");
    print(" (N)orth, you see a purple and blue mountain range.");
    print(" (S)outh, you see a meadow with tall, green grass and reeds swaying in the breeze. Something shimmers in the distance.");
    print(" East, you see an impassible drop-off into a shadowy valley beyone a rocky ledge");
    print(" West, you see towering walls of solid stone impossible to climb.");

    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_NORTH_1";       
                elif(CHOICE == "n"):
                     globals()['CurrentLocation'] = "L1_NORTH_2";
                elif(CHOICE == "s"):
                     globals()['CurrentLocation'] = "L1_CENTER"; 
                elif(CHOICE == "e"):
                     print("\n To the EAST you try to climb solid walls of stone, but you are unable.");
                     if(globals()['Acquired_IceBlasts'] == "FALSE"):
                        VIEW = "\n In the wall of stone, you see what appears to be a parchment stuffed into a crevice. ";
                        VIEW = VIEW + "\n Is it some sort of message? What could it be?";
                        print(VIEW);
                        while(CHOICE != "y" and CHOICE != "#"):
                              CHOICE = input("\n Pull it out and try to read it? (Y)es or (N)o : ");
                              CHOICE = CHOICE.lower();          
                              if(CHOICE == "y"):
                                 print("\n You pull out the parchment and unroll it. It contians details for lowering the ambient");
                                 print(" temperature around yourself and your opponents. You acquire skill: Ice Blasts!");
                                 Player_Heroine.SKILL_Has_IceBlasts = "TRUE";
                                 globals()['Acquired_IceBlasts']  = "TRUE";
                                 Player_Heroine.SKILL_Display(); 
                              elif(CHOICE == "n"):
                                   print(" You decide it's too dirty and gross. No telling what's in that crevice!");
                                   CHOICE = "#"; #Must invalidate CHOICE since "n" = north in while loop below also
                              else:
                                   print(" That choice was invalid. Ignoring it.");
                     else : print("\n You see an empty crevice in a stone wall where you formerly found the scroll of Ice Blast.");     
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     print("\n You press WEST, but stop, afraid you will drop over a steep ledge into the valley below."); 
                     ContinueIT = input("\n Press ENTER to proceed.");                    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_SOUTH_1():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] SOUTH 1");

    VIEW =        "\n View:  You are standing in a damp, cool forest of tall evergreens. The trees";
    VIEW = VIEW + "\n have grown very tall in this area, and enshadow you with a canopy far above";
    VIEW = VIEW + "\n your head. You can hear many birds singing their songs and nesting in the branches.";
    print(VIEW);

    print("\n Navigation options:");
    print(" (N)orth, you see a meadow with tall, green grass and reeds swaying in the breeze. Something shimmers in the distance.");
    print(" (S)outh, you see a lake surrounded by evergreens and rippling with their reflection.");
    print(" East, you seen an apple cart full of red, delicious apples. Beside the cart stands a pony wearing a straw hat.");
    print(" West, you see a large, pink pony bouncing playfully on a baloon.");

    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_SOUTH_1";       
                elif(CHOICE == "n"):
                     globals()['CurrentLocation'] = "L1_CENTER";
                elif(CHOICE == "s"):
                     globals()['CurrentLocation'] = "L1_SOUTH_2"; 
                elif(CHOICE == "e"):
                     print("\n You trot east towards the apple card and pony with the straw hat. She holds her hoof up and tells you to stop."); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     print("\n You run up to the pink pony. But she refuses to get off her baloon and blocks any further progress to the east at this point.");
                     ContinueIT = input("\n Press ENTER to proceed.");
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_EAST_1():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] EAST 1");

    VIEW =        "\n View:  Surrounding you is what appears to be an abandoned village. There are";
    VIEW = VIEW + "\n about a dozen wooden cottages with thatched roofs and an old hut made of straw";
    VIEW = VIEW + "\n that sits in the middle of what appears to be the town square. You can see a";
    VIEW = VIEW + "\n fire pit smoldering and what appears to be a kettle with a strange liquid brewing.";
    print(VIEW);   

    print("\n Navigation options:");
    print(" North are thick, thorny hedges through which you can see no light passing through their branches.");
    print(" South you see a small, delapidated wooden hut. In front of this hut is a hinged iron door with a key lock. ");    
    print(" (E)ast of your current position, you see a swiftly flowing broad river. There are sand bars in the distance.");
    print(" (W)est you see a meadow with tall, green grass and reeds swaying in the breeze. Something shimmers in the distance.");

    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_EAST_1";       
                elif(CHOICE == "n"):
                     print("\n You try to move north, but are blocked by painful thistles and thick hedges. If only you had a flame?"); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "s"):
                     print("\n You approach the old hut and pull on the hinged iron door with all your might. But it is locked."); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "e"):
                     globals()['CurrentLocation'] = "L1_EAST_2";
                elif(CHOICE == "w"):
                     globals()['CurrentLocation'] = "L1_CENTER";
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_WEST_1():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] WEST 1");

    VIEW =        "\n View:  You plod into an arid, sandy plane. All around you there is withered grass";
    VIEW = VIEW + "\n and sparse, dessicated, shriveled up trees. Randoml dotted here and there you see";
    VIEW = VIEW + "\n large catuses spiraling upwards towards the scorching sun. In between these random";
    VIEW = VIEW + "\n and sporadically positioned cacti, you see dull gray boulders of pourous sandstone.";
    print(VIEW);     

    print("\n Navigation options:");
    print(" (N)orth of you are wild apple trees. On them hang various red, delicious apples. Beyond that? A VILLAGE!");
    print(" South you see a an old table made of oak with a single, iron chest with a key hole in the middle.");    
    print(" (E)ast you see a meadow with tall, green grass and reeds swaying in the breeze. Something shimmers in the distance.");
    print(" (W)est of where you stand, you see dusty, grey, rocky caves protruding from a granite hillside.");

    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_WEST_1";       
                elif(CHOICE == "n"):
                     print("\n You walk towards the apple trees. Some have fallen to the ground. You see bright red apples"); 
                     print(" hanging from each tree that surrounds you. You continue walking and approach the VILLAGE ...");
                     ContinueIT = input("\n Press ENTER to proceed.");
                     globals()['CurrentLocation'] = "L1_UNICORNJUNCTION";
                elif(CHOICE == "s"):
                     print("\n You walk over to the oak table and try to open the iron chest but cannot. It is locked.");
                     print(" If only you had a key? On the table you see a 6-sided dice. Beside it a sign says:\n");
                     print("   ┌───────────────────────────────────────┐");
                     print("   │  Roll a six? It's in the mix.         │");
                     print("   │  Roll any other? Pain's your brother. │");
                     print("   └───────────────────────────────────────┘");
                     print("                    |  |                    ");
                     print("                    |  |                    ");
                     
                     if(globals()['Acquired_FireBalls'] == "FALSE"):
                        while(CHOICE != "y" and CHOICE != "#"):
                              CHOICE = input("\n Will you roll the dice? (Y)es or (N)o : ");
                              CHOICE = CHOICE.lower();          
                              if(CHOICE == "y"):
                                 print("\n You scoop up the 6-sided dice and blow a kiss to Lady Luck!\n");
                                 LadyLuck = random.randint(1,6);
                                 RollCount = 1;
                                 print("     ",end='');
                                 while(RollCount < 7):
                                       print(str(RollCount) + " . ",end='');
                                       RollCount = RollCount + 1; 
                                       time.sleep(1);
                                 print("\n\nYou rolled a " + str(LadyLuck) + "!");
                                 if(LadyLuck == 6):
                                    print("You did it! You rolled a perfect 6!");
                                    print("The dice you just rolled shimmers and turns into a KEY!");
                                    print("You insert the key into the locked box. Click! It opens!");
                                    print("\n You pull out the parchment inside and unfold it. It contians details for exciting molecules");
                                    print(" to create intense heat and spontaneous flame. You acquire skill: Fire Balls!");
                                    Player_Heroine.SKILL_Has_FireBalls = "TRUE";
                                    globals()['Acquired_FireBalls']  = "TRUE";
                                    Player_Heroine.SKILL_Display(); 
                                 else:
                                       print("Sorry Charly. No dice this time. You did not roll a 6.");
                                       print("Because you did not roll a 6, you get PAIN!");
                                       print("An energy bolt emanates from the box shocking you doing 5 points of dammage.");
                                       Player_Heroine.EntityHealth = Player_Heroine.EntityHealth - 5;
                                       print("Your current health is now: " + str(Player_Heroine.EntityHealth));
                              elif(CHOICE == "n"):
                                   print(" You decide not to roll the dice. Dangerous!");
                                   CHOICE = "#"; #Must invalidate CHOICE since "n" = north in while loop below also
                              else:
                                    print(" That choice was invalid. Ignoring it.");                    
                     else : 
                              print("\n You see the key and empty box where you formerly found the FireBall scroll."); 
                              print(" You formerly flirted with Lady Luck here and rolled the dice.");

                     ContinueIT = input("\n Press ENTER to proceed.");

                elif(CHOICE == "e"):
                     globals()['CurrentLocation'] = "L1_CENTER";
                elif(CHOICE == "w"):
                     globals()['CurrentLocation'] = "L1_WEST_2";
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_NORTH_2():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] NORTH 2");

    VIEW =        "\n View:  You find yourself at the base of a blue and purple mountain range. Further north, you";
    VIEW = VIEW + "\n a meandering path that winds its way up into mountains catches your eye. In the distance,"; 
    VIEW = VIEW + "\n you see craggy, white mountain peaks poking through puffy rings of clouds.";
    print(VIEW);

    print("\n Navigation options:");
    print(" (N)orth, you spy tall mountain peaks ringed by puffy white clouds.");
    print(" (S)outh, you see the courtyard of and old ranch house. Beside it stands a bright red barn.");
    print(" East, you see the rocky base of an exposed mountain-side. It is far to steep to climb.");
    print(" West, you notice a solitary campsite. An old, mildew-stained canvas tent is pitched against a tree. A small campfire is burning.");

    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_NORTH_2";       
                elif(CHOICE == "n"):
                     globals()['CurrentLocation'] = "L1_NORTH_3";
                elif(CHOICE == "s"):
                     globals()['CurrentLocation'] = "L1_NORTH_1"; 
                elif(CHOICE == "e"):
                     print("\n You try to ascen the exposed mountain-side, but it is far too steep and you keep sliding back."); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     print("\n You walk over to the campsite. The tent is empty. On the campfire boils a pot of soup.");
                     ContinueIT = input("\n Press ENTER to proceed.");    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_SOUTH_2():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] SOUTH 2");

    VIEW =        "\n View:  ";
    VIEW = VIEW + "\n You arrive at a beautiful, blue pristine lake. Its translucent waters are as transparent as glass."; 
    VIEW = VIEW + "\n As the wind blows, it generates ripples that cascade across the surface, generating small waves";
    VIEW = VIEW + "\n with crests and troughs. ";
    print(VIEW);

    print("\n Navigation options:");
    print(" (N)orth, you see a dark green forest of evergreens. The canopy of the trees casts its shadow over everything beneath.");
    print(" (S)outh, you see a causeway of flat, gray stones. They protroud from the water and lead to a small island not far from shore.");
    print(" East, you see a narrow beach covered with soft, white, sugary sand. You notice several playful otters darting to and fro across this sand.");
    print(" (W)est, you a section of shallow water rippling across several exposed sandbars. Beyond that? Roving green hills of wildflowers.");

    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_SOUTH_2";       
                elif(CHOICE == "n"):
                     globals()['CurrentLocation'] = "L1_SOUTH_1";
                elif(CHOICE == "s"):
                     globals()['CurrentLocation'] = "L1_SOUTH_3"; 
                elif(CHOICE == "e"):
                     print("\n You walk east. Adorable, chattering, playful otters surround you. You can go no further east."); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     print("\n Plodding westward through the shallow water, you wade among watercress. Small fish swim by your hooves.");
                     print(" Wading out of the shallows, you step onto dry land. The shore where you stand is rimmed with tall");
                     print(" grass. You glance firther to the west, ascending gradually to the top of a hill ...");
                     ContinueIT = input("\n Press ENTER to proceed.");
                     globals()['CurrentLocation'] = "L1_HILLSOFHAPPINESS";      
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_EAST_2():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] EAST 2");

    VIEW =        "\n View:  You stand beside a swiftly flowing river. Clumps of broken ice are flowing";
    VIEW = VIEW + "\n in the swiftly bubbling current that passes you by. Among the clumps of broken ice,";
    VIEW = VIEW + "\n you notice a school of fish darting to and fro around smooth rocks in the shallows.";
    print(VIEW);   

    print("\n Navigation options:");
    print(" (N)orth, there is a single, solitary fishing pole abandoned by a tree. Beyond that? You see a tall, gray mountain covered by dead trees.");
    print(" South, a cart of green apples leans against a large rock. It is missing one wheel.");    
    print(" (E)ast of where you stand, a small dirt path winds around clumps of trees towards a free-standing awning. Under it? A blacksmith forge.");
    print(" (W)est an empty looking village with a dozen wooden cottages stands. You can see smoke smouldering from a small fire in the middle.");

    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_EAST_2";       
                elif(CHOICE == "n"):
                     print("\n Trotting north, you examine the fishing pole. It has no hook, so not likely to be useful.");
                     print(" Beyond this tree, you walktowards the base of the mountain. It's covered with gray, colorless");
                     print(" lichens and moss. The entier moutain, from the base to the peak, appears completely devoid");
                     print(" of all color. You feel as though you are Dorothy and now leaving OZ to go back to Kansas.");
                     print(" For some reason, you feel very grumpy and agitated now. You begin to ascend the montain ...");
                     ContinueIT = input("\n Press ENTER to proceed.");
                     globals()['CurrentLocation'] = "L1_MOUNTAINOFMEANNESS";
                elif(CHOICE == "s"):
                     print("\n You walk south to the cart of green apples. Why is it missing a wheel? You can't go further south from here."); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "e"):
                     globals()['CurrentLocation'] = "L1_EAST_3";
                elif(CHOICE == "w"):
                     globals()['CurrentLocation'] = "L1_EAST_1";    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_WEST_2():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] WEST 2");

    VIEW =        "\n View:  You are standing in the midst of a series of gray, rocky caves";
    VIEW = VIEW + "\n carved into the exposed granite hillside of many large, protruding";
    VIEW = VIEW + "\n cracks and crevices.";
    print(VIEW);   

    print("\n Navigation options:");
    print(" North, your eyes catch glimpse of an old, salty mare who appears to be selling flowers.");
    print(" (S)outh, you see an adorable, purple, baby dragon munching on a carrot. Beyond him? A gleaming citadel.");    
    print(" (E)ast you see an arid, sandy plain with withered grass and sparse, desicated, withered trees. ");
    print(" (W)est a castle looms in the distance. Festive, colored flags wave from its towers.");

    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_WEST_2";       
                elif(CHOICE == "n"):
                     print("\n You walk north and approach the elderly, contankerous mare.");
                     print(" She wants to sell you flowers, but you have nothing to buy them with.");
                     print(" You can go no further north from this location.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "s"):
                     print("\n You trot south and strike up a conversation with the baby dragon.");
                     print(" He is more interested in munching on his carrot than talking to you.");
                     print(" You walk past him towards the gleaming citadel. As you get closer, you");
                     print(" are amazed bythe golden glow shimmering from its gilded walls. The citadel");
                     print(" is aligned perfectly between 4 towers corresponding to the cardinal directions");
                     print(" north, south, east and west. You can see compass markings on each tower, and");
                     print(" engraved within each of their polished brick walls is a beautiful pair of wings.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                     globals()['CurrentLocation'] = "L1_PEGASUSCITADEL";
                elif(CHOICE == "e"):
                     globals()['CurrentLocation'] = "L1_WEST_1";
                elif(CHOICE == "w"):
                     globals()['CurrentLocation'] = "L1_WEST_3";        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_NORTH_3():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] NORTH 3");

    VIEW =        "\n View:  You ascend the base of a mountain and find yourself several thousand feet higher";
    VIEW = VIEW + "\n amidst sparse clumps of evergreens and snow-covered boulders. A light blanket of frost"; 
    VIEW = VIEW + "\n covers the lichens and pebbles crunching beneath your feet as you walk. Looking down,";
    VIEW = VIEW + "\n you are overwhelmed by the breath-taking beauty of a ring of clouds incircling the mountain";
    VIEW = VIEW + "\n base beneath you.";
    print(VIEW);

    print("\n Navigation options:");
    print(" North, you see impenetrable mountain slopes of hardened granite covered with ice far too steep and slippery to climb.");
    print(" (S)outh, the base of a blue and purple mountain range catches your eye.");
    print(" East, you see an odd and uneven plateau, hewn into the side of the mountain as if by a giant axe.");
    print(" West, a green valley with lush farmland delights your senses. But the incline is to steep to reach it from here.");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_NORTH_3";       
                elif(CHOICE == "n"):
                     print("\n You try to ascend further north, but are unable to climb the steep, slippery slopes as they are covered with ice.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "s"):
                     globals()['CurrentLocation'] = "L1_NORTH_2"; 
                elif(CHOICE == "e"):
                     print("\n You gallop east into an artificial plateau hewn into the side of the mountain."); 
                     print(" What sort of a being could have done this? Are therey GIANTS this strong and powerful?");
                     print(" Terrifying creatures who can cut through solid granite as an axe could chop soft wood?"); 
                     print(" A shiver travels up your spine as you contemplate these things. But you can go no further east.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     print("\n You trot west but stop at the edge of the incline that descends into the valley below.");
                     print(" The lush farmland you see sprawling beneath you is indeed tantalizing.");
                     print(" But you cannot go further west fro here.");
                     ContinueIT = input("\n Press ENTER to proceed.");        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_SOUTH_3():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] SOUTH 3");

    VIEW =        "\n View:  You trot out onto a causeway of flat, gray stones. These stones have been layed out";
    VIEW = VIEW + "\n inteligently in an organized sequence that creates a winding path you can follow. If you were"; 
    VIEW = VIEW + "\n to hop from stone to evenly-spaced stone? You realize you could reach a small island they";
    VIEW = VIEW + "\n lead to in the distance that is only a small ways from the lake shore itself.";
    print(VIEW);

    print("\n Navigation options:");
    print(" (N)orth, you gaze at the totality of the pristine lake whose shore you now stand beside. It is stunningly beautiful.");
    print(" South, you cannot see beyond the shore of the lake due to a dense grove of thickets and briars.");
    print(" (E)ast, you see an old mare with a backpack. She appears to be trotting back and forth in front of a CAVE.");
    print(" West, you see the causeway of stones protruding through the water's surface and leading to the small island.");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_SOUTH_3";       
                elif(CHOICE == "n"):
                     globals()['CurrentLocation'] = "L1_SOUTH_2";
                elif(CHOICE == "s"):
                     print("\n You try to advance south, but are blocked by impenetrable thickets and briars.");
                     print(" You think to yourself if only you had a source of flame? You could remove this obstacle."); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "e"):
                     print("\n You go east towards the old mare. The burden of her pack load looks heavy.");
                     print(" You ask her why she is walking in circles around the cave entrance.");
                     print(" She gives you no answer and pays you no mind. What could get her attention?");
                     print(" You look furter east and see that the cave descends deep underground. You");
                     print(" decide to walk pas the old mare and go spelunking!");
                     ContinueIT = input("\n Press ENTER to proceed.");
                     globals()['CurrentLocation'] = "L1_UNDERGROUND";
                elif(CHOICE == "w"):
                     print("\n You walk west following the casueway, hopping from stone to stone.");
                     print(" At the end of this path, you find yourself on a small island not far from shore.");
                     print(" You see other islands further out. If only you had a boat? You could reach them.");
                     print(" You see several large ravens perching on the cobbled stone ruins of what must have been a wall.");
                     print(" One of them turns its head to one side and says \"Hello! Fine day it is. But what may come at night?\""); 
                     print(" It does not seem odd to you that that ravens speak. If only you had a boat you could go further west ...");
                     ContinueIT = input("\n Press ENTER to proceed.");      
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_EAST_3():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] EAST 3");

    VIEW =        "\n View:  You find yourself beside a free-standing awning made of dirty, brown canvas.";
    VIEW = VIEW + "\n It stretches out over a rusty, iron fire ring in the middle. From this fire ring,"; 
    VIEW = VIEW + "\n billows od smoke rise into the air under the awning making the air caustic to breathe."; 
    VIEW = VIEW + "\n You can see a large, heavy cast-iron blacksmith forge, with an anvil in the middle of";
    VIEW = VIEW + "\n a flat, polished chunk of granite used as a platform to support it.";
    print(VIEW);

    print("\n Navigation options:");
    print(" (N)orth, you see a boggy swamp. Against a mangrove at the shore a GIANT is sleeping, his enormous head against a large rock.");
    print(" South, you see an abandoned gray stone stable surrounded by pludered piles of straw and hay.");
    print(" East, you see a small granite table with a large stone surface. On it are several plated of cupcakes.");
    print(" (W)est, you see a swiftly flowing river with clumps of flowing ice.");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_EAST_3";       
                elif(CHOICE == "n"):
                     print("\n You trot north towards the GIANT. His arms and legs are sprawled haphazzardly around");
                     print(" the area. You can see no way to proceed further north without waking this GIANT."); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                     globals()['CurrentLocation'] = "L1_SWAMPOFSADNESS";   
                elif(CHOICE == "s"):
                     print("\n You go south towards the delapidated old stable. As you look around, you see piles of hay and straw.");
                     print(" Under an unraveling bail, you see something protruding but cannot make out by its ambiguous shape what it is.");
                     print(" You can proceed no further south from here.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "e"):
                     print("\n You gallop east towards the stone table with all the cupcakes. As you get closer?");
                     print(" You see dozens of colorful, delicious looking cupcakes on various platters with glass domes.");
                     print(" You wonder to yourself: Are they safe to eat? And if so? What would they do to me?");
                     print(" Looking past the stone table you see only a brick wall and no way to proceed further east."); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     globals()['CurrentLocation'] = "L1_EAST_2";         
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_WEST_3():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] WEST 3");

    VIEW =        "\n View:  You arrive at the courtyard of a beautiful stone and crystal castle. The castle is over 80 feet tall";
    VIEW = VIEW + "\n in some areas, and you realize it must contain many floors. Surrounding the castle on each of its 4 corners?"; 
    VIEW = VIEW + "\n You see colorful, festive flags flapping in the wind and curling into random shapes as the wind changes";
    VIEW = VIEW + "\n direction. The polished stones and crystal slabs that intersect with angle and edge of this amazing castle";
    VIEW = VIEW + "\n sparkle in the sunlight like a tapestry made of a thousand shimmering rainbows. How is it always DAY over";
    VIEW = VIEW + "\n this magical place, even when it is NIGHT everywhere else? Does the being who lives here somehow control the";
    VIEW = VIEW + "\n sun itself? You see a moat of crystl waters an lilies before you, surrounfing this castle. And beyond this";
    VIEW = VIEW + "\n moat? A large drawbridge that, if it were to decend? Would give you welcome access to this spectacular palace.";
    print(VIEW);

    print("\n Navigation options:");
    print(" (N)orth, you see a gold entry gate jutting out over the moat where the drawbridge would meet if extended. Beside it, a large brass bell.");
    print(" (S)outh, you see a winding path that meanders aimlessly into a forest.");
    print(" (E)ast, you see a series of gray, rocky caves carved into the exposed hillside.");
    print(" West, you see the arch of a wide castle moat as large as a small lake. It extends around the palace.");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_WEST_3";       
                elif(CHOICE == "n"):
                     print("\n You walk norhtwards towards the gate and examine the large brass bell. You decide to ring it.");
                     print(" As the bell chimes across the waters of the moat? The drawbridge to the palace extends and");
                     print(" the golden gate opens. You decide to enter the palace.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                     globals()['CurrentLocation'] = "L1_CELESTIASPALACE"; 
                elif(CHOICE == "s"):
                     print("\n Curiosity gets the best of you and you trot haphazzardly down the winding path.");
                     print("\n Tall evergreens, at first in the distance, grow closer and closer ...");
                     ContinueIT = input("\n Press ENTER to proceed.");
                     globals()['CurrentLocation'] = "L1_FRIENDSHIPFOREST"; 
                elif(CHOICE == "e"):
                     globals()['CurrentLocation'] = "L1_WEST_2"; 
                elif(CHOICE == "w"):
                     print("\n You gallop west until you stand at the center of the arch of a wide castle moat.");
                     print(" This moat completely surrounds the castle and has waters as clear as the purest crystal.");
                     print(" But it is wide and the size of a good-sized lake. Too wide to swim across.");
                     print(" You see that you can go no further west from here."); 
                     ContinueIT = input("\n Press ENTER to proceed.");    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_CELESTIASPALACE():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] Celestia's Palace");

    VIEW =        "\n View:  You across the moat over the extended drawbridge and enter Celestia's Palace.";
    VIEW = VIEW + "\n How exquisitely beautiful! You are surrounded by glittering, gleaming wallks of";
    VIEW = VIEW + "\n polished stone. Jasper, jade, emerald and amethist. Embellishing the walls on"; 
    VIEW = VIEW + "\n every side? You see rubies, diamonds, opals and saphires.";
    print(VIEW);

    print("\n Navigation options:");
    print(" North you see beautiful castle walls.");
    print(" (S)outh, you see the door from which you entered this amazing, magical place.");
    print(" East, a winding staircase ascends to the second floor.");
    print(" West, you see an elaborately crafted throne made entirely of sparkling transparent diamonds!");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_CELESTIASPALACE";      
                elif(CHOICE == "n"):
                     print("\n You attempt to proceed further north but cannot.");
                     print(" You are run into a tall, smooth and polished crystal and stone castle wall.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "s"):
                     globals()['CurrentLocation'] = "L1_WEST_3"; 
                elif(CHOICE == "e"):
                     print("\n You try to ascend to winding staircase, but cannot.");
                     print(" It appears you are blocked by an invisible field of force.");
                     print(" It is as though the air has solidified around you.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     print("\n You walk westward towards the throne. It is covered by hundreds of ornate");
                     print(" frills and swirls embellishing its gold and diamond frame with strange and");
                     print(" beautiful markings. You can go no further west from here.");
                     ContinueIT = input("\n Press ENTER to proceed.");      
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_UNDERGROUND():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] Underground");

    VIEW =        "\n View:  You descend into a large cavern. As you go deeper into the darkness?";
    VIEW = VIEW + "\n Strange shadows begin to dance and flicker across the bleak rocky walls.";
    VIEW = VIEW + "\n You glance above into the upper expanse of the cavern and are in awe. Hundreds";
    VIEW = VIEW + "\n of long, pointy stalactites hang from the cave ceiling like crystal chandeliers.";
    VIEW = VIEW + "\n As you look down at the cavern floor, you see stalagmites growing upwards, Several ";
    VIEW = VIEW + "\n are entombed in piles of sand and sharp, crumbled fragments. You tread carefully.";
    VIEW = VIEW + "\n In the distance further down into the cave? You heear a low rumbling drone";
    VIEW = VIEW + "\n mixed with the unmistakable sound of crumbling stone and falling stalactites.";
    print(VIEW);

    print("\n Navigation options:");
    print(" North you see a series wooden crates stacked against a cave wall.");
    print(" (S)outh, you spy a tunnel leading off into the darkness.");
    print(" East, you see only darkness and impenetrable cave walls.");
    print(" (W)est, you see the faint glow of light dimly streaming in from the cave entrance you came from.");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_UNDERGROUND";      
                elif(CHOICE == "n"):
                     print("\n You walk north towards the stack of wooden crates. You exaint them,");
                     print(" but find nothing special. You cannot go further north from here.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "s"):
                     print("\n You decide to explore the tunnel going south. However, after");
                     print(" walking through it for only a few moments, you find the passage");
                     print(" blocked by a giant boulder. If only you had something to blow it");
                     print(" up into smaller pieces? Or a long rod with a fulcrum might budge it");
                     print(" perhaps? You touch it and it crumbles into dust! It was an illusion.");
                     print(" You walk further into the tunnel and it begins to grow brighter ...");
                     ContinueIT = input("\n Press ENTER to proceed.");
                     globals()['CurrentLocation'] = "L1_DISCORDSLAIR"; 
                elif(CHOICE == "e"):
                     print("\n You trot further east, but are blocked by an impenetrable cave wall.");
                     ContinueIT = input("\n Press ENTER to proceed.");  
                elif(CHOICE == "w"):
                     globals()['CurrentLocation'] = "L1_SOUTH_3"; 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_DISCORDSLAIR():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] Discord's Lair");

    VIEW =        "\n View:  You walk into an enormous cavern, blinking as your pupils dilate and try to adjust to the intense green";
    VIEW = VIEW + "\n brightness reflecting from a large crystal stalactite descending from the cave ceiling far above you. It seems";
    VIEW = VIEW + "\n as bright and hot as a sun would be, and you avert your eyes as they cannot  withstand the heat and brightness";
    VIEW = VIEW + "\n for long. You look around and realize you  are surrounded by dark, flat black obsidian walls that somehow swallow";
    VIEW = VIEW + "\n the intense green light being emitted from above.\n";
    VIEW = VIEW + "\n To your enormour surprise, you see what looks like a patchwork quilt of a dragon, made up of what looks like a";
    VIEW = VIEW + "\n random assortment of mis-matched and asymmetrical spare body parts. This being is enveloped in a cloud of rainbow";
    VIEW = VIEW + "\n colors and sparkles randomly exploding all around it like fireworks. It is preoccupied with reading something from";
    VIEW = VIEW + "\n a strange tablet with unintelligible symbols. It doesn't notice you at the moment.";
    print(VIEW);

    print("\n Navigation options:");
    print(" (N)orth you see the long, dark tunnel from which you came.");
    print(" South, you see dark obsidian walls. A large shelf 100 feest long and 20 feet high holds books and stone tablets.");
    print(" East, you see a wooden table with a large clay bowl and a wodden spoon. A box of fruity cereal and a pitcher of milk sit beside it.");
    print(" West, you see several rusty iron cages with small forest creatures trapped behind their bars.");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_DISCORDSLAIR";      
                elif(CHOICE == "n"):
                     globals()['CurrentLocation'] = "L1_UNDERGROUND";
                elif(CHOICE == "s"):
                     print("\n You advance south. Examining the giant book shelf, you are completely amazed.");
                     print(" There must be THOUSANDS of books, scrolls, tomes and stone tablets on this enormous shelf!");
                     print(" You see a track that spans the length of the shelf. Attached to it is a ladder on wheels.");
                     print(" You surmise that this ladder must be used to reach the three upper levels of this giant library.");
                     print(" Your curioisty is driving you mad. You want to look at some of the books so bad. But you cannot");
                     print(" get past the rainbow-enshrouded being in front of you.");
                     ContinueIT = input("\n Press ENTER to proceed.")
                     globals()['CurrentLocation'] = "L1_DISCORDSLAIR"; 
                elif(CHOICE == "e"):
                     print("\n You trot east over to the wooden table. You look into the large clay bowl and find a rainbow-");
                     print(" colored assortment of fruit rings of various flavors. They are swimming in milk and have a pleasant");
                     print(" aroma. You wonder what would happen if you ate some? But you dare not! The strange being in the center");
                     print(" of the room could get quite upset if you ate his breakfast.");
                     ContinueIT = input("\n Press ENTER to proceed.")
                elif(CHOICE == "w"):
                     print("\n You walk west of to the rusty iron cages. As you get closer, you can see the sad, lonely faces");
                     print(" of the orest creatures trapped inside each cage. Their eyes are hollow and full of despair, as if");
                     print(" they have lost all hope. You try to open the cages and set them free, but you cannot. They are locked!");
                     print(" If only you could find the key to these locks? You could set them free and they might return to their");
                     print(" forest homes and be happy again.");
                     ContinueIT = input("\n Press ENTER to proceed.")    


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------   



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_SWAMPOFSADNESS():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] Swamp of Sadness");

    VIEW =        "\n View:  You feel heavy, sorrowful and depressed as you trot reluctantly into the Swamp of Sadness.";
    VIEW = VIEW + "\n Your hooves sink into the mud, and you feel like the weight of the entire world on your shoulders.";
    VIEW = VIEW + "\n The giant sleeping next to you is snoring, the rumble of his objstructed breath rumbling like a"; 
    VIEW = VIEW + "\n hurricane. A stench of rotten eggs and sulfur filsl yoru nostrils. You feel so sad here."; 
    print(VIEW);

    print("\n Navigation options:");
    print(" North, you see only the endless expanse of this dark and dreary swamp. It fills you with hopelessness.");
    print(" (S)outh, in the distance, you see an old canvas awning and beneath it a blacksmith's forge. You see smoke from a small fire billowing beneath.");
    print(" East, you spy a clump of mangroves. Nested in the branches of those mangroves, you see many pairs of red eyes glaring back at you.");
    print(" West, you see only murky swamp water and bubbling bogg. Here and there dead, fallen tree trunks protrude from beneath the cloudy water.");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_SWAMPOFSADNESS";       
                elif(CHOICE == "n"):
                     print("\n You amble northwards, sloshing through thick mud and murky swamp water.");
                     print(" As you progress, your hooves sink further and further into the mud."); 
                     print(" You realize you cannot proceed any further in this direction."); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "s"):
                     globals()['CurrentLocation'] = "L1_EAST_3"; 
                elif(CHOICE == "e"):
                     print("\n You trot EAST into the mangroves. You notice they have grown quite thickly together.");
                     print(" You find that you cannot tip toe around the giant, as much as you WISH you could.");
                     print(" When you try, you quickly become tangled in mangrove brnaches and vines.");
                     print(" You realize, the ONLY way to go further east from here is to WAKE the giant.");
                     print(" But you don't want to do that right now.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     print("\n You trot west out into the bubbling bogg. You see many fallen, dead tree trunks jutting");
                     print("   out above the muky depths. But they are spaced too far apart to hop from one to the other.");
                     print("   You realize it would be absolutely hopeless to go any further in this direction.");
                     ContinueIT = input("\n Press ENTER to proceed.");
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_MOUNTAINOFMEANNESS():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] Mountain of Meanness");

    VIEW =        "\n View:  You arrive at the top of this colorless, gray mountain. You don't know why, but as you pause";
    VIEW = VIEW + "\n to catch your breath? You feel absolutely angry. But why? You can't seem to stop the flood of negative";
    VIEW = VIEW + "\n emotions that are now filling your mind. You are enshrouded by a cold mist that makes you shiver."; 
    VIEW = VIEW + "\n All around you everything is covered with fog. You can only see a few feet in front of you."; 
    print(VIEW);

    print("\n Navigation options:");
    print(" North, you spy a ring of large boulders, with a patch of tall, colorless grass in the middle.");
    print(" (S)outh, looking back down the mountain, you see a swiftly flowing river with floqing clumps of ice");
    print(" East, you see a large, dead, hollow tree. You wonder - how is this long-deceased tree still standing?");
    print(" West, a sharp ledge juts out over an incline. Below this incline the side of the mountain decends into obscurity.");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_MOUNTAINOFMEANNESS";       
                elif(CHOICE == "n"):
                     print("\n You gallop north over to the large ring of boulders. Looking around, you see nothing");
                     print("\n of interest here. Just a tall clump of grass in the middle. Odd.");
                     print("\n You cna go no further north from this location.");
                     print(" "); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "s"):
                     globals()['CurrentLocation'] = "L1_EAST_2"; 
                elif(CHOICE == "e"):
                     print("\n You walk EAST over to the exposed, hollow trunnk of a long-since-deceased tree.");
                     print(" Inside the tree, you fins a clump of straw and realize it's an abandonded woodpecker's nest.");
                     print(" Peering beyond the trees dead branches and shriveled roots, you see only the steep side of");
                     print(" the mountain descending into the fathomless depths below. You can go no further east from here ...");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     print("\n Going WEST, you stop abruptly at a steel ledge. You can go no further.");
                     print(" You shudder to think what would happen if you slipped and fell on the sharp rocks below.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                           
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------  



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_HILLSOFHAPPINESS():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] Hills of Happiness");

    VIEW =        "\n View:  Climbing to the top of the incline, you are surrounded by rolling green hills. Standing";
    VIEW = VIEW + "\n here, you are strangely filled with a calm, glowing happiness as you stand in this location."; 
    VIEW = VIEW + "\n Positive feelings begin to well up within you, creating an intense feeling of contentment and inner peace.";
    print(VIEW);

    print("\n Navigation options:");
    print(" North, you see a ring of hills covered in tall, dark green grass. You imagine it would taste delightful.");
    print(" South, you spy a meadow full of colorful wildflowers. Amidst the spread, butterflies flutter freely.");
    print(" (E)ast, you see a placid, blue, beautiful and pristine lake.");
    print(" West, a ring lf small river rocks encircles a group of tall reeds and cattails.");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_HILLSOFHAPPINESS";       
                elif(CHOICE == "n"):
                     print("\n You trot over to the ring of hills covered in tall, green grass. It looks so tasty!");
                     print(" You bend down to nibble some, and it does not disappoint. Your mouth fills with a savory");
                     print(" sweetness as you munch on these tall blades of juicy greenness. Looking beyond these");
                     print(" mouth-watering stalks, you realize you can't go any firther northward. The path is blocked"); 
                     print(" by thick, thorny briars and thorny vines that are impassible."); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "s"):
                     print("\n You walk into a fragrant meadow filled with colorful wildflowers dancing in the wind.");
                     print(" Fluttering capriciously around these flowers is the laughter of nature itself - the");
                     print(" flapping wings of butterflies its poestry in motion. Beyond the meadow is the sandy");
                     print(" shore of a river, to broad to swim across and go any further south. ");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "e"):
                     globals()['CurrentLocation'] = "L1_SOUTH_2";  
                elif(CHOICE == "w"):
                     print("\n You walk WEST and into a ring of small, smooth river stones. In the middle of this ring");
                     print(" you see tall grass and cattails. Among them? Hides a strange and unusual creature with rabbit");
                     print(" ears and cat's eyes and a face like a racoon. You can proceed no further west from here.");
                     ContinueIT = input("\n Press ENTER to proceed.");                          
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_PEGASUSCITADEL():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] Pegasus Citadel");

    VIEW =        "\n View:  You find yourself in the midst of a fabulous equestrian citadel! Everywhere you look? You see small stone";
    VIEW = VIEW + "\n houses, shops, stables and buildings. Streets line this citadel, and at its center is a market where various vendors";
    VIEW = VIEW + "\n have setup their carts and tables to sell produce, fruit, tackle and clothing. All around you are colorful pegasuses,";
    VIEW = VIEW + "\n leaping to and fro and bounding into the air on their colorful wings. In the middle of the marketplace you see a tablet"; 
    VIEW = VIEW + "\n with a large, bronze plaque. Inscribed upon it are the words: \"In honor of Rainbow Dash - inventor of the Sonic RainBoom.\""; 
    print(VIEW);

    print("\n Navigation options:");
    print(" (N)orth, you see gray, rocky caves and a salty old mare selling flowers.");
    print(" South, you see cobbled stone huts and houses.");
    print(" East, you spy an enormous apple orchard. The trees are full of ripe, red delicious apples.");
    print(" West, you see a large stone building with dozens of weather veins and observation stations.");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_PEGASUSCITADEL";       
                elif(CHOICE == "n"):
                     globals()['CurrentLocation'] = "L1_WEST_2";
                elif(CHOICE == "s"):
                     print("\n You trot SOUTH and find yourself standing beside some gray and brown cobbles stone houses.");
                     print(" In between several of thes stone house you see several straw huts.");
                     print(" An abandoned wagon leans against the wall, missing all of its wheels.");
                     print(" You can go no further south from here.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "e"):
                     print("\n You walk EAST into a serene apple orchard. It's enormous! You spy tall apple trees sprawling");
                     print(" out towards the horizon as far as the eye can see. On each of these trees you see the most succulent,");
                     print(" juicy, red delicious apples you've ever seen. At the end of this orhard is a stone wall.");
                     print(" You can go no further east from here.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     print("\n You move WEST and into the large stone building. Once inside, you can see dozens of pegasuses");
                     print(" runnning around with various gadgets and gizmos taking measurements. You see a large wooden frame"); 
                     print(" on the westmost wall of thie building. It says \"Bureau of Weather Control\""); 
                     print(" There are no doors or windows on this wall, so you can go no further west.");
                     ContinueIT = input("\n Press ENTER to proceed.");        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_FRIENDSHIPFOREST():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] Friendship Forest");

    VIEW =        "\n View:  You find yourslef at the edge of a lush, everfreen forest. All around you are tall evergreen trees";
    VIEW = VIEW + "\n that spiral into the sky. The trees are so tall and clos together, the create a large canopy above that";
    VIEW = VIEW + "\n shades the earth beneath. Furry and feathery forest creatures fill the branches of these trees as far as";
    VIEW = VIEW + "\n you can see. Fluffy, squirrels and cute, cuddly bunnies dart to and fro among the massive roots of the";
    VIEW = VIEW + "\n evergreens that spread out across the forest floor.";
    print(VIEW);

    print("\n Navigation options:");
    print(" (N)orth, you see a castle courtyard in the distance. Beyond it a tall castle spirals into the sky.");
    print(" South, you see a small wooden sign planted next to a grassy path lined with evergreens on both sides.");
    print(" East, are endless woodlands full of happy hopping, scampering, flying and prancing forest creatures.");
    print(" West, a small circle of cute, chubby, fluffy bunnies has gathered together for a meeting.");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_FRIENDSHIPFOREST";       
                elif(CHOICE == "n"):
                     globals()['CurrentLocation'] = "L1_WEST_3"; 
                elif(CHOICE == "s"):
                     print("\n You gallop SOUTH down the path between the rows of trees and draw closer to the small, wooden sign.");
                     print(" As you get near it, you can see that the sign is painted with a yellow border and large, pink letters.");
                     print(" The letters say \"Fluttershy's Friendship Forest\". You can see a cottage framed on every side with");
                     print(" beautiful flower boxes further down the path. But every time you try to press further south towards the");
                     print(" cottage? Rain, hail and tornadoes descend from the sky and make an impenetrable wall of weather.");
                     print(" You can move no further SOUTH in this direction.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "e"):
                     print("\n Going EAST, you walk into the midst of dozens of happy, hopping, scurrying, twittering squirrels and birds and");
                     print(" bunnies and foxes and feral kitties and does with their fawns and racoons and possums and skunks and field mice.");
                     print(" You ask them what do they call this place in which you now find yourself. Hoping for an answer, you wait for their");
                     print(" reply but they don't giv e you one. Why can't these animals talk like other animals you have met before?");
                     print(" Afraid of getting lost, you decide not to travel any further east.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     print("\n Trotting WEST, you step into the middle of a circle of cute, fluffy bunnies. You feel a bit awkward,");
                     print(" as they all stare at you now and you are at the center of their attention. You introduce yourself, but they");
                     print(" do not repond. If only you had something to break the ice with? Something that would earn their favor?");
                     print(" You decide to go no further west until you find a way to befriend these bunnies.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                       

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 





#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def L1_UNICORNJUNCTION():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] Unicorn Junction");

    VIEW =        "\n View:  You trot into lively equestrian village. All around you, unicorns are ahoof carrying packages";
    VIEW = VIEW + "\n and parcels telikinetically by magic! The wood and straw houses in this village are all painted purple,";
    VIEW = VIEW + "\n pink and lavender. You see a large banner draped across the center of the village that says"; 
    VIEW = VIEW + "\n \"Twilight's Twinkly Friendshp Fair\". In the center of the village is a large gazebo, and doszens"; 
    VIEW = VIEW + "\n of tables have been setup around it with cupcakes! Yum!"; 
    print(VIEW);

    print("\n Navigation options:");
    print(" North, you see many tables surrounding a gazebo with colorful CUPCAKES.");
    print(" (S)outh, you see an arid, sandy a plain populated with withered grass and dessicated trees. Cactii grow between the trees.");
    print(" East, a shop with a sign that says \"Relationship Counseling\". Outside the shop are several wooden barrels.");
    print(" West, you see a cobbled stone building with a sign on top that says \"Magic Shop\".");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "L1_UNICORNJUNCTION";       
                elif(CHOICE == "n"):
                     print("\n You walk NORTH towards the gazebo and find yoruself surrounded by tables of cupcakes.");
                     print(" You wonder if they are for sale? Or perhaps prepared for someone special on their birthday?");
                     print(" From this area you can proceed no further north."); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "s"):
                     globals()['CurrentLocation'] = "L1_WEST_1";   
                elif(CHOICE == "e"):
                     print("\n You trot EAST over to the shop with the sing that reads \"Relationship Counseling\"");
                     print(" You try to turn the door knob and open the door, but you cannot. It is LOCKED.");
                     print(" If only you had a KEY? Until you find one, you can proceed no further east from here.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     print("\n You gallop WEST over towards the building with the sign that says \"Magic Shop\".");
                     print(" You see a sign hanging in the window. It says \"Out to lunch. Be back soon. Come back later.\"");
                     print(" You can go no further west from here.");
                     ContinueIT = input("\n Press ENTER to proceed.");
                         
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Save_Game():
    system("cls"); 
    print("\nSaving Game");

    # 1. Get current script directory (needs "import os").
    CurrentDir = os.getcwd();  
    print("Creating Character and Game State save files in: \"",CurrentDir,"\"",sep='');

    # 2. Create game character file based on character's name
    print("\nSaving Character Data ...");
    Char_Name = CurrentDir + "\\" + "DD_Character_" + Player_Heroine.EntityName + ".DDchar";
    print("Complete file name and path is:",Char_Name);
    
    # 3. Overwrite existing character file if already exists.
    CharSaveFile = open(Char_Name, "w");

    # 4. Create and populate Array to serialize derives and base class data members
    Char_Data = [];
    Char_Data.append( (Player_Heroine.EntityName + "\n") );
    Char_Data.append( (Player_Heroine.EntityGender + "\n") ); 
    Char_Data.append( (Player_Heroine.EntityClass + "\n") ); 
    Char_Data.append( (str(Player_Heroine.EntityHealth) + "\n") ); 
    Char_Data.append( (str(Player_Heroine.EntityDefense) + "\n") ); 
    Char_Data.append( (str(Player_Heroine.EntityAttack) + "\n") ); 
    Char_Data.append( (str(Player_Heroine.EntityMagicPower) + "\n") ); 
    Char_Data.append( (Player_Heroine.WeaponChoice + "\n") ); 
    Char_Data.append( (Player_Heroine.MagicChoice + "\n") ); 
    Char_Data.append( (Player_Heroine.ArmorChoice + "\n") ); 
    Char_Data.append( (Player_Heroine.Invisibility_Active + "\n") ); 
    Char_Data.append( (str(Player_Heroine.Invisibility_Count) + "\n") );
    Char_Data.append( (str(Player_Heroine.Dammage_Item_Staff) + "\n") );
    Char_Data.append( (str(Player_Heroine.Dammage_Item_Pendant) + "\n") );
    Char_Data.append( (str(Player_Heroine.Dammage_Item_Sigil) + "\n") );
    Char_Data.append( (str(Player_Heroine.Dammage_Item_Orb) + "\n") );
    Char_Data.append( (str(Player_Heroine.Dammage_Item_PrincessCloak) + "\n") );
    Char_Data.append( (str(Player_Heroine.Dammage_Skill_IceBlasts) + "\n") );
    Char_Data.append( (str(Player_Heroine.Dammage_Skill_FireBalls) + "\n") );
    Char_Data.append( (str(Player_Heroine.Dammage_Skill_Lightning) + "\n") );
    Char_Data.append( (str(Player_Heroine.Dammage_Skill_Telekinesis) + "\n") );
    Char_Data.append( (str(Player_Heroine.Dammage_Skill_Telepathy) + "\n") );
    Char_Data.append( (str(Player_Heroine.Dammage_Skill_Teleportation) + "\n") );
    Char_Data.append( (str(Player_Heroine.Dammage_Skill_TimeWarp) + "\n") );
    Char_Data.append( (str(Player_Heroine.Invisibility_DEF_Amt) + "\n") );
    Char_Data.append( (Player_Heroine.INV_Has_Staff + "\n") );
    Char_Data.append( (Player_Heroine.INV_Has_Pendant + "\n") );
    Char_Data.append( (Player_Heroine.INV_Has_Sigil + "\n") );
    Char_Data.append( (Player_Heroine.INV_Has_Orb + "\n") );
    Char_Data.append( (Player_Heroine.INV_Has_PrincessCloak + "\n") );
    Char_Data.append( (str(Player_Heroine.INV_Has_HealingPotions) + "\n") );
    Char_Data.append( (str(Player_Heroine.HealthPotion_Restore_Amt) + "\n") );
    Char_Data.append( (Player_Heroine.INV_Has_Chain_Mail + "\n") );
    Char_Data.append( (Player_Heroine.INV_Has_Plate_Armor + "\n") );
    Char_Data.append( (Player_Heroine.SKILL_Has_IceBlasts + "\n") );
    Char_Data.append( (Player_Heroine.SKILL_Has_FireBalls + "\n") );
    Char_Data.append( (Player_Heroine.SKILL_Has_Lightning + "\n") );
    Char_Data.append( (Player_Heroine.SKILL_Has_Telekinesis + "\n") );
    Char_Data.append( (Player_Heroine.SKILL_Has_Telepathy + "\n") );
    Char_Data.append( (Player_Heroine.SKILL_Has_Teleportation + "\n") );
    Char_Data.append( (Player_Heroine.SKILL_Has_TimeWarp + "\n") );
    Char_Data.append( (Player_Heroine.SKILL_Has_Invisibility + "\n") );
    Char_Data.append( (str(Player_Heroine.SKILL_Invisibility_Cost) + "\n") );
    Char_Data.append( (Player_Heroine.SKILL_Has_Healing + "\n") );
    Char_Data.append( (str(Player_Heroine.SKILL_Healing_Restore_Amt) + "\n") );
    Char_Data.append( (Player_Heroine.SKILL_Has_FriendshipCast + "\n") );

    # 5. Write character data to file using line as a delimiter and close file.
    CharSaveFile.writelines(Char_Data);
    CharSaveFile.close();

    # 6.  Create Game State file. 
    print("\nSaving Game State and MAP location Data ...");
    GameState_Name = CurrentDir + "\\" + "DD_GameState_" + Player_Heroine.EntityName + ".DDgame";
    print("Complete file name and path is:",GameState_Name);
    
    # 7. Overwrite existing Game State file if already exists.
    GameStateSaveFile = open(GameState_Name, "w");

    # 8. Create and populate Array to serialize Game State data
    GameState_Data = [];
    GameState_Data.append( (CurrentLocation + "\n") );
    GameState_Data.append( (Found_Staff + "\n") );
    GameState_Data.append( (Found_Pendant + "\n") );
    GameState_Data.append( (Found_Sigil + "\n") );
    GameState_Data.append( (Found_Orb + "\n") );
    GameState_Data.append( (Found_PrincessCloak + "\n") );
    GameState_Data.append( (Found_Chain_Mail + "\n") );
    GameState_Data.append( (Found_Plate_Armor + "\n") );
    GameState_Data.append( (Found_HealingPotion_1 + "\n") );
    GameState_Data.append( (Found_HealingPotion_2 + "\n") );
    GameState_Data.append( (Found_HealingPotion_3 + "\n") );
    GameState_Data.append( (Found_HealingPotion_4 + "\n") );
    GameState_Data.append( (Found_HealingPotion_CelestiasPalace + "\n") );
    GameState_Data.append( (Acquired_IceBlasts + "\n") );
    GameState_Data.append( (Acquired_FireBalls + "\n") );
    GameState_Data.append( (Acquired_Lightning  + "\n") );
    GameState_Data.append( (Acquired_Telekinesis + "\n") );
    GameState_Data.append( (Acquired_Telepathy + "\n") );
    GameState_Data.append( (Acquired_Teleportation + "\n") );
    GameState_Data.append( (Acquired_TimeWarp + "\n") );
    GameState_Data.append( (Acquired_Invisibility + "\n") );    
    GameState_Data.append( (Acquired_Healing + "\n") );   
    GameState_Data.append( (Acquired_FriendshipCast + "\n") );   

    # 9. Write Game State data to file using line as a delimiter and close file. 
    GameStateSaveFile.writelines(GameState_Data);
    GameStateSaveFile.close();   
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Load_Game():
    system("cls"); 
    print("\nLoading Game");

    # 1. Get current script directory (needs "import os").
    CurrentDir = os.getcwd();  
    print("Searching for Character and Game State save files in: \"",CurrentDir,"\"",sep='');

    # 2. List files in that directory
    print("Listing game files in this directory.");
    print("\n----------------------------------------------------------------");

    FileCounter = 0;
    Array_of_Files_In_Dir = os.listdir();
    
    for x in Array_of_Files_In_Dir:

        if(x.endswith(".DDchar") or x.endswith(".DDgame")):
           FileCounter = FileCounter + 1;
           print(FileCounter,"\b.",x);

    print("----------------------------------------------------------------\n");     

    # 3. Ask player to choose game to load and open file
    CHOICE = input("\nWhich game would you like to load? ");
    Char_File_Name = CurrentDir + "\\" + "DD_Character_" + CHOICE + ".DDchar";
    CharSave_File = open(Char_File_Name, "r");

    #4. Read data from file into an array, line by line into each element. Close file to be SAFE.
    Char_Data = CharSave_File.read().splitlines();
    CharSave_File.close(); #No longer need file open now that data has been extracted to array

    #5. Instantiate a Character object for game based on CLASS data type
    if(Char_Data[2] == "Alicorn"): 
       print("\nInstantiating an ALICORN.");
       Heroine = ALICORN();
    elif(Char_Data[2] == "Unicorn"): 
         print("\nInstantiating a UNICORN.");
         Heroine = UNICORN();   
    elif(Char_Data[2] == "Pegasus"): 
         print("\nInstantiating a PEGASUS.");
         Heroine = PEGASUS();
    elif(Char_Data[2] == "Princess"): 
         print("\nInstantiating a PRINCESS.");
         Heroine = PRINCESS();               
    elif(Char_Data[2] == "Pony"): 
         print("\nInstantiating a basic PONY.");
         Heroine = PONY();

    # 6. Assign it to global pointer once eobject has been built
    globals()['Player_Heroine'] = Heroine; 
 
    # 7. Load and assign values to newly instantiated Character object
    print("\n----------Loading Game Character data----------");
    print("Name:",Char_Data[0]);
    Player_Heroine.EntityName = Char_Data[0];
    print("Gender:",Char_Data[1]);
    Player_Heroine.EntityGender = Char_Data[1];
    print("Class:",Char_Data[2]);
    Player_Heroine.EntityClass = Char_Data[2];
    print("Health:",Char_Data[3]);
    Player_Heroine.EntityHealth = int(Char_Data[3]);
    print("Defense:",Char_Data[4]);
    Player_Heroine.EntityDefense = int(Char_Data[4]);
    print("Attack:",Char_Data[5]);
    Player_Heroine.EntityAttack = int(Char_Data[5]);
    print("Magic Power:",Char_Data[6]);
    Player_Heroine.EntityMagicPower = int(Char_Data[6]);
    print("Weapon Choice:",Char_Data[7]);
    Player_Heroine.WeaponChoice = Char_Data[7];
    print("Magic Choice:",Char_Data[8]);
    Player_Heroine.MagicChoice = Char_Data[8];
    print("Armor Choice:",Char_Data[9]);
    Player_Heroine.ArmorChoice = Char_Data[9];   
    print("Invisibility Active:",Char_Data[10]);
    Player_Heroine.Invisibility_Active = Char_Data[10];
    print("Invisibility Count:",Char_Data[11]);
    Player_Heroine.Invisibility_Count = int(Char_Data[11]);
    print("Dammage_Item_Staff:",Char_Data[12]);
    Player_Heroine.Dammage_Item_Staff = int(Char_Data[12]);
    print("Dammage_Item_Pendant:",Char_Data[13]);
    Player_Heroine.Dammage_Item_Pendant = int(Char_Data[13]);
    print("Dammage_Item_Sigil:",Char_Data[14]);
    Player_Heroine.Dammage_Item_Sigil = int(Char_Data[14]); 
    print("Dammage_Item_Orb:",Char_Data[15]);
    Player_Heroine.Dammage_Item_Orb = int(Char_Data[15]); 
    print("Dammage_Item_PrincessCloak:",Char_Data[16]);
    Player_Heroine.Dammage_Item_PrincessCloak = int(Char_Data[16]);
    print("Dammage_Skill_IceBlasts:",Char_Data[17]);
    Player_Heroine.Dammage_Skill_IceBlasts = int(Char_Data[17]);  
    print("Dammage_Skill_FireBalls:",Char_Data[18]);
    Player_Heroine.Dammage_Skill_FireBalls = int(Char_Data[18]);   
    print("Dammage_Skill_Lightning:",Char_Data[19]);
    Player_Heroine.Dammage_Skill_Lightning = int(Char_Data[19]);   
    print("Dammage_Skill_Telekinesis:",Char_Data[20]);
    Player_Heroine.Dammage_Skill_Telekinesis = int(Char_Data[20]);    
    print("Dammage_Skill_Telepathy:",Char_Data[21]);
    Player_Heroine.Dammage_Skill_Telepathy = int(Char_Data[21]);   
    print("Dammage_Skill_Teleportation:",Char_Data[22]);
    Player_Heroine.Dammage_Skill_Teleportation = int(Char_Data[22]);  
    print("Dammage_Skill_TimeWarp:",Char_Data[23]);
    Player_Heroine.Dammage_Skill_TimeWarp = int(Char_Data[23]);  
    print("Invisibility_DEF_Amt:",Char_Data[24]);
    Player_Heroine.Invisibility_DEF_Amt = int(Char_Data[24]);
    print("INV_Has_Staff:",Char_Data[25]);
    Player_Heroine.INV_Has_Staff = Char_Data[25];   
    print("INV_Has_Pendant:",Char_Data[26]);
    Player_Heroine.INV_Has_Pendant = Char_Data[26];   
    print("INV_Has_Sigil:",Char_Data[27]);
    Player_Heroine.INV_Has_Sigil = Char_Data[27];   
    print("INV_Has_Orb:",Char_Data[28]);
    Player_Heroine.INV_Has_Orb = Char_Data[28];   
    print("INV_Has_PrincessCloak:",Char_Data[29]);
    Player_Heroine.INV_Has_PrincessCloak = Char_Data[29];
    print("INV_Has_HealingPotions:",Char_Data[30]);
    Player_Heroine.INV_Has_HealingPotions = int(Char_Data[30]);
    print("HealthPotion_Restore_Amt:",Char_Data[31]);
    Player_Heroine.HealthPotion_Restore_Amt = int(Char_Data[31]);
    print("INV_Has_Chain_Mail:",Char_Data[32]);
    Player_Heroine.INV_Has_Chain_Mail = Char_Data[32];
    print("INV_Has_Plate_Armor:",Char_Data[33]);
    Player_Heroine.INV_Has_Plate_Armor = Char_Data[33]; 
    print("SKILL_Has_IceBlasts:",Char_Data[34]);
    Player_Heroine.SKILL_Has_IceBlasts = Char_Data[34];   
    print("SKILL_Has_FireBalls:",Char_Data[35]);
    Player_Heroine.SKILL_Has_FireBalls = Char_Data[35];    
    print("SKILL_Has_Lightning:",Char_Data[36]);
    Player_Heroine.SKILL_Has_Lightning = Char_Data[36];    
    print("SKILL_Has_Telekinesis:",Char_Data[37]);
    Player_Heroine.SKILL_Has_Telekinesis = Char_Data[37];    
    print("SKILL_Has_Telepathy:",Char_Data[38]);
    Player_Heroine.SKILL_Has_Telepathy = Char_Data[38];   
    print("SKILL_Has_Teleportation:",Char_Data[39]);
    Player_Heroine.SKILL_Has_Teleportation = Char_Data[39];    
    print("SKILL_Has_TimeWarp:",Char_Data[40]);
    Player_Heroine.SKILL_Has_TimeWarp = Char_Data[40];    
    print("SKILL_Has_Invisibility:",Char_Data[41]);
    Player_Heroine.SKILL_Has_Invisibility = Char_Data[41];    
    print("SKILL_Invisibility_Cost:",Char_Data[42]);
    Player_Heroine.SKILL_Invisibility_Cost = Char_Data[42];    
    print("SKILL_Has_Healing:",Char_Data[43]);
    Player_Heroine.SKILL_Has_Healing = Char_Data[43];    
    print("SKILL_Healing_Restore_Amt:",Char_Data[44]);
    Player_Heroine.SKILL_Healing_Restore_Amt = Char_Data[44];    
    print("SKILL_Has_FriendshipCast:",Char_Data[45]);
    Player_Heroine.SKILL_Has_FriendshipCast = Char_Data[45];

    # 8. Open Game State file 
    GameState_File_Name = CurrentDir + "\\" + "DD_GameState_" + CHOICE + ".DDgame";
    GameState_File = open(GameState_File_Name, "r");
    
    #9. Read data from file into an array, line by line into each element. Close file to be SAFE.
    GameState_Data = GameState_File.read().splitlines();
    GameState_File.close(); #No longer need file open now that data has been extracted to array

    # 10. Load and assign values from array to Game State
    print("\n----------Loading Game State data----------");
    print("Game Location:",GameState_Data[0]);
    globals()['CurrentLocation'] = GameState_Data[0];
    print("Found_Staff:",GameState_Data[1]);
    globals()['Found_Staff'] = GameState_Data[1];   
    print("Found_Pendant:",GameState_Data[2]);
    globals()['Found_Pendant'] = GameState_Data[2];
    print("Found_Sigil:",GameState_Data[3]);
    globals()['Found_Sigil'] = GameState_Data[3];
    print("Found_Orb :",GameState_Data[4]);
    globals()['Found_Orb'] = GameState_Data[4];   
    print("Found_PrincessCloak:",GameState_Data[5]);
    globals()['Found_PrincessCloak'] = GameState_Data[5];
    print("Found_Chain_Mail:",GameState_Data[6]);
    globals()['Found_Chain_Mail'] = GameState_Data[6]; 
    print("Found_Plate_Armor:",GameState_Data[7]);
    globals()['Found_Plate_Armor'] = GameState_Data[7];   
    print("Found_HealingPotion_1:",GameState_Data[8]);
    globals()['Found_HealingPotion_1'] = GameState_Data[8];
    print("Found_HealingPotion_2:",GameState_Data[9]);
    globals()['Found_HealingPotion_2'] = GameState_Data[9];              
    print("Found_HealingPotion_3:",GameState_Data[10]);
    globals()['Found_HealingPotion_3'] = GameState_Data[10];  
    print("Found_HealingPotion_4:",GameState_Data[11]);
    globals()['Found_HealingPotion_4'] = GameState_Data[11];     
    print("Found_HealingPotion_CelestiasPalace:",GameState_Data[12]);
    globals()['Found_HealingPotion_CelestiasPalace'] = GameState_Data[12];   
    print("Acquired_IceBlasts:",GameState_Data[13]);
    globals()['Acquired_IceBlasts'] = GameState_Data[13];      
    print("Acquired_FireBalls:",GameState_Data[14]);
    globals()['Acquired_FireBalls'] = GameState_Data[14];     
    print("Acquired_Lightning:",GameState_Data[15]);
    globals()['Acquired_Lightning'] = GameState_Data[15];   
    print("Acquired_Telekinesis:",GameState_Data[16]);
    globals()['Acquired_Telekinesis'] = GameState_Data[16];   
    print("Acquired_Telepathy:",GameState_Data[17]);
    globals()['Acquired_Telepathy'] = GameState_Data[17];     
    print("Acquired_Teleportation:",GameState_Data[18]);
    globals()['Acquired_Teleportation'] = GameState_Data[18];   
    print("Acquired_TimeWarp:",GameState_Data[19]);
    globals()['Acquired_TimeWarp'] = GameState_Data[19];      
    print("Acquired_Invisibility:",GameState_Data[20]);
    globals()['Acquired_Invisibility'] = GameState_Data[20];     
    print("Acquired_Healing:",GameState_Data[21]);
    globals()['Acquired_Healing'] = GameState_Data[21];   
    print("Acquired_FriendshipCast:",GameState_Data[22]);
    globals()['Acquired_FriendshipCast'] = GameState_Data[22];

    ContinueIT = input("\n Press ENTER to launch RPG game from last saved position, state and stats.");

    SwitchBoard();    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Map_Location_Template():
    system("cls");
    CHOICE = "";
    print("\n Location: [Level 1] ??????");

    VIEW =        "\n View:  ";
    VIEW = VIEW + "\n "; 
    print(VIEW);

    print("\n Navigation options:");
    print(" North, ");
    print(" South, ");
    print(" East, ");
    print(" West, ");
    while(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l" and globals()['CurrentLocation'] != "QUIT_GAME"):
          print("\n    Choices:");
          print("   ┌────────────────────────────────────────────────────┐");
          print("   │  Navigation:     (N)orth  (S)outh  (E)ast  (W)est  │");
          print("   │  Other Choices:  (O)ptions  (L)ook                 │");
          print("   └────────────────────────────────────────────────────┘");
          CHOICE = input("\n    Choose: ");
          CHOICE = CHOICE.lower();
          
          if(CHOICE != "n" and CHOICE != "s" and CHOICE != "e" and CHOICE != "w" and CHOICE != "o" and CHOICE != "l"):
             print(" That was not a valid option for this particular level and map location.");
          else:   
                if(CHOICE == "o"):
                   Options();
                elif(CHOICE == "l"):
                     globals()['CurrentLocation'] = "";       
                elif(CHOICE == "n"):
                     print("\n ");
                     print(" "); 
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "s"):
                     print("\n ");
                     print(" ");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "e"):
                     print("\n ");
                     print(" ");
                     ContinueIT = input("\n Press ENTER to proceed.");
                elif(CHOICE == "w"):
                     globals()['CurrentLocation'] = "L1_EAST_2";   
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 




#-----Invocations------
Main_Menu();



# ASCII codes for box menus
  # ALT + 218 = ┌
  # ALT + 191 = ┐
  # ALT + 196 = ─
  # ALT + 192 = └
  # ALT + 217 = ┘
  # ALT + 222 = ▐ 
  # ALT + 219 = █ 
  # ALT + 179 = │
  # ALT + 186 = ║
  #   ┌  ─  ┐   │ │ └  ┘
# 
# 
#
#
#File Access
# 
# A. READ file examples
     #----------------------------------------------------------------- 
     # 1. Using the read() method:
     #
     #    f = open("demofile.txt", "r");
     #    print(f.read());
     #-----------------------------------------------------------------   
     # 2. Using readlines():
     #
     #    with open('readme.txt') as f:
     #         lines = f.readlines();
     #-----------------------------------------------------------------   
     # 3.
     #    with open('the-zen-of-python.txt') as f:
     #         contents = f.read();
     #         print(contents);
     #-----------------------------------------------------------------   
     # 4. Using "with" and a for loop:
     #
     #    lines = []
     #    with open('the-zen-of-python.txt') as f:
     #         lines = f.readlines();

     #    count = 0
     #    for line in lines:
     #        count += 1;
     #        print(f'line {count}: {line}'); 
     #-----------------------------------------------------------------   
     # 5. The open() function returns an iterable object so you can also:
     #
     #    with open('the-zen-of-python.txt') as f:
     #         for line in f:
     #             print(line);
     #-----------------------------------------------------------------   
     # 6. Reading UTF-8 files that aren't ASCII
     #
     #    with open('quotes.txt', encoding='utf8') as f:
     #         for line in f:
     #             print(line.strip());
     #-----------------------------------------------------------------  
     #
#
# Methods
    # read() – read all text from file into a string
    # readline() – read text file line by line and return all lines as strings
    # readlines() – read all lines of text file and return as a list of strings
    # close() - close file when not in use so won't crash or be corrupted   Example: f.close()
    # with - closes file automatically without calling close()
#
# Arguments
     #"r" - Read - Default value. Opens a file for reading, error if the file does not exist  EXAMPLE: f = open("path_to_file", mode='r')
     #"a" - Append - Opens a file for appending, creates the file if it does not exist   EXAMPLE: f = open("path_to_file", mode = 'a')
     #"w" - Write - Opens a file for writing, creates the file if it does not exist   EXAMPLE: f = open("path_to_file", mode = 'w')
     #"x" - Create - Creates the specified file, returns an error if the file exist

#In addition you can specify if the file should be handled as binary or text mode
     #"t" - Text - Default value. Text mode
     #"b" - Binary - Binary mode (e.g. images)
# 
# New Line arguments = None, ' ', '\n', 'r', and '\r\n' 
#
# Python's default encoding is ASCII. You can change it with:  f = open("path_to_file", mode = 'r', encoding='utf-8')
#
# B. WRITE file examples
     #----------------------------------------------------------------- 
     # 1. Using the write() method to append to an existing file:
     #
     #           f = open("demofile2.txt", "a");
     #           f.write("Now the file has more content!");
     #           f.close();
     #----------------------------------------------------------------- 
     # 2. Using the write() method to overwrite existing file: 
     #
     #           f = open("demofile3.txt", "w")
     #           f.write("Woops! I have deleted the content!")
     #           f.close()
     #----------------------------------------------------------------- 
#
# Get Current Working Directory of file
#
#     1. Must  "import os" at top of script
#     2. cwd = os.getcwd() 
#
