# Title: Python File Access
# Author: C. S. Germany 01/15/2022 

# open() function takes two parameters; filename, and mode. 4 different modes:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# Specifying binary or text
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Opening a file for reading. The examples below do the same thing. The options "r" for read and "t" for text are default values.
#   So if you simply open a file without specifying any arguments it is assumed to be read-only and text. 
def File_Access_READ_0l():
    The_File = open("Python_035_File_Access_My_Data_File_Read.txt");
    The_File.close();

    The_File = open("Python_035_File_Access_My_Data_File_Read.txt","rt");
    The_File.close();
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Using the read() method to display the contents of a file
def File_Access_READ_02():
    The_File = open("Python_035_File_Access_My_Data_File_Read.txt","rt");
    print(The_File.read());
    The_File.close();
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Using the read() method to display only the first 5 chars of a file
def File_Access_READ_03():
    The_File = open("Python_035_File_Access_My_Data_File_Read.txt","rt");
    print(The_File.read(5));
    The_File.close();
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Using readline() to read an entire line of a file
def File_Access_READ_04():
    The_File = open("Python_035_File_Access_My_Data_File_Read.txt","rt");
    print(The_File.readline());
    The_File.close();
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Using readline() to read 2 lines of a file
def File_Access_READ_05():
    The_File = open("Python_035_File_Access_My_Data_File_Read.txt","rt");
    print("\n");
    print(The_File.readline(),end='');
    print(The_File.readline());
    The_File.close();
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Reading an entire file with a loop
def File_Access_READ_06():
    The_File = open("Python_035_File_Access_My_Data_File_Read.txt","rt");

    for x in The_File:
        print(x,end='');

    The_File.close();
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Closing a file with close(). When buffering, changes to a file may not show up until you close it. It also reduces the chance that file will 
#   be corrupted if your programs crashes while it is open.
def File_Access_READ_07():
    The_File = open("Python_035_File_Access_My_Data_File_Read.txt","rt");
    print(The_File.readline());
    The_File.close();
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#8. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Using getcwd() and finding the directory a script is running in to open it from the same location
def File_Access_READ_08():
    import os;
    
    Current_Dir = os.getcwd(); 
    print("\nDirectory this script is running in: \"",Current_Dir,"\"",sep='');
    File_Name = Current_Dir + "\\" + "Python_035_File_Access_My_Data_File_Read.txt";

    The_File = open(File_Name,"rt");
    
    print("\n----------Reading contents of file now----------");

    for x in The_File:
        print(x,end='');

    print("-------------------------------------------------");
    The_File.close();
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#9. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Listing the files in a directory with 
def File_Access_READ_09():
    import os;
    
    print("Listing files in this script's directory:");
    print("\n----------------------------------------------------------------");

    FileCounter = 0;
    Array_of_Files_In_Dir = os.listdir();
    
    for x in Array_of_Files_In_Dir:
        FileCounter += 1;
        print(FileCounter,"\b.",x);

    print("----------------------------------------------------------------\n"); 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#10. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Listing only files that match a certain extension in a directory
def File_Access_READ_10():
    import os;
    
    print("Listing ONLY \".py\" files in this script's directory:");
    print("\n----------------------------------------------------------------");

    FileCounter = 0;
    Array_of_Files_In_Dir = os.listdir();
    
    for x in Array_of_Files_In_Dir:
        if(x.endswith(".py")):        
           FileCounter = FileCounter + 1;
           print(FileCounter,"\b.",x);

    print("----------------------------------------------------------------\n"); 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#11. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#    When opening a file to write data to, there are 2 options:
#    "a" - Append - appends to the end of the file
#    "w" - Write - overwrites any existing content
#    "x" - Create - creates file, returns error if the file already exists

def File_Access_WRITE_01():
    The_File = open("Python_036_File_Access_My_Data_File_Write.txt","w");

    MESSAGE = "And as I watched him on that stage."; 
    MESSAGE = MESSAGE + "\nMy hands were clenched in fists of rage.";
    MESSAGE = MESSAGE + "\nNo angel born in Hell.";
    MESSAGE = MESSAGE + "\nCould break that Satan's spell.";

    The_File.write(MESSAGE);

    The_File.close();

    The_File = open("Python_036_File_Access_My_Data_File_Write.txt","r");

    print("\n----------------------File Contents----------------------");
    
    for x in The_File:
        print(x,end='');

    print("\n---------------------------------------------------------"); 

    The_File.close();      
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#12. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#    Appending data to a file that already exists

def File_Access_WRITE_02():
    The_File = open("Python_036_File_Access_My_Data_File_Write.txt","a");

    MESSAGE = "\nAnd as the flames climbed high into the night"; 
    MESSAGE = MESSAGE + "\nto light the sacrificial rite?";
    MESSAGE = MESSAGE + "\nI saw Satan laughing with delight.";
    MESSAGE = MESSAGE + "\nThe day the music died.";

    The_File.write(MESSAGE);

    The_File.close();

    The_File = open("Python_036_File_Access_My_Data_File_Write.txt","r");

    print("\n----------------------File Contents----------------------");
    
    for x in The_File:
        print(x,end='');

    print("\n---------------------------------------------------------");  

    The_File.close();     
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#13. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#    Prevent over-writing a file with the "x" argument. The code below will throw exception and generate error if file already exists.

def File_Access_WRITE_03():
    The_File = open("Python_036_File_Access_My_Data_File_Write.txt","x"); 
    The_File.close();    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#14. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#    Delete a file by importing os module and using the remove() method

def File_Access_REMOVE_01():
    import os;
    os.remove("Python_036_File_Access_My_Data_File_Write.txt");   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#15. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#    Check if file exists before deleting

def File_Access_REMOVE_02():
    import os;

    if os.path.exists("Python_036_File_Access_My_Data_File_Write.txt"):
       os.remove("Python_036_File_Access_My_Data_File_Write.txt");
    else:
       print("This file does not exist!");  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#-----Invocations-----
#File_Access_READ_0l();
#File_Access_READ_02();
#File_Access_READ_03();
#File_Access_READ_04();
#File_Access_READ_05();
#File_Access_READ_06();
#File_Access_READ_07();
#File_Access_READ_08();
#File_Access_READ_09();
#File_Access_READ_10();

#File_Access_WRITE_01();
#File_Access_WRITE_02();
#File_Access_WRITE_03();

#File_Access_REMOVE_01();
File_Access_REMOVE_02();
