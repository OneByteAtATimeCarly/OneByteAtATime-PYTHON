#Title: Discord's Dungeon 04 - Coding Expanded Inventory, Skills and Equip Methods. Building Objects. Manipulating Classes and Class Data Members.
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

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Constants - Locations on map
c_QUIT = 0;
c_INTRO = 1;
c_C1 = 2;
c_N1 = 3;
c_S1 = 4;
c_E1 = 5;
c_W1 = 6;
c_N2 = 7;
c_S2 = 8;
c_E2 = 9;
c_W2 = 10;
c_GATE =11;
c_SHAMANS_HUT = 12;
c_UNDERGRND = 13;

#Constants - Inventory items on map
c_NothingAtAll = 0;
c_HasStaff = 1;
c_HasPendant = 2;
c_HasSigil = 3;
c_HasOrb = 4;
c_HasPrincessCloak = 5;

#Constants - Magic abilities that can be earned
c_NoMagic = 0;
c_Fire = 1;
c_Ice = 2;
c_Lightning = 3;
c_TelekineticForce = 4;
c_Invisibility = 5;
c_Healing = 6;

#Constants - Armor that may be acquired
c_NoArmor = 0;
c_ChainMail = 5;
c_PLateMail = 10;

#Global for determining player position on map
CurrentLocation = None;

#Global pseudo-booleans for Inventory Items that can be found
CENTERFirstTime = "TRUE";
FoundHealingPotion = "FALSE";
S1DragonAlive = "TRUE";
E1DragonAlive = "TRUE";
W1GiantAlive = "TRUE";
FirstTimeInShamanHut = "TRUE";
FoundHP_Shaman = "FALSE";
UNDERDragonPairAlive = "TRUE";
S2MotleyCrewAlive = "TRUE";
FoundHP_West2 = "FALSE";
Willing_to_Fight = "TRUE";
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
                          MESSAGE = MESSAGE + " FriendshipCast! " + self.EntityName + " casts peace, love friendship on opponent decreasing aggression."; 
                          MESSAGE = MESSAGE + "\n Opponent no longer wishes to fight due to positive feelings of love and friendsip. Exiting combat...";
                          if(self.EntityMagicPower - 100 > 0):
                             self.EntityMagicPower = self.EntityMagicPower - 100;  
                             globals()['Willing_to_Fight'] = "FALSE";
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
      EntityClass = "Equestrian";
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
      Alicorn_Ability_01 = "Ability 1";
      Alicorn_Ability_02 = "Ability 2";

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
def Create_Characters(): 
    CHOICE = "";  
    system('cls');
    print("\n You must create a Game_Entity object before you can play.");
    print("\n First, we must Instantiate your created character as the player object.");
    print("\n 1. Choose a CLASS for your character:\n");

    while(CHOICE != "a" and CHOICE != "p" and CHOICE != "b"):
          print("    ----Character Classes----");
          print("    |                       |");
          print("    |      (A)licorn        |");
          print("    |      (P)rinces        |");
          print("    |      (B)asic Pony     |");
          print("    |                       |");
          print("    -------------------------");    
          CHOICE = input("\nChoose: ");
          CHOICE = CHOICE.lower();
          if(CHOICE == "a"): 
             print("\n Instantiating an ALICORN.");
             Heroine = ALICORN();
          elif(CHOICE == "p"): 
               print("\n Instantiating a PRINCESS.");
               Heroine = PRINCESS();
          elif(CHOICE == "b"): 
               print("\n Instantiating a basic PONY.");
               Heroine = PONY();
          else: print("That was an INVALID option. Please choose a character class.");
   
    print("\n 2. Choose a GENDER for your character (m/f):\n");
    while(CHOICE != "m" and CHOICE != "f"):
          print("    --Character Gender---");
          print("    |                   |");
          print("    |      (F)emale     |");
          print("    |      (M)ale       |");
          print("    |                   |");
          print("    ---------------------");    
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
    Heroine.Cheat_Mode();
    Heroine.Display_All();
    ContinueIT = input("\nPress ENTER to proceed.");      

    system("cls");
    print(" Second, we must instantiate the opponent object(s).");
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
          print("-----------Combat-Modes-----------");
          print("|                                |");
          print("|      (I)nteractive Combat      |");
          print("|      (A)utomated Combat        |");
          print("|                                |");
          print("----------------------------------");    
          CHOICE = input("\nChoose: ");
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
    while Player_Opponent.EntityHealth > 0 and Player_Heroine.EntityHealth > 0:               
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

    ContinueIT = input("\nPress ENTER to proceed.");  
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Options():
    Present_Options_Menu = "TRUE";

    while Present_Options_Menu != "FALSE":
          system('cls');
          print("\n      ----------------Options------------------");
          print("      |                                       |");
          print("      |        1. Display Stats               |");
          print("      |        2. Display Inventory           |");
          print("      |        3. Display Magic Skills        |");
          print("      |        4. Display Everything          |");
          print("      |        5. Equip Inventory Item        |");
          print("      |        6. Equip Magic Skill           |");
          print("      |        7. Save Game                   |");
          print("      |        8. Load Game                   |");
          print("      |        9. Activate Cheat Mode         |");
          print("      |        0. Exit                        |");
          print("      |                                       |");
          print("      -----------------------------------------");

          CHOICE = input("\n      Your choice: ");
          CHOICE = CHOICE.lower();

          if(CHOICE != "1" and CHOICE != "2" and CHOICE != "3" and CHOICE != "4" and CHOICE != "5" and 
             CHOICE != "6" and CHOICE != "7" and CHOICE != "8" and CHOICE != "9" and CHOICE != "0"):
             print("\nThat was an invalid choice.");
          else:   
                if(CHOICE == "1"): 
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
                     print("Saving game ...");
                elif(CHOICE == "8"): 
                     print("Loading game ...");
                elif(CHOICE == "9"):
                     Player_Heroine.Cheat_Mode();                     
                elif(CHOICE == "0"):
                     print("\nExiting options menu ..."); 
                     Present_Options_Menu = "FALSE";      

          ContinueIT = input("\nPress ENTER to proceed.");                                                                                                          
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Main_Menu():
    Present_Main_Menu = "TRUE";

    while Present_Main_Menu != "FALSE":
          system('cls');
          print("\nWelcome to Discord's Dungeon!");
          print("©2022 Carly Salali Germany\n\n");

          print("\n      ---------------------Main Menu-------------------");
          print("      |                                               |");
          print("      |              1. Create Character              |");
          print("      |              2. Options                       |");
          print("      |              3. Magic Combat!                 |");
          print("      |              4. Play RPG                      |");
          print("      |              5. Exit                          |");
          print("      |                                               |");
          print("      -------------------------------------------------");

          CHOICE = input("\n      Your choice: ");
          CHOICE = CHOICE.lower();

          if(CHOICE != "1" and CHOICE != "2" and CHOICE != "3" and CHOICE != "4" and CHOICE != "5"):
             print("\nThat was an invalid choice.");
          else:   
                if(CHOICE == "1"): 
                   Create_Characters();
                   #Auto_Create_Characters_for_Testing();
                elif(CHOICE == "2"): 
                     Options(); 
                elif(CHOICE == "3"): 
                     Pony_Combat();  
                elif(CHOICE == "4"): 
                     Play_RPG();                       
                elif(CHOICE == "5"): 
                     Present_Main_Menu = "FALSE";
                     print("\nNow exiting Discord's Dungeon ... Goodbye!");                                                                                                     
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



#-----Invocations------
#Magic_Battle();
#TEST1();
Main_Menu();

