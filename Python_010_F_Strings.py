# Title: Python F Strings (faster than older string formats)
# Author: C. S. Germany 01/15/2022

# Link = https://realpython.com/python-f-strings/


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Old_String_Formatting_1():
    #Old school #1: %-formatting. Replacement fields = %s. Confusing/convoluted.
    First_Name = "Carly";
    Last_Name = "Salali";
    Age = 52;
    Profession = "Unicorn";
    Affiliation = "Brotherhood of Twilight Sparkle";

    print("Hello, %s %s. You are %s. You are a %s. You were a member of %s." % (First_Name, Last_Name, Age, Profession, Affiliation));
#---------------------------------------------------------------------------------------------------------------------------------------------



#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Old_String_Formatting_2():
    #Old school #2: str.format() formatting. Replacement fields = {}. Reference variables by index value and uses format() method.
    First_Name = "Carly";
    Last_Name = "Salali";
    Age = 52;
    Profession = "Unicorn";
    Affiliation = "Brotherhood of Twilight Sparkle";

    print("\nUsing str.format() in direct sequence:");
    print("Hello, {} {}. You are {}. You are a {}. You were a member of {}.".format(First_Name,Last_Name,Age,Profession,Affiliation));

    print("\nUsing str.format() referencing by index value to reorder things:");
    print("Hello, {2} {0}. You are {4}. You are a {3}. You were a member of {1}.".format(Last_Name,Affiliation,First_Name,Profession,Age));

#---------------------------------------------------------------------------------------------------------------------------------------------

#FUNCTION-------------------------------------------------------------------------------------------------------------------------------------
def New_F_Strings_1():
    #New F Strings: Called "Formatted String Literals". Have F at beginning and {} containing expressions to be replaced with values.
    First_Name = "Carly";
    Last_Name = "Salali";
    Age = 52;
    Profession = "Unicorn";
    Affiliation = "Brotherhood of Twilight Sparkle";

    print("\nUsing a basic F String:");
    print(f"Hello, {First_Name} {Last_Name}. You are {Age}. You are a {Profession}. You were a member of {Affiliation}.");

    print("\nYou can use F Strings to print datatypes without typecasting or conversion:");
    print("2 x 444 = ",f"{2 * 444}");

    print("\nYou can call methods directly using F Strings:");
    print("My first and last name in LOWERCASE = ",f"{First_Name.lower()}"," ",f"{Last_Name.lower()}",".\n");
#---------------------------------------------------------------------------------------------------------------------------------------------



#CLASS---------------------------------------------------------------------------------------------------------------------------------------
class UNICORN:
    def __init__(self, First_Name, Last_Name, Age):
        self.First_Name = First_Name;
        self.Last_Name = Last_Name;
        self.Age = Age;

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name} is {self.Age}.";

    def __repr__(self):
        return f"{self.First_Name} {self.Last_Name} is {self.Age}. Twilight Sparkle!"
#---------------------------------------------------------------------------------------------------------------------------------------------


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def New_F_Strings_2_With_Classes():
    #F Strings used with a CLASS (UNICORN class defined above)
    New_Unicorn_Instance = UNICORN("Caly","Salali","52");

    print(f"{New_Unicorn_Instance}");
    print(f"{New_Unicorn_Instance!r}");

    #By default f-strings use __str__() but you can make sure they use __repr__() with flag !r.
    #In classes,  __str__() is the informal string representation of an object.
    #In classes,  __repr__() is the official representation.
#---------------------------------------------------------------------------------------------------------------------------------------------



#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def New_F_Strings_3_MultiLine():
    
    First_Name = "Carly";
    Last_Name = "Salali";
    Age = 52;
    Profession = "Unicorn";
    Affiliation = "Brotherhood of Twilight Sparkle";

    print("\nConcatenated F Strings:");
    Concatenated_F_Strings = f"\nHello, {First_Name} {Last_Name}. " \
                              f"\nYou are {Age} years old. " \
                              f"\nYou are a {Profession}. "  \
                              f"\nYou were a member of {Affiliation}.";

    print(Concatenated_F_Strings);

    print("\nArray of F Strings:");
    Array_of_F_Strings = (f"\nHello, {First_Name} {Last_Name}. "
                          f"\nYou are {Age} years old. "
                          f"\nYou are a {Profession}. " 
                          f"\nYou were a member of {Affiliation}.");

    print(Array_of_F_Strings);
#---------------------------------------------------------------------------------------------------------------------------------------------


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def New_F_Strings_4_With_Dictionaries():
    #Define Dictionary
    UNICORN = { 'First_Name': 'Carly','Last_Name': 'Salali','Age': '52', };
    print(f"The UNICORN is {UNICORN['First_Name']} {UNICORN['Last_Name']}. She is aged {UNICORN['Age']}.");
#---------------------------------------------------------------------------------------------------------------------------------------------



#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def New_F_Strings_5_Escape_Sequences():
    print(f"\n\"Carly Salali\"",f".    To make BRACES appear double them: ",f"{{3+2}} \n");
 #---------------------------------------------------------------------------------------------------------------------------------------------   

#-----Function Invocations-----
#Old_String_Formatting_1();
#Old_String_Formatting_2();
#New_F_Strings_1();
#New_F_Strings_2_With_Classes();
#New_F_Strings_3_MultiLine();
#New_F_Strings_4_With_Dictionaries();
New_F_Strings_5_Escape_Sequences();
