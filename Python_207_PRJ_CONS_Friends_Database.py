#Title: Database Friends and Contacts
#Author: Carly S. Germany
#Created: 08/08/2022
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0


# Address Book. Practice with File Access.

#Imports
from os import system;
import os;
import csv;

#Globals
Group_of_Friends = [];

#---BEGIN-FRIEND-CLASS---------------------------------------------------------------------------------------------------------------------------
class FRIEND:

      #----- Data Members -----
      FirstName = " ";
      LastName = " ";
      EmailAddress = " ";
      MobilePhone = " ";
      StreetAddress = " ";
      City = " ";
      State = " ";
      Country = " ";
      BirthDay = " ";
      FaveColor = " ";
      FaveFood = " ";      
      
      #Constructor sets PARENT (base) class values for this derived CHILD class
      def __init__(self,Fn="",Ln="",Ea="",Mp="",Sa="",Cty="",St="",Ctry="",Bd="",Fc="",Ff=""):
          print("Instantiating a FRIEND class object.");
          self.FirstName = Fn;
          self.LastName = Ln;
          self.EmailAddress = Ea;
          self.MobilePhone = Mp;
          self.StreetAddress = Sa;
          self.City = Cty;
          self.State = St;
          self.Country = Ctry;
          self.BirthDay = Bd;
          self.FaveColor = Fc;
          self.FaveFood = Ff;  

    #-----------------------------------------------------------------------------
      def Display_FRIEND(self):
          Message = "";
          Message += "  First Name: " + self.FirstName;
          Message += "\n  Last Name: " + self.LastName;
          Message += "\n  Email: " + self.EmailAddress;
          Message += "\n  Mobile Phone: " + self.MobilePhone;
          Message += "\n  Street Address: " + self.StreetAddress;
          Message += "\n  City: " + self.City;
          Message += "\n  State: " + self.State;
          Message += "\n  Country: " + self.Country;
          Message += "\n  Birthday: " + self.BirthDay;
          Message += "\n  Favorite Color: " + self.FaveColor;
          Message += "\n  Favorite Food: " + self.FaveFood;
          print(Message);

    #-----------------------------------------------------------------------------
      def New_FRIEND(self):
          print("\n");
          self.FirstName = input("First Name? ");
          self.LastName= input("Last Name? ");
          self.EmailAddress= input("Email? ");
          self.MobilePhone= input("Mobile Phone? ");
          self.StreetAddress= input("Street Address? ");
          self.City= input("City? ");
          self.State= input("State? ");
          self.Country= input("Country? ");
          self.BirthDay= input("Birthday? ");
          self.FaveColor= input("Favorite Color? ");
          self.FaveFood= input("Favorite Food? ");    

    #-----------------------------------------------------------------------------
      def Edit_FRIEND(self):
          Message = "\nChoose an attbiute to change:\n";
          Message += "\n  1. First Name: " + self.FirstName;
          Message += "\n  2. Last Name: " + self.LastName;
          Message += "\n  3. Email: " + self.EmailAddress;
          Message += "\n  4. Mobile Phone: " + self.MobilePhone;
          Message += "\n  5. Street Address: " + self.StreetAddress;
          Message += "\n  6. City: " + self.City;
          Message += "\n  7. State: " + self.State;
          Message += "\n  8. Country: " + self.Country;
          Message += "\n  9. Birthday: " + self.BirthDay;
          Message += "\n  10. Favorite Color: " + self.FaveColor;
          Message += "\n  11. Favorite Food: " + self.FaveFood;
          print(Message);       

          CHOICE = input("\nWhich value do you wish to edit? (1-11) "); 

          if(CHOICE == "1"): self.FirstName = input("First Name? ");
          if(CHOICE == "2"): self.LastName = input("Last Name? ");
          if(CHOICE == "3"): self.EmailAddress = input("Email? ");
          if(CHOICE == "4"): self.MobilePhone = input("Mobile Phone? ");
          if(CHOICE == "5"): self.StreetAddress = input("Street Address? ");
          if(CHOICE == "6"): self.City = input("City? ");
          if(CHOICE == "7"): self.State = input("State? ");
          if(CHOICE == "8"): self.Country = input("Country? ");
          if(CHOICE == "9"): self.BirthDay = input("Birthday? ");
          if(CHOICE == "10"): self.FaveColor = input("Favorite Color? ");
          if(CHOICE == "11"): self.FaveFood = input("Favorite Food? ");

          print("\n");
          self.Display_FRIEND();

              
#---END-FRIEND-CLASS-------------------------------------------------------------------------------------------------------------------------        


#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def MAIN():
    CHOICE = "*";

    while(CHOICE != "q"):
          system('cls');
          print("\n\"Friends\" 1.0 (Address Book) - 2022 - Carly Salali Germany\n");

          print("\n     -----------Main Menu-------------");
          print("     |                               |");
          print("     |     (B)rowse Friend Index     |");
          print("     |     (D)isplay Friends         |");
          print("     |     (L)oad Friends            |");
          print("     |     (S)ave Friends            |");
          print("     |     (F)ind a Friend           |");
          print("     |     (A)dd a Friend            |");
          print("     |     (E)dit a Friend           |");
          print("     |     (R)emove a Friend         |");
          print("     |     (Q)uit                    |");
          print("     |                               |");
          print("     ---------------------------------");

          CHOICE = (input("\n              CHOICE? ")).lower();

          if(CHOICE == "b"): Browse_Friends();
          elif(CHOICE == "d"): Display_Friends();
          elif(CHOICE == "l"): Load_Friends();
          elif(CHOICE == "s"): Save_Friends();
          elif(CHOICE == "f"): Find_A_Friend();
          elif(CHOICE == "a"): Add_Friend();
          elif(CHOICE == "e"): Edit_Friend();
          elif(CHOICE == "r"): Remove_Friend();
          elif(CHOICE == "q"): 
                             print("\n  Exiting \"Friends\" 1.0...");
                             break;
          else: 
                print("\nThat was an invalid choice. Please choose again.");
                NULL = input("Press \"ENTER\" to continue.");
#--------------------------------------------------------------------------------------------------------------------------------------------



#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def List_All_FRIENDs():
    for x in range(len(globals()['Group_of_Friends'])):
        FRND_FirstName = globals()['Group_of_Friends'][x].FirstName;
        FRND_LastName = globals()['Group_of_Friends'][x].LastName;
        FRND_Num = str((x+1)) + ".";
        print("-----------------------------------------------------------------------------------");
        print('{:<5}{:<7}{:<20}{:<5}{:>0}'.format(FRND_Num,"First: ",FRND_FirstName,"Last: ",FRND_LastName));
#--------------------------------------------------------------------------------------------------------------------------------------------



#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def Browse_Friends():
    system('cls');
    print("\n                    Index of FRIENDS:\n");
    List_All_FRIENDs();
    print("-----------------------------------------------------------------------------------");
    NULL = input("\nPress \"ENTER\" to continue.");    

#--------------------------------------------------------------------------------------------------------------------------------------------


#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def Display_Friends():
    system('cls');
    print("\n                    Displaying FRIENDS:\n");
    for x in range(len(globals()['Group_of_Friends'])):
        print("-----------------------------------------------------------------");
        print("  FRIEND: " + str((x+1)));
        globals()['Group_of_Friends'][x].Display_FRIEND();

    print("-----------------------------------------------------------------");
    NULL = input("\nPress \"ENTER\" to continue.");  
#--------------------------------------------------------------------------------------------------------------------------------------------


#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def Add_Friend():
    system('cls');
    print("\n                    Add a new FRIEND:\n");
    A_New_Friend = FRIEND();
    A_New_Friend.New_FRIEND();
    globals()['Group_of_Friends'].append(A_New_Friend);
    NULL = input("\nPress \"ENTER\" to continue.");
#--------------------------------------------------------------------------------------------------------------------------------------------


#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def Save_Friends():
    system('cls');
    print("\n                    Saving FRIENDs:\n");
    Current_Directory = os.getcwd();
    FRIEND_File = "\Python_072_PRJ_CONS_Database_FRIENDS_DATA.csv";
    FRIENDS_Data_Path = Current_Directory + FRIEND_File;

    os.remove(FRIENDS_Data_Path);
    The_File = open(FRIENDS_Data_Path,'a',newline='');
    CSV_Writer = csv.writer(The_File,delimiter=",");

    #Write field names to CSV
    CSV_Writer.writerow(["First-Name",
                         "Last-Name",
                         "Email-Address",
                         "Mobile-Phone",
                         "Street-Address",
                         "City",
                         "State",
                         "Country",
                         "Birth-Day",
                         "Fave-Color",
                         "Fave-Food"]);

    #Write data members of each instantiated FRIEND class object in array to CSV file.
    FRND_Counter = 0;
    for FRND in globals()['Group_of_Friends']:
        FRND_Counter += 1;
        print("-----------------------------------------------------------------");
        print("  Saving FRIEND:",FRND_Counter);
        CSV_Writer.writerow([FRND.FirstName,
                             FRND.LastName,
                             FRND.EmailAddress,
                             FRND.MobilePhone,
                             FRND.StreetAddress,
                             FRND.City,
                             FRND.State,
                             FRND.Country,
                             FRND.BirthDay,
                             FRND.FaveColor,
                             FRND.FaveFood]);    

    The_File.close();
    NULL = input("\nPress \"ENTER\" to continue.");
#--------------------------------------------------------------------------------------------------------------------------------------------



#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def Load_Friends():
    system('cls');
    print("\n                    Loading FRIENDs:\n");
    
    globals()['Group_of_Friends'].clear();

    Current_Directory = os.getcwd();
    FRIEND_File = "\Python_072_PRJ_CONS_Database_FRIENDS_DATA.csv";
    FRIENDS_Data_Path = Current_Directory + FRIEND_File;
    The_File = open(FRIENDS_Data_Path,'r',newline='');
    CSV_Reader = csv.reader(The_File,delimiter=",");
    
    #Skip 1st line before reading each row since it's field value names
    NULL = next(CSV_Reader);

    FRND_Counter = 0;
    for FRND in CSV_Reader:
        FRND_Counter += 1;
        print("-----------------------------------------------------------------");
        print("Loading FRIEND:",FRND_Counter);
        print(FRND);
        print("First:",FRND[0]);
        print("Last:",FRND[1]);
        print("Email:",FRND[2]);
        print("MobilePhone:",FRND[3]);
        print("StreetAddress:",FRND[4]);
        print("City:",FRND[5]);
        print("State:",FRND[6]);
        print("Country:",FRND[7]);
        print("BirthDay:",FRND[8]);
        print("FaveColor:",FRND[9]);
        print("FaveFood:",FRND[10]);

        A_New_Friend = FRIEND();
        A_New_Friend.FirstName = FRND[0];
        A_New_Friend.LastName = FRND[1];
        A_New_Friend.EmailAddress = FRND[2];
        A_New_Friend.MobilePhone = FRND[3];
        A_New_Friend.StreetAddress = FRND[4];
        A_New_Friend.City = FRND[5];
        A_New_Friend.State = FRND[6];
        A_New_Friend.Country = FRND[7];
        A_New_Friend.BirthDay = FRND[8];
        A_New_Friend.FaveColor = FRND[9];
        A_New_Friend.FaveFood = FRND[10];

        globals()['Group_of_Friends'].append(A_New_Friend);

    NULL = input("\nPress \"ENTER\" to continue.");    
#--------------------------------------------------------------------------------------------------------------------------------------------





#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def Find_A_Friend():
    system('cls');
    print("\n                    Find a FRIEND:\n");
    FoundAFriend = False;

    F_Name = input("Enter FIRST Name: ");
    L_Name = input("Enter LAST Name: ");

    for x in range(len(globals()['Group_of_Friends'])):
        if(F_Name == globals()['Group_of_Friends'][x].FirstName and 
           L_Name == globals()['Group_of_Friends'][x].LastName):
           print("\n-----------------------------------------------------------------");
           globals()['Group_of_Friends'][x].Display_FRIEND(); 
           FoundAFriend = True; 

    if(FoundAFriend == False):
       print("\nNo Friends found matching " + 
             "\n  First Name: " + F_Name + 
             "\n  Last Name: " + L_Name);
          
    NULL = input("\nPress \"ENTER\" to continue."); 
#--------------------------------------------------------------------------------------------------------------------------------------------


#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def Edit_Friend():
    system('cls');
    print("\n                    Edit a FRIEND:\n");
    CHOICE = "*";

    while(CHOICE != "1" and CHOICE != "2" and CHOICE != "3"):
          print("\n\n            Select an Option:");
          print("------------------------------------------");
          print("|                                        |");
          print("|      1. Select FRIEND by Number.       |");
          print("|      2. Select FRIEND by Name.         |");
          print("|      3. Exit                           |");
          print("|                                        |");
          print("------------------------------------------");
          CHOICE = input("           Your CHOICE? ");

          if(CHOICE == "1"): Edit_Friend_By_Number();
          elif(CHOICE == "2"): Edit_Friend_By_Name();
          elif(CHOICE == "3"): break;
          else: print("\n Invalid option. Please choose again.");   

#--------------------------------------------------------------------------------------------------------------------------------------------





#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def Edit_Friend_By_Number():
    system('cls');
    print("\n                 Choose a FRIEND to Edit by NUMBER:\n");
    List_All_FRIENDs();

    CHOICE = input("\nSelect a FRIEND by number from the List above: ");

    if(CHOICE.isnumeric()):
       print("CHOICE is numeric. Converting to int.");
       SELECTION = int(CHOICE);

       if(SELECTION >= 1 and SELECTION <= len(globals()['Group_of_Friends'])):
          print("Selected FRIEND is within the valid range: ");
          #Subtract 1 for FENCEPOST issue
          globals()['Group_of_Friends'][(SELECTION-1)].Display_FRIEND();
          globals()['Group_of_Friends'][(SELECTION-1)].Edit_FRIEND();
       else: print("Selected FRIEND is outside the valid range.");

    else: print("CHOICE is not numeric. Invalid option.");

    NULL = input("\nPress \"ENTER\" to continue.");
#--------------------------------------------------------------------------------------------------------------------------------------------


#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def Edit_Friend_By_Name():
    system('cls');
    print("\n                    Edit FRIEND by NAME:\n");

    FoundAFriend = False;

    F_Name = input("Enter FIRST Name: ");
    L_Name = input("Enter LAST Name: ");

    for x in range(len(globals()['Group_of_Friends'])):
        if(F_Name == globals()['Group_of_Friends'][x].FirstName and 
           L_Name == globals()['Group_of_Friends'][x].LastName):
           print("\n-----------------------------------------------------------------");
           globals()['Group_of_Friends'][x].Display_FRIEND(); 
           globals()['Group_of_Friends'][x].Edit_FRIEND(); 
           FoundAFriend = True; 

    if(FoundAFriend == False):
       print("\nNo Friends found matching " + 
             "\n  First Name: " + F_Name + 
             "\n  Last Name: " + L_Name);
          
    NULL = input("\nPress \"ENTER\" to continue.");     
#--------------------------------------------------------------------------------------------------------------------------------------------



#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def Remove_Friend():
    system('cls');
    print("\n                    Remove a FRIEND:\n");
    List_All_FRIENDs();

    CHOICE = input("\nSelect a FRIEND by number from the List above: ");

    if(CHOICE.isnumeric()):
       print("\nCHOICE is numeric. Converting to int.");
       SELECTION = int(CHOICE);

       if(SELECTION >= 1 and SELECTION <= len(globals()['Group_of_Friends'])):
          print("Selected FRIEND is within the valid range.\n");
          #Subtract 1 for FENCEPOST issue
          globals()['Group_of_Friends'][(SELECTION-1)].Display_FRIEND();
          Are_You_Sure = (input("\nAre you SURE you want to DELETE this FRIEND? ")).lower();
          if(Are_You_Sure == "yes" or Are_You_Sure == "y"): 
             print("DELETEing FRIEND!");
             globals()['Group_of_Friends'].pop((SELECTION-1));
          elif(Are_You_Sure == "no" or Are_You_Sure == "n"):
             print("Ok. This FRIEND remains. Aborting...");
          else: print("That is an invalid option. Valid options are \"yes\" or \"no\".");
          
       else: print("Selected FRIEND is outside the valid range.");

    else: print("CHOICE is not numeric. Invalid option.");

    NULL = input("\nPress \"ENTER\" to continue.");
#--------------------------------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------------------------------
def TEST():
    Social_Circle = FRIEND();
    Social_Circle.Edit_FRIEND();
#--------------------------------------------------------------------------------------------------------------------------------------------

#---Invocations----
#TEST();
MAIN();

