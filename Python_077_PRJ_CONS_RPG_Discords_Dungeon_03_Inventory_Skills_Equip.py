#Title: Discord's Dungeon 03 - Coding Inventory, Skills and Equipping/Using Items. Accessing and Manipulating Class Data Members. Instantiation.
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
      SKILL_Has_Healing = "FALSE";
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
          self.SKILL_Has_FriendshipCast = "TRUE";
          self.WeaponChoice = "Orb";
          self.MagicChoice= "Telekinesis";
          self.ArmorChoice = "PlateArmor";
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
          elif self.WeaponChoice == "Staff": STATS = STATS + "Staff";
          elif self.WeaponChoice == "Pendant": STATS = STATS + "Pendant";    
          elif self.WeaponChoice == "Sigil": STATS = STATS + "Sigil";
          elif self.WeaponChoice == "Orb": STATS = STATS + "Orb";
          elif self.WeaponChoice == "PrincessCloak": STATS = STATS + "PrincessCloak";
          print("     ","Selected Weapon:",STATS);

          STATS = "";
          if self.ArmorChoice == "None": 
             STATS = STATS + "Nothing but ";
             if self.EntityGender == "Female": STATS = STATS + "her";
             elif self.EntityGender == "Male": STATS = STATS + "his";
             STATS = STATS + " birthday suit.";
          elif self.ArmorChoice == "ChainMail": STATS = STATS + "Link Chain Mail";
          elif self.ArmorChoice == "PlateArmor": STATS = STATS + "Plate Armor";    
          print("     ","Selected Armor:",STATS);

          STATS = "";
          if self.MagicChoice == "None": 
             STATS = STATS + "Nothing but ";
             if self.EntityGender == "Female": STATS = STATS + "her";
             elif self.EntityGender == "Male": STATS = STATS + "his";
             STATS = STATS + " wits!";
          elif self.MagicChoice == "IceBlasts": STATS = STATS + "Ice Blasts"; 
          elif self.MagicChoice == "FireBalls": STATS = STATS + "Fire Balls";             
          elif self.MagicChoice == "Lightning": STATS = STATS + "Lightning";
          elif self.MagicChoice == "Telekinesis": STATS = STATS + "Telekinesis"; 
          elif self.MagicChoice == "Telepathy": STATS = STATS + "Telepathy"; 
          elif self.MagicChoice == "Teleportation": STATS = STATS + "Teleportation";
          elif self.MagicChoice == "TimeWarp": STATS = STATS + "Time Warp";
          elif self.MagicChoice == "Invisibility": STATS = STATS + "Invisibility";
          elif self.MagicChoice == "Healing": STATS = STATS + "Healing"; 
          elif self.MagicChoice == "FriendshipCast": STATS = STATS + "Friendship Cast"; 
          print("     ","Selected Magic:",STATS); 
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
                       print("\n      You open a flask and drink a healing potion, restoring 100 health!");
                       self.EntityHealth = self.EntityHealth + 100;
                       self.INV_Has_HealingPotions = self.INV_Has_HealingPotions -1;
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
                       print("\nLight begins to bend around your body in every direction. You make yourself disappear with Invisbility!");
                       self.MagicChoice = "Invisibility";
                    else: print("\nSorry, you haven't acquired the Invisbility skill yet.");     
               elif(CHOICE == "h"):
                    if(self.SKILL_Has_Healing == "TRUE"):
                       print("\nYou lay hands upon yourself and cause healing energy to surge throughout your body. You use Healing.");
                       self.MagicChoice = "Healing";
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

          print("\n----------------------Beginning " + self.EntityName + "'s entity attack sequence----------------------");
          time.sleep(2);

          if(self.FirstTimeShowOpponentInfo == "TRUE"):
             print("\nThe Opponent being faced:");
             Opponent.DisplayStats();
             self.FirstTimeShowOpponentInfo = "FALSE"
             time.sleep(4);
             
          print("\n",Opponent.EntityName,"'s health BEFORE",self.EntityName,"'s attack:",Opponent.EntityHealth);
          
          #1.Generate base dammage to opponent for this combat round.
          DAMMAGE = random.randint(MinDammage,MaxDammage);
          print("\n" + self.EntityName + "generates" + DAMMAGE + "of random base dammage due to their magical prowess and strength.");
          time.sleep(2);

          #2.Add ATK skill and experience of Entitiy to base dammage generated.
          DAMMAGE_ATK = random.randint(1,self.EntityAttack);
          print("\n" + self.EntityName + "generates" + DAMMAGE_ATK + "additional dammage due to their attack skill and experience.");
          DAMMAGE = DAMMAGE + DAMMAGE_ATK;
          time.sleep(2);          

          #3.If class of object allowed to use a magic ITEM? Process that Entity's choice and calculate additional dammage.
          if(self.EntityClass == "Princess" or self.EntityClass == "Alicorn" or self.EntityClass == "Unicorn" or self.EntityClass == "Pegasus"):
             if(self.WeaponChoice == "None" or self.WeaponChoice == "Staff" or self.WeaponChoice == "Pendant" or self.WeaponChoice == "Sigil" or 
                self.WeaponChoice == "Orb" or self.WeaponChoice == "PrincessCloak"):
                if self.WeaponChoice == "None": 
                   MESSAGE = "\nForegoing the use of any magic items, " + self.EntityName + " fights with bare hooves of horror!\n";              
                else: 
                   MESSAGE = self.EntityName + "chooses to use a MAGIC item!\n";  
                   if self.WeaponChoice == "Staff": 
                      MESSAGE = MESSAGE + " raises their Staff to fire a bolt of lightning! Zzzzzt! (possible +" + self.Dammage_Item_Staff + ")\n";
                      DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Staff - 3),self.Dammage_Item_Staff); 
                   elif self.WeaponChoice == "Pendant": 
                        MESSAGE = MESSAGE + " touches their Pendant enveloping thier opponent in flames! Woosh! (possible +" + self.Dammage_Item_Pendant + ")\n";
                        DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Pendant - 5),self.Dammage_Item_Pendant);
                   elif self.WeaponChoice == "Sigil": 
                        MESSAGE = MESSAGE + " points their Sigil at their opponent unleashing blunt force telekinetic trauma! Pow! (possible +" + self.Dammage_Item_Sigil + ")\n";
                        DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Sigil - 10),self.Dammage_Item_Sigil);
                   elif self.WeaponChoice == "Orb": 
                        MESSAGE = MESSAGE + " cups their Orb in their hands covering their opponent in damaging darkness! Vroww! (possible +" + self.Dammage_Item_Orb + ")\n";
                        DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_Orb - 15),self.Dammage_Item_Orb);
                   elif self.WeaponChoice == "PrincessCloak":
                        MESSAGE = MESSAGE + " flips their PrincessCloak showering their opoonent with clestial projectiles. Boom! (possible +" + self.Dammage_Item_PrincessCloak + ")\n";
                        DAMMAGE_MAGIC_ITEM = random.randint((self.Dammage_Item_PrincessCloak - 20),self.Dammage_Item_PrincessCloak);
             else: MESSAGE = "\nThat magic item choice was invalid.";            

          print(MESSAGE);   
          time.sleep(3);   
          
          #4.Add magic ITEM damage to total dammage if applicable.
          if(DAMMAGE_MAGIC_ITEM > 0):
             print("\n" + self.EntityName + "generates" + DAMMAGE_MAGIC_ITEM + "additional dammage by magic ITEM.");
             DAMMAGE = DAMMAGE + DAMMAGE_MAGIC_ITEM;

          #5.If class of object allowed to use a magic SKILL? Process that Entity's choice and calculate additional dammage.
          if(self.EntityClass == "Princess" or self.EntityClass == "Alicorn" or self.EntityClass == "Unicorn" or self.EntityClass == "Pegasus"):            
             if(self.MagicChoice == "None" or self.MagicChoice == "IceBlasts" or self.MagicChoice == "FireBalls" or self.MagicChoice == "Lightning" or 
                self.MagicChoice == "Telekinesis" or self.MagicChoice == "Telepathy" or self.MagicChoice == "Teleportation" or  self.MagicChoice == "TimeWarp" or
                self.MagicChoice == "Invisibility" or self.MagicChoice == "Healing" or self.MagicChoice == "FriendshipCast"):
                if self.MagicChoice == "None": 
                   MESSAGE = self.EntityName + "decides not to use magic, leveraging only ";
                   if self.EntityGender == "Female": MESSAGE = MESSAGE +  "her";
                   elif self.EntityGender == "Male": MESSAGE = MESSAGE +  "his";
                   MESSAGE = MESSAGE +  " wits!";
                else: 
                     MESSAGE = self.EntityName + "chooses to use a MAGIC skill!\n";   
                     if(self.MagicChoice == "IceBlasts"): 
                        if(self.EntityMagicPower - 5 > 0): 
                           MESSAGE = MESSAGE + "Ice Blast! The ambient temperature around the opponent nears absolute zero, inflicting severe cold damage (possible +" + self.Dammage_Skill_IceBlasts + ")\n";
                           DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_IceBlasts-5,self.Dammage_Skill_IceBlasts);
                           self.EntityMagicPower = self.EntityMagicPower - 5; 
                        else: MESSAGE = MESSAGE + "Sorry, you do not have enough magic power to activate a Ice Blast.";    
                     elif(self.MagicChoice == "FireBalls"): 
                          if(self.EntityMagicPower - 8 > 0): 
                             MESSAGE = MESSAGE + "Fire Ball! Super-heated balls of plasma coalesce out of thin air and rush towards the opponent (possible +" + self.Dammage_Skill_FireBalls + ")\n";
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_FireBalls-8,self.Dammage_Skill_FireBalls); 
                             self.EntityMagicPower = self.EntityMagicPower - 8; 
                          else: MESSAGE = MESSAGE + "Sorry, you do not have enough magic power to activate a Fire Balls.";   
                     elif(self.MagicChoice == "Lightning"): 
                          if(self.EntityMagicPower - 15 > 0): 
                             MESSAGE = MESSAGE + "Lightning! Massive electrical potential builds and sparks and an arc of lightning races towards the opponent. (possible +" + self.Dammage_Skill_Lightning + ")\n";
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_Lightning-15,self.Dammage_Skill_Lightning);
                             self.EntityMagicPower = self.EntityMagicPower - 15;  
                          else: MESSAGE = MESSAGE + "Sorry, you do not have enough magic power to activate a Lightning.";   
                     elif(self.MagicChoice == "Telekinesis"): 
                          if(self.EntityMagicPower - 20 > 0): 
                             MESSAGE = MESSAGE + "Telekinesis! Mind over matter deals massive blunt force trauma to the opponent (possible +" + self.Dammage_Skill_Telekinesis + ")\n";
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_Telekinesis-20,self.Dammage_Skill_Telekinesis);
                             self.EntityMagicPower = self.EntityMagicPower - 20;  
                          else: MESSAGE = MESSAGE + "Sorry, you do not have enough magic power to activate a Telekinesis.";
                     elif(self.MagicChoice == "Telepathy"): 
                          if(self.EntityMagicPower - 35 > 0): 
                             MESSAGE = MESSAGE + "Telepathy! Opponent's mind is temporarily taken over and they commit self-harm (possible +" + self.Dammage_Skill_Telepathy + ")\n";
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_Telepathy-35,self.Dammage_Skill_Telepathy);                           
                             self.EntityMagicPower = self.EntityMagicPower - 35;
                          else: MESSAGE = MESSAGE + "Sorry, you do not have enough magic power to activate a Telepathy.";   
                     elif(self.MagicChoice == "Teleportation"): 
                          if(self.EntityMagicPower - 40 > 0): 
                             MESSAGE = MESSAGE + "Teleportation! Teleporting into opponent's most vulnerable spot, they are devastated by a focused attack (possible +" + self.Dammage_Skill_Teleportation + ")\n"; 
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_Teleportation-40,self.Dammage_Skill_Teleportation); 
                             self.EntityMagicPower = self.EntityMagicPower - 40; 
                          else: MESSAGE = MESSAGE + "Sorry, you do not have enough magic power to activate a Teleportation.";  
                     elif(self.MagicChoice == "TimeWarp"): 
                          if(self.EntityMagicPower - 50 > 0): 
                             MESSAGE = MESSAGE + "TimeWarp! Time warp initiated around opponent. As times slows, multiple succesive blows are sustained (possible +" + self.Dammage_Skill_TimeWarp + ")\n";  
                             DAMMAGE_MAGIC_SKILL = random.randint(self.Dammage_Skill_TimeWarp-50,self.Dammage_Skill_TimeWarp);
                             self.EntityMagicPower = self.EntityMagicPower - 50; 
                          else: MESSAGE = MESSAGE + "Sorry, you do not have enough magic power to activate a TimeWarp.";     
                     elif(self.MagicChoice == "Invisibility"): 
                          if(self.EntityMagicPower - 300 > 0):
                             MESSAGE = MESSAGE + "Invisibility Active! " + self.EntityName + " bends light around them to make themselves invisible, enhancing their defense."; 
                             self.Invisibility_Active = "TRUE";
                             self.Invisibility_Count = self.Invisibility_Count +3;
                             self.EntityMagicPower = self.EntityMagicPower - 300;
                          else: MESSAGE = MESSAGE + "Sorry, you do not have enough magic power to activate a Invisibility.";  
                     elif(self.MagicChoice == "Healing"): 
                          MESSAGE = MESSAGE + "Healing! " + self.EntityName + " concentrates their energy around themselves, healing 100 dammage."; 
                          if(self.EntityMagicPower - 100 > 0):
                             self.EntityMagicPower = self.EntityMagicPower - 100;  
                             self.EntityHealth = self.EntityHealth + 100;
                          else: MESSAGE = MESSAGE + "Sorry, you do not have enough magic power to activate a Healing.";  
                     elif(self.MagicChoice == "FriendshipCast"): 
                          MESSAGE = MESSAGE + "FriendshipCast! " + self.EntityName + " casts peace, love friendship on opponent decreasing aggression."; 
                          MESSAGE = MESSAGE + "\nOpponent no longer wishes to fight due to positive feelings of love and friendsip. Exiting combat...";
                          if(self.EntityMagicPower - 100 > 0):
                             self.EntityMagicPower = self.EntityMagicPower - 100;  
                             globals()['Willing_to_Fight'] = "FALSE";
                          else: MESSAGE = MESSAGE + "Sorry, you do not have enough magic power to activate a FriendshipCast.";   
             else: MESSAGE = "\nThat magic item skill choice was invalid.";

          print(MESSAGE); 

          #6.Add magic SKILL damage to total dammage if applicable damage-causing skill was chosen.
          if(DAMMAGE_MAGIC_SKILL > 0):
             print("\n" + self.EntityName + "generates" + DAMMAGE_MAGIC_SKILL + "additional dammage by magic SKILL.");
             DAMMAGE = DAMMAGE + DAMMAGE_MAGIC_SKILL;
          
          #7.Calculate Opponent's base defense se to skill and experience
          DAMMAGE_DEF = random.randint(1,Opponent.EntityDefense);
          print("\n" + Opponent.EntityName + "defends! Reducing dammage absorbed in this attack by" + DAMMAGE_DEF + ".");

          #8.If Opponent using INVISBILITY, add to their base defense amount.
          if(Opponent.Invisibility_Active == "TRUE"):
             print("\nInvisibility active for entity",Opponent.EntityName,"!");
             print("This temporarily increases opponent's defense by",self.Invisibility_DEF_Amt,". Hard to hit what you can't see!");
             DAMMAGE_DEF = DAMMAGE_DEF + self.Invisibility_DEF_Amt;
             Opponent.Invisibility_Count = Opponent.Invisibility_Count - 1;
             if(Opponent.Invisibility_Count < 1): 
                Opponent.Invisibility_Active == "FALSE";
                Opponent.Invisibility_Count = 0;

             #9.Subtract Opponent's DEFENSE from dammage.
             if(DAMMAGE > DAMMAGE_DEF):
                DAMMAGE = DAMMAGE - DAMMAGE_DEF;
             else: DAMMAGE = 0;
          
          #10.Display resulting dammage after adding magic item and magic skill and subtracting all Opponent defense.
          print("\nAfter all attack and defense moves calculated for this combat round:");
          print("" + self.EntityName + "generated" + DAMMAGE + "total dammage against their opponent in this round.");

          #Prevent negative values, if Opponent health less than 1 this round, they are effectively defeated
          if(Opponent.EntityHealth - DAMMAGE > 0):
             Opponent.EntityHealth = Opponent.EntityHealth - DAMMAGE;
          else: Opponent.EntityHealth = 0;

          print("\n------------AFTER Attack Sequence------------");
          print("   " + self.EntityName+ "Health:" + self.EntityHealth);
          print("   " + Opponent.EntityName+ "Health:" + Opponent.EntityHealth);
    #END-MemberMethod-Attack----------------------------------------------------------------------------------------------------------------------------

#END-ClassSpecification-Game_Entity------------------------------------------------------------------------------------------------------------------------------------------------------




#A derived child class------------------------------------------------------------------------------------------------------------------------------------------------------
class Antagonist(Game_Entity):
      #Class Attributes
      EntityName = "Anonymous Antagonist";
      EntityGender = "Male";
      EntityClass = "Antagonist";
      EntityHealth = 50;
      EntityDefense = 5;
      EntityAttack = 5;
      EntityMagicPower = 25;
      Antagonist_Ability_1 = "Warp SpaceTime";
      Antagonist_Ability_2 = "Improbability Materilization";
      Antagonist_Ability_3 = "Wish Projection";
      Antagonist_Ability_4 = "Ultimate Chaos";

      #Member Methods
      def Display_Character(self):
          self.Display_Entity();
          print("\n     ",self.EntityClass,"Special Abilities:");
          print("     ","Ability 1:",self.Antagonist_Ability_1);
          print("     ","Ability 2:",self.Antagonist_Ability_2);
          print("     ","Ability 3:",self.Antagonist_Ability_3);  
          print("     ","Ability 4:",self.Antagonist_Ability_4);   

 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 


#Example: PARENT (base) Class with CONSTRUCTOR (init method) and DEFAULT ARGUMENTS (can't overload constructors in Python)
#A derived child class-------------------------------------------------------------------------------------------------------------------------------------------------------------------
class PONY(Game_Entity):
      #Class Attributes
      EntityName = "Anonymous Pony";
      EntityGender = "Female";
      EntityClass = "Equestrian";
      EntityHealth = 100;
      EntityDefense = 10;
      EntityAttack = 10;
      EntityMagicPower = 50;      
   
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

#Example: CHILD (derived) Class that inherits from PARENT (base) class of PONY
#A derived grandchild class-------------------------------------------------------------------------------------------------------------------------------------------------------------------
class PRINCESS_PONY(PONY):
      #Class Attributes
      EntityName = "Celestia";
      EntityGender = "Female";
      EntityClass = "Princess";
      EntityHealth = 32000;
      EntityDefense = 500;
      EntityAttack = 300;
      EntityMagicPower = 32000; 
      Princess_Power = 15000;
      Princess_Charisma = 50;
      Princess_Ability_01 = "Ability 1";
      Princess_Ability_02 = "Ability 2";
      Princess_Ability_03 = "Ability 3";


      #Constructor sets PARENT (base) class values for this derived CHILD class
      def __init__(self):
          self.PonyClass = "Alicorn Princess Pony";
          self.Health = 32000;
          self.MagicPower = 32000;
          self.Defense = 500;
          self.Attack = 300;


      def Display_Character(self):
          self.Display_Entity();
          print("\n     ","Princess Pony Special Abilities:");
          print("     ","Ability 1:",self.Princess_Ability_01);
          print("     ","Ability 2:",self.Princess_Ability_02);
          print("     ","Ability 3:",self.Princess_Ability_03); 
       

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Create_Characters():   
    system('cls');
    print("\nCreating Game_Entity objects for level 1.");
    print("\n1. Instantiating a Heroine");
    Heroine = PONY();
    Heroine.EntityName = "Twilight Sparkle";
    Heroine.Display_All();
    Heroine.Cheat_Mode();
    globals()['Player_Heroine'] = Heroine;

    #print("\n2. Instantiating an Opponent");
    #Opponent = Antagonist();
    #Opponent.EntityName = "Discord";
    #Opponent.EntityClass = "Supreme Agent of Chaos";
    #Opponent.EntityHealth = 32000;
    #Opponent.EntityDefense = 300;
    #Opponent.EntityAttack = 500;
    #Opponent.EntityMagicPower = 32000;
    #Opponent.Display_Character();   
    #globals()['Player_Opponent'] = Opponent;

    ContinueIT = input("\nENTER anything to continue:");
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Display_Combat_Stats():
    print("\n");
    print ("{:<14} {:<7} {:<7} {:<8} {:<11} {:<20}".format("Name","Health","Attack","Defense","MagicPower","Class"));
    print("---------------------------------------------------------------------------");
    print ("{:<14} {:<7} {:<7} {:<8} {:<11} {:<20}".format(Player_Opponent.EntityName,Player_Opponent.EntityHealth,Player_Opponent.EntityAttack,Player_Opponent.EntityDefense,Player_Opponent.EntityMagicPower,Player_Opponent.EntityClass));
    print ("{:<14} {:<7} {:<7} {:<8} {:<11} {:<20}".format(Player_Heroine.EntityName,Player_Heroine.EntityHealth,Player_Heroine.EntityAttack,Player_Heroine.v,Player_Heroine.EntityMagicPower,Player_Heroine.EntityClass));
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
    print("\nMagic Battle!!!",Player_Opponent.EntityName,"vs.",Player_Heroine.EntityName,"!");
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
    while Player_Opponent.EntityHealth > 0 and Player_Heroine.EntityHealth > 0:      
          
          print("\nBeginning combat sequence round #:",RoundCounter); 
          time.sleep(2);

          #If player is HEROINE
          if CurrentPlayer == "Heroine":
             #Don't allow player any post-mortem attacks if lost combat sequence
             if Player_Heroine.EntityHealth > 0:
                print("\n------------------------------------------------------------------------------------");
                print(Player_Heroine.EntityName,"attacks",Player_Opponent.EntityName,"\b!");
                time.sleep(2);
                DAMMAGE = random.randint(MinDammage,MaxDammage);
                print(Player_Heroine.EntityName,"generates",DAMMAGE,"dammage.");
                time.sleep(2);
                ATK_Points = random.randint(10,Player_Heroine.Attack);
                print(Player_Heroine.EntityName,"'s attack skills add",ATK_Points,"to this magic dammage!");
                time.sleep(2);
                DAMMAGE = DAMMAGE + ATK_Points;
                DEF_Points = random.randint(10,Player_Opponent.Antagonist_Defense);
                print("But",Player_Opponent.EntityName,"defends themselves, blocking",DEF_Points,"dammage.");
                time.sleep(2);
                DAMMAGE = DAMMAGE - DEF_Points;
                print("The total resulting dammage dealt by",Player_Heroine.EntityName,"for this combat round is:",DAMMAGE);
                time.sleep(2);
                #prevent negative values of dammage which would actually ADD health to opponent
                if DAMMAGE < 0: DAMMAGE = 0;
                if (Player_Opponent.EntityHealth - DAMMAGE) < 0:
                   Player_Opponent.EntityHealth = 0;
                else:
                   Player_Opponent.EntityHealth = Player_Opponent.EntityHealth - DAMMAGE;
                CurrentPlayer = "Antagonist";
             else: print("\n",Player_Heroine.EntityName,"cannot attack anymore. She has LOST!");

          #If player is ANTAGONIST
          elif CurrentPlayer == "Antagonist":
               #Don't allow player any post-mortem attacks if lost combat sequence
               if Player_Opponent.EntityHealth > 0:
                  print("\n------------------------------------------------------------------------------------");
                  print(Player_Opponent.EntityName,"attacks",Player_Heroine.EntityName,"\b!");
                  time.sleep(2);
                  DAMMAGE = random.randint(MinDammage,MaxDammage);
                  print(Player_Opponent.EntityName,"generates",DAMMAGE,"dammage.");
                  time.sleep(2);
                  ATK_Points = random.randint(10,Player_Opponent.Antagonist_Attack);
                  print(Player_Opponent.EntityName,"'s attack skills add",ATK_Points,"to this magic dammage.");
                  time.sleep(2);
                  DAMMAGE = DAMMAGE + ATK_Points;
                  DEF_Points = random.randint(10,Player_Heroine.Defense);
                  print("But",Player_Heroine.EntityName,"defends themselves, blocking",DEF_Points,"dammage.");
                  time.sleep(2);
                  DAMMAGE = DAMMAGE - DEF_Points;
                  print("The total resulting dammage dealt by",Player_Opponent.EntityName,"for this combat round is:",DAMMAGE);
                  time.sleep(2);
                  #prevent negative values of dammage which would actually ADD health to opponent
                  if DAMMAGE < 0: DAMMAGE = 0;
                  if (Player_Heroine.EntityHealth - DAMMAGE) < 0:
                      Player_Heroine.EntityHealth = 0;
                  else:
                      Player_Heroine.EntityHealth = Player_Heroine.EntityHealth - DAMMAGE;
                  CurrentPlayer = "Heroine";
               else: print("\n",Player_Opponent.EntityName,"cannot attack anymore. They have LOST!");
         
          else: print("\nERROR. This should never happen."); 

          ClearCounter = ClearCounter + 1;
          RoundCounter = RoundCounter + 1;
          Display_Combat_Stats();
          time.sleep(3); 
          if ClearCounter == 2: 
            ClearCounter = 0;
            system('cls');

    print("\nMagic Battle Complete!");

    if Player_Heroine.EntityHealth > 0: print("\n",Player_Heroine.EntityName,"is victorious! She defeats",Player_Opponent.EntityName,"\b!");
    else: print("\n",Player_Opponent.EntityName,"is victorious! They defeat",Player_Heroine.EntityName,"\b!");

    Display_Combat_Stats();
          
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
          print("      |        9. Exit                        |");
          print("      |                                       |");
          print("      -----------------------------------------");

          CHOICE = input("\n      Your choice: ");
          CHOICE = CHOICE.lower();

          if(CHOICE != "1" and CHOICE != "2" and CHOICE != "3" and CHOICE != "4" and CHOICE != "5" and 
             CHOICE != "6" and CHOICE != "7" and CHOICE != "8" and CHOICE != "9"):
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
                     print("\nExiting options menu ..."); 
                     Present_Options_Menu = "FALSE";      

          ContinueIT = input("\nENTER anything to continue:");                                                                                                           
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
          print("      |              3. Exit                          |");
          print("      |                                               |");
          print("      -------------------------------------------------");

          CHOICE = input("\n      Your choice: ");
          CHOICE = CHOICE.lower();

          if(CHOICE != "1" and CHOICE != "2" and CHOICE != "3"):
             print("\nThat was an invalid choice.");
          else:   
                if(CHOICE == "1"): 
                   Create_Characters();
                elif(CHOICE == "2"): 
                     Options();   
                elif(CHOICE == "3"): 
                     Present_Main_Menu = "FALSE";
                     print("\nNow exiting Discord's Dungeon ... Goodbye!");                                                                                                     
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def TEST1():   

    print("------------------------------------------------------------------------------------------------");
    print("\n1. Instantiating a Pony");
    Heroine = PONY();
    Heroine.EntityName = "Twilight Sparkle";
    print("\n\n***********************BEFORE CHEAT:**************************");
    Heroine.Display_All();
    Heroine.Cheat_Mode();
    print("\n\n***********************AFTER CHEAT:**************************");
    Heroine.Display_All();     

    globals()['Player_Heroine'] = Heroine;
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function----------------------------------------------------------------------------------------------------------------------------------------------------------------
def TEST2():   

    print("------------------------------------------------------------------------------------------------");
    print("\n2. Instantiating a Princess");
    PRINCESS = PRINCESS_PONY();
    PRINCESS.Display_All();  

    print("------------------------------------------------------------------------------------------------");
    print("\n3. Instantiating an Antagonist");
    Lord_of_Chaos =Antagonist();
    Lord_of_Chaos.EntityName = "Discord";
    Lord_of_Chaos.Display_Character();      
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-----Invocations------
#Magic_Battle();
#TEST1();
Main_Menu();

