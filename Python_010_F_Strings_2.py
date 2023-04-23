
#Title: Python Programming 10 - F-Strings
#Author: Carly S. Germany
#Created: 01/15/2022
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Old_String_Formatting_1():
    #Old school #1: %-formatting. Replacement fields = %s. Confusing/convoluted.
    First_Name = "Carly";
    Last_Name = "Salali";
    Age = 53;
    Profession = "Unicorn";
    Affiliation = "The Brotherhood of Twilight Sparkle";

    print("\nHello, %s %s. You are %s. You are a %s. You are a member of %s.\n" % (First_Name, Last_Name, Age, Profession, Affiliation));
#---------------------------------------------------------------------------------------------------------------------------------------------



#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Old_String_Formatting_2():
    #Old school #2: str.format() formatting. Replacement fields = {}. Reference variables by index value and uses format() method.
    First_Name = "Carly";
    Last_Name = "Salali";
    Age = 53;
    Profession = "Unicorn";
    Affiliation = "The Brotherhood of Twilight Sparkle";

    print("\nA. Using str.format() in direct sequence:");
    print("Hello, {} {}. You are {}. You are a {}. You are a member of {}.".format(First_Name,Last_Name,Age,Profession,Affiliation));

    print("\nB. Using str.format() referencing by index value to reorder things:");
    print("Hello, {2} {0}. You are {4}. You are a {3}. You are a member of {1}.\n".format(Last_Name,Affiliation,First_Name,Profession,Age));

#---------------------------------------------------------------------------------------------------------------------------------------------


#FUNCTION-------------------------------------------------------------------------------------------------------------------------------------
def New_F_Strings_1():
    #New F Strings: Called "Formatted String Literals". Have F at beginning and {} containing expressions to be replaced with values.
    First_Name = "Carly";
    Last_Name = "Salali";
    Age = 53;
    Profession = "Unicorn";
    Affiliation = "The Brotherhood of Twilight Sparkle";

    print("\nA. Using a basic F String (prefixed with an \"f\"):");
    print(f"Hello, {First_Name} {Last_Name}. You are {Age}. You are a {Profession}. You are a member of {Affiliation}.");

    print("\nB. You can use F Strings to print datatypes without typecasting or conversion:");
    print("2 x 444 = ",f"{2 * 444}");

    print("\nC. You can call methods directly using F Strings:");
    print("My first and last name in LOWERCASE = ",f"{First_Name.lower()}",f"{Last_Name.lower()}",".\n");
#---------------------------------------------------------------------------------------------------------------------------------------------


#CLASS---------------------------------------------------------------------------------------------------------------------------------------
class UNICORN:
    def __init__(self, First_Name, Last_Name, Age):
        self.First_Name = First_Name;
        self.Last_Name = Last_Name;
        self.Age = Age;

    #__str__() Returns a human-readable (informal) string representation of a class object. Less detailed. For std users.
    def __str__(self):
        return f"{self.First_Name} {self.Last_Name} is {self.Age}.";

    #If you don’t define a __str__() method for a class  __repr__() method is called instead. More detailed, for developers.
    def __repr__(self):
        return f"{self.First_Name} {self.Last_Name} is {self.Age}. A disciple of Twilight Sparkle!"
#---------------------------------------------------------------------------------------------------------------------------------------------


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def New_F_Strings_2_With_Classes():
    #F Strings used with a CLASS (UNICORN class defined above)
    New_Unicorn_Instance = UNICORN("Carly","Salali","53");

    print("\n");
    print(f"{New_Unicorn_Instance}");
    print(f"{New_Unicorn_Instance!r}");
    print("\n");

    #By default f-strings use __str__() but you can make sure they use __repr__() with flag !r.
    #In classes,  __str__() is the informal string representation of an object.
    #In classes,  __repr__() is the official representation.
#---------------------------------------------------------------------------------------------------------------------------------------------


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def New_F_Strings_3_MultiLine():
    First_Name = "Carly";
    Last_Name = "Salali";
    Age = 53;
    Profession = "Unicorn";
    Affiliation = "The Brotherhood of Twilight Sparkle";

    print("\nA. Concatenated F Strings:");
    Concatenated_F_Strings = f"   Hello, {First_Name} {Last_Name}. " \
                             f"\n   You are {Age} years old. " \
                             f"\n   You are a {Profession}. "  \
                             f"\n   You are a member of {Affiliation}.";

    print(Concatenated_F_Strings);

    print("\nB. An Array of F Strings:");
    Array_of_F_Strings = (f"   Hello, {First_Name} {Last_Name}. "
                          f"\n   You are {Age} years old. "
                          f"\n   You are a {Profession}. "
                          f"\n   You are a member of {Affiliation}.\n");

    print(Array_of_F_Strings);
#---------------------------------------------------------------------------------------------------------------------------------------------


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def New_F_Strings_4_With_Dictionaries():
    #Define Dictionary which contains KEY + VALUE pairs
    UNICORN = { 'First_Name': 'Carly','Last_Name': 'Salali','Age': '53', };

    #An F-String can pull out each value from the Dictionary defined above by its key name
    print("\nAn F-String can pull out each value from the Dictionary defined above by its key name.\n");
    print(f"This unicorn is {UNICORN['First_Name']} {UNICORN['Last_Name']}. It has lived to the ripe old age of {UNICORN['Age']}.");
    print("\n");
#---------------------------------------------------------------------------------------------------------------------------------------------



#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def New_F_Strings_5_Escape_Sequences():
    #You can use double sequences of characters as escape sequences instead of a "\" back-slash"" with F-Strings
    print("\nYou can use double sequences of characters as escape sequences instead of a \"\\\" with F-Strings\n");
    print(f"\"Carly Salali\"",f".    To make BRACES appear double them: ",f"{{3+2}} \n");
    print("\n");
 #---------------------------------------------------------------------------------------------------------------------------------------------   


#-----Function Invocations-----
#Old_String_Formatting_1();
#Old_String_Formatting_2();
#New_F_Strings_1();
#New_F_Strings_2_With_Classes();
#New_F_Strings_3_MultiLine();
#New_F_Strings_4_With_Dictionaries();
New_F_Strings_5_Escape_Sequences();







